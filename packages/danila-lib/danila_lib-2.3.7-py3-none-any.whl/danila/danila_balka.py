from danila.Danila_balka_classify import Danila_balka_classify
from data.neuro.prods import RAMA_PRODS, BALKA_PRODS
from data.result.Text_cut_recognize_result import Text_cut_recognize_result
from data.result.Text_recognize_result import Text_recognize_result
from data.result.balka_prod import Balka_Prod


class Danila_balka:
    def __init__(self, yolov5_dir, danila_balka_params):
        self.danila_balka_params = danila_balka_params
        self.danila_balka_classify = Danila_balka_classify(yolov5_dir, self.danila_balka_params.danila_balka_classify_params)

    def balka_classify(self,img, detail):
        balka_prod_conf = self.danila_balka_classify.balka_classify(img)
        if detail is None:
            detail_prod = Text_cut_recognize_result('balka', 1)
            det = Text_recognize_result(detail_prod)
        else:
            det = detail
        if balka_prod_conf.balka_prod != Balka_Prod.no_balka:
            text_prod = BALKA_PRODS[balka_prod_conf.balka_prod]
            det.prod = Text_cut_recognize_result(text_prod, balka_prod_conf.conf)
        return det