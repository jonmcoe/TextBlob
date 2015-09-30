from unittest import TestCase

from textblob import Word
from textblob.en.inflect import plural_categories, singular_uninflected, singular_ie, singular_irregular, singular_uncountable


class BigPluralsTestCase(TestCase):

    def test_all_plurals_in_categories(self):
        for category in plural_categories.values():
            for word in category:
                print(word)
                self.assertEqual(Word(word), Word(word).pluralize().singularize())

    def test_singular_uninflected(self):
        for word in singular_uninflected:
            print(word)
            self.assertEqual(Word(word), Word(word).pluralize().singularize())

    def test_singular_ie(self):
        for word in singular_ie:
            print(word)
            self.assertEqual(Word(word), Word(word).pluralize().singularize())

    def test_singular_irregular(self):
        for word in singular_irregular.keys():
            print(word)
            self.assertEqual(Word(singular_irregular[word]), Word(word).singularize())

    def test_singular_uncountable(self):
        for word in singular_uncountable:
            print(word)
            self.assertEqual(Word(word), Word(word).pluralize().singularize())

    def test_is_this_running(self):
        self.assertTrue(True)
