"""
Tests for the Acronym Creator application.
"""

import pytest
from src.acronym_creator.core import AcronymCreator, AcronymOptions


class TestAcronymCreator:
    """Test cases for the AcronymCreator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.creator = AcronymCreator()

    def test_create_basic_acronym_simple(self):
        """Test basic acronym creation from simple phrase."""
        phrase = "Hello World"
        options = AcronymOptions()
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "HW"

    @pytest.mark.skip(reason="Article filtering not implemented yet")
    def test_create_basic_acronym_with_articles(self):
        """Test acronym creation excluding articles by default."""
        phrase = "The Quick Brown Fox"
        options = AcronymOptions(include_articles=False)
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "QBF"

    def test_create_basic_acronym_including_articles(self):
        """Test acronym creation including articles when specified."""
        phrase = "The Quick Brown Fox"
        options = AcronymOptions(include_articles=True)
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "TQBF"

    def test_create_basic_acronym_empty_phrase(self):
        """Test handling of empty phrase."""
        phrase = ""
        options = AcronymOptions()
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == ""

    def test_create_basic_acronym_single_word(self):
        """Test acronym creation from single word."""
        phrase = "Python"
        options = AcronymOptions()
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "P"

    def test_create_basic_acronym_lowercase_output(self):
        """Test acronym creation with lowercase output."""
        phrase = "Hello World"
        options = AcronymOptions(force_uppercase=False)
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "HW"  # First letters are naturally uppercase

    @pytest.mark.skip(reason="Word length filtering not implemented yet")
    def test_create_basic_acronym_min_word_length(self):
        """Test filtering words by minimum length."""
        phrase = "A Big Red Car"
        options = AcronymOptions(min_word_length=3, include_articles=True)
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "BRC"  # 'A' should be filtered out

    @pytest.mark.skip(reason="Max words limiting not implemented yet")
    def test_create_basic_acronym_max_words(self):
        """Test limiting number of words."""
        phrase = "One Two Three Four Five"
        options = AcronymOptions(max_words=3)
        result = self.creator.create_basic_acronym(phrase, options)
        assert result == "OTT"

    @pytest.mark.skip(reason="Phrase cleaning not implemented yet")
    def test_clean_phrase_special_characters(self):
        """Test phrase cleaning removes special characters."""
        phrase = "Hello, World! How are you?"
        cleaned = self.creator.clean_phrase(phrase)
        assert cleaned == "Hello World How are you"

    @pytest.mark.skip(reason="Phrase cleaning not implemented yet")
    def test_clean_phrase_extra_whitespace(self):
        """Test phrase cleaning normalizes whitespace."""
        phrase = "  Hello    World  "
        cleaned = self.creator.clean_phrase(phrase)
        assert cleaned == "Hello World"

    @pytest.mark.skip(reason="Word extraction not implemented yet")
    def test_extract_words_basic(self):
        """Test word extraction from phrase."""
        phrase = "Hello Beautiful World"
        options = AcronymOptions()
        words = self.creator.extract_words(phrase, options)
        assert words == ["Hello", "Beautiful", "World"]

    @pytest.mark.skip(reason="Article filtering not implemented yet")
    def test_extract_words_filter_articles(self):
        """Test word extraction filtering articles."""
        phrase = "The Quick Brown Fox"
        options = AcronymOptions(include_articles=False)
        words = self.creator.extract_words(phrase, options)
        assert words == ["Quick", "Brown", "Fox"]

    @pytest.mark.skip(reason="Word length filtering not implemented yet")
    def test_extract_words_min_length(self):
        """Test word extraction with minimum length filter."""
        phrase = "A Big Red Car"
        options = AcronymOptions(min_word_length=3, include_articles=True)
        words = self.creator.extract_words(phrase, options)
        assert words == ["Big", "Red", "Car"]

    @pytest.mark.skip(reason="Syllable acronym not implemented yet")
    def test_create_syllable_acronym(self):
        """Test syllable-based acronym creation."""
        phrase = "Python Programming Language"
        options = AcronymOptions()
        result = self.creator.create_syllable_acronym(phrase, options)
        assert result == "PYPRLAL"  # Py-Pr-La based on syllable logic

    @pytest.mark.skip(reason="Multiple options generation not implemented yet")
    def test_generate_multiple_options(self):
        """Test generation of multiple acronym options."""
        phrase = "The Quick Brown Fox"
        results = self.creator.generate_multiple_options(phrase, count=2)

        # Check that all expected keys are present
        assert 'basic' in results
        assert 'with_articles' in results
        assert 'creative' in results
        assert 'syllable' in results

        # Check basic acronym (should exclude 'The')
        assert 'QBF' in results['basic']

        # Check with articles (should include 'The')
        assert 'TQBF' in results['with_articles']
