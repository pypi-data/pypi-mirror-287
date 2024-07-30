[![Python package](https://github.com/WMU-Herculaneum-Project/wmu_greek_utils/actions/workflows/test.yml/badge.svg)](https://github.com/WMU-Herculaneum-Project/wmu_greek_utils/actions)

# Greek Language Utilties from the WMU Hecurlaneum Project.

This package provides a set of utilities for working with Greek text. It is designed to be used in conjunction with the WMU Herculaneum Project, but can be used independently.

## Installation

```bash
poetry add wmu_greek_utils
```

## Usage

### AGDT morphological parsing

#### parse_mophology

The `parse_morphology` function can be used to parse the morphology field of a morphological code.

Examples:

1. Parsing a verb morphology code:

```python
>>> parse_morphology("v3sasm---", include_names=False)
['verb', 'third person', 'singular', 'aorist', 'subjunctive', 'middle', None, None, None]
```

2. Parsing a noun morphology code:

```python
>>> parse_morphology("n-s---mn-", include_names=False)
['noun', None, 'singular', None, None, None, 'masculine', 'nominative', None]
```

3. Including the position names in the output:

```python
   >>> list(parse_morphology("n-s---mn-"))
    [('part_of_speech', 'noun'), ('person', None), ('number', 'singular'), ('tense', None), ('mood', None), ('voice', None), ('gender', 'masculine'), ('case', 'nominative'), ('degree', None)]
```

#### morphology_string

Given a list of forms, produce the morphology string to the best of our ability.

Examples:

1. Basic usage with a list of forms:

```python
>>> morphology_string(['noun', 'masculine', 'singular', 'nominative'])
'n-s---mn-'
```

2. Usage with a randomized list of forms (in other words, the order of the forms does not matter):

```python
>>> list = ['noun', 'masculine', 'singular', 'nominative']
>>> random.shuffle(list)
>>> morphology_string(list)
'n-s---mn-'
```

3. Usage with abbreviated forms:

```python
>>> morphology_string(['masc', 'sing', 'nom', 'n'])
'n-s---mn-'
```

4. Usage with a more complex list of forms:

```python
>>> morphology_string(['verb', 'third person', 'singular', 'aorist', 'subjunctive', 'middle', None, None, None])
'v3sasm---'
```

5. Usage with a partial list of forms:

```python
>>> morphology_string(['verb', 'third person', 'singular', 'aorist', 'subjunctive', 'middle'])
'v3sasm---'
```

#### position_to_name

"""
Given a 0-based position, return the name of the position.

```python >>> position_to_name(0)
'part_of_speech' >>> position_to_name(8)
'degree'
```

#### name_to_position

Given a name, return the 0-based position. Can use some short
or alternate names for the name.

```python
    >>> name_to_position('part_of_speech')
    0
    >>> name_to_position('pos')
    0
    >>> name_to_position('degree')
    8
```

### recreate_sentence

Given a list of words and a list of morphologies, recreate the sentence,
along with the positions in the sentence.

```python
words = [
        ("The", "det"),
        ("cat", "noun"),
        (",", "punctuation"),
        ("the", "det"),
        ("dog", "noun"),
        (",", "punctuation"),
        ("and", "conj"),
        ("the", "det"),
        ("frog", "noun"),
        ("sat", "verb"),
        ("on", "prep"),
        ("the", "det"),
        ("mat", "noun"),
        (".", "punctuation"),
    ]
sentence, poss = agdt.recreate_sentence(words)
assert sentence == "The cat, the dog, and the frog sat on the mat."
assert poss == [
        (0, 2),
        (4, 6),
        (7, 7),
        (9, 11),
        (13, 15),
        (16, 16),
        (18, 20),
        (22, 24),
        (26, 29),
        (31, 33),
        (35, 36),
        (38, 40),
        (42, 44),
        (45, 45),
    ]
```
