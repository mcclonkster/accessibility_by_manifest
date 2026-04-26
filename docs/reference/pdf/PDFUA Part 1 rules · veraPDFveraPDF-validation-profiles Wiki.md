---
created: 2026-04-20T21:47:45 (UTC -05:00)
tags: []
source: https://github.com/veraPDF/veraPDF-validation-profiles/wiki/PDFUA-Part-1-rules/
author: 
---

# PDFUA Part 1 rules · veraPDF/veraPDF-validation-profiles Wiki

> ## Excerpt
> PDF/UA-1 validation rules The PDF/UA version and conformance level of a file shall be specified using the PDF/UA Identification extension schema. The document metadata stream doesn't contain PDF/UA Id

---
# PDF/UA-1 validation rules

> _The PDF/UA version and conformance level of a file shall be specified using the PDF/UA Identification extension schema._

The document metadata stream doesn't contain PDF/UA Identification Schema.

-   Object type: `MainXMPPackage`
-   Test condition: `containsPDFUAIdentification == true`
-   Specification: ISO 14289-1:2014

> _The value of "pdfuaid:part" shall be the part number of the International Standard to which the file conforms._

The "part" property of the PDF/UA Identification Schema is not 1 for PDF/UA-1 conforming file.

-   Object type: `PDFUAIdentification`
-   Test condition: `part == 1`
-   Specification: ISO 14289-1:2014

> _Property "part" of the PDF/UA Identification Schema shall have namespace prefix "pdfuaid"_

Property "part" of the PDF/UA Identification Schema has an invalid namespace prefix

-   Object type: `PDFUAIdentification`
-   Test condition: `partPrefix == null || partPrefix == "pdfuaid"`
-   Specification: ISO 14289-1:2014

> _Property "amd" of the PDF/UA Identification Schema shall have namespace prefix "pdfuaid"_

Property "amd" of the PDF/UA Identification Schema has an invalid namespace prefix

-   Object type: `PDFUAIdentification`
-   Test condition: `amdPrefix == null || amdPrefix == "pdfuaid"`
-   Specification: ISO 14289-1:2014

> _Property "corr" of the PDF/UA Identification Schema shall have namespace prefix "pdfuaid"_

Property "corr" of the PDF/UA Identification Schema has an invalid namespace prefix

-   Object type: `PDFUAIdentification`
-   Test condition: `corrPrefix == null || corrPrefix == "pdfuaid"`
-   Specification: ISO 14289-1:2014

> _The file header shall consist of "%PDF-1.n" followed by a single EOL marker, where 'n' is a single digit number between 0 (30h) and 7 (37h)_

A file header does not match the pattern %PDF-1.n, where 'n' is a single digit number between 0 and 7

-   Object type: `CosDocument`
-   Test condition: `/^%PDF-1\.[0-7]$/.test(header)`
-   Specification: ISO 14289-1:2014

> _The document catalog dictionary shall include a MarkInfo dictionary containing an entry, Marked, whose value shall be true._

MarkInfo dictionary is not present in the document catalog, or Marked entry is set to false or is not present in the MarkInfo dictionary.

This setting indicates that the file conforms to the Tagged PDF conventions.

-   Object type: `CosDocument`
-   Test condition: `Marked == true`
-   Specifications: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.7.1

> _Content marked as Artifact should not be present inside tagged content_

Content marked as Artifact is present inside tagged content

-   Object type: `SEMarkedContent`
-   Test condition: `tag != 'Artifact' || isTaggedContent == false`
-   Specification: ISO 14289-1:2014

> _Tagged content should not be present inside content marked as Artifact_

Tagged content is present inside content marked as Artifact

-   Object type: `SEMarkedContent`
-   Test condition: `isTaggedContent == false || parentsTags.contains('Artifact') == false`
-   Specification: ISO 14289-1:2014

> _Content shall be marked as Artifact or tagged as real content_

Content is neither marked as Artifact nor tagged as real content

-   Object type: `SESimpleContentItem`
-   Test condition: `isTaggedContent == true || parentsTags.contains('Artifact') == true`
-   Specification: ISO 14289-1:2014

> _Files shall have a Suspects value of false(ISO 32000-1:2008, Table 321)_

Suspects entry has a value of true

-   Object type: `CosDocument`
-   Test condition: `Suspects != true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.7.1

> _All non-standard structure types shall be mapped to the nearest functionally equivalent standard type, as defined in ISO 32000-1:2008, 14.8.4, in the role map dictionary of the structure tree root. This mapping may be indirect; within the role map a non-standard type can map directly to another non-standard type, but eventually the mapping shall terminate at a standard type._

Non-standard structure type is not mapped to a standard type

-   Object type: `SENonStandard`
-   Test condition: `isNotMappedToStandardType == false`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4

> _A circular mapping shall not exist_

A circular mapping exists

-   Object type: `PDStructElem`
-   Test condition: `circularMappingExist != true`
-   Specification: ISO 14289-1:2014

> _Standard tags defined in ISO 32000-1:2008, 14.8.4, shall not be remapped._

Standard type is remapped

-   Object type: `PDStructElem`
-   Test condition: `remappedStandardType == null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4

> _The Catalog dictionary of a conforming file shall contain the Metadata key whose value is a metadata stream as defined in ISO 32000-1:2008, 14.3.2. The metadata stream dictionary shall contain entry Type with value /Metadata and entry Subtype with value /XML_

The document catalog dictionary doesn't contain metadata key or metadata stream dictionary does not contain either entry Type with value /Metadata or entry Subtype with value /XML.

-   Object type: `PDDocument`
-   Test condition: `containsMetadata == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.3.2

> _The Metadata stream in the document's catalog dictionary shall contain a dc:title entry, where dc is the recommended prefix for the Dublin Core metadata schema as defined in the XMP specification, which clearly identifies the document._

Metadata stream does not contain dc:title

-   Object type: `MainXMPPackage`
-   Test condition: `dc_title != null`
-   Specification: ISO 14289-1:2014

> _The document catalog dictionary shall include a ViewerPreferences dictionary containing a DisplayDocTitle key, whose value shall be true._

ViewerPreferences dictionary is not present in the document Catalog, or DisplayDocTitle key is set to false or is not present in the ViewerPreferences dictionary.

-   Object type: `CosDocument`
-   Test condition: `DisplayDocTitle == true`
-   Specification: ISO 14289-1:2014

> _The logical structure of the conforming file shall be described by a structure hierarchy rooted in the StructTreeRoot entry of the document's Catalog dictionary, as described in ISO 32000-1:2008, 14.7._

StructTreeRoot entry is not present in the document catalog

The logical structure of a document is described by a hierarchy of objects called the structure hierarchy or structure tree. At the root of the hierarchy is a dictionary object called the structure tree root, located via the StructTreeRoot entry in the document catalog.

-   Object type: `PDDocument`
-   Test condition: `containsStructTreeRoot == true`
-   Specifications: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.7

> _A structure element dictionary shall contain the P (parent) entry according to ISO 32000-1:2008, 14.7.2, Table 355_

A structure element dictionary does not contain the P (parent) entry

-   Object type: `PDStructElem`
-   Test condition: `containsParent == true`
-   Specifications: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.7.2, Table 355

> _Natural language in the Outline entries shall be determined_

Natural language in the Outline entries cannot be determined

-   Object type: `PDOutline`
-   Test condition: `gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Table element may contain only TR, THead, TBody, TFoot and Caption elements_

Table element contains element(s) different from TR, THead, TBode, TFoot or Caption

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem != 'TR' && elem != 'THead' && elem != 'TBody' && elem != 'TFoot' && elem != 'Caption').length == 0 || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TR element should be contained in Table, THead, TBody or TFoot element_

TR element not contained in Table, THead, TBody and TFoot element

-   Object type: `SETR`
-   Test condition: `/^(Table|THead|TBody|TFoot)$/.test(parentStandardType)`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _THead element should be contained in Table element_

THead element not contained in Table element

-   Object type: `SETHead`
-   Test condition: `parentStandardType == 'Table'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TBody element should be contained in Table element_

TBody element not contained in Table element

-   Object type: `SETBody`
-   Test condition: `parentStandardType == 'Table'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TFoot element should be contained in Table element_

TFoot element not contained in Table element

-   Object type: `SETFoot`
-   Test condition: `parentStandardType == 'Table'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TH element should be contained in TR element_

TH element not contained in TR element

-   Object type: `SETH`
-   Test condition: `parentStandardType == 'TR'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TD element should be contained in TR element_

TD element not contained in TR element

-   Object type: `SETD`
-   Test condition: `parentStandardType == 'TR'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TR element may contain only TH and TD elements_

TR element contains not a TH or TD elements

-   Object type: `SETR`
-   Test condition: `/^(TH|TD)(&(TH|TD))*$/.test(kidsStandardTypes) || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Table element should contain zero or one THead kid_

Table element contains more than one THead kid

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem == 'THead').length <= 1`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Table element should contain zero or one TFoot kid_

Table element contains more than one TFoot kid

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem == 'TFoot').length <= 1`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _If Table element contains TFoot kid, Table element should contain one or more TBody kids_

Table element contains TFoot kid, but does not contain TBody kids

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem == 'TFoot').length == 0 || kidsStandardTypes.split('&').filter(elem => elem == 'TBody').length > 0`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _If Table element contains THead kid, Table element should contain one or more TBody kids_

Table element contains THead kid, but does not contain TBody kids

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem == 'THead').length == 0 || kidsStandardTypes.split('&').filter(elem => elem == 'TBody').length > 0`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _A table cell shall not have intersection with other cells_

Table cell has intersection with other cells

-   Object type: `SETableCell`
-   Test condition: `hasIntersection != true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Table element may contain a Caption element as its first or last kid_

Table element contains Caption not as its first or last child

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.indexOf('&Caption&') < 0`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _LI element should be contained in L element_

LI element not contained in L element

-   Object type: `SELI`
-   Test condition: `parentStandardType == 'L'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.3

> _LBody element should be contained in LI element_

LBody element not contained in LI element

-   Object type: `SELBody`
-   Test condition: `parentStandardType == 'LI'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.3

> _L element may contain only L, LI and Caption elements_

L element contains element(s) different from L, LI or Caption

-   Object type: `SEL`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem != 'L' && elem != 'LI' && elem != 'Caption').length == 0 || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.3

> _LI element may contain only Lbl and LBody elements_

LI element contains not a Lbl or LBody elements

-   Object type: `SELI`
-   Test condition: `/^(Lbl|LBody)(&(Lbl|LBody))*$/.test(kidsStandardTypes) || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.3

> _Natural language for text in ActualText attribute shall be determined_

Natural language for text in ActualText attribute cannot be determined

-   Object type: `PDStructElem`
-   Test condition: `ActualText == null || containsLang == true || parentLang != null || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language for text in Alt attribute shall be determined_

Natural language for text in Alt attribute cannot be determined

-   Object type: `PDStructElem`
-   Test condition: `Alt == null || containsLang == true || parentLang != null || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language for text in E attribute shall be determined_

Natural language for text in E attribute cannot be determined

-   Object type: `PDStructElem`
-   Test condition: `E == null || containsLang == true || parentLang != null || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language in the Contents entry for annotations shall be determined_

Natural language in the Contents entry for annotations cannot be determined

-   Object type: `PDAnnot`
-   Test condition: `Contents == null || containsLang == true || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language in the TU key for form fields shall be determined_

Natural language in the TU key for form fields cannot be determined

-   Object type: `PDFormField`
-   Test condition: `TU == null || containsLang == true || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _TOCI element should be contained in TOC element_

TOCI element not contained in TOC element

-   Object type: `SETOCI`
-   Test condition: `parentStandardType == 'TOC'`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.2

> _TOC element may contain only TOC, TOCI and Caption elements_

TOC element contains element(s) different from TOC, TOCI or Caption

-   Object type: `SETOC`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem != 'TOC' && elem != 'TOCI' && elem != 'Caption').length == 0 || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.2

> _TOC element may contain a Caption element only as its first kid_

TOC element contains Caption child not as its first one

-   Object type: `SETOC`
-   Test condition: `kidsStandardTypes == '' || kidsStandardTypes.split('&').slice(1).findIndex(elem => elem == 'Caption') < 0`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.2

> _If the Lang entry is present in the document's Catalog dictionary or in a structure element dictionary or property list, its value shall be a language identifier as described in ISO 32000-1:2008, 14.9.2. A language identifier shall be a Language-Tag as defined in RFC 3066, Tags for the Identification of Languages._

Value of the Lang entry is not a Language-Tag

-   Object type: `CosLang`
-   Test condition: `/^[a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})*$/.test(unicodeValue)`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.9.2
    -   RFC 3066, 2.1

> _Natural language for text in ActualText attribute in Span Marked Content shall be determined_

Natural language for text in ActualText attribute in Span Marked Content cannot be determined

-   Object type: `SEMarkedContent`
-   Test condition: `tag != 'Span' || ActualText == null || Lang != null || inheritedLang != null || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language for text in Alt attribute in Span Marked Content shall be determined_

Natural language for text in Alt attribute in Span Marked Content cannot be determined

-   Object type: `SEMarkedContent`
-   Test condition: `tag != 'Span' || Alt == null || Lang != null || inheritedLang != null || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language for text in E attribute in Span Marked Content shall be determined_

Natural language for text in E attribute in Span Marked Content cannot be determined

-   Object type: `SEMarkedContent`
-   Test condition: `tag != 'Span' || E == null || Lang != null || inheritedLang != null || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language for document metadata shall be determined_

Natural language for document metadata cannot be determined

-   Object type: `XMPLangAlt`
-   Test condition: `xDefault == false || gContainsCatalogLang == true`
-   Specification: ISO 14289-1:2014

> _Natural language for text in page content shall be determined_

Natural language for text in page content cannot be determined

-   Object type: `SETextItem`
-   Test condition: `gContainsCatalogLang == true || Lang != null`
-   Specification: ISO 14289-1:2014

> _THead element may contain only TR elements_

THead element contains not a TR elements

-   Object type: `SETHead`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem != 'TR').length == 0 || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TBody element may contain only TR elements_

TBody element contains not a TR elements

-   Object type: `SETBody`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem != 'TR').length == 0 || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _TFoot element may contain only TR elements_

TFoot element contains not a TR elements

-   Object type: `SETFoot`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem != 'TR').length == 0 || kidsStandardTypes == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Table element may contain only one Caption element_

Table element contains several Caption elements instead of one

-   Object type: `SETable`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem == 'Caption').length < 2`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _L element may contain a Caption element only as its first kid_

L element contains Caption child not as its first one

-   Object type: `SEL`
-   Test condition: `kidsStandardTypes == '' || kidsStandardTypes.split('&').slice(1).findIndex(elem => elem == 'Caption') < 0`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.2

> _Table columns shall have the same number of rows (taking into account row spans)_

Some table columns span different number of rows

-   Object type: `SETable`
-   Test condition: `numberOfColumnWithWrongRowSpan == null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Table rows shall have the same number of columns (taking into account column spans)_

Some table rows span different number of columns

-   Object type: `SETable`
-   Test condition: `numberOfRowWithWrongColumnSpan == null || wrongColumnSpan != null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Table rows shall have the same number of columns (taking into account column spans)_

Some table rows span different number of columns

-   Object type: `SETable`
-   Test condition: `numberOfRowWithWrongColumnSpan == null || wrongColumnSpan == null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.4

> _Figure tags shall include an alternative representation or replacement text that represents the contents marked with the Figure tag as noted in ISO 32000-1:2008, 14.7.2, Table 323_

Figure structure element neither has an alternate description nor a replacement text

-   Object type: `SEFigure`
-   Test condition: `(Alt != null && Alt != '') || ActualText != null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.7.2

> _For documents that are not strongly structured, as described in ISO 32000-1:2008, 14.8.4.3.5, heading tags shall be used as follows:_

> -   _If any heading tags are used, H1 shall be the first._

> -   _A document may use more than one instance of any specific tag level. For example, a tag level may be repeated if document content requires it._

> -   _If document semantics require a descending sequence of headers, such a sequence shall proceed in strict numerical order and shall not skip an intervening heading level._

> -   _A document may increment its heading sequence without restarting at H1 if document semantics require it._

A heading level is skipped in a descending sequence of header levels

-   Object type: `SEHn`
-   Test condition: `hasCorrectNestingLevel == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.3.5

> _Each node in the tag tree shall contain at most one child H tag._

A node contains more than one H tag

-   Object type: `PDStructElem`
-   Test condition: `kidsStandardTypes.split('&').filter(elem => elem == 'H').length <= 1`
-   Specification: ISO 14289-1:2014

> _All documents shall be either strongly or weakly structured, but not both._

Document uses both H and H# tags

-   Object type: `SEH`
-   Test condition: `usesHn == false`
-   Specification: ISO 14289-1:2014

> _All documents shall be either strongly or weakly structured, but not both._

Document uses both H and H# tags

-   Object type: `SEHn`
-   Test condition: `usesH == false`
-   Specification: ISO 14289-1:2014

> _If the table's structure is not determinable via Headers and IDs, then structure elements of type TH shall have a Scope attribute_

TD does not contain Headers attribute, and Headers for this table cell can not be determined via algorithm from ISO 32000-2, 14.8.4.8.3.

-   Object type: `SETD`
-   Test condition: `hasConnectedHeader != false || unknownHeaders != ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-2, 14.8.4.8.3

> _If the table's structure is not determinable via Headers and IDs, then structure elements of type TH shall have a Scope attribute_

TD references undefined Header(s), and Headers for this table cell can not be determined via algorithm from ISO 32000-2, 14.8.4.8.3.

-   Object type: `SETD`
-   Test condition: `hasConnectedHeader != false || unknownHeaders == ''`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-2, 14.8.4.8.3

> _All mathematical expressions shall be enclosed within a Formula tag as detailed in ISO 32000-1:2008, 14.8.4.5 and shall have Alt or ActualText attributes_

Formula structure element neither has an alternate description nor a replacement text

-   Object type: `SEFormula`
-   Test condition: `(Alt != null && Alt != '') || ActualText != null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.5

> _Note tag shall have ID entry_

ID key of the Note tag is not present

-   Object type: `SENote`
-   Test condition: `noteID != null && noteID != ''`
-   Specification: ISO 14289-1:2014

> _Each Note tag shall have unique ID key_

ID key of the Note tag is non-unique

-   Object type: `SENote`
-   Test condition: `hasDuplicateNoteID == false`
-   Specification: ISO 14289-1:2014

> _Each optional content configuration dictionary that forms the value of the D key, or that is an element in the array that forms the value of the Configs key in the OCProperties dictionary, shall contain the Name key._

Missing or empty Name entry of the optional content configuration dictionary

-   Object type: `PDOCConfig`
-   Test condition: `Name != null && Name.length() > 0`
-   Specification: ISO 14289-1:2014

> _The AS key shall not appear in any optional content configuration dictionary._

AS key is present in the optional content configuration dictionary

-   Object type: `PDOCConfig`
-   Test condition: `AS == null`
-   Specification: ISO 14289-1:2014

> _The file specification dictionary for an embedded file shall contain the non-empty F and UF keys_

The file specification dictionary for an embedded file does not contain either F or EF key or at least one of the keys is empty

-   Object type: `CosFileSpecification`
-   Test condition: `containsEF == false || (F != null && F != '' && UF != null && UF != '')`
-   Specification: ISO 14289-1:2014

> _Dynamic XFA forms shall not be used_

Dynamic XFA forms is present

-   Object type: `PDAcroForm`
-   Test condition: `dynamicRender != 'required'`
-   Specification: ISO 14289-1:2014

> _An encrypted conforming file shall contain a P key in its encryption dictionary (ISO 32000-1:2008, 7.6.3.2, Table 21). The 10th bit position of the P key shall be true._

The file is encrypted but does not contain a P entry in its encryption dictionary or the file is encrypted and does contain a P entry, but the 10th bit position of the P entry is false

-   Object type: `PDEncryption`
-   Test condition: `P != null && (P & 512) == 512`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 7.6.3.2

> _An annotation, excluding annotations of subtype Widget, PrinterMark or Link, shall be nested within an Annot tag_

An annotation, excluding annotations of subtype Widget, PrinterMark or Link, is an Artifact or is not nested within an Annot tag

-   Object type: `PDAnnot`
-   Test condition: `Subtype == 'Widget' || Subtype == 'PrinterMark' || Subtype == 'Link' || isOutsideCropBox == true || (F & 2) == 2 || structParentStandardType == 'Annot'`
-   Specification: ISO 14289-1:2014

> _An annotation (except Widget annotations or hidden annotations, or those having rectangle outside the crop-box) shall have either Contents key or an Alt entry in the enclosing structure element_

An annotation whose hidden flag is not set and whose rectangle is not outside the crop-box has neither Contents key nor an Alt entry in the enclosing structure element

-   Object type: `PDAnnot`
-   Test condition: `Subtype == 'Widget' || isOutsideCropBox == true || (F & 2) == 2 || (Contents != null && Contents != '') || (Alt != null && Alt != '')`
-   Specification: ISO 14289-1:2014

> _A form field shall have a TU key present or all its Widget annotations shall have alternative descriptions (in the form of an Alt entry in the enclosing structure elements)_

A form field neither has TU key nor its Widget annotations have alternative descriptions (in the form of an Alt entry in the enclosing structure element)

-   Object type: `PDWidgetAnnot`
-   Test condition: `isOutsideCropBox == true || (F & 2) == 2 || (TU != null && TU != '') || (Alt != null && Alt != '')`
-   Specification: ISO 14289-1:2014

> _Annotations of subtype TrapNet shall not be permitted._

An annotation of subtype TrapNet exists

-   Object type: `PDTrapNetAnnot`
-   Test condition: `isOutsideCropBox == true || (F & 2) == 2`
-   Specification: ISO 14289-1:2014

> _Every page on which there is an annotation shall contain in its page dictionary the key Tabs, and its value shall be S._

A page with annotation(s) does not contain a Tabs key or has a Tabs key with a value other than S.

-   Object type: `PDPage`
-   Test condition: `containsAnnotations == false || Tabs == 'S'`
-   Specification: ISO 14289-1:2014

> _A Widget annotation shall be nested within a Form tag per ISO 32000-1:2008, 14.8.4.5, Table 340._

A widget annotation is an Artifact or is not nested within a Form tag

-   Object type: `PDWidgetAnnot`
-   Test condition: `structParentStandardType == 'Form' || isOutsideCropBox == true || (F & 2) == 2`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.5

> _If the Form element omits a Role attribute (Table 348), it shall have only one child: an object reference (14.7.4.3) identifying the widget annotation per ISO 32000-1:2008, 14.8.4.5, Table 340._

The Form element omits a Role attribute and doesn't have only one child identifying the widget annotation

-   Object type: `SEForm`
-   Test condition: `roleAttribute != null || hasOneInteractiveChild == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.5

> _Links shall be tagged according to ISO 32000-1:2008, 14.8.4.4.2, Link Element._

A link annotation is an Artifact or is not nested within a Link tag

-   Object type: `PDLinkAnnot`
-   Test condition: `structParentStandardType == 'Link' || isOutsideCropBox == true || (F & 2) == 2`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.4.4.2

> _Links shall contain an alternate description via their Contents key as described in ISO 32000-1:2008, 14.9.3._

A link annotation does not include an alternate description in the Contents Key

-   Object type: `PDLinkAnnot`
-   Test condition: `(Contents != null && Contents != '') || isOutsideCropBox == true || (F & 2) == 2`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.9.3

> _In the media clip data dictionary, the optional CT key (ISO 32000-1:2008, 13.2.4.2, Table 274) is required._

CT key is missing from the media clip data dictionary.

-   Object type: `PDMediaClip`
-   Test condition: `CT != null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 13.2.4.2

> _In the media clip data dictionary, the optional Alt key (ISO 32000-1:2008, 13.2.4.2, Table 274) is required._

Alt key is missing from the media clip data dictionary

-   Object type: `PDMediaClip`
-   Test condition: `hasCorrectAlt == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 13.2.4.2

> _PrinterMark annotations, if present, shall be considered Incidental Artifacts, as if they are hidden page elements as defined in ISO 32000-1:2008, 14.8.2.2.3._

A PrinterMark annotation is included in logical structure

-   Object type: `PDPrinterMarkAnnot`
-   Test condition: `structParentType == null || isOutsideCropBox == true || (F & 2) == 2`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.8.2.2.3

> _A conforming file shall not contain any reference XObjects_

The document contains a reference XObject (Ref key in the form XObject dictionary)

Reference XObjects enable one PDF document to import content from another. The document in which the reference occurs is called the containing document; the one whose content is being imported is the target document. The target document may reside in a file external to the containing document or may be included within it as an embedded file stream.

As this makes the initial PDF document dependent on the presence of external resources, this mechanism is not permitted in PDF/UA-compliant documents.

-   Object type: `PDXForm`
-   Test condition: `containsRef == false`
-   Specification: ISO 14289-1:2014

> _The content of Form XObjects shall be incorporated into structure elements according to ISO 32000-1:2008, 14.7.2._

Form XObject contains MCIDs and is referenced more than once

-   Object type: `PDXForm`
-   Test condition: `isUniqueSemanticParent == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 14.7.2

> _For any given composite (Type 0) font within a conforming file, the CIDSystemInfo entry in its CIDFont dictionary and its Encoding dictionary shall have the following relationship:_
> 
> -   _If the Encoding key in the Type 0 font dictionary is Identity-H or Identity-V, any values of Registry, Ordering, and Supplement may be used in the CIDSystemInfo entry of the CIDFont._
> -   _Otherwise, the corresponding Registry and Ordering strings in both CIDSystemInfo dictionaries shall be identical, and the value of the Supplement key in the CIDSystemInfo dictionary of the CIDFont shall be less than or equal to the Supplement key in the CIDSystemInfo dictionary of the CMap._

CIDSystemInfo entries the CIDFont and CMap dictionaries of a Type 0 font are not compatible

CIDFont and CMap dictionaries contain a CIDSystemInfo entry specifying the character collection assumed by the CIDFont or by each CIDFont associated with the CMap - that is, the interpretation of the CID numbers used by the CIDFont. A character collection is uniquely identified by the Registry, Ordering, and Supplement entries in the CIDSystemInfo dictionary. Character collections whose Registry and Ordering values are the same are compatible.

PDF/UA-1 standard requires that the Registry and Ordering strings of the CIDSystemInfo dictionaries for that font shall be identical and the value of the Supplement key in the CIDSystemInfo dictionary of the CIDFont shall be less than or equal to the Supplement key in the CIDSystemInfo dictionary of the CMap, unless the value of the CMap dictionary UserCMap key is "Identity-H" or "Identity-V".

-   Object type: `PDType0Font`
-   Test condition: `cmapName == "Identity-H" || cmapName == "Identity-V" || (CIDFontOrdering != null && CIDFontOrdering == CMapOrdering && CIDFontRegistry != null && CIDFontRegistry == CMapRegistry && CIDFontSupplement != null && CMapSupplement != null && CIDFontSupplement <= CMapSupplement)`
-   Specification: ISO 14289-1:2014

> _ISO 32000-1:2008, 9.7.4, Table 117 requires that all embedded Type 2 CIDFonts in the CIDFont dictionary shall contain a CIDToGIDMap entry that shall be a stream mapping from CIDs to glyph indices or the name Identity, as described in ISO 32000-1:2008, 9.7.4, Table 117._

A Type 2 CIDFont dictionary has missing or invalid CIDToGIDMap entry

For Type 2, the CIDFont program is actually a TrueType font program, which has no native notion of CIDs. In a TrueType font program, glyph descriptions are identified by glyph index values. Glyph indices are internal to the font and are not defined consistently from one font to another. Instead, a TrueType font program contains a "cmap" table that provides mappings directly from character codes to glyph indices for one or more predefined encodings.

If the TrueType font program is embedded, the Type 2 CIDFont dictionary must contain a CIDToGIDMap entry that maps CIDs to the glyph indices for the appropriate glyph descriptions in that font program.

-   Object type: `PDCIDFont`
-   Test condition: `Subtype != "CIDFontType2" || CIDToGIDMap != null || containsFontFile == false`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 9.7.4, Table 117

> _All CMaps used within a PDF/UA file, except those listed in ISO 32000-1:2008, 9.7.5.2, Table 118, shall be embedded in that file as described in ISO 32000-1:2008, 9.7.5._

A non-standard CMap is not embedded

-   Object type: `PDCMap`
-   Test condition: `CMapName == "Identity-H" || CMapName == "Identity-V" || CMapName == "GB-EUC-H" || CMapName == "GB-EUC-V" || CMapName == "GBpc-EUC-H" || CMapName == "GBpc-EUC-V" || CMapName == "GBK-EUC-H" || CMapName == "GBK-EUC-V" || CMapName == "GBKp-EUC-H" || CMapName == "GBKp-EUC-V" || CMapName == "GBK2K-H" || CMapName == "GBK2K-V" || CMapName == "UniGB-UCS2-H" || CMapName == "UniGB-UCS2-V" || CMapName == "UniGB-UFT16-H" || CMapName == "UniGB-UFT16-V" || CMapName == "B5pc-H" || CMapName == "B5pc-V" || CMapName == "HKscs-B5-H" || CMapName == "HKscs-B5-V" || CMapName == "ETen-B5-H" || CMapName == "ETen-B5-V" || CMapName == "ETenms-B5-H" || CMapName == "ETenms-B5-V" || CMapName == "CNS-EUC-H" || CMapName == "CNS-EUC-V" || CMapName == "UniCNS-UCS2-H" || CMapName == "UniCNS-UCS2-V" || CMapName == "UniCNS-UFT16-H" || CMapName == "UniCNS-UTF16-V" || CMapName == "83pv-RKSJ-H" || CMapName == "90ms-RKSJ-H" || CMapName == "90ms-RKSJ-V" || CMapName == "90msp-RKSJ-H" || CMapName == "90msp-RKSJ-V" || CMapName == "90pv-RKSJ-H" || CMapName == "Add-RKSJ-H" || CMapName == "Add-RKSJ-V" || CMapName == "EUC-H" || CMapName == "EUC-V" || CMapName == "Ext-RKSJ-H" || CMapName == "Ext-RKSJ-V" || CMapName == "H" || CMapName == "V" || CMapName == "UniJIS-UCS2-H" || CMapName == "UniJIS-UCS2-V" || CMapName == "UniJIS-UCS2-HW-H" || CMapName == "UniJIS-UCS2-HW-V" || CMapName == "UniJIS-UTF16-H" || CMapName == "UniJIS-UTF16-V" || CMapName == "KSC-EUC-H" || CMapName == "KSC-EUC-V" || CMapName == "KSCms-UHC-H" || CMapName == "KSCms-UHC-V" || CMapName == "KSCms-UHC-HW-H" || CMapName == "KSCms-UHC-HW-V" || CMapName == "KSCpc-EUC-H" || CMapName == "UniKS-UCS2-H" || CMapName == "UniKS-UCS2-V" || CMapName == "UniKS-UTF16-H" || CMapName == "UniKS-UTF16-V" || containsEmbeddedFile == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 9.7.5.2, Table 118

> _For those CMaps that are embedded, the integer value of the WMode entry in the CMap dictionary shall be identical to the WMode value in the embedded CMap stream._

WMode entry in the embedded CMap and in the CMap dictionary are not identical

A CMap also specifies the writing mode (horizontal or vertical) for any CIDFont with which the CMap is combined. This determines which metrics are to be used when glyphs are painted from that font.

In case of embedded CMap file, the writing mode is specified in two different places: in the PDF dictionary associated with the embedded CMap, and inside the embedded CMap file itself. To avoid any ambiguities, PDF/A standard requires that values of these two writing modes coincide.

-   Object type: `CMapFile`
-   Test condition: `WMode == dictWMode`
-   Specification: ISO 14289-1:2014

> _A CMap shall not reference any other CMap except those listed in ISO 32000-1:2008, 9.7.5.2, Table 118._

A CMap references another non-standard CMap

-   Object type: `PDReferencedCMap`
-   Test condition: `CMapName == "Identity-H" || CMapName == "Identity-V" || CMapName == "GB-EUC-H" || CMapName == "GB-EUC-V" || CMapName == "GBpc-EUC-H" || CMapName == "GBpc-EUC-V" || CMapName == "GBK-EUC-H" || CMapName == "GBK-EUC-V" || CMapName == "GBKp-EUC-H" || CMapName == "GBKp-EUC-V" || CMapName == "GBK2K-H" || CMapName == "GBK2K-V" || CMapName == "UniGB-UCS2-H" || CMapName == "UniGB-UCS2-V" || CMapName == "UniGB-UFT16-H" || CMapName == "UniGB-UFT16-V" || CMapName == "B5pc-H" || CMapName == "B5pc-V" || CMapName == "HKscs-B5-H" || CMapName == "HKscs-B5-V" || CMapName == "ETen-B5-H" || CMapName == "ETen-B5-V" || CMapName == "ETenms-B5-H" || CMapName == "ETenms-B5-V" || CMapName == "CNS-EUC-H" || CMapName == "CNS-EUC-V" || CMapName == "UniCNS-UCS2-H" || CMapName == "UniCNS-UCS2-V" || CMapName == "UniCNS-UFT16-H" || CMapName == "UniCNS-UTF16-V" || CMapName == "83pv-RKSJ-H" || CMapName == "90ms-RKSJ-H" || CMapName == "90ms-RKSJ-V" || CMapName == "90msp-RKSJ-H" || CMapName == "90msp-RKSJ-V" || CMapName == "90pv-RKSJ-H" || CMapName == "Add-RKSJ-H" || CMapName == "Add-RKSJ-V" || CMapName == "EUC-H" || CMapName == "EUC-V" || CMapName == "Ext-RKSJ-H" || CMapName == "Ext-RKSJ-V" || CMapName == "H" || CMapName == "V" || CMapName == "UniJIS-UCS2-H" || CMapName == "UniJIS-UCS2-V" || CMapName == "UniJIS-UCS2-HW-H" || CMapName == "UniJIS-UCS2-HW-V" || CMapName == "UniJIS-UTF16-H" || CMapName == "UniJIS-UTF16-V" || CMapName == "KSC-EUC-H" || CMapName == "KSC-EUC-V" || CMapName == "KSCms-UHC-H" || CMapName == "KSCms-UHC-V" || CMapName == "KSCms-UHC-HW-H" || CMapName == "KSCms-UHC-HW-V" || CMapName == "KSCpc-EUC-H" || CMapName == "UniKS-UCS2-H" || CMapName == "UniKS-UCS2-V" || CMapName == "UniKS-UTF16-H" || CMapName == "UniKS-UTF16-V"`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 9.7.5.2, Table 118

> _The font programs for all fonts used for rendering within a conforming file shall be embedded within that file, as defined in ISO 32000-1:2008, 9.9._

The font program is not embedded

Text rendering mode 3 specifies that glyphs are not stroked, filled or used as a clipping boundary. A font referenced for use solely in this mode is therefore not rendered and is thus exempt from the embedding requirement.

-   Object type: `PDFont`
-   Test condition: `Subtype == "Type3" || Subtype == "Type0" || renderingMode == 3 || containsFontFile == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 9.9

> _Embedded fonts shall define all glyphs referenced for rendering within the conforming file. A font referenced solely in text rendering mode 3 is not rendered and is thus exempt from the requirements that impact the visual representation of the glyphs of a font. In all cases for TrueType fonts that are to be rendered, character codes shall be able to be mapped to glyphs according to ISO 32000-1:2008, 9.6.6.4 without the use of a non-standard mapping chosen by the conforming processor._

Not all glyphs referenced for rendering are present in the embedded font program

All conforming PDF/UA readers shall use the embedded fonts, rather than other locally resident, substituted or simulated fonts, for rendering.

The fonts used exclusively with text rendering mode 3 (invisible) are exempt from this requirement. OCR solutions often use such invisible fonts on top of the original scanned image to enable selection and copying of recognized text.

There is no exemption from the requirements of this rule for the 14 standard Type 1 fonts. The PostScript names of 14 Type 1 fonts, known as the standard fonts, are as follows:

```scss
Times−Roman      Helvetica             Courier             Symbol
Times−Bold       Helvetica−Bold        Courier−Bold        ZapfDingbats
Times−Italic     Helvetica−Oblique     Courier−Oblique
Times−BoldItalic Helvetica−BoldOblique Courier−BoldOblique
```

-   Object type: `Glyph`
-   Test condition: `renderingMode == 3 || isGlyphPresent == null || isGlyphPresent == true`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 32000-1:2008, 9.6.6.4

> _If the FontDescriptor dictionary of an embedded Type 1 font contains a CharSet string, then it shall list the character names of all glyphs present in the font program, regardless of whether a glyph in the font is referenced or used by the PDF or not._

A CharSet entry in the Descriptor dictionary of a Type1 font incorrectly lists glyphs present in the font program

-   Object type: `PDType1Font`
-   Test condition: `containsFontFile == false || fontName.search(/[A-Z]{6}\+/) != 0 || CharSet == null || charSetListsAllGlyphs == true`
-   Specification: ISO 14289-1:2014

> _If the FontDescriptor dictionary of an embedded CID font contains a CIDSet stream, then it shall identify all CIDs which are present in the font program, regardless of whether a CID in the font is referenced or used by the PDF or not._

A CIDSet entry in the Font descriptor does not correctly identify all glyphs present in the embedded font subset

-   Object type: `PDCIDFont`
-   Test condition: `containsFontFile == false || fontName.search(/[A-Z]{6}\+/) != 0 || containsCIDSet == false || cidSetListsAllGlyphs == true`
-   Specification: ISO 14289-1:2014

> _For every font embedded in a conforming file and used for rendering, the glyph width information in the font dictionary and in the embedded font program shall be consistent._

Glyph width information in the embedded font program is not consistent with the Widths entry of the font dictionary

This requirement is necessary to ensure predictable font rendering, regardless of whether a given reader uses the metrics in the Widths entry or those in the font program.

-   Object type: `Glyph`
-   Test condition: `renderingMode == 3 || widthFromFontProgram == null || widthFromDictionary == null || Math.abs(widthFromFontProgram - widthFromDictionary) <= 1`
-   Specification: ISO 14289-1:2014

> _For all non-symbolic TrueType fonts used for rendering, the embedded TrueType font program shall contain one or several non-symbolic cmap entries such that all necessary glyph lookups can be carried out._

The embedded font program for a non-symbolic TrueType font does not contain non-symbolic cmap entries

-   Object type: `TrueTypeFontProgram`
-   Test condition: `isSymbolic == true || (cmap30Present == true ? nrCmaps > 1 : nrCmaps > 0)`
-   Specification: ISO 14289-1:2014

> _All non-symbolic TrueType fonts shall have either MacRomanEncoding or WinAnsiEncoding as the value for the Encoding key in the Font dictionary or as the value for the BaseEncoding key in the dictionary which is the value of the Encoding key in the Font dictionary. In addition, no non-symbolic TrueType font shall define a Differences array unless all of the glyph names in the Differences array are listed in the Adobe Glyph List and the embedded font program contains at least the Microsoft Unicode (3,1 – Platform ID=3, Encoding ID=1) encoding in the 'cmap' table._

A non-symbolic TrueType font encoding does not define a correct mapping to the Adobe Glyph List

-   Object type: `PDTrueTypeFont`
-   Test condition: `isSymbolic == true || ((Encoding == "MacRomanEncoding" || Encoding == "WinAnsiEncoding") && (containsDifferences == false || differencesAreUnicodeCompliant == true))`
-   Specification: ISO 14289-1:2014

> _Symbolic TrueType fonts shall not contain an Encoding entry in the font dictionary_

A symbolic TrueType font specifies an Encoding entry in its dictionary

A Font is called symbolic if it contains characters outside the Adobe standard Latin character set. It is marked by special flag in its font descriptor dictionary.

-   Object type: `PDTrueTypeFont`
-   Test condition: `isSymbolic == false || Encoding == null`
-   Specification: ISO 14289-1:2014

> _The 'cmap' table in the embedded font program for a symbolic TrueType font shall contain either exactly one encoding or it shall contain, at least, the Microsoft Symbol (3,0 - Platform ID=3, Encoding ID=0) encoding._

The embedded font program for a symbolic TrueType font contains more than one cmap subtable

-   Object type: `TrueTypeFontProgram`
-   Test condition: `isSymbolic == false || nrCmaps == 1 || cmap30Present == true`
-   Specification: ISO 14289-1:2014

> _The Font dictionary of all fonts shall define the map of all used character codes to Unicode values, either via a ToUnicode entry, or other mechanisms as defined in ISO 14289-1, 7.21.7._

The glyph can not be mapped to Unicode

-   Object type: `Glyph`
-   Test condition: `toUnicode != null`
-   Specification: ISO 14289-1:2014
-   Additional references:
    -   ISO 14289-1:2014, 7.21.7

> _The Unicode values specified in the ToUnicode CMap shall all be greater than zero (0), but not equal to either U+FEFF or U+FFFE._

The glyph has an invalid Unicode value, which is either 0, or is equal to U+FEFF or U+FFFE.

The font dictionary of all fonts, regardless of their rendering mode usage, shall include a ToUnicode entry whose value is a CMap stream object that maps character codes for at least all referenced glyphs to Unicode values, as described in ISO 32000-1:2008, 9.10.3, unless the font meets at least one of the following four conditions:

-   fonts that use the predefined encodings MacRomanEncoding, MacExpertEncoding or WinAnsiEncoding;
-   Type 1 and Type 3 fonts where the glyph names of the glyphs referenced are all contained in the Adobe Glyph List or the set of named characters in the Symbol font, as defined in ISO 32000-1:2008, Annex D;
-   Type 0 fonts whose descendant CIDFont uses the Adobe-GB1, Adobe-CNS1, Adobe-Japan1 or Adobe-Korea1 character collections.
-   Non-symbolic TrueType fonts.

This requirement ensures that the values in the ToUnicode CMap will be useful values and not simply placeholders.

-   Object type: `Glyph`
-   Test condition: `toUnicode == null || (toUnicode.indexOf("\u0000") == -1 && toUnicode.indexOf("\uFFFE") == -1 && toUnicode.indexOf("\uFEFF") == -1)`
-   Specification: ISO 14289-1:2014

> _A PDF/UA compliant document shall not contain a reference to the .notdef glyph from any of the text showing operators, regardless of text rendering mode, in any content stream._

The document contains a reference to the .notdef glyph

-   Object type: `Glyph`
-   Test condition: `name != ".notdef"`
-   Specification: ISO 14289-1:2014
