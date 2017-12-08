import numpy as np
import unittest

from recog.recog import Recog
from utils.utils import Utils

class TestRecog(unittest.TestCase):
    # imgpath = "datasets/testdata/test1.jpg"
    # imgans = np.array(["A","B","C","0","3","2","6","8"])
    imgpath = "datasets/testdata/test2.jpg"
    imgans = np.array(['4','0','A','8','B','9','1','5','2','C','6','1','3','3','7','3','2','5','1','8'])
    # imgpath = "datasets/testdata/test3.jpg"
    # imgans = np.array(['4','=','8','C','B'])
    # imgpath = "datasets/testdata/test4.jpg"
    # imgans = np.array(['A','3','0','4','=', 'B', 'C', '5', '0', '6', '7', '1', '2', '8'])

    def test_recog_attr(self):
        recog16 = Recog("16")
        self.assertTrue(hasattr(recog16, "size"))
        self.assertTrue(hasattr(recog16, "train"))

    def test_recog_equaly(self):
        self.assertTrue(Recog("16") == Recog("16"))
        self.assertFalse(Recog("16") == Recog("32"))

    def test_recog_generate(self):
        recog16 = Recog.recog16()
        recog32 = Recog.recog32()
        self.assertTrue(recog16 == Recog("16"))
        self.assertTrue(recog32 == Recog("32"))
        self.assertFalse(recog16 == recog32)

    ## 識別結果を返す(重いからコメントアウト推奨)
    def test_recog_letter(self):
        recog16 = Recog.recog16()
        recog32 = Recog.recog32()
        imgans = TestRecog.imgans
        ret16 = recog16.recog(TestRecog.imgpath, box_view=False)
        ret32 = recog32.recog(TestRecog.imgpath, box_view=False)
        acc16 = np.where(ret16 == TestRecog.imgans)[0].shape[0] / TestRecog.imgans.shape[0]
        acc32 = np.where(ret32 == TestRecog.imgans)[0].shape[0] / TestRecog.imgans.shape[0]
        self.assertTrue(Utils.nparray_eq(recog16.recog(TestRecog.imgpath), TestRecog.imgans))
        self.assertTrue(Utils.nparray_eq(recog32.recog(TestRecog.imgpath), TestRecog.imgans))

    ## 精度確認用(重いからコメントアウト推奨)
    # def test_cross_validation(self):
    #     recog16 = Recog.recog16()
    #     recog32 = Recog.recog32()
    #     score16 = recog16.cross_validation()
    #     score32 = recog32.cross_validation()
    #     self.assertTrue(score16 > 0.7)
    #     self.assertTrue(score32 > 0.7)
    #     self.assertTrue(False)

    ## テストデータそれぞれのボックスを一枚として表示用
    # def test_recog_letter_with_show(self):
    #     recog16 = Recog.recog16()
    #     recog32 = Recog.recog32()
    #     recog16.recog(TestRecog.imgpath, box_view=True)
    #     recog32.recog(TestRecog.imgpath, box_view=True)

    # def test_show_letter(self):
    #     recog = Recog.recog32()
    #     recog.show_letter(TestRecog.imgpath)

if __name__ == '__main__':
    unittest.main()
