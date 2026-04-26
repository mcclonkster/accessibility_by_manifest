---
created: 2026-04-20T20:28:35 (UTC -05:00)
tags: []
source: https://www.colorado.edu/digital-accessibility/pdfs
author: 
---

# Understanding PDF Accessibility | Digital Accessibility Office | University of Colorado Boulder

> ## Excerpt
> This page will teach you how to do some basic assessment of PDFs for accessibility, help you understand the process of creating an accessible PDF, and point you to additional resources that can help y

---
This page will teach you how to do some basic assessment of PDFs for accessibility, help you understand the process of creating an accessible PDF, and point you to additional resources that can help you learn more or experts who can help.

## PDFs and Accessibility

Making accessible PDFs or fixing accessibility problems in existing PDF files can be a complex and highly variable process. 

PDFs are typically created from a source document such as a Microsoft Word, Adobe InDesign, or Microsoft PowerPoint file, and then are exported into the PDF format. Alternatively, many PDF files are simply images of text that are created by scanning hard copy documents. Unfortunately, [image-based PDFs](https://www.colorado.edu/digital-accessibility/resources/accessibility-fundamentals/images-text) are completely inaccessible as they are and require conversion into text using optical character recognition (OCR) software before they are accessible.

Because there are a wide array of source applications that can generate PDF files, creating an accessible PDF file can be a complex process and requires a variety of skills in both Acrobat and the original software in which the document was created. Because of this complexity, one important rule of PDF accessibility is that if you can replace a PDF with a web page or a Word document, you should. HTML documents offer similar functionality to PDFs, such as the inability of viewers to edit the document and the ability to control the way the document is displayed across devices and platforms. PDF accessibility can be complex, and fixing problems in a PDF document requires a high level of expertise that represents a significant investment in training and practice.

To create an accessible PDF from a source file, two things must happen. First, all [accessibility best practices](https://www.colorado.edu/digital-accessibility/resources/content-accessibility-fundamentals) should be followed when creating the document in the original software. Secondly, the process of exporting to PDF must be done in a way that preserves the accessibility features of the original file. If either step does not occur, the resulting PDF will not be accessible. 

If you have an existing inaccessible PDF file and no longer have access to the source file, it can be remediated for accessibility directly within Acrobat Pro, but it is not a simple task. Remediating a PDF file created from an inaccessible Word file, for example, takes much more time than creating an accessible Word file and then exporting it as a PDF.  

[Adobe Acrobat Pro](https://oit.colorado.edu/software-hardware/software-catalog/adobe-acrobat-pro/download-and-setup) is available for download for faculty and staff at CU Boulder at no cost and is required for certain processes to assess or improve the accessibility of PDFs.

## Assessing a PDF for Accessibility

Accessibility is a continuum; the more accessible you want a document to be for all users, the more time and tools you will need for testing, the more knowledge you will need to understand and fix the problems, and the more expert help and training you will need to achieve complete remediation. Learning to achieve basic levels of PDF accessibility is possible without much specialized training; however, complete remediation of a document for accessibility is likely to require expert help or additional training. There are two standards generally used to assess PDF accessibility: WCAG and PDF/UA. Read more in [Adobe’s overview of PDF accessibility](https://www.adobe.com/accessibility/pdf/pdf-accessibility-overview.html).

Instructors: Please consult our [Choosing Accessible PDFs for Your Course](https://www.colorado.edu/digital-accessibility/node/587) guidance for more tips on evaluating PDFs of readings for use in academic contexts.

To start, you may just want a quick test of your document to see how much remediation it may require. There are two basic tests that give you a baseline estimate of the document's accessibility; passing them doesn't guarantee full accessibility, but failing them definitely means that the document is inaccessible.

A PDF should be considered inaccessible if…

## PDFs and Accessibility

-   **It is an image of text.** This can be tested by trying to select text within the PDF. If the entire page highlights when you click on it, that means the text is not selectable and your PDF is an image. To remediate this, run your PDF through an optical character recognition (OCR) program like [SensusAccess](https://oit.colorado.edu/services/business-services/sensusaccess). (Please note that OCR programs like SensusAccess can only conduct automated conversions, and the PDF created will most likely require further editing in Acrobat Pro to ensure 100% accuracy.)
-   **It doesn’t have any tags**. [PDF tag structure](https://www.adobe.com/accessibility/products/acrobat/pdf-repair-add-tags.html) can be assessed within Adobe Acrobat Pro via Document Properties or the Tag panel in the Navigation Pane. A tag allows assistive technology to identify the type of content contained in a PDF, such as paragraphs, images, or tables. Proper conversion processes from programs such as Word will get most elements properly tagged and in the appropriate reading order. If you encounter the text "No Tags available" when you open the Tag pane, then your document is not accessible.  
     
    
    ![Tags pane with the text "No tags available"](https://www.colorado.edu/digital-accessibility/sites/default/files/styles/small_500px_25_display_size_/public/page/screen_shot_2021-02-23_at_9.37.58_am.png?itok=MjV-YT-q)
    

If your PDF fails either of the two tests above, you will need to remediate it. If it passes both, then you may or may not have an accessible document, and more assessment is needed.

The [Accessibility Checker in Acrobat Pro](https://www.adobe.com/accessibility/products/acrobat/using-acrobat-pro-accessibility-checker.html) is a good next step in assessing your document. However, it will only alert you to errors detectable by a computer, like missing alt-text, and is not able to accurately assess things like the accuracy or usability of the alt-text, or errors in the page reading order. To determine if your PDF is fully accessible, you will need to consult with an expert or start to develop your own PDF accessibility expertise by taking the two Lynda.com trainings listed in the Resources section below.

## Creating Accessible PDFs

PDFs are generally created by exporting documents from their native format into PDF. Typically, most PDF documents are created in Microsoft Word, Microsoft PowerPoint, or Adobe InDesign. Regardless of the origin of the document, you must ensure that the document is fully accessible in its native format before you export it to PDF. 

Tutorials for creating accessible source documents:

-   [Creating Accessible Microsoft Word Files](https://www.colorado.edu/digital-accessibility/accessible-technology/node/535)
-   [Creating Accessible PowerPoint Files](https://www.colorado.edu/digital-accessibility/node/529)
-   Creating Accessible InDesign Files: [CS5.5](https://www.washington.edu/accessibility/documents/indesign/), [CS6](https://webaccess.msu.edu/Tutorials/indesign.html)

Then the document must be properly exported to PDF in a way that preserves those accessibility features. WebAIM has a tutorial that walks through the process of [exporting to PDF from MS Word](https://webaim.org/techniques/acrobat/converting#save). See the Resources section below for more tutorials on the export process.

## PDF Forms

Creating accessible PDF forms will always require a significant amount of work within Acrobat Pro. Creating accessible form fields requires more than just dropping form elements into a document. The form creator must ensure that each of the fields is properly named, that all fields are in the proper reading and tab order, and more. Along with all of the steps involved, the form creator needs to complete the steps in the correct order to ensure they function correctly. Specialized training will be needed to create accessible PDF forms. The Lynda.com Advanced Accessible PDFs is a good place to start, but may not be sufficient on its own. Contact [DigitalAccessibility@Colorado.EDU](mailto:digitalaccessibility@colorado.edu) for support with this topic.  

## Resources

LinkedIn Learning has two intensive trainings about [Creating Accessible PDFs](https://www.lynda.com/Acrobat-tutorials/Creating-Accessible-PDFs/669540-2.html) and [Advanced Accessible PDFs](https://www.lynda.com/Acrobat-tutorials/Advanced-Accessible-PDFs/372674-2.html). The trainings are 4.5 and 2.5 hours in length respectively, and may be appropriate for individuals who are frequently required to create accessible PDFs in their position.

The University of Washington has a variety of short tutorials explaining how to create accessible PDFs from other applications and how to remediate PDFs within Acrobat.

-   [Accessible PDFs from MS Word](https://www.washington.edu/accessibility/documents/pdf-word/)
-   [Accessible PDF forms in Acrobat Pro](https://www.washington.edu/accessibility/documents/pdf-forms/)
-   [Accessible PDFs from InDesign](https://www.washington.edu/accessibility/documents/indesign/)
-   [Remediating PDFs in Acrobat Pro](https://www.washington.edu/accessibility/documents/pdf-acrobat/)

If you do not have time to invest in learning about PDF accessibility, there are a variety of vendors who can remediate PDFs and other documents to meet accessibility standards.

Questions? Email [DigitalAccessibility@Colorado.EDU](mailto:digitalaccessibility@colorado.edu).
