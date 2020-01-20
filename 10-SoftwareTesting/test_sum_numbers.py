import unittest

from sum_numbers import sum_even


class TestSumEven(unittest.TestCase):
    def test_sum_even(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z dowolnego przedziału m,n
        m = 1
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_fromeven(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m parzyste
        m = 2
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie n<m
        m = 5
        n = 2
        result = sum_even(m,n)
        self.assertEqual(result, 0)
        
    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m lub n są mniejsze od 0
        m = -5
        n = 10
        result = sum_even(m,n)
        self.assertEqual(result, 30)
        
    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m lub n są mniejsze od 0
        m = 2.123
        n = 6.23
        result = sum_even(m,n)
        self.assertEqual(result, 10)
    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m lub n są mniejsze od 0
        m = "jeden"
        n = "osiem"
        result = sum_even(m,n)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()