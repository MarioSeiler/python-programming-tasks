import unittest
from Matrix2Dim import Matrix2Dim


class Matrix2DimTest(unittest.TestCase):

  def setUp(self) -> None:
    self.matrix1 = Matrix2Dim((2, 3), [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]])
    self.matrix2 = Matrix2Dim((3, 2), [[0.0, 3.0], [1.0, 4.0], [2.0, 5.0]])
    self.matrix3 = Matrix2Dim((2, 1), [[1.0], [2.0]])
    self.matrix4 = Matrix2Dim((2, 2), [[0.0, 1.0], [1.0, 2.0]])
    return super().setUp()

  def test_transpose(self):
    matrix1_transposed = self.matrix1
    matrix1_transposed.transpose()
    self.assertEqual(matrix1_transposed.elements, self.matrix2.elements)
    self.assertEqual(matrix1_transposed.dimensions, (3, 2))

    self.matrix1.transpose()

    self.assertEqual(matrix1_transposed, self.matrix1)

    self.matrix3.transpose()
    self.assertEqual(self.matrix3.elements, [[1.0, 2.0]])

    self.matrix4.transpose()
    self.assertEqual(self.matrix4.elements, [[0.0, 1.0], [1.0, 2.0]])

  def test_is_symmetric(self):
    self.assertFalse(self.matrix1.is_symmetric())
    self.assertFalse(self.matrix2.is_symmetric())
    self.assertFalse(self.matrix3.is_symmetric())
    self.assertTrue(self.matrix4.is_symmetric())

  def test_total(self):
    self.assertEqual(self.matrix1.total(), 15.0)
    self.assertEqual(self.matrix2.total(), 15.0)
    self.assertEqual(self.matrix3.total(), 3.0)
    self.assertEqual(self.matrix4.total(), 4.0)

  def test_average(self):

    self.assertEqual(self.matrix1.average(), 2.5)
    self.assertEqual(self.matrix2.average(), 2.5)
    self.assertEqual(self.matrix3.average(), 1.5)
    self.assertEqual(self.matrix4.average(), 1.0)

  def test_stddeviation(self):
    self.assertAlmostEqual(self.matrix1.stddeviation(), 1.707825127659933)
    self.assertAlmostEqual(self.matrix2.stddeviation(), 1.707825127659933)
    self.assertAlmostEqual(self.matrix3.stddeviation(), 0.5)
    self.assertAlmostEqual(self.matrix4.stddeviation(), 0.70710678118655)

  def test_is_coherent(self):
    self.assertTrue(self.matrix1.is_coherent())
    self.assertTrue(self.matrix2.is_coherent())
    self.assertTrue(self.matrix3.is_coherent())
    self.assertTrue(self.matrix4.is_coherent())

  def tearDown(self) -> None:
    return super().tearDown()
  

if __name__ == '__main__':
  unittest.main()
