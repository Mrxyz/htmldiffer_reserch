# -*- coding:utf-8 -*-
from htmldiffer import diff

html1 = "<p>粮食订购合同</p><p>　甲方（订购方）：_____深圳函宇餐饮有限公司     </p><p>地址： 深圳市宝安区福永街道凤凰第一工业区岭北四路2号10层                    </p><p>邮码：               </p><p>电话：    187-1233-2564           </p><p>法定代表人：____刘琴________</p><p>职务：____监事____</p><p>乙方（交售方）：_____深圳天楷粮业有限公______</p><p>地址：深圳市龙华新区龙华街道松和社区油松商务大厦11层</p><p>邮码：____________ </p><p>电话：__0731-1254-3654__________</p><p>法定代表人：_____李东_______</p><p>职务：___执行董事_________</p><p>　　甲、乙双方根据国家粮食购销管理政策，在平等、自愿、合作、互利的原则下，经充分协商，达成如下协议。</p><p>　　一、甲方向乙方定购粮食____5000_公斤，每公斤5元，粮食款共计25000元。</p><p>　　1.品种：优质大米</p><p>　　2.订购数：5000公斤</p><p>　　3.订购价：5元/公斤</p><p>　　二、合同订购的粮食质量、等级、水分执行国家规定标准。</p><p>　　三、合同订购的收购：</p> <p>  </p> <p>　　四、甲方必须做到及时收购，保证不借故压车、退车，做到认真执行国家质价政策，保证不压等压价。对乙方交售的粮食，结算形式不限，现金、转帐由本人任选。除农业税外，不代任何部门扣款，不打白条。</p><p>　　五、乙方必须做到按签订的合同订购品种、数量、种足种好各种作物，正常年景保证按合同规定的品种、数量交售。遇灾可向甲方申请减免。</p><p>　　六、在执行本合同期间，乙方负责人（承包人）有变动时，由接替人继续执行本合同。</p><p>　　七、乙方交售粮食时，需携带本合同，每次结算，甲方要在合同的附表内给予记载。</p><p>　　八、本合同一式三份，甲乙双方、粮管所各一份。</p><p>　　甲 方：_____深圳函宇餐饮有限公司____</p><p>　　法定代表人：____刘琴____________</p><p>__2018__年_12_月_18_日</p><p>乙 方：____深圳天楷粮业有限公____________________</p><p>法定代表人：______李东__________</p><p>__2018__年_12_月_18_日</p><p> </p>"
html2 = "<p>粮食订购合同</p><p>　甲方（订购方）： _________________     </p><p>地址：__________                    </p><p>邮码：               </p><p>电话: ________         </p><p>法定代表人：_______________</p><p>职务：__________</p><p>乙方（交售方）：__________________</p><p>地址：_______________________</p><p>邮码：____________ </p><p>电话：________</p><p>法定代表人：__________</p><p>职务：______________</p><p>　　甲、乙双方根据国家粮食购销管理政策，在平等、自愿、合作、互利的原则下，经充分协商，达成如下协议。</p><p>　　一、甲方向乙方定购粮食____公斤，每公斤___元，粮食款共计_____元。</p><p>　　1.品种：优质大米</p><p>　　2.订购数：______公斤</p><p>　　3.订购价：_____元/公斤</p><p>　　二、合同订购的粮食质量、等级、水分执行国家规定标准。</p><p>　　三、合同订购的收购：</p><p>　　四、甲方必须做到及时收购，保证不借故压车、退车，做到认真执行国家质价政策，保证不压等压价。对乙方交售的粮食，结算形式不限，现金、转帐由本人任选。除农业税外，不代任何部门扣款，不打白条。</p><p>　　五、乙方必须做到按签订的合同订购品种、数量、种足种好各种作物，正常年景保证按合同规定的品种、数量交售。遇灾可向甲方申请减免。</p><p>　　六、在执行本合同期间，乙方负责人（承包人）有变动时，由接替人继续执行本合同。</p><p>　　七、乙方交售粮食时，需携带本合同，每次结算，甲方要在合同的附表内给予记载。</p><p>　　八、本合同一式三份，甲乙双方、粮管所各一份。</p><p>　　甲 方：_______________</p><p>　　法定代表人：___________</p><p>______年____月____日</p><p>乙 方：_______________________</p><p>法定代表人：_______________</p><p>_______年____月____日</p><p> </p>"

html_head = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>differ</title>\
             <link rel="stylesheet" type="text/css" href="htmldiffer_stylesheet.css"></head><body>'
html_end = '</body></html>'


# mode 0: side by side 1:line by line
def htmldiffer_process(mode, str1, str2):
    result = diff.HTMLDiffer(html1, html2)
    if mode == 0:
        with open('html_combin.html', 'w') as tmp:  # create differ html file
            tmp.writelines(html_head)
            tmp.writelines(result.combined_diff)
            tmp.writelines(html_end)
        return result.combined_diff
    elif mode == 1:
        with open('html_delete.html', 'w') as tmp:
            tmp.writelines(html_head)
            tmp.writelines(result.deleted_diff)
            tmp.writelines(html_end)
        with open('html_insert.html', 'w') as tmp:
            tmp.writelines(html_head)
            tmp.writelines(result.inserted_diff)
            tmp.writelines(html_end)
        return [result.deleted_diff, result.inserted_diff]
    else:
        return 'input error'

# print the information of differ
result = diff.HTMLDiffer(html1, html2)
print('line by line: {}\nside by side:\n  delte: {}\n  inser: {}'.format(result.combined_diff, result.deleted_diff, result.inserted_diff))

if __name__ == '__main__':
    htmldiffer_process(1, html1, html2)





