---
created: 2026-04-26T13:15:10 (UTC -05:00)
tags: []
source: https://www.section508.gov/create/pdfs/common-tags-and-usage/
author: 
---

# Common PDF Tags and Their Usage | Section508.gov

> ## Excerpt
> As with all types of data, structure is crucial to how readers navigate, access, and comprehend information. Tags are the structural foundation of an accessible Portable Document File (PDF). Each piec

---
As with all types of data, structure is crucial to how readers navigate, access, and comprehend information. Tags are the structural foundation of an accessible Portable Document File (PDF). Each piece of content has a corresponding **tag** that dictates how it is understood and read by assistive technology. This guide helps document authors understand why and how each commonly used tag is used in making an accessible PDF.

## Root Tag

The first tag in any PDF should always be a **<Document>** tag. All tags within a PDF will either be nested directly below it within a container/grouping tag or within a block-level tag.

|    Tag     |   Name   |                    Purpose                     |                                   Show Me                                    |
|------------|----------|------------------------------------------------|------------------------------------------------------------------------------|
| <Document> | Document | Main tag under which all other tags are nested | ![Screenshot of the tags panel showing the 'Document' tag with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-01.jpg) |

Container/grouping tags are not required, but they can be helpful to group tags by chapter or to separate call-out text. They exist directly under the **<Document>** tag.

|  Tag   |  Name   |                                    Purpose                                    |                                                                               Show Me                                                                                |
|--------|---------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <Part> |  Part   |       Large major section of the document (e.g., a chapter of a report)       | ![Screenshot of the tags panel showing the 'Part' tag as the parent element to an 'H1' and 'H2', each with a tag symbols, and a 'P' tag with its paragraph symbol (¶).](https://www.section508.gov/assets/images/pdf-tags-figure-02.jpg) |
| <Sect> | Section | Small section within a larger part (e.g., pull quote, sidebar, or boxed text) |                    ![Screenshot of the tags panel showing the 'SECT' tag as the parent element to two 'P' tags, each with its paragraph symbol (¶).](https://www.section508.gov/assets/images/pdf-tags-figure-03.jpg)                    |

## Text Tags

### Block-Level Heading Tags

Heading tags designate the heading structure and hierarchy of the document. They exist directly below the **<Document>** tag.

|     Tag     |         Name          |            Purpose             |                                   Show Me                                    |
|-------------|-----------------------|--------------------------------|------------------------------------------------------------------------------|
|    <H1>     |       Heading 1       |        Document’s title        | ![Screenshot of the tags panel showing the 'H1' tag along with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-04.jpg) |
|    <H2>     |       Heading 2       | Chapter or main-level headings | ![Screenshot of the tags panel showing the 'H2' tag along with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-05.jpg) |
| <H3> - <H6> | Heading 3 - Heading 6 |     Subsequent subheadings     | ![Screenshot of the tags panel showing the 'H3' tag along with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-06.jpg) |

### Block-Level Text Tags

Block-level text tags designate the main text components of a document, like body text and lists, among others. They exist directly below the **<Document>** tag.

## Root Tag

|     Tag      |       Name        |                                                   Purpose                                                    |                                                                                                        Show Me                                                                                                         |
|--------------|-------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     <P>      |     Paragraph     |                                       Body text (most often used tag)                                        |                                                                 ![Screenshot of the tags panel showing the 'P' tag along with its paragraph symbol (¶).](https://www.section508.gov/assets/images/pdf-tags-figure-07.jpg)                                                                  |
|     <L>      |       List        |                                Main tag under which all list items are nested                                |                        ![Screenshot of the tags panel showing the 'L' tag as the parent element to a 'LI' tag, which is a parent element to a 'Lbl' and 'Body' tag, each with its own tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-08.jpg)                        |
|     <LI>     |     List Item     |                             Each item (bullet and associated text) within a list                             |                        ![Screenshot of the tags panel showing the 'L' tag as the parent element to a 'LI' tag, which is a parent element to a 'Lbl' and 'Body' tag, each with its own tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-08.jpg)                        |
|    <Lbl>     |       Label       |                            Bullet identifier (e.g., bullet point, number, letter)                            |                        ![Screenshot of the tags panel showing the 'L' tag as the parent element to a 'LI' tag, which is a parent element to a 'Lbl' and 'Body' tag, each with its own tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-08.jpg)                        |
|   <LBody>    |    Label Body     |                                         Text of a bulleted list item                                         |                       ![Screenshot of the tags panel showing the 'L' tag as the parent element to a 'LI' tag, which is the parent element to a 'Lbl' and 'Body' tag, each with its own tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-08.jpg)                       |
|    <TOC>     | Table of Contents |                            Main tag under which all Contents TOC items are nested                            |     ![Screenshot of the tags panel showing the 'TOC' tag as the parent element to a 'TOCI' tag, which is the parent element to a 'Reference' tag, the parent element to a 'Link' tag, each with its own tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-09.jpg)      |
|    <TOCI>    |     TOC Item      |           TOC entry (houses the <Reference> and <Link> tag for the TOC entry and its Link - OBJR)            |     ![Screenshot of the tags panel showing the 'TOC' tag as the parent element to a 'TOCI' tag, which is the parent element to a 'Reference' tag, the parent element to a 'Link' tag, each with its own tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-09.jpg)      |
|  <Caption>   |      Caption      | Figure or table caption (placed above or below the figure or table depending on the physical page structure) | ![Screenshot of the tags panel showing the 'Caption' and 'Figure' tag, each with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-10.jpg)<br>![Screenshot of the tags panel showing the 'Caption' tag with its tag symbol, and a 'Table' tag, with its grid symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-11.jpg) |
| <BlockQuote> |       Quote       |                             Block quotes (i.e., long quote in its own paragraph)                             |                                                                     ![Screenshot of the tags panel showing the 'BlockQuote' tag with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-12.jpg)                                                                     |

### Character-Level Text Tags

Character-level tags are nested under a block-level tag, so they should never appear directly under the **<Document>** tag.

|     Tag     |       Name       |                                            Purpose                                             |                                                                                                                                                                                                                                     Show Me                                                                                                                                                                                                                                      |
|-------------|------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   <Link>    |    Hyperlinks    |                             Active link (e.g., URL, email address)                             |                                                                                                                                ![Screenshot of the tags panel showing the 'P' tag as the parent element to a 'Link' tag, which is the parent element to a the object 'www.ed.gov', with its box symbol, and a 'Link' tag each with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-13.jpg)                                                                                                                                 |
|   <OBJR>    | Object Reference |     Active component of the Reference link or reference; must be present within <Link> tag     |                                                                                                                                  ![Screenshot of the tags panel showing the 'P' tag as the parent element to a 'Link' tag, which is the parent element to an object 'www.ed.gov', with its box symbol, and a 'Link' tag each with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-13.jpg)                                                                                                                                  |
| <Reference> |    Reference     |                     Internal link (e.g., cross- reference, footnote, TOC)                      |                                                                               ![Screenshot of the tags panel showing the 'P' tag, with its paragraph symbol (¶), as the parent element to a 'Reference' tag, which is the parent element to a 'Link' tag, each with its box symbol, and a 'Link' tag, each with its tag symbol, as the parent element to a box object '1', and a 'Link - OBJR' tag.](https://www.section508.gov/assets/images/pdf-tags-figure-14.jpg)                                                                                |
|   <Span>    |       Span       | Separator for differently formatted text (e.g., italics, bolding, track changes, highlighting) |                                                                                                                                                                   ![Screenshot of the tags panel showing the 'P' tag, with its paragraph symbol (¶), as the parent element to a 'Span' tag, with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-15.jpg)                                                                                                                                                                   |
|   <Note>    |       Note       |                               Footnote, endnote, or source note                                | ![Screenshot of the tags panel showing the 'P' tag, with its paragraph symbol (¶), as the parent element to object 'Postsecondary...', with its box symbol, a 'Reference' and 'Note' tag, each with a tag symbol, followed by another object 'If a student with...'. The 'Reference' tag is a parent element to a 'Link' tag, which is a parent to an object '33' and 'Link - OBJR' tag. The 'Note' element is also a parent of an object '33 42 U.S.C. §...' with its box symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-16.jpg) |
|   <Form>    |       Form       |        Interactive form-fillable elements (e.g., checkboxes, fillable text, signatures)        |                                                                                                                                    ![Screenshot of the tags panel showing the 'P' tag, with its paragraph symbol (¶), as the parent element to a 'Forms' tag, which is the parent element to a 'Last Name - OBJR' tag, each with a tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-17.jpg)                                                                                                                                     |

Figure and Formula tags contain all image-related tags. They exist below the **<Document>** tag. For both, descriptive alt text should be embedded in the properties of the tag.

|    Tag    |  Name   |                          Purpose                          |                                                                     Show Me                                                                     |
|-----------|---------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <Figure>  | Figure  | Graphic element (e.g., logo, illustration, photo, chart,) | ![Screenshot of the tags panel showing the 'Figure' tag, with its tag symbol, as the parent element to a 'Image (5)' object, with its box symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-18.jpg) |
| <Formula> | Formula |                   Mathematical formula                    |                                  ![Screenshot of the tags panel showing the 'Formula' tag, with its tag symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-19.jpg)                                   |

Table tags contain all table-related tags. They exist below the **<Document>** tag.

|   Tag   |     Name     |                       Purpose                       |                                                                                                                              Show Me                                                                                                                              |
|---------|--------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <Table> |    Table     |    Main tag that houses all table tag components    | ![Screenshot of the tags panel showing the 'Table' tag, with its grid symbol, as the parent element to a 'TR' tag, with its grid row symbol, which is the parent element to a 'TH', with its grid header symbol, and two 'TD' tags, each with its grid cell symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-20.jpg) |
|  <TR>   |  Table Row   | Main tag that houses all tags within a specific row | ![Screenshot of the tags panel showing the 'Table' tag, with its grid symbol, as the parent element to a 'TR' tag, with its grid row symbol, which is the parent element to a 'TH', with its grid header symbol, and two 'TD' tags, each with its grid cell symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-20.jpg) |
|  <TH>   | Table Header |         Heading cells within table row tag          | ![Screenshot of the tags panel showing the 'Table' tag, with its grid symbol, as the parent element to a 'TR' tag, with its grid row symbol, which is the parent element to a 'TH', with its grid header symbol, and two 'TD' tags, each with its grid cell symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-20.jpg) |
|  <TD>   |  Table Data  |           Data cells within table row tag           | ![Screenshot of the tags panel showing the 'Table' tag, with its grid symbol, as the parent element to a 'TR' tag, with its grid row symbol, which is the parent element to a 'TH', with its grid header symbol, and two 'TD' tags, each with its grid cell symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-20.jpg) |

Elements that convey no meaning can be converted to an artifact so that they will not appear in the Tag tree. Screen readers will not read artifacted content. Artifacts can be created via the Content panel and will only appear there.

|    Tag     |   Name   |                 Purpose                  |                                                  Show Me                                                  |
|------------|----------|------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <Artifact> | Artifact | Decorative images, non-essential content | ![Screenshot of the tags panel showing the 'Artifact' tag, with a box symbol similar to the objects symbol.](https://www.section508.gov/assets/images/pdf-tags-figure-21.jpg) |

**NOTE:** Images of tags and their relationships are taken from the Tags panel within Adobe Acrobat Pro for training purposes and do not imply that GSA or ED endorses the product.

**Reviewed/Updated:** August 2024
