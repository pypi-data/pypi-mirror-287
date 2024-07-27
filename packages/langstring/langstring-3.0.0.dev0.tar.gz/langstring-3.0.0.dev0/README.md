[![Project DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10211480.svg)](https://doi.org/10.5281/zenodo.10211480)
[![Project Status - Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![GitHub - Release Date - PublishedAt](https://img.shields.io/github/release-date/pedropaulofb/langstring)
![GitHub - Last Commit - Branch](https://img.shields.io/github/last-commit/pedropaulofb/langstring/main)
![PyPI - Project](https://img.shields.io/pypi/v/langstring)
![PyPI - Downloads](https://img.shields.io/pypi/dm/langstring)
![Language - Top](https://img.shields.io/github/languages/top/pedropaulofb/langstring)
![Language - Version](https://img.shields.io/pypi/pyversions/langstring)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/pedropaulofb/langstring)
![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/pedropaulofb/langstring/badge)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License - GitHub](https://img.shields.io/github/license/pedropaulofb/langstring)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pedropaulofb/langstring/main.svg)](https://results.pre-commit.ci/latest/github/pedropaulofb/langstring/main)
![Website](https://img.shields.io/website/http/pedropaulofb.github.io/langstring.svg)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/pedropaulofb/langstring/code_testing.yml)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8328/badge)](https://www.bestpractices.dev/projects/8328)

# LangString Python Library

LangString is a Python library designed to handle multilingual text data with precision and flexibility. Although the need for robust management of multilingual content is critical, existing solutions often lack the necessary features to manage language-tagged strings, sets of strings, and collections of multilingual strings effectively. LangString addresses this gap by providing classes and utilities that enable the creation, manipulation, and validation of multilingual text data consistently and accurately. Inspired by [RDFS's langstrings](https://www.w3.org/TR/rdf-schema/), LangString integrates seamlessly into Python applications, offering familiar methods that mimic those of regular Python types, making it intuitive for developers to adopt and use.

**📦 PyPI Package:**
The library is conveniently [available as a PyPI package](https://pypi.org/project/langstring/), allowing users to easily import it into other Python projects.

**📚 Documentation:**
For detailed documentation and code examples, please refer to the library's [docstring-generated documentation](https://pedropaulofb.github.io/langstring).

## Contents

<!-- TOC -->
* [LangString Python Library](#langstring-python-library)
  * [Contents](#contents)
  * [LangString Library](#langstring-library)
    * [Purpose and Contextualization](#purpose-and-contextualization)
    * [Key Components](#key-components)
    * [Practical Use Cases](#practical-use-cases)
    * [Related Work and Differences](#related-work-and-differences)
    * [Installation and Use](#installation-and-use)
  * [LangStrings](#langstrings)
    * [LangStrings’ Methods](#langstrings-methods)
      * [`__init__`](#init)
      * [`to_string`](#tostring)
      * [`__str__`](#str)
      * [`__eq__`](#eq)
      * [`__hash__`](#hash)
  * [MultiLangStrings](#multilangstrings)
    * [MultiLangStrings’ Methods](#multilangstrings-methods)
      * [`__init__`](#init-1)
      * [`add_entry`](#addentry)
      * [`add_langstring`](#addlangstring)
      * [`remove_entry`](#removeentry)
      * [`remove_lang`](#removelang)
      * [`get_langstring`](#getlangstring)
      * [`get_langstrings_lang`](#getlangstringslang)
      * [`get_langstrings_all`](#getlangstringsall)
      * [`get_langstrings_pref_lang`](#getlangstringspreflang)
      * [`get_strings_lang`](#getstringslang)
      * [`get_strings_pref_lang`](#getstringspreflang)
      * [`get_strings_all`](#getstringsall)
      * [`get_strings_langstring_lang`](#getstringslangstringlang)
      * [`get_strings_langstring_pref_lang`](#getstringslangstringpreflang)
      * [`get_strings_langstring_all`](#getstringslangstringall)
      * [`len_entries_all`](#lenentriesall)
      * [`len_entries_lang`](#lenentrieslang)
      * [`len_langs`](#lenlangs)
      * [`__repr__`](#repr)
      * [`__str__`](#str-1)
      * [`__eq__`](#eq-1)
      * [`__hash__`](#hash-1)
  * [Control and Flags](#control-and-flags)
    * [Flags](#flags)
      * [`ENSURE_TEXT`](#ensuretext)
      * [`ENSURE_ANY_LANG`](#ensureanylang)
      * [`ENSURE_VALID_LANG`](#ensurevalidlang)
    * [Control](#control)
      * [Control Methods](#control-methods)
        * [`set_flag`](#setflag)
        * [`get_flag`](#getflag)
        * [`reset_flags`](#resetflags)
        * [`print_flags`](#printflags)
  * [Code Testing](#code-testing)
  * [Version 2: Key Differences and Improvements](#version-2-key-differences-and-improvements)
  * [How to Contribute](#how-to-contribute)
    * [Reporting Issues](#reporting-issues)
    * [Code Contributions](#code-contributions)
    * [Test Contributions](#test-contributions)
    * [General Guidelines](#general-guidelines)
  * [Dependencies](#dependencies)
    * [Using Poetry](#using-poetry)
    * [Using `requirements.txt`](#using-requirementstxt)
  * [License](#license)
  * [Author](#author)
<!-- TOC -->

## Installation and Use

### Basic Installation

Install with:

```bash
pip install langstring
```

## Dependencies

The LangString Python Library is designed with simplicity and ease of use in mind. To achieve this, we have minimized external dependencies.

The LangString Library depends only on the [langcodes package](https://pypi.org/project/langcodes/), particularly for validating language tags when the `ENSURE_VALID_LANG` flag is enabled. This dependency is crucial for ensuring that language tags used in `LangString` and `MultiLangString` instances are valid and conform to international standards, thereby maintaining the integrity and reliability of multilingual text processing.

This project can be set up using either Poetry or `requirements.txt`. Both are kept in sync to ensure consistency in dependencies.

### Installation of Extra Dependencies

### Installation of Dev Dependencies

### Using Poetry

[Poetry](https://python-poetry.org/) is used for easy management of dependencies and packaging. To install the dependencies with Poetry, first [install Poetry](https://python-poetry.org/docs/#installation) if you haven't already, and then run:

```bash
poetry install
```

This will install all the dependencies as specified in `pyproject.toml`.

### Using `requirements.txt`

If you prefer not to use Poetry, a `requirements.txt` file is also provided. You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

This is a straightforward way to set up the project if you are accustomed to using pip and traditional requirements files.

### Usage

After installation, you can use the `LangString` and `MultiLangString` classes in your project. Simply import the classes and start encapsulating strings with their language tags.

```python
from langstring import LangString, MultiLangString, Controller, LangStringFlag, MultiLangStringFlag
```

## Main Elements

### LangStrings

The `LangString` class is a fundamental component of the LangString Library, designed to encapsulate a single string along with its associated language information. It is primarily used in scenarios where the language context of a text string is crucial, such as in multilingual applications, content management systems, or any software that deals with language-specific data. The class provides a structured way to manage text strings, ensuring that each piece of text is correctly associated with its respective language.

In the LangString class, the string representation format varies based on the presence of a language tag. When a language tag is provided, the format is `text`. Without a language tag, it is formatted as `"text"@lang`, where lang is the language code.

### SetLangStrings

TODO

### MultiLangStrings

The `MultiLangString` class is a key component of the LangString Library, designed to manage and manipulate text strings across multiple languages. This class is particularly useful in applications that require handling of text in a multilingual context, such as websites, applications with internationalization support, and data processing tools that deal with multilingual data. The primary purpose of `MultiLangString` is to store, retrieve, and manipulate text entries in various languages, offering a flexible and efficient way to handle multilingual content.


### Controller and Flags

The Control and Flags system in the LangString Library plays a pivotal role in managing and configuring the behavior of `LangString` and `MultiLangString` instances.

This system operates at a global, class-level context, meaning that the flags and controls applied have a uniform effect across all instances of these classes. In other words, when a flag is set or reset using the control classes, it impacts every instance of `LangString` and `MultiLangString` throughout the application. This ensures consistent behavior and validation rules across all instances, as individual instances cannot have differing flag values.

In the following subsections, we will delve into the specifics of the available flags and the control methods. The flags define key aspects of how `LangString` and `MultiLangString` instances handle multilingual text, including validation rules and representation formats. Understanding these flags is crucial for effectively utilizing the library in various scenarios, especially those involving multilingual content.

The control methods, shared between `Controller` and `MultiLangStringControl`, provide the mechanisms to set, retrieve, and reset these flags. These methods ensure that you can dynamically configure the behavior of the library to suit your application's needs. We will explore each method in detail, providing insights into their usage and impact on the library's functionality.

The LangString and MultiLangString classes use a set of flags to control various aspects of their behavior. These flags are managed by `Controller` and `MultiLangStringControl` respectively. The flags provide a flexible way to customize the behavior of `LangString` and `MultiLangString` classes according to the specific needs of your application. By adjusting these flags, you can enforce different levels of validation and control over the language data being processed. The available flags and their effects are as follows.

The Control classes, namely `Controller` and `MultiLangStringControl`, act as static managers for the flags. They provide methods to set, retrieve, and reset the states of these flags, ensuring consistent behavior across all instances of `LangString` and `MultiLangString`.

### Converter

## Code Testing

The code provided has undergone rigorous testing to ensure its reliability and correctness. The tests can be found in the 'tests' directory of the project. To run the tests, navigate to the project root directory and execute the following command:

```bash
langstring> pytest .\tests
```

## How to Contribute

### Reporting Issues

- If you find a bug or wish to suggest a feature, please [open a new issue](https://github.com/pedropaulofb/langstring/issues/new).
- If you notice any discrepancies in the documentation created with the aid of AI, feel free to [report them by opening an issue](https://github.com/pedropaulofb/langstring/issues/new).

### Code Contributions

1. Fork the project repository and create a new feature branch for your work: `git checkout -b feature/YourFeatureName`.
2. Make and commit your changes with descriptive commit messages.
3. Push your work back up to your fork: `git push origin feature/YourFeatureName`.
4. Submit a pull request to propose merging your feature branch into the main project repository.

### Test Contributions

- Enhance the project's reliability by adding new tests or improving existing ones.

### General Guidelines

- Ensure your code follows our coding standards.
- Update the documentation as necessary.
- Make sure your contributions do not introduce new issues.

We appreciate your time and expertise in contributing to this project!

### Related Work and Differences

The LangString Library offers unique functionalities for handling multilingual text in Python applications. While there are several libraries and tools available for internationalization, localization, and language processing, they differ from the LangString Library in scope and functionality. Below is an overview of related work and how they compare to the LangString Library:

- **Babel**
    - https://pypi.org/project/Babel/
    - Babel is a Python library for internationalization and localization. It primarily focuses on formatting dates, numbers, and currency values for different locales.
    - Difference: Unlike Babel, the LangString Library specifically manages multilingual text strings, providing a more direct approach to handling language-specific text data.

- **gettext**
    - https://pypi.org/project/python-gettext/
    - gettext is a GNU system used for internationalizing applications. It allows for translating fixed strings in different languages using message catalogs.
    - Difference: The LangString Library, in contrast, is designed for dynamic management of multilingual content, not just for translation of static strings.

- **langcodes**
    - https://pypi.org/project/langcodes/
    - langcodes provides tools for parsing and understanding language tags.
    - Difference: While langcodes is useful for handling language codes, the LangString Library extends beyond this by managing actual multilingual text strings associated with these codes.

- **Polyglot**
    - https://pypi.org/project/polyglot/
    - Polyglot is a natural language pipeline that supports multiple languages for various NLP tasks.
    - Difference: Polyglot focuses on language processing rather than the structured management of multilingual text, which is the core functionality of the LangString Library.

- **CLD3**
    - https://pypi.org/project/gcld3/
    - Google's CLD3 is a model for language identification.
    - Difference: CLD3 is specialized in detecting the language of a text, whereas the LangString Library is about storing and manipulating text in multiple languages.

- **spaCy**
    - https://pypi.org/project/spacy/
    - spaCy is a comprehensive NLP library that supports multiple languages.
    - Difference: spaCy is geared towards analyzing text, not managing it. The LangString Library, on the other hand, is designed for the structured handling and storage of multilingual text.

In summary, while these related tools and libraries offer valuable functionalities for internationalization, localization, and language processing, the LangString Library stands out for its specific focus on managing and manipulating multilingual text strings in a structured and efficient manner.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/pedropaulofb/langstring/blob/main/LICENSE) file for details.

## Author

This project is an initiative of the [Semantics, Cybersecurity & Services (SCS) Group](https://www.utwente.nl/en/eemcs/scs/) at the [University of Twente](https://www.utwente.nl/), The Netherlands. The main developer is:

- Pedro Paulo Favato Barcelos [[GitHub](https://github.com/pedropaulofb)] [[LinkedIn](https://www.linkedin.com/in/pedro-paulo-favato-barcelos/)]

Feel free to reach out using the provided links. For inquiries, contributions, or to report any issues, you can [open a new issue](https://github.com/pedropaulofb/langstring/issues/new) on this repository.
