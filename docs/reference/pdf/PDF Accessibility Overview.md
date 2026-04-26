---
created: 2026-04-20T20:27:57 (UTC -05:00)
tags: []
source: https://www.adobe.com/accessibility/pdf/pdf-accessibility-overview.html
author: 
---

# PDF Accessibility Overview

> ## Excerpt
> PDF Accessibility ReviewPDF file format accessibility features combined with Adobe® Acrobat® and Adobe Reader® allow universal access to documentsA document or application is considered accessible if 

---
## PDF Accessibility Review

## PDF file format accessibility features combined with Adobe® Acrobat® and Adobe Reader® allow universal access to documents

A document or application is considered accessible if meets certain technical criteria and can be used by people with disabilities. This includes access by people who are mobility impaired, blind, low vision, deaf, hard of hearing, or who have cognitive impairments. Accessibility features in Adobe Acrobat, Adobe Reader and in the Portable Document Format (PDF) make it easier for people with disabilities to use PDF documents and forms, with and without the aid of assistive technology software and devices such as screen readers, screen magnifiers, text-to-speech software, speech recognition software, alternative input devices, Braille embossers, and refreshable Braille displays.

The [Web Content Accessibility Guidelines](http://www.w3.org/TR/WCAG20/) (WCAG) 2.0 ([ISO/IEC 40500:2012](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=58625)) and the [PDF/UA (ISO 14289-1)](http://www.iso.org/iso/catalogue_detail.htm?csnumber=54564) standard cover a wide range of recommendations for making content more accessible to people with disabilities. One benefit of following these guidelines is that content becomes more usable for all users. For example, the underlying document structure that makes it possible for a screen reader to properly read a PDF out loud also makes it possible for a mobile device to correctly reflow and display the document on a small screen. Similarly, the preset tab order of an accessible PDF form helps all users—not just users who rely on the keyboard—complete the form more easily.

## Overview of Portable Document Format (PDF)

The PDF format is the native file format of the Adobe Acrobat family of products. The goal of this format and these products is to enable users to exchange and view electronic documents easily and reliably, independently of the environment in which they were created. PDF relies on the same imaging model as the PostScript® page description language to describe text and graphics in a device-independent and resolution-independent manner. To improve performance for interactive viewing, PDF defines a more structured format than that used by most PostScript language programs. PDF also includes objects, such as annotations and hypertext links, that are not part of the page itself but that are useful for interactive viewing and document interchange.

A logical tagged structure tree is used within each document to provide a meaningful reading order for content, as well as a method for defining structural elements role and relationship to page content. Within this tag structure, other properties such as alternative text and replacement text can be provided.

## Determine the Accessibility Path for each PDF Document

PDF files are created in a variety of ways, from a variety of applications, and for a variety of purposes. Achieving the desired accessibility goals for an individual PDF file requires understanding the nature of the PDF and its intended use. Adobe Acrobat Pro provides several tools including the Make Accessible Menu in the Action Wizard mode and the Accessibility Checker to assist authors in evaluating and fixing issues that can impact accessibility.

The Adobe Acrobat Pro Accessibility Guide: PDF Accessibility Repair Workflow document provides details on how to assess existing PDF files for accessibility. By following these procedures in the recommended order, authors can efficiently proceed through the analysis of a PDF file in a systematic fashion. Systematically ruling out or confirming certain characteristics found in a PDF file will guide the author to the most appropriate path for making an individual PDF document accessible.

## Start with an Accessible Document

The PDF format is a destination file format. PDF files are typically created in some other application. Optimally document accessibility should begin in the native document format. For example, many documents are created in a word processing or desktop publishing application, and then exported as PDF documents. There many things that can be done in native document applications to support accessibility, such as adding alternative text for images; defining structural headings, lists, and data tables; providing document language; and setting document properties such as titles. Adobe desktop publishing applications such as [Adobe InDesign](https://www.adobe.com/products/indesign.html) and [Framemaker](https://www.adobe.com/products/framemaker.html) support these features, as well as other word processing applications such as Microsoft Word. For information on building accessibility into documents created with Adobe products visit the [Adobe Accessibility website](https://www.adobe.com/accessibility.html). To gain assistance on adding accessibility into Microsoft Word documents prior to conversion to PDF format please visit the [Microsoft Enable website](http://www.microsoft.com/enable/). Making the native document accessible allows for less work when changes are made to the native document and the PDF document is regenerated.

If the native document is not available, in most cases, the document can still be made fully accessible. Without accessibility in the native format there will likely be more manual work required in the PDF to properly tag the document. There are some items such as choosing sufficient contrast between foreground and background colors that must be implemented in the native document.

## Characteristics of Accessible PDF files

Accessible PDFs include but are not limited to the following characteristics:

**Searchable text**

A document that consists of scanned images of text is inherently inaccessible because the content of the document is a graphic representing the letters on the page, not searchable text. Assistive technology software cannot read or extract the words in a graphical representation. Furthermore, users cannot select or edit the text or manipulate the PDF for accessibility. Scanned images of text must be converted into to searchable text using optical character recognition (OCR) before addressing accessibility in the document.

**Fonts that allow Characters to be Extracted to Text**

The fonts in an accessible PDF must contain enough information for Acrobat to correctly extract all of the characters to text for purposes other than displaying text on the screen. Acrobat extracts characters to Unicode text when you read a PDF with a screen reader or the Read Out Loud tool, or when you save as text for a Braille embosser. This extraction fails if Acrobat cannot determine how to map the font to Unicode characters.

**Interactive Labeled Form Fields with Accessible Error Messages and No Timing**

Some PDFs contain interactive forms that people fill out using a computer. To be accessible, form fields must be interactive; that is, a user must be able to enter values into the form fields. Interactive PDF forms also have a defined tab order which allows users of assistive technology to use the Tab key in order to progress from one form field or interactive control to the next in a logical manner. Refer to the document Adobe® Acrobat® Pro Accessibility Guide: Creating Accessible Forms for complete details. Forms must provide identification, give tips on proper completion, and prevent errors. Form entry should not be timed unless the user can request more time.

**Other Interactive Features: Hyperlinks and Navigational Aids**

Navigational aids in a PDF — such as links, bookmarks, headings, a table of contents, and a preset tab order for form fields — assist all users in using the document without having to read through the entire document, word by word. Bookmarks are especially useful and can be created from document headings. These features can be accessed using the keyboard without relying on the mouse, and allow for multiple way for users to navigation content.

**Document Language and Title Indication**

Specifying the document language in a PDF enables some screen readers to switch the current speech synthesizer to the appropriate language, allowing correct pronunciation of content in different languages. Providing a document title allows the user to locate and identify the document.

**Security that will not Interfere with Assistive Technology**

Some authors of PDFs restrict users from printing, copying, extracting, editing or adding comments to text. The text of an accessible PDF must be available to a screen reader. Acrobat’s security settings can be set to protect document content while not interfering with a screen reader’s ability to convert the on-screen text to speech or Braille.

**Document Structure Tags and Proper Reading Order**

To read a document’s text and present it in a way that makes sense to the user, a screen reader or other text-to-speech tool requires that the document be structured. Document structure tags in a PDF define the reading order and identify headings, paragraphs, sections, tables and other page elements. The tags structure also allows for documents to be resized and reflowed for viewing at larger sizes and on mobile devices.

**Alternative Text Descriptions for Non-Text Elements**

Document features such as images and interactive form fields cannot be understood by the user of a screen reader unless they have associated alternative text. Though link text is available to screen reader users, it is possible to provide more meaningful descriptions via replacement (actual) text. Alternative text for images and tooltips can aid many users, including those with learning disabilities. Equivalents for multimedia, including any audio and video elements, must also be present.

## Other Accessible Document Characteristics

There are additional characteristics of accessible documents including:

## Start with an Accessible Document

-   No reliance on color or sensory characteristics alone to convey meaning
-   Use of color combinations that provides a sufficient degree of contrast
-   Controls for audio
-   Use of text instead of images of text
-   No use of flashing or blinking elements
-   No focus changes without user initiation
-   Consistent navigation and identification of elements

## Adobe Acrobat and Adobe Acrobat Reader Accessibility Features

Accessibility features in Adobe Acrobat and Adobe Acrobat Reader fall into two broad categories: features that make the reading of PDF documents more accessible, and features that help create accessible PDF documents. To create accessible PDF documents, you must use Acrobat Pro.

**Features to Support the Reading of PDFs by People with Disabilities**

All versions of Adobe Acrobat, Adobe Acrobat Reader, Acrobat Standard and Acrobat Pro provide support for the accessible reading of PDF files by persons with disabilities:

-   Preferences and commands to optimize output for assistive technology software and devices, such as saving as accessible text for a Braille printer
-   Preferences and commands to make navigation of PDFs more accessible, such as automatic scrolling and opening PDFs to the last page read
-   An Accessibility Setup Assistant Wizard for easy setting of most preferences related to accessibility
-   Keyboard alternatives to mouse actions
-   Reflow capability to temporarily present the text of a PDF in a single, easy-to-read column
-   Read Out Loud text-to-speech conversion
-   Support for screen readers and screen magnifiers
-   Support for high contrast and alternative foreground and background colors

**Features to Support the Creation of Accessible PDFs**

-   Creation of tagged PDFs from authoring applications
-   Conversion of untagged PDFs to tagged PDFs from within Acrobat
-   Security settings that allow screen readers to access text while preventing users from copying, printing, editing and extracting text
-   Ability to add text to scanned pages to improve accessibility
-   Tools for editing reading order and document structure
-   Tools for creating accessible PDF forms
-   Ability to set document properties including title and expose them through the title bar of the application

Though Acrobat Standard provides some functionality for making existing PDFs accessible, Acrobat Pro must be used to perform most tasks — such as editing reading order or editing document structure tags — that are necessary to make PDF documents and forms accessible (For more information see Comparison of Accessibility Features in Adobe Acrobat Plans).

## The Acrobat Pro Accessibility Guide Series

Adobe has created a series of accessibility guides for Adobe Acrobat Pro to assist content authors in creating accessible PDF documents. There are four guides in this series:

**PDF Accessibility Overview (this document)**

The Adobe Acrobat Pro Accessibility Guide: PDF Accessibility Overview details what is meant by accessibility in the PDF file format. It distinguishes between the accessibility features of the file format, of Adobe Acrobat and of the Adobe Acrobat Reader application, and how the features of the software and the file format interact to achieve accessibility for people with disabilities.

**Acrobat Pro PDF Accessibility Repair Workflow**

The Adobe Acrobat Pro Accessibility Guide: PDF Accessibility Repair Workflow provides a step-by-step method for analyzing existing PDF files and making them accessible based upon that analysis. This workflow coincides with the workflow provided in the Make Accessible Action wizard and potential issues tested for in the Accessibility Checker tool.

**Using the Accessibility Checker in Acrobat Pro**

The Adobe Acrobat Pro Accessibility Guide: Using the Accessibility Checker describes the PDF accessibility checkers that are included in Adobe Acrobat Pro. Even if you generate an accessible PDF file from an authoring application such a word processor or desktop publishing program, you should then follow the steps in this guide in order to identify any items that may have been missed in the initial conversion, or to add PDF accessibility features that were not provided by the authoring tool.

**Creating Accessible PDF Forms with Acrobat Pro**

The guide entitled Adobe Acrobat Pro Accessibility Guide: Creating Accessible Forms describes how to use the forms tools within Adobe Acrobat Pro to add descriptions to form fields, tag untagged forms, set the tab order, manipulate tags and perform other PDF accessibility tasks. These techniques do not apply to PDF forms from Adobe LiveCycle Designer, as a separate process is provided for making LiveCycle forms accessible.
