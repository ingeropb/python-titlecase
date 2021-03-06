#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for titlecase"""

from __future__ import print_function

import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from titlecase import titlecase

TEST_DATA = (
    (
        "word/word",
        "Word/Word"
    ),
    (
        "dance with me/let’s face the music and dance",
        "Dance With Me/Let’s Face the Music and Dance"
    ),
    (
        "34th 3rd 2nd 1st",
        "34th 3rd 2nd 1st"
    ),
    (
        "Q&A with steve jobs: 'that's what happens in technology'",
        "Q&A With Steve Jobs: 'That's What Happens in Technology'"
    ),
    (
        "What is AT&T's problem?",
        "What Is AT&T's Problem?"
    ),
    (
        "Apple deal with AT&T falls through",
        "Apple Deal With AT&T Falls Through"
    ),
    (
        "this v that",
        "This v That"
    ),
    (
        "this v. that",
        "This v. That"
    ),
    (
        "this vs that",
        "This vs That"
    ),
    (
        "this vs. that",
        "This vs. That"
    ),
    (
        "The SEC's Apple probe: what you need to know",
        "The SEC's Apple Probe: What You Need to Know"
    ),
    (
        "'by the Way, small word at the start but within quotes.'",
        "'By the Way, Small Word at the Start but Within Quotes.'"
    ),
    (
        "Small word at end is nothing to be afraid of",
        "Small Word at End Is Nothing to Be Afraid Of"
    ),
    (
        "Starting Sub-Phrase With a Small Word: a Trick, Perhaps?",
        "Starting Sub-Phrase With a Small Word: A Trick, Perhaps?"
    ),
    (
        "Sub-Phrase With a Small Word in Quotes: 'a Trick, Perhaps?'",
        "Sub-Phrase With a Small Word in Quotes: 'A Trick, Perhaps?'"
    ),
    (
        'sub-phrase with a small word in quotes: "a trick, perhaps?"',
        'Sub-Phrase With a Small Word in Quotes: "A Trick, Perhaps?"'
    ),
    (
        '"Nothing to Be Afraid of?"',
        '"Nothing to Be Afraid Of?"'
    ),
    (
        '"Nothing to be Afraid Of?"',
        '"Nothing to Be Afraid Of?"'
    ),
    (
        'a thing',
        'A Thing'
    ),
    (
        "2lmc Spool: 'gruber on OmniFocus and vapo(u)rware'",
        "2lmc Spool: 'Gruber on OmniFocus and Vapo(u)rware'"
    ),
    (
        'this is just an example.com',
        'This Is Just an example.com'
    ),
    (
        'this is something listed on del.icio.us',
        'This Is Something Listed on del.icio.us'
    ),
    (
        'iTunes should be unmolested',
        'iTunes Should Be Unmolested'
    ),
    (
        'reading between the lines of steve jobs’s ‘thoughts on music’',
        'Reading Between the Lines of Steve Jobs’s ‘Thoughts on Music’'
    ),
    (
        'seriously, ‘repair permissions’ is voodoo',
        'Seriously, ‘Repair Permissions’ Is Voodoo'
    ),
    (
        'generalissimo francisco franco: still dead; kieren McCarthy: still a jackass',
        'Generalissimo Francisco Franco: Still Dead; Kieren McCarthy: Still a Jackass'
    ),
    (
        "O'Reilly should be untouched",
        "O'Reilly Should Be Untouched"
    ),
    (
        "my name is o'reilly",
        "My Name Is O'Reilly"
    ),
    (
        "WASHINGTON, D.C. SHOULD BE FIXED BUT MIGHT BE A PROBLEM",
        "Washington, D.C. Should Be Fixed but Might Be a Problem"
    ),
    (
        "THIS IS ALL CAPS AND SHOULD BE ADDRESSED",
        "This Is All Caps and Should Be Addressed"
    ),
    (
        "Mr McTavish went to MacDonalds",
        "Mr McTavish Went to MacDonalds"
    ),
    (
        "this shouldn't\nget mangled",
        "This Shouldn't\nGet Mangled"
    ),
    (
        "this is http://foo.com",
        "This Is http://foo.com"
    ),
    (
        "mac mc MAC MC machine",
        "Mac Mc MAC MC Machine",
    ),
    (
        "FOO BAR 5TH ST",
        "Foo Bar 5th St",
    ),
    (
        "foo bar 5th st",
        "Foo Bar 5th St",
    ),
    (
        "l'grange l'grange l'Grange l'Grange",
        "l'Grange l'Grange l'Grange l'Grange",
    ),
    (
        "L'grange L'grange L'Grange L'Grange",
        "l'Grange l'Grange l'Grange l'Grange",
    ),
    (
        "l'GranGe",
        "l'GranGe",
    ),
    (
        "o'grange O'grange o'Grange O'Grange",
        "O'Grange O'Grange O'Grange O'Grange",
    ),
    (
        "O'GranGe",
        "O'GranGe",
    ),
    (
        "o'melveny/o'doyle o'Melveny/o'doyle O'melveny/o'doyle o'melveny/o'Doyle o'melveny/O'doyle",
        "O'Melveny/O'Doyle O'Melveny/O'Doyle O'Melveny/O'Doyle O'Melveny/O'Doyle O'Melveny/O'Doyle",
    ),
    (
        "oblon, spivak, mcclelland, maier & neustadt",
        "Oblon, Spivak, McClelland, Maier & Neustadt",
    ),
    (
        "Mcoblon, spivak, mcclelland, mcmaier, & mcneustadt",
        "McOblon, Spivak, McClelland, McMaier, & McNeustadt",
    )
)

def check_input_matches_expected_output(in_, out):
    """Function yielded by test generator"""
    try:
        assert titlecase(in_) == out
    except AssertionError:
        print("{0} != {1}".format(titlecase(in_), out))
        raise

class TitleCaseTest(unittest.TestCase):
    def test_all_caps_regex(self):
        """Test - all capitals regex"""
        from titlecase import ALL_CAPS
        assert bool(ALL_CAPS.match('THIS IS ALL CAPS')) is True


    def test_initials_regex(self):
        """Test - uppercase initals regex with A.B"""
        from titlecase import UC_INITIALS
        assert bool(UC_INITIALS.match('A.B')) is True


    def test_initials_regex_2(self):
        """Test - uppercase initals regex with A.B."""
        from titlecase import UC_INITIALS
        assert bool(UC_INITIALS.match('A.B.')) is True


    def test_initials_regex_3(self):
        """Test - uppercase initals regex with ABCD"""
        from titlecase import UC_INITIALS
        assert bool(UC_INITIALS.match('ABCD')) is False

    def test_ordinals_list_item(self):
        """
        Test - numbers ending in ordinals like 1st and 24th
        """
        from titlecase import ORDINALS
        assert '34Th' not in titlecase(TEST_DATA[2][0])
        assert '1st' in titlecase(TEST_DATA[2][0])

    def test_input_output(self):
        """Generated tests"""
        for data in TEST_DATA:
            yield check_input_matches_expected_output, data[0], data[1]


    def test_callback(self):
        def abbreviation(word, **kwargs):
            if word.upper() in ('TCP', 'UDP'):
                return word.upper()
        s = 'a simple tcp and udp wrapper'
        assert titlecase(s) == 'A Simple Tcp and Udp Wrapper'
        assert titlecase(s, callback=abbreviation) == 'A Simple TCP and UDP Wrapper'
        assert titlecase(s.upper(), callback=abbreviation) == 'A Simple TCP and UDP Wrapper'


    if __name__ == "__main__":
        import nose
        nose.main()
