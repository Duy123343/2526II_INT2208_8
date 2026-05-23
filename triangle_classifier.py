import unittest

def classify_triangle(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "Invalid Input"

    if not (1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100):
        return "Invalid Input"

    if not (a + b > c and a + c > b and b + c > a):
        return "Not a Triangle"

    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

class TestTriangleClassifier(unittest.TestCase):
    def test_tc01_below_lower_bound(self):
        self.assertEqual(classify_triangle(0, 50, 50), "Invalid Input")

    def test_tc02_above_upper_bound(self):
        self.assertEqual(classify_triangle(101, 50, 50), "Invalid Input")

    def test_tc03_min_boundary_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")

    def test_tc04_max_boundary_equilateral(self):
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")

    def test_tc05_invalid_sum_equal(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a Triangle")

    def test_tc06_invalid_sum_less(self):
        self.assertEqual(classify_triangle(5, 12, 5), "Not a Triangle")

    def test_tc07_isosceles_ab(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_tc08_isosceles_bc(self):
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    def test_tc09_isosceles_ac(self):
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")

    def test_tc10_valid_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene")

if __name__ == "__main__":
    print("--- ĐANG CHẠY TEST SUITE ---")
    unittest.main()
