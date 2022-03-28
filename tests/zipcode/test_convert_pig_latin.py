import sys

sys.path.append("..")


from nose.tools import assert_list_equal, assert_is_none, assert_equal
from src.zip_lookup.utils.convert_pig_latin import convert_name_to_pig_latin, convert_word_to_pig_latin


class TestPigLatin(object):
    @classmethod
    def setup_class(cls):
        cls.word_start_with_vowel = "Alice"
        cls.word_not_start_with_vowel = "Miller"
        cls.word_capitalize = "ALICE"
        cls.word_all_lowercase = "alice"
        cls.word_some_letter_capitalize = "alICe"

    def test_convert_word_to_pig_latin(self):
        word_start_with_vowel_result = convert_word_to_pig_latin(self.word_start_with_vowel)
        word_not_start_with_vowel_result = convert_word_to_pig_latin(self.word_not_start_with_vowel)
        word_capitalize_result = convert_word_to_pig_latin(self.word_capitalize)
        word_all_lowercase_result = convert_word_to_pig_latin(self.word_all_lowercase)
        word_some_letter_capitalize = convert_word_to_pig_latin(self.word_some_letter_capitalize)

        expected_start_with_vowel = "aliceay"
        expected_not_start_with_vowel = "illermay"

        assert_equal(word_start_with_vowel_result, expected_start_with_vowel)
        assert_equal(word_not_start_with_vowel_result, expected_not_start_with_vowel)
        assert_equal(word_capitalize_result, expected_start_with_vowel)
        assert_equal(word_all_lowercase_result, expected_start_with_vowel)
        assert_equal(word_some_letter_capitalize, expected_start_with_vowel)

    def test_convert_name_to_pig_latin(self):
        expected_str = "Aliceay, illermay"
        expected_another_str = "Illermay, aliceay"

        start_with_alice = convert_name_to_pig_latin(self.word_start_with_vowel, self.word_not_start_with_vowel)
        not_start_with_alice = convert_name_to_pig_latin(self.word_not_start_with_vowel, self.word_start_with_vowel)

        assert_equal(expected_str, start_with_alice)
        assert_equal(expected_another_str, not_start_with_alice)



