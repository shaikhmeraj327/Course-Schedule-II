import unittest

from solution import Solution, findOrder, find_course_order


class CourseScheduleTests(unittest.TestCase):
    def assert_is_valid_order(self, order, num_courses, prerequisites):
        self.assertEqual(len(order), num_courses)
        positions = {course: idx for idx, course in enumerate(order)}
        self.assertEqual(len(positions), num_courses)
        for course, prerequisite in prerequisites:
            self.assertLess(positions[prerequisite], positions[course])

    def test_valid_schedule(self):
        num_courses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        order = find_course_order(num_courses, prerequisites)
        self.assert_is_valid_order(order, num_courses, prerequisites)

    def test_cycle_returns_empty(self):
        num_courses = 2
        prerequisites = [[0, 1], [1, 0]]
        self.assertEqual(find_course_order(num_courses, prerequisites), [])
        self.assertEqual(findOrder(num_courses, prerequisites), [])
        self.assertEqual(Solution().findOrder(num_courses, prerequisites), [])

    def test_no_prerequisites(self):
        num_courses = 3
        prerequisites = []
        order = find_course_order(num_courses, prerequisites)
        self.assertEqual(len(order), num_courses)
        self.assertEqual(set(order), {0, 1, 2})

    def test_invalid_course_index_returns_empty(self):
        self.assertEqual(find_course_order(2, [[1, 2]]), [])
        self.assertEqual(find_course_order(2, [[-1, 0]]), [])


if __name__ == "__main__":
    unittest.main()
