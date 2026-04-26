---
created: 2026-04-20T21:47:54 (UTC -05:00)
tags: []
source: https://github.com/veraPDF/veraPDF-validation-profiles/wiki/PDFUA-Part-2-rules/
author: 
---

# PDFUA Part 2 rules · veraPDF/veraPDF-validation-profiles Wiki

> ## Excerpt
> PDF/UA-2 validation rules The PDF/UA version of a file shall be specified in the value of the Metadata entry in the document catalog using the PDF/UA identification schema The document metadata stream

---
# PDF/UA-2 validation rules

> _The PDF/UA version of a file shall be specified in the value of the Metadata entry in the document catalog using the PDF/UA identification schema_

The document metadata stream does not contains PDF/UA Identification Schema

-   Object type: `MainXMPPackage`
-   Test condition: `containsPDFUAIdentification == true`
-   Specification: ISO 14289-2:2024

> _The value of "pdfuaid:part" shall be the part number of the International Standard to which the file conforms_

The "part" property of the PDF/UA Identification Schema is not 2 for PDF/UA-2 conforming file

-   Object type: `PDFUAIdentification`
-   Test condition: `part == 2`
-   Specification: ISO 14289-2:2024

> _Property "part" of the PDF/UA Identification Schema shall have namespace prefix "pdfuaid"_

Property "part" of the PDF/UA Identification Schema has an invalid namespace prefix

-   Object type: `PDFUAIdentification`
-   Test condition: `partPrefix == null || partPrefix == "pdfuaid"`
-   Specification: ISO 14289-2:2024

> _Property "rev" of the PDF/UA Identification Schema shall have namespace prefix "pdfuaid"_

Property "rev" of the PDF/UA Identification Schema has an invalid namespace prefix

-   Object type: `PDFUAIdentification`
-   Test condition: `revPrefix == null || revPrefix == "pdfuaid"`
-   Specification: ISO 14289-2:2024

> _The value of "pdfuaid:rev" shall be the four digit year_

The value of "pdfuaid:rev" is not the four digit year

-   Object type: `PDFUAIdentification`
-   Test condition: `/^\d{4}$/.test(rev)`
-   Specification: ISO 14289-2:2024

> _The document catalog dictionary shall include a MarkInfo dictionary containing an entry, Marked, whose value shall be true._

MarkInfo dictionary is not present in the document catalog, or Marked entry is set to false or is not present in the MarkInfo dictionary.

This setting indicates that the file conforms to the Tagged PDF conventions.

-   Object type: `CosDocument`
-   Test condition: `Marked == true`
-   Specifications: ISO 14289-2:2014
-   Additional references:
    -   ISO 32000-2:2020, 14.7.1

> _The logical structure of the conforming file shall be described by a structure hierarchy rooted in the StructTreeRoot entry of the document catalog dictionary, as described in ISO 32000-2:2020, 14.7_

StructTreeRoot entry is not present in the document catalog. This indicates that the document is not tagged.

-   Object type: `PDDocument`
-   Test condition: `containsStructTreeRoot == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.7

> _A structure element dictionary shall contain the P (parent) entry according to ISO 32000-2:2020, 14.7.2, Table 323_

A structure element dictionary does not contain the P (parent) entry. This usually indicates that the structure hierarchy of the PDF document is malformed.

-   Object type: `PDStructElem`
-   Test condition: `containsParent == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.7.2, Table 323

> _Content that is not considered real shall be an artifact_

Content is neither marked as Artifact nor tagged as real content. This error indicates that a part of the document is not properly tagged.

-   Object type: `SESimpleContentItem`
-   Test condition: `isTaggedContent == true || parentsTags.contains('Artifact') == true`
-   Specification: ISO 14289-2:2024

> _All structure elements shall belong to, or be role mapped to, at least one of the following namespaces specified in ISO 32000-2:2020, 14.8.6: — the PDF 1.7 namespace; — the PDF 2.0 namespace; — the MathML namespace_

A non-standard structure type is not mapped to a standard type. The semantics of such element is not defined by PDF 1.7 or PDF 2.0.

-   Object type: `SENonStandard`
-   Test condition: `isNotMappedToStandardType == false`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.8.6

> _A circular mapping shall not exist_

A circular mapping exists. This indicates that the structure tree of the PDF document is malformed.

-   Object type: `PDStructElem`
-   Test condition: `circularMappingExist != true`
-   Specification: ISO 14289-2:2024

> _Within a given explicitly provided namespace, structure types shall not be role mapped to other structure types in the same namespace_

A structure type is role mapped to other structure type in the same namespace. It is not permitted to redefine semantics of structure elements within the same namespace. It is however permitted to map structure element types from one namespace to another namespace.

-   Object type: `PDStructElem`
-   Test condition: `roleMapToSameNamespaceTag == null`
-   Specification: ISO 14289-2:2024

> _All structure elements shall belong to, or be role mapped to, at least one of the following namespaces specified in ISO 32000-2:2020, 14.8.6: — the PDF 1.7 namespace; — the PDF 2.0 namespace; — the MathML namespace_

A standard structure type is remapped to a non-standard type. It is only permitted to map non-standard structure types to standard ones, or standard structure types within one namespace (for example, PDF 2.0) to another standard namespace (for example, PDF 1.7).

-   Object type: `SENonStandard`
-   Test condition: `remappedStandardType == null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.8.6

> _The structure tree root shall contain a single Document structure element as its only child, as specified in ISO 32000-2:2020, Annex L and ISO/TS 32005_

The structure tree root contains element(s) other than a single Document structure element

-   Object type: `PDStructTreeRoot`
-   Test condition: `kidsStandardTypes == 'Document'`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.7.2
    -   ISO 32000-2:2020, 14.8.6
    -   ISO 32000-2:2020, Annex L
    -   ISO/TS 32005, clause

> _The structure tree root shall contain a single Document structure element as its only child. The namespace for that element shall be specified as the PDF 2.0 namespace_

The structure tree root contains a single Document structure element, but this element is not within the PDF 2.0 namespace

-   Object type: `PDStructTreeRoot`
-   Test condition: `kidsStandardTypes != 'Document' || firstChildStandardTypeNamespaceURL == 'http://iso.org/pdf2/ssn'`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.7.2
    -   ISO 32000-2:2020, 14.8.6
    -   ISO 32000-2:2020, Annex L
    -   ISO/TS 32005, clause

> _Each TOCI in the table of contents shall identify the target of the reference using the Ref entry, either directly on the TOCI structure element itself or on one of its child structure elements_

TOCI (TOC item) in the TOC (Tabled of Contents) does not contain the Ref entry, neither directly on the TOCI structure element itself nor on its descendant structure elements. The Ref entry in TOCI is used to reference the destination structure element for this TOC item.

-   Object type: `SETOCI`
-   Test condition: `containsRef == true`
-   Specification: ISO 14289-2:2024

> _Conforming files shall not use the H structure type_

Document uses H structure type. This structure element has a meaning of a generic heading. The numbered heading elements shall be used instead to unambiguously define the high level structure of the document.

-   Object type: `SEH`
-   Test condition: `false`
-   Specification: ISO 14289-2:2024

> _The Note standard structure type shall not be present in conforming documents unless role mapped to a structure element in the PDF 2.0 namespace_

Document uses Note structure type. This structure element exists only in PDF 1.7 namespace and was removed from PDF 2.0. The FENote structure element shall be used instead.

-   Object type: `SENote`
-   Test condition: `false`
-   Specification: ISO 14289-2:2024

> _Real content that refers to footnotes or endnotes (real content enclosed in FENote structure elements) shall use the Ref entry on the referring structure element to reference the FENote. The corresponding FENote shall also use the Ref entry to identify all citations that reference it_

Ref entry in the FENote does not reference structure elements, while these structure elements reference this FENote

-   Object type: `SEFENote`
-   Test condition: `orphanRefs == null`
-   Specification: ISO 14289-2:2024

> _Real content that refers to footnotes or endnotes (real content enclosed in FENote structure elements) shall use the Ref entry on the referring structure element to reference the FENote. The corresponding FENote shall also use the Ref entry to identify all citations that reference it_

Ref entry in the FENote reference structure elements, while these structure elements do not reference this FENote

-   Object type: `SEFENote`
-   Test condition: `ghostRefs == null`
-   Specification: ISO 14289-2:2024

> _The value of the NoteType attribute of the FENote structure element shall be Footnote, Endnote or None_

NoteType attribute of the FENote structure element has value other than Footnote, Endnote or None

-   Object type: `SEFENote`
-   Test condition: `NoteType == 'Footnote' || NoteType == 'Endnote' || NoteType == 'None'`
-   Specification: ISO 14289-2:2024

> _A link annotation and its associated content shall be enclosed in either a Link or Reference structure element_

A Link annotation is an Artifact or is nested within tag other than Link or Reference

-   Object type: `PDLinkAnnot`
-   Test condition: `structParentStandardType == 'Link' || structParentStandardType == 'Reference'`
-   Specification: ISO 14289-2:2024

> _Link annotations that target different locations shall be in separate Link or Reference structure elements_

Structure element contains Link annotations that target different locations. All link annotations within a single structure element (Link or Reference) shall target the same location. Otherwise they have to be placed in different structure elements.

-   Object type: `PDLinkAnnot`
-   Test condition: `differentTargetAnnotObjectKey == null`
-   Specification: ISO 14289-2:2024

> _A Ruby structure element shall contain a single RB structure element and a single RT structure element or a Ruby structure element shall consist of a four-element subsequence: RB, RP, RT, RP_

The Ruby structure element has invalid sequence of children

-   Object type: `SERuby`
-   Test condition: `kidsStandardTypes == 'RB&RT' || kidsStandardTypes == 'RB&RP&RT&RP'`
-   Specification: ISO 14289-2:2024

> _Content typeset as warichu shall be tagged in a three-element sequence consisting of the structure elements WP, WT and WP, grouped inside a Warichu structure element_

The Warichu structure element has invalid sequence of children

-   Object type: `SEWarichu`
-   Test condition: `kidsStandardTypes == 'WP&WT&WP'`
-   Specification: ISO 14289-2:2024

> _If Lbl structure elements are present, the ListNumbering attribute shall be present on the respective L structure element; in such cases the value None shall not be used_

List items contain Lbl structure elements, but the ListNumbering attribute is not present on the respective L structure element or it has value None. The ListNumbering attribute identifies whether the list is numbered or unnumbered and may provide additional information on the label pattern.

-   Object type: `SEL`
-   Test condition: `containsLabels == false || ListNumbering != 'None'`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 14289-2:2024, Annex B, 2

> _Any real content within an LI structure element that is not enclosed in an Lbl structure element shall be enclosed in an LBody structure element_

The LI structure element contains real content as its direct child instead of enclosing it into Lbl or LBody structure elements. Any LI (list item) element shall consist of single Lbl element followed by LBody element with no direct content in-between.

-   Object type: `SELI`
-   Test condition: `hasContentItems == false`
-   Specification: ISO 14289-2:2024

> _Tables shall be regular. A table cell shall not have intersection with other cells_

Table cell has intersection with other cells. This may happen if row or column spans are incorrect.

-   Object type: `SETableCell`
-   Test condition: `hasIntersection != true`
-   Specification: ISO 14289-2:2024

> _Tables shall be regular. Row groupings formed by THead, TBody and TFoot structure elements shall be regular. Table columns shall have the same number of rows (taking into account row spans) in table and each row groupings formed by THead, TBody and TFoot structure elements_

Some table columns have different number of rows in table, or within one of row groupings formed by THead, TBody and TFoot structure elements

-   Object type: `SETable`
-   Test condition: `numberOfColumnWithWrongRowSpan == null`
-   Specification: ISO 14289-2:2024

> _Tables shall be regular. Table rows shall have the same number of columns (taking into account column spans)_

Some table rows have different number of columns. Columns are counted taking into account column spans.

-   Object type: `SETable`
-   Test condition: `numberOfRowWithWrongColumnSpan == null || wrongColumnSpan != null`
-   Specification: ISO 14289-2:2024

> _Tables shall be regular. Table rows shall have the same number of columns (taking into account column spans)_

Some table row has number of columns that exceeds the number of columns in the first row. Columns are counted taking into account column spans.

-   Object type: `SETable`
-   Test condition: `numberOfRowWithWrongColumnSpan == null || wrongColumnSpan == null`
-   Specification: ISO 14289-2:2024

> _When a table contains header cells, that table shall provide sufficient semantic information to allow accurate determination of which of its table header cells (structure element TH) pertain to other cells as specified in ISO 32000-2:2020, 14.8.5.7_

TD does not contain explicit Headers attribute, and Headers for this table cell cannot be determined algorithmically based on table structure

-   Object type: `SETD`
-   Test condition: `hasConnectedHeader != false || unknownHeaders != ''`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.8.4.8.3
    -   ISO 32000-2:2020, 14.8.5.7

> _When a table contains header cells, that table shall provide sufficient semantic information to allow accurate determination of which of its table header cells (structure element TH) pertain to other cells as specified in ISO 32000-2:2020, 14.8.5.7_

TD references undefined Header(s), and Headers for this table cell cannot be determined algorithmically based on table structure

-   Object type: `SETD`
-   Test condition: `hasConnectedHeader != false || unknownHeaders == ''`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.8.4.8.3
    -   ISO 32000-2:2020, 14.8.5.7

> _When present, the Caption element shall be the first or the last child of the structure element_

A structure element contains Caption not as its first or last child

-   Object type: `PDStructElem`
-   Test condition: `kidsStandardTypes.indexOf('&Caption&') < 0`
-   Specification: ISO 14289-2:2024

> _A Figure structure element shall have at least one of the following properties: a) an alternate description (Alt property), as specified in ISO 32000-2:2020, 14.9.3; b) a replacement text (ActualText property) that represents the content enclosed by the Figure structure element_

Figure structure element neither has an alternate description nor a replacement text

-   Object type: `SEFigure`
-   Test condition: `Alt != null || ActualText != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.9.3

> _The math structure type shall occur only as a child of a Formula structure element_

The math structure type is nested within tag other than Formula. The math structure type is used in PDF to represent mathematical formulas in MathML syntax.

-   Object type: `SEMathMLStructElem`
-   Test condition: `parentStandardType == 'Formula' || parentStandardType == 'MathML'`
-   Specification: ISO 14289-2:2024

> _In all cases, where real content maps to Unicode PUA values, an ActualText or Alt entry shall be present_

Real content maps to Unicode PUA values, but ActualText and Alt entry are not present. Unicode Private Use Area (PUA) is a range of code points that, by definition, will not be assigned characters by the Unicode. It is required that any such code points in PDF are accompanied with either replacement text (specified via ActualText entry) or with an alternative description (via Alt entry).

-   Object type: `Glyph`
-   Test condition: `isRealContent == false || unicodePUA == false || actualTextPresent == true || altPresent == true`
-   Specification: ISO 14289-2:2024

> _The ActualText entry shall not contain any PUA values_

The ActualText entry contains Unicode PUA (Private Use Area) code points

-   Object type: `CosActualText`
-   Test condition: `containsPUA == false`
-   Specification: ISO 14289-2:2024

> _The Alt entry shall not contain any PUA values_

The Alt entry contains Unicode PUA (Private Use Area) code points

-   Object type: `CosAlt`
-   Test condition: `containsPUA == false`
-   Specification: ISO 14289-2:2024

> _The default natural language for content and text strings shall be specified using the Lang entry, with a non-empty value, in the catalog dictionary_

Catalog dictionary does not contain Lang entry. This Lang entry defines the default language for all text strings in the document.

-   Object type: `PDDocument`
-   Test condition: `containsLang == true`
-   Specification: ISO 14289-2:2024

> _If the Lang entry is present in the document's Catalog dictionary or in a structure element dictionary or property list, its value shall be a language identifier as described in ISO 32000-2:2020, 14.9.2. A language identifier shall be a Language-Tag as defined in RFC 3066, Tags for the Identification of Languages_

Value of the Lang entry is not a Language-Tag. The permitted formats for Language Tag are defined in RFC 3066.

-   Object type: `CosLang`
-   Test condition: `/^[a-zA-Z]{1,8}(-[a-zA-Z0-9]{1,8})*$/.test(unicodeValue)`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.9.2
    -   RFC 3066, 2.1

> _For any given composite (Type 0) font within a conforming file, the CIDSystemInfo entry in its CIDFont dictionary and its Encoding dictionary shall have the following relationship: - If the Encoding key in the Type 0 font dictionary has a value of Identity-H or Identity-V, then any values for the Registry, Ordering, and Supplement keys may be used in the CIDSystemInfo dictionary of the CIDFont. - Otherwise the corresponding values of the Registry and Ordering keys in both CIDSystemInfo dictionaries shall be identical, and the value of the Supplement key in the CIDSystemInfo dictionary of the CIDFont shall be less than or equal to the value of the Supplement key in the CIDSystemInfo dictionary of the CMap_

CIDSystemInfo entries the CIDFont and CMap dictionaries of a Type 0 font are not compatible. This introduces a potential risk that some of the characters in page content will be incorrectly mapped to the glyphs in the embedded font program.

-   Object type: `PDType0Font`
-   Test condition: `cmapName == "Identity-H" || cmapName == "Identity-V" || (CIDFontOrdering != null && CIDFontOrdering == CMapOrdering && CIDFontRegistry != null && CIDFontRegistry == CMapRegistry && CIDFontSupplement != null && CMapSupplement != null && CIDFontSupplement <= CMapSupplement)`
-   Specification: ISO 14289-2:2024

> _All embedded Type 2 CIDFonts in the CIDFont dictionary shall contain a CIDToGIDMap entry that shall be a stream mapping from CIDs to glyph indices or the name Identity, as described in ISO 32000-2:2020, Table 115_

A Type 2 CIDFont dictionary has missing or invalid CIDToGIDMap entry. This entry is used to map characters in PDF page content to the glyph identifiers in the embedded TrueType / OpenType font program.

-   Object type: `PDCIDFont`
-   Test condition: `Subtype != "CIDFontType2" || CIDToGIDMap != null || containsFontFile == false`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 9.7.4, Table 115

> _All CMaps used within a file that conforms to PDF/UA-2, except those listed in ISO 32000-2:2020, Table 116, shall be embedded in that file, as described in ISO 32000-2:2020, 9.7.5_

A non-standard CMap is not embedded

-   Object type: `PDCMap`
-   Test condition: `CMapName == "Identity-H" || CMapName == "Identity-V" || CMapName == "GB-EUC-H" || CMapName == "GB-EUC-V" || CMapName == "GBpc-EUC-H" || CMapName == "GBpc-EUC-V" || CMapName == "GBK-EUC-H" || CMapName == "GBK-EUC-V" || CMapName == "GBKp-EUC-H" || CMapName == "GBKp-EUC-V" || CMapName == "GBK2K-H" || CMapName == "GBK2K-V" || CMapName == "UniGB-UCS2-H" || CMapName == "UniGB-UCS2-V" || CMapName == "UniGB-UFT16-H" || CMapName == "UniGB-UFT16-V" || CMapName == "B5pc-H" || CMapName == "B5pc-V" || CMapName == "HKscs-B5-H" || CMapName == "HKscs-B5-V" || CMapName == "ETen-B5-H" || CMapName == "ETen-B5-V" || CMapName == "ETenms-B5-H" || CMapName == "ETenms-B5-V" || CMapName == "CNS-EUC-H" || CMapName == "CNS-EUC-V" || CMapName == "UniCNS-UCS2-H" || CMapName == "UniCNS-UCS2-V" || CMapName == "UniCNS-UFT16-H" || CMapName == "UniCNS-UTF16-V" || CMapName == "83pv-RKSJ-H" || CMapName == "90ms-RKSJ-H" || CMapName == "90ms-RKSJ-V" || CMapName == "90msp-RKSJ-H" || CMapName == "90msp-RKSJ-V" || CMapName == "90pv-RKSJ-H" || CMapName == "Add-RKSJ-H" || CMapName == "Add-RKSJ-V" || CMapName == "EUC-H" || CMapName == "EUC-V" || CMapName == "Ext-RKSJ-H" || CMapName == "Ext-RKSJ-V" || CMapName == "H" || CMapName == "V" || CMapName == "UniJIS-UCS2-H" || CMapName == "UniJIS-UCS2-V" || CMapName == "UniJIS-UCS2-HW-H" || CMapName == "UniJIS-UCS2-HW-V" || CMapName == "UniJIS-UTF16-H" || CMapName == "UniJIS-UTF16-V" || CMapName == "KSC-EUC-H" || CMapName == "KSC-EUC-V" || CMapName == "KSCms-UHC-H" || CMapName == "KSCms-UHC-V" || CMapName == "KSCms-UHC-HW-H" || CMapName == "KSCms-UHC-HW-V" || CMapName == "KSCpc-EUC-H" || CMapName == "UniKS-UCS2-H" || CMapName == "UniKS-UCS2-V" || CMapName == "UniKS-UTF16-H" || CMapName == "UniKS-UTF16-V" || containsEmbeddedFile == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 9.7.5.2, Table 116

> _For those CMaps that are embedded, the integer value of the WMode entry in the CMap dictionary shall be identical to the WMode value in the embedded CMap stream_

WMode entry in the embedded CMap and in the CMap dictionary are not identical. This indicates that an invalid CMap was used for the font.

-   Object type: `CMapFile`
-   Test condition: `WMode == dictWMode`
-   Specification: ISO 14289-2:2024

> _A CMap shall not reference any other CMap except those listed in ISO 32000-2:2020, 9.7.5.2 Table 116_

A CMap references another non-standard CMap

-   Object type: `PDReferencedCMap`
-   Test condition: `CMapName == "Identity-H" || CMapName == "Identity-V" || CMapName == "GB-EUC-H" || CMapName == "GB-EUC-V" || CMapName == "GBpc-EUC-H" || CMapName == "GBpc-EUC-V" || CMapName == "GBK-EUC-H" || CMapName == "GBK-EUC-V" || CMapName == "GBKp-EUC-H" || CMapName == "GBKp-EUC-V" || CMapName == "GBK2K-H" || CMapName == "GBK2K-V" || CMapName == "UniGB-UCS2-H" || CMapName == "UniGB-UCS2-V" || CMapName == "UniGB-UFT16-H" || CMapName == "UniGB-UFT16-V" || CMapName == "B5pc-H" || CMapName == "B5pc-V" || CMapName == "HKscs-B5-H" || CMapName == "HKscs-B5-V" || CMapName == "ETen-B5-H" || CMapName == "ETen-B5-V" || CMapName == "ETenms-B5-H" || CMapName == "ETenms-B5-V" || CMapName == "CNS-EUC-H" || CMapName == "CNS-EUC-V" || CMapName == "UniCNS-UCS2-H" || CMapName == "UniCNS-UCS2-V" || CMapName == "UniCNS-UFT16-H" || CMapName == "UniCNS-UTF16-V" || CMapName == "83pv-RKSJ-H" || CMapName == "90ms-RKSJ-H" || CMapName == "90ms-RKSJ-V" || CMapName == "90msp-RKSJ-H" || CMapName == "90msp-RKSJ-V" || CMapName == "90pv-RKSJ-H" || CMapName == "Add-RKSJ-H" || CMapName == "Add-RKSJ-V" || CMapName == "EUC-H" || CMapName == "EUC-V" || CMapName == "Ext-RKSJ-H" || CMapName == "Ext-RKSJ-V" || CMapName == "H" || CMapName == "V" || CMapName == "UniJIS-UCS2-H" || CMapName == "UniJIS-UCS2-V" || CMapName == "UniJIS-UCS2-HW-H" || CMapName == "UniJIS-UCS2-HW-V" || CMapName == "UniJIS-UTF16-H" || CMapName == "UniJIS-UTF16-V" || CMapName == "KSC-EUC-H" || CMapName == "KSC-EUC-V" || CMapName == "KSCms-UHC-H" || CMapName == "KSCms-UHC-V" || CMapName == "KSCms-UHC-HW-H" || CMapName == "KSCms-UHC-HW-V" || CMapName == "KSCpc-EUC-H" || CMapName == "UniKS-UCS2-H" || CMapName == "UniKS-UCS2-V" || CMapName == "UniKS-UTF16-H" || CMapName == "UniKS-UTF16-V"`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 9.7.5.2, Table 116

> _The font programs for all fonts used for rendering within a conforming file shall be embedded within that file, as defined in ISO 32000-2:2020, 9.9_

The font program is not embedded

-   Object type: `PDFont`
-   Test condition: `Subtype == "Type3" || Subtype == "Type0" || renderingMode == 3 || containsFontFile == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 9.9

> _Embedded fonts shall define all glyphs referenced for rendering within the conforming file. A font referenced solely in text rendering mode 3 is not rendered and is thus exempt from the requirements that impact the visual representation of the glyphs of a font. In all cases for TrueType fonts that are to be rendered, character codes shall be able to be mapped to glyphs in accordance with ISO 32000-2:2020, 9.6.5, without the use of a non-standard mapping chosen by the conforming processor_

Not all glyphs referenced for rendering are present in the embedded font program

-   Object type: `Glyph`
-   Test condition: `renderingMode == 3 || isGlyphPresent == null || isGlyphPresent == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 9.3.6
    -   ISO 32000-2:2020, 9.6.5

> _For every font embedded in a conforming file and referenced for rendering, the glyph width information in the font dictionary and in the embedded font program shall be consistent for every glyph_

Glyph width in the embedded font program is not consistent with the Widths entry of the font dictionary. This might cause ambiguity in page rendering.

-   Object type: `Glyph`
-   Test condition: `renderingMode == 3 || widthFromFontProgram == null || widthFromDictionary == null || Math.abs(widthFromFontProgram - widthFromDictionary) <= 1`
-   Specification: ISO 14289-2:2024

> _For all non-symbolic TrueType fonts used for rendering, the embedded TrueType font program shall contain at least Microsoft Unicode (3,1 – Platform ID=3, Encoding ID=1), or Macintosh Roman (1,0 – Platform ID=1, Encoding ID=0) 'cmap' subtable_

The embedded font program for a non-symbolic TrueType font does not contain Microsoft Symbol (3,1 – Platform ID=3, Encoding ID=1) or the Mac Roman (1,0 – Platform ID=1, Encoding ID=0) encoding. This may create ambiguity in the correct choice of the encoding subtable in the embedded TrueType program and, as a result, incorrect glyphs rendered on the page.

-   Object type: `TrueTypeFontProgram`
-   Test condition: `isSymbolic == true || cmap31Present == true || cmap10Present == true`
-   Specification: ISO 14289-2:2024

> _All non-symbolic TrueType fonts shall have either MacRomanEncoding or WinAnsiEncoding as the value for the Encoding key in the Font dictionary or as the value for the BaseEncoding key in the dictionary which is the value of the Encoding key in the Font dictionary. In addition, no non-symbolic TrueType font shall define a Differences array unless all of the glyph names in the Differences array are listed in the Adobe Glyph List and the embedded font program contains at least the Microsoft Unicode (3,1 – Platform ID=3, Encoding ID=1) encoding in the 'cmap' table_

A non-symbolic TrueType font encoding does not define a correct mapping to the Adobe Glyph List. This may cause incorrect glyph selection for some characters on the page.

-   Object type: `PDTrueTypeFont`
-   Test condition: `isSymbolic == true || ((Encoding == "MacRomanEncoding" || Encoding == "WinAnsiEncoding") && (containsDifferences == false || differencesAreUnicodeCompliant == true))`
-   Specification: ISO 14289-2:2024

> _Symbolic TrueType fonts shall not contain an Encoding entry in the font dictionary_

A symbolic TrueType font specifies an Encoding entry in its dictionary

-   Object type: `PDTrueTypeFont`
-   Test condition: `isSymbolic == false || Encoding == null`
-   Specification: ISO 14289-2:2024

> _The 'cmap' subtable in the embedded font program shall either contain the Microsoft Symbol (3,0 – Platform ID=3, Encoding ID=0) or the Mac Roman (1,0 – Platform ID=1, Encoding ID=0) encoding_

The embedded font program for a symbolic TrueType font does not contain Microsoft Symbol (3,0 – Platform ID=3, Encoding ID=0) or the Mac Roman (1,0 – Platform ID=1, Encoding ID=0) encoding. This may create ambiguity in the correct choice of the encoding subtable in the embedded TrueType program and, as a result, incorrect glyphs rendered on the page.

-   Object type: `TrueTypeFontProgram`
-   Test condition: `isSymbolic == false || cmap30Present == true || cmap10Present == true`
-   Specification: ISO 14289-2:2024

> _The Font dictionary of all fonts shall define the map of all used character codes to Unicode values, either via a ToUnicode entry, or other mechanisms as defined in ISO 14289-2, 8.4.5.8_

The glyph can not be mapped to Unicode

-   Object type: `Glyph`
-   Test condition: `toUnicode != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 14289-2:2024, 8.4.5.8
    -   ISO 32000-2:2020, 9.10.3

> -   If a ToUnicode CMap is present, the Unicode values it specifies shall all be greater than zero (0), but not equal to either U+FEFF or U+FFFE\*

The glyph has Unicode value 0, U+FEFF or U+FFFE, which is invalid by Unicode standard

-   Object type: `Glyph`
-   Test condition: `toUnicode == null || (toUnicode.indexOf("\u0000") == -1 && toUnicode.indexOf("\uFFFE") == -1 && toUnicode.indexOf("\uFEFF") == -1)`
-   Specification: ISO 14289-2:2024

> _A file in conformance with PDF/UA-2 shall not contain a reference to the .notdef glyph from any of the text showing operators, regardless of text rendering mode, in any content stream_

The document contains a reference to the .notdef glyph

-   Object type: `Glyph`
-   Test condition: `name != ".notdef"`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 9.7.6.3

> _Text strings intended to be human readable shall not use the Unicode PUA_

Text string intended to be human readable (such as outline, font name or other) uses Unicode PUA (Private Use Area)

-   Object type: `CosTextString`
-   Test condition: `containsPUA == false`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 7.9.2.2

> _All optional content configuration dictionaries in the document, including the default optional content configuration dictionary, shall contain a Name entry (see ISO 32000-2:2020, Table 96) whose value is a non-empty text string when: a) a document contains a Configs entry in the OCProperties entry of the catalog dictionary (see ISO 32000-2:2020, Table 29), and b) the Configs entry contains at least one optional content configuration dictionary_

Missing or empty Name entry of the optional content configuration dictionary. This entry specifies a human readable name of an optional layer.

-   Object type: `PDOCConfig`
-   Test condition: `gContainsConfigs == false || (Name != null && Name.length() > 0)`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 7.7.2, Table 29
    -   ISO 32000-2:2020, 8.11.2.1, Table 96

> _The AS key shall not appear in any optional content configuration dictionary_

AS key is present in the optional content configuration dictionary. AS entry is used for automatically setting the visibility states of optional content groups (layers) based on external factors, such as the current system language or viewing magnification. This mechanism is not permitted in PDF/UA documents.

-   Object type: `PDOCConfig`
-   Test condition: `AS == null`
-   Specification: ISO 14289-2:2024

> _All destinations whose target lies within the current document shall be structure destinations_

Destination in Outline item, OpenAction or Link annotation is not a structure destination. Structure destinations define the target of a link as a structure element in the document, rather than a particular rectangle on the page.

-   Object type: `PDDestination`
-   Test condition: `isStructDestination == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.3.2
    -   ISO 32000-2:2020, 12.3.2.3

> _All destinations whose target lies within the current document shall be structure destinations_

Destination in GoTo action is not a structure destination. Structure destinations define the target of a link as a structure element in the document, rather than a particular rectangle on the page.

-   Object type: `PDGoToAction`
-   Test condition: `containsStructDestination == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.3.2
    -   ISO 32000-2:2020, 12.3.2.3

> _Annotations shall be artifacts, if the Invisible flag is set in accordance with ISO 32000-2:2020, Table 167_

An invisible annotation is included in logical structure. Annotations may be marked as invisible, which suggests that they are not a part of a real content.

-   Object type: `PDAnnot`
-   Test condition: `structParentType == null || isArtifact == true || (F & 1) == 0`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.5.3, Table 167

> _Annotations shall be artifacts if the NoView flag is set and the ToggleNoView flag is not set in accordance with ISO 32000-2:2020, Table 167_

A no-view annotation is included in logical structure. Annotations may have a no-view flag, which makes them invisible suggests that they are not a part of a real content.

-   Object type: `PDAnnot`
-   Test condition: `structParentType == null || isArtifact == true || ((F & 32) == 0 || (F & 256) == 256)`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.5.3, Table 167

> _Markup annotations shall be enclosed within Annot structure elements_

A Markup annotation is an Artifact or is nested within tag other than Annot

-   Object type: `PDMarkupAnnot`
-   Test condition: `structParentStandardType == 'Annot'`
-   Specification: ISO 14289-2:2024

> _When both RC and Contents entries are present for markup annotation, they shall be textually equivalent_

A Markup annotation contains Contents and RC entries with non-equivalent textual values. RC entry is a rich text alternative for the plain text of Contents entry of an annotation.

-   Object type: `PDMarkupAnnot`
-   Test condition: `containsRC == false || Contents == null || RC == Contents`
-   Specification: ISO 14289-2:2024

> _If the Name entry is insufficient to describe the intent of the stamp annotation, a Contents entry describing the author’s intent shall be provided_

Rubber stamp annotation contains neither Name nor Contents entry

-   Object type: `PDRubberStampAnnot`
-   Test condition: `Name != null || Contents != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.5.6.2

> _A Contents entry describing the author’s intent shall be provided for Ink annotation_

Ink annotation does not contain Contents entry

-   Object type: `PDInkAnnot`
-   Test condition: `Contents != null`
-   Specification: ISO 14289-2:2024

> _Popup annotations shall not be present in the structure tree_

A Popup annotation is included in the logical structure of the document. Popup annotations define visual representation of activated Markup annotations and do not carry any additional semantics.

-   Object type: `PDPopupAnnot`
-   Test condition: `structParentType == null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.11.3

> _When a file attachment annotation references a file specification dictionary, the file specification dictionary shall include an AFRelationship entry_

The file specification dictionary referenced by a file attachment annotation does not include AFRelationship entry. The AFRelationship entry defines the type (or purpose) of association of an embedded file to the document.

-   Object type: `PDFileAttachmentAnnot`
-   Test condition: `containsFS == false || AFRelationship != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 7.11.3
    -   ISO 32000-2:2020, 12.5.6.15

> _Sound annotation cannot be used when conforming to PDF/UA-2_

An annotation of subtype Sound exists

-   Object type: `PDSoundAnnot`
-   Test condition: `false`
-   Specification: ISO 14289-2:2024

> _Movie annotation cannot be used when conforming to PDF/UA-2_

An annotation of subtype Movie exists

-   Object type: `PDMovieAnnot`
-   Test condition: `false`
-   Specification: ISO 14289-2:2024

> _Screen annotations shall include a Contents entry_

Screen annotation does not contain Contents entry

-   Object type: `PDScreenAnnot`
-   Test condition: `Contents != null`
-   Specification: ISO 14289-2:2024

> _A widget annotation of zero height and width shall be an artifact_

A Widget annotation of zero height and width is not marked as an Artifact. Widget annotations of zero width and height are often used to embed an invisible digital signature into the document.

-   Object type: `PDWidgetAnnot`
-   Test condition: `width != 0 || height != 0 || structParentType == null || isArtifact == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.7.5.5

> _A printer's mark annotation shall be an artifact_

A PrinterMark annotation is included in logical structure. Printer marks are used for document printing and have no semantic meaning.

-   Object type: `PDPrinterMarkAnnot`
-   Test condition: `structParentType == null || isArtifact == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.11.3

> _Trap network annotations shall not be used in files conforming to PDF/UA-2_

An annotation of subtype TrapNet exists. TrapNet annotations are used for document printing and have no semantic meaning.

-   Object type: `PDTrapNetAnnot`
-   Test condition: `false`
-   Specification: ISO 14289-2:2024

> _When used as real content, Watermark annotations shall be enclosed within Annot structure elements_

A Watermark annotation is nested within a tag other than Annot

-   Object type: `PDWatermarkAnnot`
-   Test condition: `structParentType == null || isArtifact == true || structParentStandardType == 'Annot'`
-   Specification: ISO 14289-2:2024

> _3D annotation shall include alternate description in respective Contents entry_

3D annotation does not contain Contents entry

-   Object type: `PD3DAnnot`
-   Test condition: `Contents != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.5.2, Table 166

> _RichMedia annotation shall include alternate description in respective Contents entry_

RichMedia annotation does not contain Contents entry

-   Object type: `PDRichMediaAnnot`
-   Test condition: `Contents != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.5.2, Table 166

> _Every page that includes an annotation shall contain a Tabs entry in its page dictionary in accordance with ISO 32000-2:2020, Table 31, and its value shall be A, W or S_

A page with annotation(s) contains Tabs key with value other than A, W or S. The Tabs entry defines the order in which page annotations shall be processed. If this entry is missing, different PDF processors may choose different order, which creates ambiguity in the document presentation.

-   Object type: `PDPage`
-   Test condition: `containsAnnotations == false || Tabs == 'A' || Tabs == 'W' || Tabs == 'S'`
-   Specification: ISO 14289-2:2024

> _Where an annotation has a Contents entry and the directly enclosing structure element has an Alt entry, the values of Alt and Contents shall be identical_

Both Contents and Alt entries are present for the annotation, but they are not identical. They both define an alternative description of the annotation and thus shall be identical.

-   Object type: `PDAnnot`
-   Test condition: `Contents == null || Alt == null || Contents == Alt`
-   Specification: ISO 14289-2:2024

> _Each widget annotation shall be enclosed by a Form structure element unless the widget annotation is an artifact_

A Widget annotation is nested within tag other than Form or Artifact. Widget annotations are used to define interactive forms in PDF.

-   Object type: `PDWidgetAnnot`
-   Test condition: `structParentType == null || structParentStandardType == 'Form' || isArtifact == true`
-   Specification: ISO 14289-2:2024

> _A Form structure element shall contain at most one widget annotation_

A Form structure element contains more than one widget annotation. Widget annotations are used to define interactive forms in PDF.

-   Object type: `SEForm`
-   Test condition: `widgetAnnotsCount <= 1`
-   Specification: ISO 14289-2:2024

> _XFA forms shall not be present_

XFA form is present. XFA is a deprecated technology to construct PDF content dynamically based on XML data. It is not permitted in PDF/UA documents.

-   Object type: `PDAcroForm`
-   Test condition: `containsXFA == false`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, Annex K

> _If a label for a widget annotation is not present, a Contents entry shall be provided to supply description and context for the widget_

Widget annotation contains neither label nor Contents entry. This makes an alternative description of the Widget annotation (or a related form field) undefined.

-   Object type: `PDWidgetAnnot`
-   Test condition: `containsLbl == true || Contents != null`
-   Specification: ISO 14289-2:2024

> _If an additional action (AA) entry is present in a widget annotation dictionary, the respective widget's Contents entry shall be present_

Widget annotation dictionary contains an AA entry, but does not contain the Contents entry

-   Object type: `PDWidgetAnnot`
-   Test condition: `containsAA == false || Contents != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, Table 191

> _For text fields, when an RV entry is present a V entry shall also be present, and they shall be textually equivalent_

Text field contains RV entry, but no V entry or they are not textually equivalent. RV entry defined a rich text version of the plain text of V entry. Both entries stoke the value of the text input field in PDF.

-   Object type: `PDTextField`
-   Test condition: `containsRV == false || (V != null && RV == V)`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, Table 226
    -   ISO 32000-2:2020, Table 228

> _If a portion of the appearance of a signature is represented by a graphic, alternative text shall be provided for that graphic_

A portion of the appearance of a signature is represented by a graphic, but alternative text is not provided for that graphic

-   Object type: `SEGraphicContentItem`
-   Test condition: `isSignature == false || Alt != null`
-   Specification: ISO 14289-2:2024

> _The Metadata stream as specified in ISO 32000-2:2020, 14.3 in the document catalog dictionary shall contain a dc:title entry_

Metadata stream does not contain dc:title. The dc:title metadata property is used by PDF viewers as a title of the viewer window.

-   Object type: `MainXMPPackage`
-   Test condition: `dc_title != null`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.3

> _The Catalog dictionary of a conforming file shall contain the Metadata key whose value is a metadata stream as defined in ISO 32000-2:2020, 14.3. The metadata stream dictionary shall contain entry Type with value /Metadata and entry Subtype with value /XML_

The document catalog dictionary doesn't contain metadata key or metadata stream dictionary does not contain either entry Type with value /Metadata or entry Subtype with value /XML.

-   Object type: `PDDocument`
-   Test condition: `containsMetadata == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 14.3.2

> _The ViewerPreferences dictionary of the document catalog dictionary shall be present and shall contain at least the DisplayDocTitle key with a value of true, as described in ISO 32000-2:2020, Table 147_

ViewerPreferences dictionary is not present in the document Catalog, or DisplayDocTitle key is set to false or is not present in the ViewerPreferences dictionary. This prevents PDF viewers from correctly displaying the title of the document.

-   Object type: `CosDocument`
-   Test condition: `DisplayDocTitle == true`
-   Specification: ISO 14289-2:2024
-   Additional references:
    -   ISO 32000-2:2020, 12.2, Table 147

> _The Desc entry shall be present on all file specification dictionaries present in the EmbeddedFiles name tree of a conforming document_

The file specification dictionary for an embedded file does not contain Desc key

-   Object type: `CosFileSpecification`
-   Test condition: `containsDesc == true || presentInEmbeddedFiles == false`
-   Specification: ISO 14289-2:2024
