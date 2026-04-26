---
created: 2026-04-26T13:13:18 (UTC -05:00)
tags: []
source: https://www.w3.org/TR/wcag2ict-22/
author: Mary Jo Mueller (IBM)
---

# Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT)

> ## Excerpt
> Abstract This document describes how the Web Content Accessibility Guidelines (WCAG) versions 2.0 [WCAG20], 2.1 [WCAG21], and 2.2 [WCAG22] principles, guidelines, and success criteria can be applied t

---
## Abstract

This document describes how the Web Content Accessibility Guidelines (WCAG) versions 2.0 \[[WCAG20](https://www.w3.org/TR/wcag2ict-22/#bib-wcag20 "Web Content Accessibility Guidelines (WCAG) 2.0")\], 2.1 \[[WCAG21](https://www.w3.org/TR/wcag2ict-22/#bib-wcag21 "Web Content Accessibility Guidelines (WCAG) 2.1")\], and 2.2 \[[WCAG22](https://www.w3.org/TR/wcag2ict-22/#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")\] principles, guidelines, and success criteria can be applied to non-web Information and Communications Technologies (ICT), specifically to non-web documents and software. It provides informative guidance (guidance that is not normative and does not set requirements).

This document is part of a series of technical and educational documents published by the [W3C Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/) and available from the [WCAG2ICT Overview](https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/).

## Status of This Document

_This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C standards and drafts index](https://www.w3.org/TR/)._

This is a W3C Group Note on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT). The purpose of this work is to update the previous WCAG2ICT Note's guidance to include changes made in WCAG 2.1 and 2.2, as well as to address public feedback received after first publication of this updated Note.

To comment, file an issue in the [W3C WCAG2ICT](https://github.com/w3c/wcag2ict/) GitHub repository. Create separate GitHub issues for each topic, rather than commenting on multiple topics in a single issue. It is free to create a GitHub account to file issues. If filing issues in GitHub is not feasible, send email to [public-wcag2ict-comments@w3.org](mailto:public-wcag2ict-comments@w3.org) (comment archive).

This document was published by the [Accessibility Guidelines Working Group](https://www.w3.org/groups/wg/ag) as a Group Note using the [Note track](https://www.w3.org/policies/process/20250818/#recs-and-notes).

This Group Note is endorsed by the [Accessibility Guidelines Working Group](https://www.w3.org/groups/wg/ag), but is not endorsed by W3C itself nor its Members.

The [W3C Patent Policy](https://www.w3.org/policies/patent-policy/) does not carry any licensing requirements or commitments on this document.

This document is governed by the [18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/).

## Table of Contents

1.  [Abstract](https://www.w3.org/TR/wcag2ict-22/#abstract)
2.  [Status of This Document](https://www.w3.org/TR/wcag2ict-22/#sotd)
3.  [Introduction](https://www.w3.org/TR/wcag2ict-22/#introduction)
    1.  [Background](https://www.w3.org/TR/wcag2ict-22/#background)
    2.  [Guidance in This Document](https://www.w3.org/TR/wcag2ict-22/#guidance-in-this-document)
        1.  [Interpretation of Web Terminology in a Non-Web Context](https://www.w3.org/TR/wcag2ict-22/#interpretation-of-web-terminology-in-a-non-web-context)
    3.  [Excluded from Scope](https://www.w3.org/TR/wcag2ict-22/#excluded-from-scope)
    4.  [Document Overview](https://www.w3.org/TR/wcag2ict-22/#document-overview)
    5.  [Document Conventions](https://www.w3.org/TR/wcag2ict-22/#document-conventions)
    6.  [Comparison with the 2013 WCAG2ICT Note](https://www.w3.org/TR/wcag2ict-22/#comparison-with-the-2013-wcag2ict-note)
4.  [Key Terms](https://www.w3.org/TR/wcag2ict-22/#key-terms)
    1.  [Accessibility Services of Platform Software](https://www.w3.org/TR/wcag2ict-22/#accessibility-services-of-platform-software)
    2.  [Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#closed-functionality)
    3.  [Content (on and off the web)](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web)
    4.  [Document](https://www.w3.org/TR/wcag2ict-22/#document)
    5.  [Menu-driven Interface](https://www.w3.org/TR/wcag2ict-22/#menu-driven-interface)
    6.  [Platform Software](https://www.w3.org/TR/wcag2ict-22/#platform-software)
    7.  [Set of Documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents)
    8.  [Set of Software Programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs)
    9.  [Software](https://www.w3.org/TR/wcag2ict-22/#software)
    10.  [User Agent](https://www.w3.org/TR/wcag2ict-22/#user-agent)
    11.  [Virtual Keyboard](https://www.w3.org/TR/wcag2ict-22/#virtual-keyboard)
5.  [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality)
6.  [Text / Command-Line / Terminal Applications and Interfaces](https://www.w3.org/TR/wcag2ict-22/#text-command-line-terminal-applications-and-interfaces)
7.  [Comments on Conformance](https://www.w3.org/TR/wcag2ict-22/#comments-on-conformance)
8.  [Comments by Guideline and Success Criterion](https://www.w3.org/TR/wcag2ict-22/#comments-by-guideline-and-success-criterion)
    1.  [1\. Perceivable](https://www.w3.org/TR/wcag2ict-22/#perceivable)
        1.  [1.1 Text Alternatives](https://www.w3.org/TR/wcag2ict-22/#text-alternatives)
            1.  [1.1.1 Non-text Content](https://www.w3.org/TR/wcag2ict-22/#non-text-content)
                
        2.  [1.2 Time-based Media](https://www.w3.org/TR/wcag2ict-22/#time-based-media)
            1.  [1.2.1 Audio-only and Video-only (Prerecorded)](https://www.w3.org/TR/wcag2ict-22/#audio-only-and-video-only-prerecorded)
                
            2.  [1.2.2 Captions (Prerecorded)](https://www.w3.org/TR/wcag2ict-22/#captions-prerecorded)
                
            3.  [1.2.3 Audio Description or Media Alternative (Prerecorded)](https://www.w3.org/TR/wcag2ict-22/#audio-description-or-media-alternative-prerecorded)
                
            4.  [1.2.4 Captions (Live)](https://www.w3.org/TR/wcag2ict-22/#captions-live)
                
            5.  [1.2.5 Audio Description (Prerecorded)](https://www.w3.org/TR/wcag2ict-22/#audio-description-prerecorded)
                
        3.  [1.3 Adaptable](https://www.w3.org/TR/wcag2ict-22/#adaptable)
            1.  [1.3.1 Info and Relationships](https://www.w3.org/TR/wcag2ict-22/#info-and-relationships)
                
            2.  [1.3.2 Meaningful Sequence](https://www.w3.org/TR/wcag2ict-22/#meaningful-sequence)
                
            3.  [1.3.3 Sensory Characteristics](https://www.w3.org/TR/wcag2ict-22/#sensory-characteristics)
                
            4.  [1.3.4 Orientation](https://www.w3.org/TR/wcag2ict-22/#orientation)
                
            5.  [1.3.5 Identify Input Purpose](https://www.w3.org/TR/wcag2ict-22/#identify-input-purpose)
                
        4.  [1.4 Distinguishable](https://www.w3.org/TR/wcag2ict-22/#distinguishable)
            1.  [1.4.1 Use of Color](https://www.w3.org/TR/wcag2ict-22/#use-of-color)
                
            2.  [1.4.2 Audio Control](https://www.w3.org/TR/wcag2ict-22/#audio-control)
                
            3.  [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/wcag2ict-22/#contrast-minimum)
                
            4.  [1.4.4 Resize Text](https://www.w3.org/TR/wcag2ict-22/#resize-text)
                
            5.  [1.4.5 Images of Text](https://www.w3.org/TR/wcag2ict-22/#images-of-text)
                
            6.  [1.4.10 Reflow](https://www.w3.org/TR/wcag2ict-22/#reflow)
                
            7.  [1.4.11 Non-text Contrast](https://www.w3.org/TR/wcag2ict-22/#non-text-contrast)
                
            8.  [1.4.12 Text Spacing](https://www.w3.org/TR/wcag2ict-22/#text-spacing)
                
            9.  [1.4.13 Content on Hover or Focus](https://www.w3.org/TR/wcag2ict-22/#content-on-hover-or-focus)
                
    2.  [2\. Operable](https://www.w3.org/TR/wcag2ict-22/#operable)
        1.  [2.1 Keyboard Accessible](https://www.w3.org/TR/wcag2ict-22/#keyboard-accessible)
            1.  [2.1.1 Keyboard](https://www.w3.org/TR/wcag2ict-22/#keyboard)
                
            2.  [2.1.2 No Keyboard Trap](https://www.w3.org/TR/wcag2ict-22/#no-keyboard-trap)
                
            3.  [2.1.4 Character Key Shortcuts](https://www.w3.org/TR/wcag2ict-22/#character-key-shortcuts)
                
        2.  [2.2 Enough Time](https://www.w3.org/TR/wcag2ict-22/#enough-time)
            1.  [2.2.1 Timing Adjustable](https://www.w3.org/TR/wcag2ict-22/#timing-adjustable)
                
            2.  [2.2.2 Pause, Stop, Hide](https://www.w3.org/TR/wcag2ict-22/#pause-stop-hide)
                
        3.  [2.3 Seizures and Physical Reactions](https://www.w3.org/TR/wcag2ict-22/#seizures-and-physical-reactions)
            1.  [2.3.1 Three Flashes or Below Threshold](https://www.w3.org/TR/wcag2ict-22/#three-flashes-or-below-threshold)
                
        4.  [2.4 Navigable](https://www.w3.org/TR/wcag2ict-22/#navigable)
            1.  [2.4.1 Bypass Blocks](https://www.w3.org/TR/wcag2ict-22/#bypass-blocks)
                
            2.  [2.4.2 Page Titled](https://www.w3.org/TR/wcag2ict-22/#page-titled)
                
            3.  [2.4.3 Focus Order](https://www.w3.org/TR/wcag2ict-22/#focus-order)
                
            4.  [2.4.4 Link Purpose (In Context)](https://www.w3.org/TR/wcag2ict-22/#link-purpose-in-context)
                
            5.  [2.4.5 Multiple Ways](https://www.w3.org/TR/wcag2ict-22/#multiple-ways)
                
            6.  [2.4.6 Headings and Labels](https://www.w3.org/TR/wcag2ict-22/#headings-and-labels)
                
            7.  [2.4.7 Focus Visible](https://www.w3.org/TR/wcag2ict-22/#focus-visible)
                
            8.  [2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/TR/wcag2ict-22/#focus-not-obscured-minimum)
                
        5.  [2.5 Input Modalities](https://www.w3.org/TR/wcag2ict-22/#input-modalities)
            1.  [2.5.1 Pointer Gestures](https://www.w3.org/TR/wcag2ict-22/#pointer-gestures)
                
            2.  [2.5.2 Pointer Cancellation](https://www.w3.org/TR/wcag2ict-22/#pointer-cancellation)
                
            3.  [2.5.3 Label in Name](https://www.w3.org/TR/wcag2ict-22/#label-in-name)
                
            4.  [2.5.4 Motion Actuation](https://www.w3.org/TR/wcag2ict-22/#motion-actuation)
                
            5.  [2.5.7 Dragging Movements](https://www.w3.org/TR/wcag2ict-22/#dragging-movements)
                
            6.  [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/wcag2ict-22/#target-size-minimum)
                
    3.  [3\. Understandable](https://www.w3.org/TR/wcag2ict-22/#understandable)
        1.  [3.1 Readable](https://www.w3.org/TR/wcag2ict-22/#readable)
            1.  [3.1.1 Language of Page](https://www.w3.org/TR/wcag2ict-22/#language-of-page)
                
            2.  [3.1.2 Language of Parts](https://www.w3.org/TR/wcag2ict-22/#language-of-parts)
                
        2.  [3.2 Predictable](https://www.w3.org/TR/wcag2ict-22/#predictable)
            1.  [3.2.1 On Focus](https://www.w3.org/TR/wcag2ict-22/#on-focus)
                
            2.  [3.2.2 On Input](https://www.w3.org/TR/wcag2ict-22/#on-input)
                
            3.  [3.2.3 Consistent Navigation](https://www.w3.org/TR/wcag2ict-22/#consistent-navigation)
                
            4.  [3.2.4 Consistent Identification](https://www.w3.org/TR/wcag2ict-22/#consistent-identification)
                
            5.  [3.2.6 Consistent Help](https://www.w3.org/TR/wcag2ict-22/#consistent-help)
                
        3.  [3.3 Input Assistance](https://www.w3.org/TR/wcag2ict-22/#input-assistance)
            1.  [3.3.1 Error Identification](https://www.w3.org/TR/wcag2ict-22/#error-identification)
                
            2.  [3.3.2 Labels or Instructions](https://www.w3.org/TR/wcag2ict-22/#labels-or-instructions)
                
            3.  [3.3.3 Error Suggestion](https://www.w3.org/TR/wcag2ict-22/#error-suggestion)
                
            4.  [3.3.4 Error Prevention (Legal, Financial, Data)](https://www.w3.org/TR/wcag2ict-22/#error-prevention-legal-financial-data)
                
            5.  [3.3.7 Redundant Entry](https://www.w3.org/TR/wcag2ict-22/#redundant-entry)
                
            6.  [3.3.8 Accessible Authentication (Minimum)](https://www.w3.org/TR/wcag2ict-22/#accessible-authentication-minimum)
                
    4.  [4\. Robust](https://www.w3.org/TR/wcag2ict-22/#robust)
        1.  [4.1 Compatible](https://www.w3.org/TR/wcag2ict-22/#compatible)
            1.  [4.1.1 Parsing (WCAG 2.1)](https://www.w3.org/TR/wcag2ict-22/#parsing21)
                
            2.  [4.1.1 Parsing (WCAG 2.2)](https://www.w3.org/TR/wcag2ict-22/#parsing22)
                
            3.  [4.1.2 Name, Role, Value](https://www.w3.org/TR/wcag2ict-22/#name-role-value)
                
            4.  [4.1.3 Status Messages](https://www.w3.org/TR/wcag2ict-22/#status-messages)
                
9.  [Comments on Definitions in WCAG 2 Glossary](https://www.w3.org/TR/wcag2ict-22/#comments-on-definitions-in-wcag-2-glossary)
    1.  [Glossary Items that Apply to All Technologies](https://www.w3.org/TR/wcag2ict-22/#glossary-items-that-apply-to-all-technologies)
    2.  [Glossary Items Used only in AAA Success Criteria](https://www.w3.org/TR/wcag2ict-22/#glossary-items-used-only-in-aaa-success-criteria)
    3.  [Glossary Items with Specific Guidance](https://www.w3.org/TR/wcag2ict-22/#glossary-items-with-specific-guidance)
        1.  [accessibility supported](https://www.w3.org/TR/wcag2ict-22/#dfn-accessibility-supported)
            
        2.  [ambiguous to users in general](https://www.w3.org/TR/wcag2ict-22/#dfn-ambiguous-to-users-in-general)
            
        3.  [assistive technology](https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies)
            
        4.  [changes of context](https://www.w3.org/TR/wcag2ict-22/#dfn-change-of-context)
            
        5.  [cognitive function test](https://www.w3.org/TR/wcag2ict-22/#dfn-cognitive-function-test)
            
        6.  [conforming alternate version](https://www.w3.org/TR/wcag2ict-22/#dfn-conforming-alternate-versions)
            
        7.  [content](https://www.w3.org/TR/wcag2ict-22/#dfn-content)
            
        8.  [contrast ratio](https://www.w3.org/TR/wcag2ict-22/#dfn-contrast-ratio)
            
        9.  [CSS pixel](https://www.w3.org/TR/wcag2ict-22/#dfn-css-pixels)
            
        10.  [down-event](https://www.w3.org/TR/wcag2ict-22/#dfn-down-event)
            
        11.  [general flash and red flash thresholds](https://www.w3.org/TR/wcag2ict-22/#dfn-general-flash-and-red-flash-thresholds)
            
        12.  [input error](https://www.w3.org/TR/wcag2ict-22/#dfn-input-error)
            
        13.  [keyboard interface](https://www.w3.org/TR/wcag2ict-22/#dfn-keyboard-interface)
            
        14.  [keyboard shortcut](https://www.w3.org/TR/wcag2ict-22/#dfn-keyboard-shortcuts)
            
        15.  [label](https://www.w3.org/TR/wcag2ict-22/#dfn-labels)
            
        16.  [large scale](https://www.w3.org/TR/wcag2ict-22/#dfn-large-scale)
            
        17.  [name](https://www.w3.org/TR/wcag2ict-22/#dfn-name)
            
        18.  [programmatically determined](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-determinable)
            
        19.  [programmatically set](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-set)
            
        20.  [relative luminance](https://www.w3.org/TR/wcag2ict-22/#dfn-relative-luminance)
            
        21.  [role](https://www.w3.org/TR/wcag2ict-22/#dfn-role)
            
        22.  [same functionality](https://www.w3.org/TR/wcag2ict-22/#dfn-same-functionality)
            
        23.  [satisfies a success criterion](https://www.w3.org/TR/wcag2ict-22/#dfn-satisfies)
            
        24.  [set of web pages](https://www.w3.org/TR/wcag2ict-22/#dfn-set-of-web-pages)
            
        25.  [structure](https://www.w3.org/TR/wcag2ict-22/#dfn-structure)
            
        26.  [style property](https://www.w3.org/TR/wcag2ict-22/#dfn-style-properties)
            
        27.  [target](https://www.w3.org/TR/wcag2ict-22/#dfn-targets)
            
        28.  [technology](https://www.w3.org/TR/wcag2ict-22/#dfn-technologies)
            
        29.  [up-event](https://www.w3.org/TR/wcag2ict-22/#dfn-up-event)
            
        30.  [user agent](https://www.w3.org/TR/wcag2ict-22/#dfn-user-agents)
            
        31.  [user interface component](https://www.w3.org/TR/wcag2ict-22/#dfn-user-interface-components)
            
        32.  [viewport](https://www.w3.org/TR/wcag2ict-22/#dfn-viewport)
            
        33.  [web page](https://www.w3.org/TR/wcag2ict-22/#dfn-web-page-s)
            
10.  [Privacy Considerations](https://www.w3.org/TR/wcag2ict-22/#privacy-considerations)
11.  [Security Considerations](https://www.w3.org/TR/wcag2ict-22/#security-considerations)
12.  [A. Success Criteria Problematic for Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#success-criteria-problematic-for-closed-functionality)
13.  [B. Background on Text / Command-Line / Terminal Applications and Interfaces](https://www.w3.org/TR/wcag2ict-22/#background-on-text-command-line-terminal-applications-and-interfaces)
    1.  [B.1 How Text Interfaces Are Realized](https://www.w3.org/TR/wcag2ict-22/#how-text-interfaces-are-realized)
    2.  [B.2 How Text Applications Have Been Made Accessible Via Assistive Technology](https://www.w3.org/TR/wcag2ict-22/#how-text-applications-have-been-made-accessible-via-assistive-technology)
    3.  [B.3 Applying WCAG 2 to Text Applications](https://www.w3.org/TR/wcag2ict-22/#applying-wcag-2-to-text-applications)
14.  [C. Acknowledgements](https://www.w3.org/TR/wcag2ict-22/#acknowledgements)
    1.  [C.1 Active Participants of the WCAG2ICT Task Force Involved in the Development of This Document](https://www.w3.org/TR/wcag2ict-22/#active-participants-of-the-wcag2ict-task-force-involved-in-the-development-of-this-document)
    2.  [C.2 Participants in the AG Working Group that Actively Reviewed and Contributed](https://www.w3.org/TR/wcag2ict-22/#participants-in-the-ag-working-group-that-actively-reviewed-and-contributed)
    3.  [C.3 Other Participants of the WCAG2ICT Task Force](https://www.w3.org/TR/wcag2ict-22/#other-participants-of-the-wcag2ict-task-force)
    4.  [C.4 Previous Contributors](https://www.w3.org/TR/wcag2ict-22/#previous-contributors)
    5.  [C.5 Enabling Funders](https://www.w3.org/TR/wcag2ict-22/#enabling-funders)
15.  [D. Changelog](https://www.w3.org/TR/wcag2ict-22/#changelog)
    1.  [D.1 Changes since the 21 August 2025 Note](https://www.w3.org/TR/wcag2ict-22/#changes-since-20250821)
    2.  [D.2 Changes since the 15 November 2024 Note](https://www.w3.org/TR/wcag2ict-22/#changes-since-20241115)
16.  [E. References](https://www.w3.org/TR/wcag2ict-22/#references)
    1.  [E.1 Informative references](https://www.w3.org/TR/wcag2ict-22/#informative-references)

## Introduction

### Background

This document is an update to a W3C [Working Group Note](https://www.w3.org/2005/10/Process-20051014/tr#WGNote) to incorporate new guidelines, success criteria, and definitions added in WCAG 2.1 and 2.2.

[Guidance on Applying WCAG 2.0 to Non-Web Information and Communications Technologies (WCAG2ICT)](https://www.w3.org/TR/2013/NOTE-wcag2ict-20130905/), approved in September 2013, described how WCAG 2.0 could be applied to non-web documents and software. WCAG2ICT was organized to mirror WCAG's sections: Perceivable, Operable, Understandable, and Robust. WCAG2ICT clarified when and how WCAG success criteria could be applied to non-web documents and software. Some were applicable without modification and some were applicable with edits and/or notes. Glossary terms were also reviewed. Level AAA success criteria were not addressed in the 2013 WCAG2ICT Working Group Note.

The 2013 version of WCAG2ICT has been relied upon in regulations and legislation. An example is \[[etsi-en-301-549](https://www.w3.org/TR/wcag2ict-22/#bib-etsi-en-301-549 "ETSI EN 301 549 V3.2.1 (2021-03): Accessibility requirements for ICT products and services")\] (Europe) as well as other standards that reference or incorporate EN 301 549 (e.g., India, Kenya, Australia). Another example is the U.S. Section 508’s [Application of WCAG 2.0 to Non-Web ICT](https://www.federalregister.gov/documents/2017/01/18/2017-00395/information-and-communication-technology-ict-standards-and-guidelines#h-36), where WCAG was incorporated by reference into Section 508 as the [accessibility standard applicable to non-web documents](https://www.access-board.gov/ict/#E205.4) and which also requires [WCAG conformance for non-web software](https://www.access-board.gov/ict/#E207.2).

These standards looked to WCAG2ICT for detailed direction and guidance on how to apply WCAG non-web technology. The WCAG2ICT guidance also led to a few exceptions where specific success criteria are not required in non-web contexts.

### Guidance in This Document

This document provides informative guidance (guidance that is not [normative](https://www.w3.org/TR/WCAG22/#dfn-normative) and does not set requirements) with regard to the interpretation and application of Web Content Accessibility Guidelines (WCAG) to non-web information and communications technologies (ICT). This document is a [Working Group Note](https://www.w3.org/2021/Process-20211102/#WGNote) (in contrast to WCAG 2.0, WCAG 2.1, and WCAG 2.2, which are W3C Recommendations). Specifically, this document provides informative guidance on applying WCAG 2.0, 2.1, and 2.2 Level A and AA success criteria to non-web ICT, specifically to non-web documents and software.

Note 1

Hereafter, the use of WCAG 2 means all WCAG 2.x versions — 2.0, 2.1, and 2.2.

This document is intended to help clarify how to use WCAG 2 to make non-web documents and software more accessible to people with disabilities. Addressing accessibility involves addressing the needs of people with auditory, cognitive, neurological, physical, speech, and visual impairments, as well as the accessibility needs of people caused by the effects of aging. Although WCAG 2 addresses some user needs for people with cognitive and learning disabilities, as well as those with mental health-related disabilities, following the WCAG supplement [Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) is recommended for non-web ICT in order to address the user needs of these groups. Developers are also encouraged to obtain testing input from people with disabilities who use their applications and content.

Although this document covers a wide range of issues, it is not able to address all the needs of all people with disabilities. Since WCAG 2 was developed for the Web, addressing accessibility for non-web documents and software may involve requirements and considerations beyond those included in this document. Authors and developers are encouraged to seek relevant advice about current best practices to ensure that non-web documents and software are as accessible as possible to people with disabilities. The following supporting documents contain helpful information for learning about the user needs, intent, and generalized implementation techniques to support a wider range of people with disabilities:

-   [WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
-   [Techniques for WCAG 2.2](https://www.w3.org/WAI/WCAG22/Techniques/) \[[WCAG22-TECHS](https://www.w3.org/TR/wcag2ict-22/#bib-wcag22-techs "Techniques for WCAG 2.2")\]
-   [How to Meet WCAG (Quick Reference)](https://www.w3.org/WAI/WCAG22/quickref/)
-   [Additional Accessibility Guidelines Working Group - Publications](https://www.w3.org/groups/wg/ag/publications/)

While WCAG 2 was designed to be technology neutral, it assumes the presence of a “user agent” such as a browser, media player, or assistive technology that is used as a means to access web content. As a result, the application of WCAG 2 to documents and software in non-web contexts necessitates some interpretation in order to determine how the intent of each WCAG 2 success criterion could be met in these different contexts of use. Therefore, the bulk of the WCAG2ICT Task Force's work involved evaluating how each WCAG 2 success criterion would apply in the context of non-web ICT.

The WCAG2ICT Task Force found that the majority of WCAG 2 success criteria can be applied to non-web documents and software with either no or minimal changes. Since many of the Level A and Level AA success criteria do not include any web-related terms, they apply directly as written and as described in the “Intent” sections from the [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) \[[UNDERSTANDING-WCAG22](https://www.w3.org/TR/wcag2ict-22/#bib-understanding-wcag22 "Understanding Web Content Accessibility Guidelines 2.2")\] resource. Additional notes were provided, as needed, to increase understanding about applying WCAG success criteria to non-web documents and software.

#### Interpretation of Web Terminology in a Non-Web Context

When certain web-specific terms or phrases like “web page(s)” were used in success criteria, those were replaced with non-web terms or phrases like “non-web document(s) and software”. Additional notes were also provided to explain the terminology replacements.

A small number of success criteria are written to apply to “a set of web pages” or “multiple web pages” and depend upon all pages in the set to share some characteristic or behavior. Since the unit of conformance in WCAG 2 is a single web page, the task force agreed that the equivalent unit of conformance for non-web documents is a single document. It follows that an equivalent unit of evaluation for a “set of web pages” would be a “set of documents”. Since it isn't possible to unambiguously carve up non-web software into discrete pieces, a single “web page” was equated to a “software program” and a “set of web pages” was equated to a “set of software programs”.  Both of these terms are defined in the Key Terms section of this document. See “[set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents)” and “[set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs)” to determine when a group of documents or pieces of software are considered a set.

Note

Sets of non-web software that meet this definition appear to be extremely rare.

Not all success criteria have been fully adopted in all local regulations and legislation, and may not be applicable to all technologies. WCAG2ICT has been used in some regulations to determine whether or not to apply certain success criteria. For example, some local standards such as Section 508 in the U.S., and EN 301 549 in Europe, state that WCAG 2.0 Success Criteria 2.4.1 Bypass Blocks, 2.4.5 Multiple Ways, 3.2.3 Consistent Navigation, and 3.2.4 Consistent Identification do not apply to non-web documents and non-web software. In addition, EN 301 549 states that 2.4.2 Page Titled and 3.1.2 Language of Parts do not apply to non-web software. In contrast, the U.S. Department of Justice regulation, Nondiscrimination on the Basis of Disability; Accessibility of Web Information and Services of State and Local Government Entities (89 FR 31320, 24 April 2024), directs implementers to utilize the guidance in this document to determine the applicability of success criteria and how to apply the requirements to mobile applications. Since this document does not specifically say which criteria can or should apply, those implementing this document (WCAG2ICT) should consider the applicability of individual success criteria to non-web documents and software.

The glossary terms in WCAG 2 were also reviewed and most of them applied to non-web documents and software, as written. Some applied with additional notes or edits (largely related to phrases like “web page(s)”), and a small number of terms were only used in Level AAA success criteria, which are not addressed by the WCAG2ICT Note at this time.

### Excluded from Scope

The following are out of scope for this document:

-   This document does not seek to determine which WCAG 2 provisions (principles, guidelines, or success criteria) should or should not apply to non-web documents and software, but rather — if applied — _how_ they would apply.
-   This document does not propose changes to WCAG 2 or its supporting documents. However, during the development of this document, the WCAG2ICT Task Force did seek clarification on the intent of a number of the success criteria, which led to clarifications in the Understanding WCAG 2 document.
-   This document does not include interpretations for implementing WCAG 2 in web technologies.
-   This document is not sufficient by itself to ensure accessibility in non-web documents and software. This is because this document does not address accessibility requirements beyond those covered by WCAG which, as a web standard, does not fully cover all accessibility requirements for non-user interface aspects of platforms, user-interface components as individual items, or ICT with closed functionality (where there is no assistive technology to communicate programmatic information).
-   This document does not comment on hardware aspects of products because the basic constructs on which WCAG 2 is built do not apply to hardware.
-   This document does not provide supporting techniques for implementing WCAG 2 in non-web documents and software.
-   This document is purely an informative Note about non-web ICT. It is not a standard — so it does not describe how non-web ICT should conform to it.

### Document Overview

This document includes text quoted from the WCAG 2.2 principles, guidelines, success criteria, and glossary definitions without any changes. The guidance provided by this document for each principle, guideline, success criterion, and definition is preceded by a heading beginning with “Applying…”. This guidance was created by the WCAG2ICT Task Force, then reviewed and approved by the Accessibility Guidelines Working Group.

### Document Conventions

The following stylistic conventions are used in this document:

-   Quotes from WCAG 2 are in `<blockquote>` elements and visually styled with a gray bar on the left, and immediately follow the heading for the principle, guideline, or success criterion.
-   Additional guidance provided by this document begins with the phrase “Applying” and has no special visual styling.
-   Replacement text that is presented to show how a success criterion would read as modified by the advice in this document are in `<ins>` elements that are visually styled as green text with a dotted underline.
-   Links that are contained in the word replacement text are also styled with bold text.
-   Notes are slightly inset and begin with the phrase “NOTE” — each note is in its own inset box that is styled in pale green with a darker green line on the left side of the box.
-   Where WCAG Notes have been replaced or significantly rewritten in the guidance, they are notated with "(REPLACED)"; and where WCAG2ICT added new notes, they are notated with "(ADDED)".
-   References to glossary items from WCAG 2 are presented in `<cite>` elements that are visually styled as ordinary text with a dotted underline, and contain title attributes noting these are WCAG definitions — they turn blue with a yellow background when mouse or keyboard focus is placed over them.
-   References to glossary items in this document are presented in `<cite>` elements that are visually styled as ordinary text with a dark gray underline.
-   Hereafter, the short title “WCAG2ICT” is used to reference this document.
-   In headings, the term "Success Criterion" has been shortened to “SC” for brevity.

The following changes and additions have been made to update the 2013 WCAG2ICT document to incorporate the [new features in WCAG 2.1](https://www.w3.org/TR/WCAG21/#new-features-in-wcag-2-1), the [new features in WCAG 2.2](https://www.w3.org/TR/WCAG22/#new-features-in-wcag-2-2), and the change to 4.1.1 Parsing listed in the [Comparison with WCAG 2.1](https://www.w3.org/TR/WCAG22/#comparison-with-wcag-2-1) section:

-   New [Background](https://www.w3.org/TR/wcag2ict-22/#background) section to explain the history and known uses of WCAG2ICT
-   New key terms introduced by WCAG2ICT:
    -   [closed functionality](https://www.w3.org/TR/wcag2ict-22/#closed-functionality)
    -   [menu-driven interface](https://www.w3.org/TR/wcag2ict-22/#menu-driven-interface)
    -   [platform software](https://www.w3.org/TR/wcag2ict-22/#platform-software)
    -   [virtual keyboard](https://www.w3.org/TR/wcag2ict-22/#virtual-keyboard)
-   New WCAG 2.1 success criteria and guidelines:
    -   [Success Criterion 1.3.4 Orientation](https://www.w3.org/TR/wcag2ict-22/#orientation)
    -   [Success Criterion 1.3.5 Identify Input Purpose](https://www.w3.org/TR/wcag2ict-22/#identify-input-purpose)
    -   [Success Criterion 1.4.10 Reflow](https://www.w3.org/TR/wcag2ict-22/#reflow)
    -   [Success Criterion 1.4.11 Non-text Contrast](https://www.w3.org/TR/wcag2ict-22/#non-text-contrast)
    -   [Success Criterion 1.4.12 Text Spacing](https://www.w3.org/TR/wcag2ict-22/#text-spacing)
    -   [Success Criterion 1.4.13 Content on Hover or Focus](https://www.w3.org/TR/wcag2ict-22/#content-on-hover-or-focus)
    -   [Success Criterion 2.1.4 Character Key Shortcuts](https://www.w3.org/TR/wcag2ict-22/#character-key-shortcuts)
    -   [Guideline 2.5 Input Modalities](https://www.w3.org/TR/wcag2ict-22/#input-modalities)
    -   [Success Criterion 2.5.1 Pointer Gestures](https://www.w3.org/TR/wcag2ict-22/#pointer-gestures)
    -   [Success Criterion 2.5.2 Pointer Cancellation](https://www.w3.org/TR/wcag2ict-22/#pointer-cancellation)
    -   [Success Criterion 2.5.3 Label in Name](https://www.w3.org/TR/wcag2ict-22/#label-in-name)
    -   [Success Criterion 2.5.4 Motion Actuation](https://www.w3.org/TR/wcag2ict-22/#motion-actuation)
    -   [Success Criterion 4.1.3 Status Messages](https://www.w3.org/TR/wcag2ict-22/#status-messages)
-   New WCAG 2.2 success criteria:
    -   [Success Criterion 2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/TR/wcag2ict-22/#focus-not-obscured-minimum)
    -   [Success Criterion 2.5.7 Dragging Movements](https://www.w3.org/TR/wcag2ict-22/#dragging-movements)
    -   [Success Criterion 2.5.8 Target Size (Minimum)](https://www.w3.org/TR/wcag2ict-22/#target-size-minimum)
    -   [Success Criterion 3.2.6 Consistent Help](https://www.w3.org/TR/wcag2ict-22/#consistent-help)
    -   [Success Criterion 3.3.7 Redundant Entry](https://www.w3.org/TR/wcag2ict-22/#redundant-entry)
    -   [Success Criterion 3.3.8 Accessible Authentication (Minimum)](https://www.w3.org/TR/wcag2ict-22/#accessible-authentication-minimum)
-   Obsolete and Removed WCAG 2.2 success criteria that have errata for WCAG 2.0 and 2.1:
    -   [Success Criterion 4.1.1 Parsing](https://www.w3.org/TR/wcag2ict-22/#parsing22)
-   New terms from WCAG 2.1 and 2.2:
    -   added to [Glossary Items that Apply to All Technologies](https://www.w3.org/TR/wcag2ict-22/#glossary-items-that-apply-to-all-technologies):
        -   dragging movements, focus indicator, minimum bounding box, pointer input, process, single pointer, state, and status message
    -   added to [Glossary Items Used only in AAA Success Criteria](https://www.w3.org/TR/wcag2ict-22/#glossary-items-used-only-in-aaa-success-criteria):
        -   motion animation, perimeter, region, and user inactivity
    -   added to [Glossary Items with Specific Guidance](https://www.w3.org/TR/wcag2ict-22/#glossary-items-with-specific-guidance):
        -   [cognitive function test](https://www.w3.org/TR/wcag2ict-22/#dfn-cognitive-function-test)
        -   [css pixel](https://www.w3.org/TR/wcag2ict-22/#dfn-css-pixels)
        -   [down event](https://www.w3.org/TR/wcag2ict-22/#dfn-down-event)
        -   [keyboard shortcut](https://www.w3.org/TR/wcag2ict-22/#dfn-keyboard-shortcuts)
        -   [style property](https://www.w3.org/TR/wcag2ict-22/#dfn-style-properties)
        -   [target](https://www.w3.org/TR/wcag2ict-22/#dfn-targets)
        -   [up event](https://www.w3.org/TR/wcag2ict-22/#dfn-up-event)
-   Updated terms:
    -   [large scale](https://www.w3.org/TR/wcag2ict-22/#dfn-large-scale)
    -   [set of web pages](https://www.w3.org/TR/wcag2ict-22/#dfn-set-of-web-pages)
    -   [set of non-web documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents)
    -   [set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs)
-   Updated sections:
    
    Note
    
    -   All of the existing sections have undergone WCAG2ICT Task Force review to identify the necessary updates.
    -   Many sections needed only minor editorial and link URL updates, such as the guidance for the WCAG 2.0 success criteria.
    

## Key Terms

WCAG2ICT provides some key glossary terms to address differences between web and non-web contexts and to introduce terms that are nonexistent in WCAG but important to define for a non-web context. “Content” and “user agent” are glossary terms from WCAG 2 that need to be interpreted significantly differently when applied to non-web ICT. The glossary term “web page” in WCAG 2 is replaced with the defined terms “document” and “software”, and both “set of web pages” and “multiple web pages” are replaced with the defined terms “set of documents” and “set of software programs”. The terms introduced by WCAG2ICT are “accessibility services of platform software” because non-web software doesn't leverage the WCAG notion of a user agent, and "closed functionality" which is specific to non-web software. The remaining glossary terms from WCAG 2 are addressed in [Chapter 7 Comments on Definitions in WCAG 2 Glossary](https://www.w3.org/TR/wcag2ict-22/#comments-on-definitions-in-wcag-2-glossary). Terms defined and used in WCAG2ICT are applicable only to the interpretation of the guidance in this document. The particular definitions should not be interpreted as having applicability to situations beyond the scope of WCAG2ICT. Further information on usage of these terms follows.

### Accessibility Services of Platform Software

The term **accessibility services of platform software**, as used in WCAG2ICT, has the meaning below:

accessibility services of platform software (as used in WCAG2ICT)

services provided by an operating system, [user agent](https://www.w3.org/TR/wcag2ict-22/#user-agent), or other [platform software](https://www.w3.org/TR/wcag2ict-22/#platform-software) that enable non-web [documents](https://www.w3.org/TR/wcag2ict-22/#document) or [software](https://www.w3.org/TR/wcag2ict-22/#software) to expose information about the user interface and events to assistive technologies and accessibility features of software

Note

These services are commonly provided in the form of accessibility APIs (application programming interfaces), and they provide two-way communication with assistive technologies, including exposing information about objects and events.

### Closed Functionality

The term **closed functionality**, as used in WCAG2ICT, has the meaning below:

closed functionality (as used in WCAG2ICT)

a property or characteristic that prevents users from attaching, installing, or using [assistive technology](https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies)

Note 1

To support users with disabilities, ICT with closed functionality might instead provide built-in features that function as assistive technology or use other mechanisms to make the technology accessible.

Example: Examples of technology that may have closed functionality include but are not limited to:

-   self-service transaction machines or kiosks — examples include machines used for retail self-checkout, point of sales (POS) terminals, ticketing and self-check-in, and Automated Teller Machines (ATMs).
-   telephony devices such as internet phones, feature phones, smartphones, and phone-enabled tablets
-   educational devices such as interactive whiteboards and smart boards
-   entertainment technologies including gaming platforms or consoles, smart TVs, set-top boxes, smart displays, smart speakers, smart watches, and tablets
-   an ebook reader or standalone ebook software that allows assistive technologies to access all of the user interface controls of the ebook program (open functionality) but does not allow the assistive technologies to access the actual content of book (closed functionality).
-   medical devices such as digital blood pressure monitors, glucose meters, or other wearable devices
-   an operating system that makes the user provide login credentials before it allows any assistive technologies to be loaded. The login portion would be closed functionality.
-   other technology devices, such as printers, displays, and Internet of Things (IoT) devices

Note 2

Some of these technologies, though closed to some external assistive technologies, often have extensive internal accessibility features that serve as assistive technology that can be used by applications on these devices in the same way assistive technology is used on fully open devices, such as desktop computers. Others are open to some types of assistive technology but not others.

### Content (on and off the web)

WCAG 2 defines **content** as:

> information and sensory experience to be communicated to the user by means of a [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents), including code or markup that defines the content's [structure](https://www.w3.org/TR/WCAG22/#dfn-structure), [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation), and interactions

For non-web content it is necessary to view this a bit more broadly. Within WCAG2ICT, the term “content” is used as follows:

content (non-web content) (as used in WCAG2ICT)

information and sensory experience to be communicated to the user by means of **<ins>[<a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a>]</ins>**, including code or markup that defines the content's [structure](https://www.w3.org/TR/wcag2ict-22/#dfn-structure), [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation), and interactions

Note 1

Non-web content occurs in two places; documents and software. When content occurs in a non-web document, a user agent is needed in order to communicate the content's information and sensory experience to the user. When content occurs in non-web software, a separate user agent isn't needed — the software itself performs that function.

Note 2

Content from a third party needs special consideration since sometimes it may be under the control of the author (e.g. contracted and therefore may not be considered 3rd party) and sometimes it is completely out of the control of the author (e.g. email in an email client).

Note 3

For non-web software, content also includes the user interface.

Note 4

Within WCAG2ICT wherever “content” or “web content” appears in a success criterion it is replaced with “content” using the definition above.

### Document

The term **document**, as used in WCAG2ICT, has the meaning below:

document (as used in WCAG2ICT)

assembly of [content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web), such as a file, set of files, or streamed media that functions as a single item rather than a collection, that is not part of software and that does not include its own user agent

Note 1

A document always depends upon a user agent to present its content to the user.

Note 2

Letters, spreadsheets, emails, books, pictures, presentations, and movies are examples of documents.

Note 3

Software configuration and storage files such as databases and virus definitions, as well as computer instruction files such as source code, batch/script files, and firmware, are examples of files that function as part of [software](https://www.w3.org/TR/wcag2ict-22/#software) and thus are not examples of documents. If and where software retrieves “information and sensory experience to be communicated to the user” from such files, it is just another part of the content that occurs in software and is covered by WCAG2ICT like any other parts of the software. Where such files contain one or more embedded documents, the embedded documents remain documents under this definition.

Note 4

A collection of files zipped together into an archive, stored within a single virtual hard drive file, or stored in a single "encrypted file system" file, do not constitute a single document.

Note 5

Anything that can present its own content without involving a user agent, such as a self-playing book, is not a document but is software.

Note 6

A single document may be composed of multiple files such as the video content, closed caption text, etc. This fact is not usually apparent to the end-user consuming the document / content. This is similar to how a single web page can be composed of content from multiple URIs (e.g. the page text, images, the JavaScript, a CSS file etc.).

Example: An assembly of files that represented the video, audio, captions, and timing files for a movie would be a document.

Counterexample: A binder file used to bind together the various exhibits for a legal case would not be a document.

### Platform Software

The term **platform software**, as used in WCAG2ICT, has the meaning below:

platform software

software that runs on an underlying software or hardware layer and that provides a set of software services to other software components

Note 1

Platform software may run or host other software, and may isolate them from underlying software or hardware layers.

Note 2

A single software component may have both platform and non-platform aspects.

Example: Examples of platforms are: desktop operating systems; embedded operating systems, including mobile systems; web browsers; plug-ins to web browsers that render a particular media or format; and sets of components that allow other applications to execute, such as applications which support macros or scripting.

This definition is based on the definition of "platform software" found in \[[ISO\_9241-171](https://www.w3.org/TR/wcag2ict-22/#bib-iso_9241-171 "Ergonomics of human-system interaction Part 171: Guidance on software accessibility")\] and \[[ISO/IEC\_13066-1](https://www.w3.org/TR/wcag2ict-22/#bib-iso/iec_13066-1 "Information technology - Interoperability with assistive technology (AT) Part 1: Requirements and recommendations for interoperability")\].

### Set of Documents

The term **set of documents**, as used in WCAG2ICT, has the meaning below:

set of documents (non-web) (as used in WCAG2ICT)

collection of **<ins>[<a href="https://www.w3.org/TR/wcag2ict-22/#document">documents</a>]</ins>** that share a common purpose; are created by the same author, group or organization; **<ins>[are published together; and all refer to each other by name or link]</ins>**

Note 1

Republishing or bundling previously published documents as a collection does not constitute a set of documents.

Note 2

If a set is broken apart, the individual parts are no longer part of a set, and would be evaluated as any other individual document is evaluated.

Example: One example of a set of documents would be a three-part report where each part is a separate file. The table of contents is repeated at the beginning of each file to enable navigation to the other parts.

### Set of Software Programs

The term **set of software programs**, as used in WCAG2ICT, has the meaning below:

set of software programs (as used in WCAG2ICT)

collection of **<ins>[<a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a> programs]</ins>** that share a common purpose; are created by the same author, group or organization; **<ins>[and are distributed together and can be launched and used independently from each other, but are interlinked each with every other one such that users can navigate from one program to another via a consistent method that appears in each member of the set]</ins>**

Note 1

Although "sets of web pages" occur frequently, "sets of software programs" appear to be extremely rare.

Note 2

Redistributing or bundling previously distributed software as a collection does not constitute a set of software programs.

Note 3

Consistent does not mean identical. For example, if a list of choices is provided it might not include the name of the current program.

Note 4

If a member of the set is separated from the set, it is no longer part of a set, and would be evaluated as any other individual software program.

Note 5

Any software program that is not part of a set, per this definition, would automatically [satisfy any success criterion](https://www.w3.org/TR/wcag2ict-22/#dfn-satisfies) that is specified to apply to “sets of” software (as is true for any success criterion that is scoped to only apply to some other type of content).

Note 6

If there is any ambiguity whether the group is a set, then the group is not a set.

Note 7

If there is no independent method to launch the software programs (as is common in ICT with closed functionality), those programs would not meet the definition of a “set of software programs”.

Note 8

Although the term “software” is used throughout this document because this would apply to stand-alone software programs as well as individual software components and the software components in software-hardware combinations, the concept of “set of software programs” would only apply (by definition) to programs that can be launched separately from each other. Therefore, in the WCAG2ICT guidance for the provisions that use the phrase “set of” (success criteria 2.4.1, 2.4.5, 3.2.3, 3.2.4, and 3.2.6), the phrase “set of software programs” is used.

Example: One example of a set of software programs would be a group of programs that can be launched and used separately but are distributed together and all have a menu that allows users to launch, or switch to, each of the other programs in the group.

Counterexamples: Examples of things that are **not** sets of software programs:

-   A suite of programs for authoring different types of documents (text, spreadsheets, presentations, etc.) where the programs don't provide an explicit, consistent means to launch, or switch to, each of the other programs in the group.
-   An office package consisting of multiple programs that launches as a single program that provides multiple functionalities such as writing, spreadsheet, etc., but the only way to navigate between programs is to open a document in one of the programs.
-   A bundle of software programs that is sold together but the only way to navigate between the programs in the bundle is to use a platform software level menu to navigate between them (and not via a menu provided by each program that allows you to navigate to just the other programs in this bundle).
-   A group of programs that was a set, but the programs have been moved to separate locations so that their “set” behaviors were disrupted and no longer work. Even though they _were_ a set at one time, because they are no longer installed as a set they no longer _are_ a set and would not need to meet any success criteria that apply to sets of software.

### Software

The term **software** as used in WCAG2ICT, has the meaning below:

software (as used in WCAG2ICT)

software products, or software aspects of hardware-software products, that have a user interface and do not depend upon a separate [user agent](https://www.w3.org/TR/wcag2ict-22/#user-agent) to present any of its [content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web)

Note 1

For software, the user interface and any other embedded content is covered by these guidelines. The software provides a function equivalent to a user agent for the embedded content.

Note 2

Software without a user interface does not have content and is not covered by these guidelines. For example, driver software with no user interface would not be covered.

Note 3

Because software with a user interface provides a function equivalent to a user agent in addition to content, the application of some WCAG 2 success criteria would be different for content embedded in software versus content in a document, where it is viewed through a separate user agent (e.g. browser, player, viewer, etc.).

### User Agent

WCAG 2 defines **user agent** as:

> any software that retrieves and presents web content for users
> 
> Example: Web browsers, media players, plug-ins, and other programs — including [assistive technologies](https://www.w3.org/TR/wcag22/#dfn-assistive-technologies) — that help in retrieving, rendering, and interacting with web content.

For non-web ICT, “user agent” needs to be viewed differently. In WCAG 2, the term “user agent” only refers to retrieval and display of web content. For non-web ICT, the term “user agent” refers to retrieval and display of separate content that is _not on the web_, which WCAG2ICT refers to as a “document”. Within WCAG2ICT, the term “user agent” is used as follows:

user agent (as used in WCAG2ICT)

any [software](https://www.w3.org/TR/wcag2ict-22/#software) that retrieves and presents **<ins>[documents]</ins>** for users

Note 1

Software that only displays the [content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web) contained within it is not considered to be a user agent. It is just considered to be software.

Note 2

An example of software that is not a user agent is a calculator application that doesn't retrieve the calculations from outside the software to present it to a user. In this case, the calculator software is not a user agent, it is simply software with a user interface.

Note 3

Software that only shows a preview of content, such as a thumbnail or other non-fully functioning presentation, is not providing full user agent functionality.

### Virtual Keyboard

The term **virtual keyboard**, as used in WCAG2ICT, has the meaning below:

virtual keyboard (as used in WCAG2ICT)

any software that acts as a keyboard and generates output that is treated by other software as keystrokes from a keyboard

Note

Eye-gaze, morse code, speech, and switches (e.g. sip-and-puff) have all been used by virtual keyboards as input that generates "keystroke" output.

## Text / Command-Line / Terminal Applications and Interfaces

Text applications are a class of software ICT that appeared decades ago, prior to the emergence of the graphical user interface (GUI) and the Web. The interface of a text application is generated using only text characters, and either a hardware terminal or a software terminal application handles the rendering of the text application—similar to how a web user agent handles the rendering of a web application. Text applications only accept text input, though some may also support the use of a mouse or other input devices. More recently, terminal applications that render text applications in the GUI may utilize spoken input through Automated Speech Recognition (ASR). Both GUI and native text environment interfaces also now commonly support word-completion prediction technologies. Command-line applications are a subset of text applications with further specific properties.

Historically, assistive technologies developed alongside text applications, making it possible for text applications to be accessible. Although there are far fewer new text applications being developed compared to new GUI or web applications, text applications remain in use today. In fact, command-line interfaces have seen a resurgence in recent years, especially in popular programming and revision-tracking environments with continued development and greater functionality. In some cases this has precipitated renewed developments in assistive technology support for text applications.

Assistive technology support continues to evolve in today's text applications. Key examples include:

-   In command line interfaces (CLI), support often includes context-sensitive help, so that help output following one command argument is different from the help provided following two arguments, and different still after three arguments. This helps users be more efficient and places no new requirements on assistive technologies.
-   Output options generally include machine-readable structured text formats (such as JSON), in addition to the still powerful and widely used options of input/output redirection and piping. In these scenarios the assistive technology user can make use of the same range of output options as anyone else who finds the CLI environment compelling.

As noted in [Appendix B. Background on Text / Command-Line / Terminal Applications and Interfaces](https://www.w3.org/TR/wcag2ict-22/#background-on-text-command-line-terminal-applications-and-interfaces), applying WCAG to text / command-line applications involves understanding how text applications are rendered, how text applications have been made accessible via assistive technologies, and how to apply the concepts of “accessibility supported” and “programmatically determined” to text applications.

The sections that follow are organized according to the principles, guidelines, and success criteria from WCAG 2. The text of each success criterion from WCAG 2 is copied as quoted text. Following that, the WCAG2ICT guidance is provided. The WCAG2ICT guidance can be found in the sections where the headings begin with "Applying..." to highlight that this is the content specific to this document. Within these sections custom notes added by WCAG2ICT are marked with the text "ADDED".

### 1\. Perceivable

> Information and user interface components must be presentable to users in ways they can perceive.

#### Applying Principle 1 Perceivable to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 1 applies directly as written.

#### 1.1 Text Alternatives

> Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language.

##### Applying Guideline 1.1 Text Alternatives to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.1 applies directly as written.

##### 1.1.1 Non-text Content

(Level A)

> All [non-text content](https://www.w3.org/TR/WCAG22/#dfn-non-text-content "any content that is not a sequence of characters that can be programmatically determined or where the sequence is not expressing something in human language") that is presented to the user has a [text alternative](https://www.w3.org/TR/WCAG22/#dfn-text-alternative "Text that is programmatically associated with non-text content or referred to from text that is programmatically associated with non-text content. Programmatically associated text is text whose location can be programmatically determined from the non-text content.") that serves the equivalent purpose, except for the situations listed below.
> 
> Controls, Input
> 
> If non-text content is a control or accepts user input, then it has a [name](https://www.w3.org/TR/WCAG22/#dfn-name "text by which software can identify a component within web content to the user") that describes its purpose. (Refer to [Success Criterion 4.1.2](https://www.w3.org/TR/WCAG22/#name-role-value) for additional requirements for controls and content that accepts user input.)
> 
> Time-Based Media
> 
> If non-text content is time-based media, then text alternatives at least provide descriptive identification of the non-text content. (Refer to [Guideline 1.2](https://www.w3.org/TR/WCAG22/#time-based-media) for additional requirements for media.)
> 
> Test
> 
> If non-text content is a test or exercise that would be invalid if presented in [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language"), then text alternatives at least provide descriptive identification of the non-text content.
> 
> Sensory
> 
> If non-text content is primarily intended to create a [specific sensory experience](https://www.w3.org/TR/WCAG22/#dfn-specific-sensory-experience "a sensory experience that is not purely decorative and does not primarily convey important information or perform a function"), then text alternatives at least provide descriptive identification of the non-text content.
> 
> [CAPTCHA](https://www.w3.org/TR/WCAG22/#dfn-captcha "initialism for "Completely Automated Public Turing test to tell Computers and Humans Apart"")
> 
> If the purpose of non-text content is to confirm that content is being accessed by a person rather than a computer, then text alternatives that identify and describe the purpose of the non-text content are provided, and alternative forms of CAPTCHA using output modes for different types of sensory perception are provided to accommodate different disabilities.
> 
> Decoration, Formatting, Invisible
> 
> If non-text content is [pure decoration](https://www.w3.org/TR/WCAG22/#dfn-pure-decoration "serving only an aesthetic purpose, providing no information, and having no functionality"), is used only for visual formatting, or is not presented to users, then it is implemented in a way that it can be ignored by [assistive technology](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents").

###### Applying SC 1.1.1 Non-text Content to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content#intent).

Note 1 (Added)

CAPTCHAs do not currently appear outside of the Web. However, if they do appear, this guidance is accurate.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

#### 1.2 Time-based Media

> Provide alternatives for time-based media.

##### Applying Guideline 1.2 Time Based Media to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.2 applies directly as written.

##### 1.2.1 Audio-only and Video-only (Prerecorded)

(Level A)

> For [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live") [audio-only](https://www.w3.org/TR/WCAG22/#dfn-audio-only "a time-based presentation that contains only audio (no video and no interaction)") and prerecorded [video-only](https://www.w3.org/TR/WCAG22/#dfn-video-only "a time-based presentation that contains only video (no audio and no interaction)") media, the following are true, except when the audio or video is a [media alternative for text](https://www.w3.org/TR/WCAG22/#dfn-media-alternative-for-text "media that presents no more information than is already presented in text (directly or via text alternatives)") and is clearly labeled as such:
> 
> Prerecorded Audio-only
> 
> An [alternative for time-based media](https://www.w3.org/TR/WCAG22/#dfn-alternative-for-time-based-media "document including correctly sequenced text descriptions of time-based visual and auditory information and providing a means for achieving the outcomes of any time-based interaction") is provided that presents equivalent information for prerecorded audio-only content.
> 
> Prerecorded Video-only
> 
> Either an alternative for time-based media or an audio track is provided that presents equivalent information for prerecorded video-only content.

###### Applying SC 1.2.1 Audio-only and Video-only (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.1](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded#intent).

Note 1 (Added)

The alternative can be provided directly in the [non-web document](https://www.w3.org/TR/wcag2ict-22/#document) or [software](https://www.w3.org/TR/wcag2ict-22/#software) – or provided in an alternate version that satisfies the success criterion.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.2.2 Captions (Prerecorded)

(Level A)

> [Captions](https://www.w3.org/TR/WCAG22/#dfn-captions "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content") are provided for all [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live") [audio](https://www.w3.org/TR/WCAG22/#dfn-audio "the technology of sound reproduction") content in [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such"), except when the media is a [media alternative for text](https://www.w3.org/TR/WCAG22/#dfn-media-alternative-for-text "media that presents no more information than is already presented in text (directly or via text alternatives)") and is clearly labeled as such.

###### Applying SC 1.2.2 Captions (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded#intent).

Note (Added)

The WCAG 2 definition of “[captions](https://www.w3.org/TR/WCAG22/#dfn-captions)” notes that “in some countries, captions are called subtitles”. They are also sometimes referred to as “subtitles for the hearing impaired". Per the definition in WCAG 2, to satisfy this success criterion, whether called captions or subtitles, they would have to provide “synchronized visual and/or [text alternative](https://www.w3.org/TR/WCAG22/#dfn-text-alternative) for both speech and non-speech audio information needed to understand the media content” where non-speech information includes “sound effects, music, laughter, speaker identification and location”.

##### 1.2.3 Audio Description or Media Alternative (Prerecorded)

(Level A)

> An [alternative for time-based media](https://www.w3.org/TR/WCAG22/#dfn-alternative-for-time-based-media "document including correctly sequenced text descriptions of time-based visual and auditory information and providing a means for achieving the outcomes of any time-based interaction") or [audio description](https://www.w3.org/TR/WCAG22/#dfn-audio-descriptions "narration added to the soundtrack to describe important visual details that cannot be understood from the main soundtrack alone") of the [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live") [video](https://www.w3.org/TR/WCAG22/#dfn-video "the technology of moving or sequenced pictures or images") content is provided for [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such"), except when the media is a [media alternative for text](https://www.w3.org/TR/WCAG22/#dfn-media-alternative-for-text "media that presents no more information than is already presented in text (directly or via text alternatives)") and is clearly labeled as such.

###### Applying SC 1.2.3 Audio Description or Media Alternative (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.3](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded#intent).

Note 1 (Added)

Audio descriptions (also called "video descriptions", "descriptive narration", and "described videos") describe important visual information needed to understand the video content, including text displayed in the video. Where the main audio track of the video fully describes important visual information, audio descriptions would not be needed at all as the requirement would already be met. When audio descriptions are needed, one way to implement them is by providing a second audio track within the synchronized media.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.2.4 Captions (Live)

(Level AA)

> [Captions](https://www.w3.org/TR/WCAG22/#dfn-captions "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content") are provided for all [live](https://www.w3.org/TR/WCAG22/#dfn-live "information captured from a real-world event and transmitted to the receiver with no more than a broadcast delay") [audio](https://www.w3.org/TR/WCAG22/#dfn-audio "the technology of sound reproduction") content in [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such").

###### Applying SC 1.2.4 Captions (Live) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.4](https://www.w3.org/WAI/WCAG22/Understanding/captions-live#intent).

Note (Added)

The WCAG 2 definition of “[captions](https://www.w3.org/TR/WCAG22/#dfn-captions)” notes that “In some countries, captions are called subtitles”. They are also sometimes referred to as “subtitles for the hearing impaired". Per the definition in WCAG 2, to satisfy this success criterion, whether called captions or subtitles, they would have to provide “synchronized visual and/or [text alternative](https://www.w3.org/TR/WCAG22/#dfn-text-alternative) for both speech and non-speech audio information needed to understand the media content” where non-speech information includes “sound effects, music, laughter, speaker identification and location”.

##### 1.2.5 Audio Description (Prerecorded)

(Level AA)

> [Audio description](https://www.w3.org/TR/WCAG22/#dfn-audio-descriptions "narration added to the soundtrack to describe important visual details that cannot be understood from the main soundtrack alone") is provided for all [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live") [video](https://www.w3.org/TR/WCAG22/#dfn-video "the technology of moving or sequenced pictures or images") content in [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such").

###### Applying SC 1.2.5 Audio Description (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.5](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded#intent).

Note (Added)

Audio descriptions (also called "video descriptions", "descriptive narration", and "described videos") describe important visual information needed to understand the video content, including text displayed in the video. Where the main audio track of the video fully describes important visual information, audio descriptions would not be needed at all as the requirement would already be met. When audio descriptions are needed, one way to implement them is by providing a second audio track within the synchronized media.

#### 1.3 Adaptable

> Create content that can be presented in different ways (for example simpler layout) without losing information or structure.

##### Applying Guideline 1.3 Adaptable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.3 applies directly as written.

##### 1.3.1 Info and Relationships

(Level A)

> Information, [structure](https://www.w3.org/TR/WCAG22/#dfn-structure "The way the parts of a web page are organized in relation to each other; and The way a collection of web pages is organized"), and [relationships](https://www.w3.org/TR/WCAG22/#dfn-relationships "meaningful associations between distinct pieces of content") conveyed through [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation "rendering of the content in a form to be perceived by users") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") or are available in text.

###### Applying SC 1.3.1 Info and Relationships to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships#intent).

Note 1 (Added) (for non-web documents)

Where non-web documents contain non-standard structure types (roles), it is best practice to map them to a standard structure type as a fall-back solution for the reader.

Note 2 (Added) (for non-web software)

In non-web software, programmatic determinability is best achieved by using the [accessibility services of platform software](https://www.w3.org/TR/wcag2ict-22/#accessibility-services-of-platform-software) to enable interoperability between the software and assistive technologies and accessibility features of software.

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.3.2 Meaningful Sequence

(Level A)

> When the sequence in which content is presented affects its meaning, a [correct reading sequence](https://www.w3.org/TR/WCAG22/#dfn-correct-reading-sequence "any sequence where words and paragraphs are presented in an order that does not change the meaning of the content") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities").

###### Applying SC 1.3.2 Meaningful Sequence to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.3.3 Sensory Characteristics

(Level A)

> Instructions provided for understanding and operating content do not rely solely on sensory characteristics of components such as shape, color, size, visual location, orientation, or sound.

###### Applying SC 1.3.3 Sensory Characteristics to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.3](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics#intent).

##### 1.3.4 Orientation

(Level AA)

> Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform").
> 
> Note
> 
> Examples where a particular display orientation may be essential are a bank check, a piano application, slides for a projector or television, or virtual reality content where content is not necessarily restricted to landscape or portrait display orientation.

###### Applying SC 1.3.4 Orientation to Non-Web Documents

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.4](https://www.w3.org/WAI/WCAG22/Understanding/orientation#intent), except for non-web documents that will never be displayed on hardware that is reoriented in typical use.

Example (Added) (for non-web documents): Examples of non-web documents that will never be displayed on hardware that is reoriented in typical use include but are not limited to:

-   a building directory that is only displayed on displays (of any type including tablets) that are all fixed to the wall in one orientation,
-   reports of results of a test that are displayed only on the screen of the testing device, and
-   the status report sent to the screen of a copy machine (but not the status report that would be sent to a web interface to the same machine).

###### Applying SC 1.3.4 Orientation to Non-Web Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.4](https://www.w3.org/WAI/WCAG22/Understanding/orientation#intent), except for non-web software that will never be displayed on hardware that is reoriented in typical use.

Note 1 (Added) (for non-web software)

Non-web software that is only used on hardware that supports a single display orientation, or where it is an application that is displayed only on hardware that is physically fixed in one orientation (e.g. a digital building directory) is excluded by the precondition and therefore does not need to provide support for orientation changes.

Example (Added) (for non-web software): Examples of non-web software that will never be displayed on hardware that is reoriented in typical use include but are not limited to:

-   software for a typical calculator that does not support screen re-orientation,
-   software menus and controls on a copier or other device that is not intended to be viewed in more than one orientation (but not any remote control software or app for the same device that runs on computers or mobile devices),
-   software on a wristwatch that is not intended to be viewed when the watch is not on the wrist, and
-   special applications such as software for displays around a building that will only be used on a known set of displays that are all permanently affixed in the same orientation.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.3.5 Identify Input Purpose

(Level AA)

> The purpose of each input field collecting information about the user can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") when:
> 
> -   The input field serves a purpose identified in the [Input Purposes for user interface components section](https://www.w3.org/TR/WCAG22/#input-purposes); and
> -   The content is implemented using technologies with support for identifying the expected meaning for form input data.

###### Applying SC 1.3.5 Identify Input Purpose to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.5](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html#intent).

Note 1 (Added)

[Non-web software](https://www.w3.org/TR/wcag2ict-22/#software) and [non-web document](https://www.w3.org/TR/wcag2ict-22/#document) technologies that do not provide attributes that support identifying the expected meaning for the form input data are not in scope for this success criterion.

Note 2 (Added)

For non-web software and non-web documents that present input fields, the terms for the input purposes would be the equivalent terms to those listed in the WCAG 2 section [Input Purposes for User Interface Components](https://www.w3.org/TR/WCAG22/#input-purposes) that are supported by the technology used.

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

#### 1.4 Distinguishable

> Make it easier for users to see and hear content including separating foreground from background.

##### Applying Guideline 1.4 Distinguishable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.4 applies directly as written.

##### 1.4.1 Use of Color

(Level A)

> Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.
> 
> Note
> 
> This success criterion addresses color perception specifically. Other forms of perception are covered in [Guideline 1.3](https://www.w3.org/TR/WCAG22/#adaptable) including programmatic access to color and other visual presentation coding.

###### Applying SC 1.4.1 Use of Color to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color#intent).

##### 1.4.2 Audio Control

(Level A)

> If any audio on a web page plays automatically for more than 3 seconds, either a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to [pause](https://www.w3.org/TR/WCAG22/#dfn-pause "stopped by user request and not resumed until requested by user") or stop the audio, or a mechanism is available to control audio volume independently from the overall system volume level.
> 
> Note
> 
> Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether or not it is used to meet other success criteria) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).

###### Applying SC 1.4.2 Audio Control to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.2](https://www.w3.org/WAI/WCAG22/Understanding/audio-control#intent), replacing “on a web page” with “in the non-web document or software”, “whole page” with “whole non-web document or software”, and “on the web page” with “in the non-web document or software”; removing “See Conformance Requirement 5: Non-Interference”; and adjusting Note 1 to avoid the use of the normative term "must".

With these substitutions, it would read:

**1.4.2 Audio Control:** If any audio <ins>[in the <strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> plays automatically for more than 3 seconds, either a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to pause or stop the audio, or a mechanism is available to control audio volume independently from the overall system volume level.

Note 1

Since any content that does not meet this success criterion can interfere with a user's ability to use the <ins>[whole non-web document or software]</ins>, <ins>[it would be necessary for]</ins> all content <ins>[in the non-web document or software]</ins> (whether or not it is used to meet other success criteria) <ins>[to]</ins> meet this success criterion.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.3 Contrast (Minimum)

(Level AA)

> The visual presentation of [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") and [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect") has a [contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio "(L1 + 0.05) / (L2 + 0.05), where") of at least 4.5:1, except for the following:
> 
> Large Text
> 
> [Large-scale](https://www.w3.org/TR/WCAG22/#dfn-large-scale "with at least 18 point or 14 point bold or font size that would yield equivalent size for Chinese, Japanese and Korean (CJK) fonts") text and images of large-scale text have a contrast ratio of at least 3:1;
> 
> Incidental
> 
> Text or images of text that are part of an inactive [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function"), that are [pure decoration](https://www.w3.org/TR/WCAG22/#dfn-pure-decoration "serving only an aesthetic purpose, providing no information, and having no functionality"), that are not visible to anyone, or that are part of a picture that contains significant other visual content, have no contrast requirement.
> 
> Logotypes
> 
> Text that is part of a logo or brand name has no contrast requirement.

###### Applying SC 1.4.3 Contrast Minimum to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.4 Resize Text

(Level AA)

> Except for [captions](https://www.w3.org/TR/WCAG22/#dfn-captions "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content") and [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect"), [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") can be resized without [assistive technology](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents") up to 200 percent without loss of content or functionality.

###### Applying SC 1.4.4 Resize Text to Non-Web Documents

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text#intent).

Note 1 (Added)

It is best practice to use only fonts that allow for scaling without loss of quality (e.g. pixelized presentation). This applies in particular to embedded fonts.

Note 2 (Added) (for non-web documents)

[Content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web) for which there are viewers or editors with a 200 percent zoom feature would automatically satisfy this success criterion when used with such viewers or editors, unless the content will not work with that zoom feature.

###### Applying SC 1.4.4 Resize Text to Non-Web Software

This success criterion is problematic to apply directly to non-web software because not all platforms provide text enlargement features that increase all displayed text to 200%. Non-web software needs to work with platform capabilities where they exist, but when the platform has text resizing support up to 200%, but not all text types scale to 200%, it is unreasonable for all apps on a particular platform to be required to build in their own text resizing. Where the platform has text resizing support up to 200%, but where not all text resizes to 200% (because some of the text is already 200% of the default body text size), and provided semantic meaning indicated through differences in text size is maintained, the non-web software should work with the text sizing features to the extent the platform provides. Doing so would still address the user needs identified in the [Intent from Understanding Success Criterion 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text#intent). The following criterion is recommended as a substitute for the WCAG language:

Except for captions and images of text, text can be resized without loss of content or functionality and without assistive technology either up to 200 percent or, if the platform provides text resizing capabilities but it does not reach 200 percent for all text, up to the text sizing capabilities of the platform.

Note 1 (Added)

It is best practice to use only fonts that allow for scaling without loss of quality (e.g. pixelized presentation). This applies in particular to embedded fonts.

Note 2 (Added) (for non-web software)

The [Intent section in Understanding 1.4.4 Resize Text](http://section/) refers to the ability to allow users to enlarge the text on screen at least up to 200% without needing to use [assistive technologies](https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies). This means that the [non-web software](https://www.w3.org/TR/wcag2ict-22/#software) provides some means for enlarging the text 200% (zoom or otherwise) without loss of [content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web) or functionality, or that the non-web software works with the platform features to satisfy this success criterion.

Note 3 (Added) (for non-web software)

For non-web software, sometimes the platform provides text scaling to 200% for most, but not all text (e.g. headings, which are naturally large, may not be increased in size to 200%, but other text does increase to 200%). In such cases, authors would only need to support text scaling to the extent provided by user settings in the platform, without losing text-size semantics, content or functionality, to satisfy this success criterion.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.5 Images of Text

(Level AA)

> If the technologies being used can achieve the visual presentation, [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") is used to convey information rather than [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect") except for the following:
> 
> Customizable
> 
> The image of text can be [visually customized](https://www.w3.org/TR/WCAG22/#dfn-visually-customized "the font, size, color, and background can be set") to the user's requirements;
> 
> Essential
> 
> A particular presentation of text is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") to the information being conveyed.
> 
> Note
> 
> Logotypes (text that is part of a logo or brand name) are considered essential.

###### Applying SC 1.4.5 Images of Text to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.5](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.10 Reflow

(Level AA)

> Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
> 
> -   Vertical scrolling content at a width equivalent to 320 [CSS pixels](https://www.w3.org/TR/WCAG22/#dfn-css-pixels "visual angle of about 0.0213 degrees");
> -   Horizontal scrolling content at a height equivalent to 256 [CSS pixels](https://www.w3.org/TR/WCAG22/#dfn-css-pixels "visual angle of about 0.0213 degrees").
> 
> Except for parts of the content which require two-dimensional layout for usage or meaning.
> 
> Note 1
> 
> 320 CSS pixels is equivalent to a starting [viewport](https://www.w3.org/TR/WCAG22/#dfn-viewport "object in which the user agent presents content") width of 1280 CSS pixels wide at 400% zoom. For web content which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.
> 
> Note 2
> 
> Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

###### Applying SC 1.4.10 Reflow to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html#intent), replacing “web content” with “content”.

With this substitution, it would read:

**1.4.10 Reflow:** Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:

-   Vertical scrolling content at a width equivalent to 320 [CSS pixels](https://www.w3.org/TR/wcag2ict-22/#dfn-css-pixels);
-   Horizontal scrolling content at a height equivalent to 256 [CSS pixels](https://www.w3.org/TR/wcag2ict-22/#dfn-css-pixels).

Except for parts of the content which require two-dimensional layout for usage or meaning.

Note 1

320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom. For <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web">content</a></strong>]</ins> which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.

Note 2

Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

Note 3 (Added)

In technologies where CSS is not used, the definition of 'CSS pixel' applies as described in [Applying “CSS pixel” to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-css-pixel-to-non-web-documents-and-software).

Note 4 (Added) (for non-web documents)

If a [non-web document](https://www.w3.org/TR/wcag2ict-22/#document) type and its available [user agents](https://www.w3.org/TR/wcag2ict-22/#user-agent) do not support reflow, it may not be possible for a document of that type to satisfy this success criterion.

Note 5 (Added) (for non-web software)

The intent section refers to the ability for content to reflow (for vertical scrolling content at a width equivalent to 320 CSS pixels, or for horizontal scrolling content at a height equivalent to 256 CSS pixels) when user agent zooming is used to scale content or when the [viewport](https://www.w3.org/TR/wcag2ict-22/#dfn-viewport) changes in width. For [non-web software](https://www.w3.org/TR/wcag2ict-22/#software), this means that when users scale content, adjust the size of a window, dialog, or other resizable content area, or change the screen resolution, the content will reflow without loss of information or functionality, and without requiring scrolling in two dimensions; or that the non-web software works with platform features that satisfy this success criterion.

Note 6 (Added) (for non-web software)

Non-web software will have more frequent cases where two-dimensional layout is relied upon for usage or meaning than what occurs on the Web. For example:

-   When the non-web software has a complex user interface with toolbars that need to be visible while manipulating content, as explained in the Intent from Understanding 1.4.10 Reflow.

Note 7 (Added) (for non-web software)

As written, this success criterion can only be met by non-web software where the underlying user agent or platform software can present content at a width equivalent to 320 CSS pixels for vertical scrolling content and a height equivalent to 256 CSS pixels for horizontal scrolling content.

When the underlying user agent or platform software does not support these dimensions for scrolling, reflow is encouraged as this capability is important to people with low vision. As a reasonable benchmark, evaluate at the nearest size to what the Reflow success criterion specifies.

When users modify zoom, scaling, and/or display resolution at the platform software level (e.g. Operating System), it impacts the size of all applications and the [platform software](https://www.w3.org/TR/wcag2ict-22/#platform-software) itself. This can result in improved readability in some applications but unwanted consequences in others.

Note 8 (Added) (for non-web software)

Some non-web software applications provide a mode of operation where reflow is possible, while other modes are unable to reflow. An example is a document authoring tool, which includes both a "print preview mode" (without reflow, for users to view the spatial formatting) and a "drafting view mode" where reflow is supported. Such software would satisfy this success criterion as long as there is no loss of information or functionality in the drafting view.

Note 9 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.11 Non-text Contrast

(Level AA)

> The visual [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation "rendering of the content in a form to be perceived by users") of the following have a [contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio "(L1 + 0.05) / (L2 + 0.05), where") of at least 3:1 against adjacent color(s):
> 
> User Interface Components
> 
> Visual information required to identify [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") and [states](https://www.w3.org/TR/WCAG22/#dfn-states "dynamic property expressing characteristics of a user interface component that may change in response to user action or automated processes"), except for inactive components or where the appearance of the component is determined by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and not modified by the author;
> 
> Graphical Objects
> 
> Parts of graphics required to understand the content, except when a particular presentation of graphics is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") to the information being conveyed.

###### Applying SC 1.4.11 Non-text Contrast to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html#intent), replacing "user agent" with "user agent or other platform software".

With this substitution, it would read:

**1.4.11 Non-text Contrast:** The visual [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation) of the following have a [contrast ratio](https://www.w3.org/TR/wcag2ict-22/#dfn-contrast-ratio) of at least 3:1 against adjacent color(s):

User Interface Components

Visual information required to identify [user interface components](https://www.w3.org/TR/wcag2ict-22/#dfn-user-interface-components) and [states](https://www.w3.org/TR/WCAG22/#dfn-states), except for inactive components or where the appearance of the component is determined by the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#user-agent">user agent</a></strong> or other <strong><a href="https://www.w3.org/TR/wcag2ict-22/#platform-software">platform software</a></strong>]</ins> and not modified by the author;

Graphical Objects

Parts of graphics required to understand the content, except when a particular presentation of graphics is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential) to the information being conveyed.

Note 1 (Added)

An example of appearance modification by the author is content that sets the visual style of a control, such as a color or border, to differ from the default style for the user agent or platform.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.12 Text Spacing

(Level AA)

> In content implemented using markup languages that support the following [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") [style properties](https://www.w3.org/TR/WCAG22/#dfn-style-properties "property whose value determines the presentation (e.g. font, color, size, location, padding, volume, synthesized speech prosody) of content elements as they are rendered (e.g. onscreen, via loudspeaker, via braille display) by user agents"), no loss of content or functionality occurs by setting all of the following and by changing no other style property:
> 
> -   Line height (line spacing) to at least 1.5 times the font size;
> -   Spacing following paragraphs to at least 2 times the font size;
> -   Letter spacing (tracking) to at least 0.12 times the font size;
> -   Word spacing to at least 0.16 times the font size.
> 
> Exception: [Human languages](https://www.w3.org/TR/WCAG22/#dfn-human-language-s "language that is spoken, written or signed (through visual or tactile means) to communicate with humans") and scripts that do not make use of one or more of these text style properties in written text can conform using only the properties that exist for that combination of language and script.
> 
> Note 1
> 
> Content is not required to use these text spacing values. The requirement is to ensure that when a user overrides the authored text spacing, content or functionality is not lost.
> 
> Note 2
> 
> Writing systems for some languages use different text spacing settings, such as paragraph start indent. Authors are encouraged to follow locally available guidance for improving readability and legibility of text in their writing system.

###### Applying SC 1.4.12 Text Spacing to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html#intent).

Note 1 (Added)

This success criterion only applies to [non-web documents](https://www.w3.org/TR/wcag2ict-22/#document) and [software](https://www.w3.org/TR/wcag2ict-22/#software) that are implemented using markup languages and allow the user to modify these text spacing properties.

Note 2 (Added) (for non-web documents)

There are several mechanisms that allow users to modify a document's text spacing properties of content implemented in markup languages. For example, an eBook technology may have an available user agent that allows users to override document text styles. When such a mechanism is available, the success criterion requires that the content responds appropriately to it.

Note 3 (Added) (for non-web software)

There are several mechanisms that allow users to modify software's text spacing properties of content implemented in markup languages. For example, a software application may provide a "user style sheet" facility to modify the appearance of the software's own user interface. This success criterion does not mean that non-web software needs to implement their own mechanisms to allow users to set text spacing; however, when such a mechanism is available, the success criterion requires that the content responds appropriately to it.

Note 4 (Added) (for non-web software)

"Content implemented using markup languages" includes parts of software that use markup internally to define a user interface. Examples of markup languages that are used internally to define a software user interface include but are not limited to: HTML (e.g., in [Electron](https://www.electronjs.org/) applications or iOS application web views), XAML, XML (e.g., in Android application layouts), and XUL.

Note 5 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 1.4.13 Content on Hover or Focus

(Level AA)

> Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:
> 
> Dismissible
> 
> A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an [input error](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") or does not obscure or replace other content;
> 
> Hoverable
> 
> If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;
> 
> Persistent
> 
> The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.
> 
> Exception: The visual presentation of the additional content is controlled by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and is not modified by the author.
> 
> Note 1
> 
> Examples of additional content controlled by the user agent include browser tooltips created through use of the HTML [`title` attribute](https://html.spec.whatwg.org/multipage/dom.html#the-title-attribute) \[[HTML](https://www.w3.org/TR/WCAG22/#bib-html "HTML Standard")\].
> 
> Note 2
> 
> Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.
> 
> Note 3
> 
> This criterion applies to content that appears in addition to the triggering component itself. Since hidden components that are made visible on keyboard focus (such as links used to skip to another part of a page) do not present additional content they are not covered by this criterion.

###### Applying SC 1.4.13 Content on Hover or Focus to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html), replacing "user agent" with "user agent or other platform software", "browser tooltips" with "tooltips", "the HTML title attribute" with "user interface object attributes", "links" with "links or other UI controls that behave like a link", and "a page" with "the non-web document or software".

With these substitutions, it would read:

**1.4.13 Content on Hover or Focus:** Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:

Dismissible

A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an [input error](https://www.w3.org/TR/wcag2ict-22/#dfn-input-error) or does not obscure or replace other content;

Hoverable

If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;

Persistent

The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.

Exception: The visual presentation of the additional content is controlled by the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#user-agent">user agent</a></strong> or other <strong><a href="https://www.w3.org/TR/wcag2ict-22/#platform-software">platform software</a></strong>]</ins> and is not modified by the author.

Note 1

Examples of additional content controlled by the <ins>[user agent or other platform software]</ins> include <ins>[tooltips]</ins> created through use of <ins>[user interface object attributes]</ins>.

Note 2

Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.

Note 3

This criterion applies to content that appears in addition to the triggering component itself. Since hidden components that are made visible on keyboard focus (such as <ins>[links or other UI controls that behave like a link]</ins> used to skip to another part of <ins>[the non-web document or software]</ins>) do not present additional content they are not covered by this criterion.

### 2\. Operable

> User interface components and navigation must be operable.

#### Applying Principle 2 Operable to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 2 applies directly as written.

#### 2.1 Keyboard Accessible

> Make all functionality available from a keyboard.

##### Applying Guideline 2.1 Keyboard Accessible to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.1 applies directly as written.

##### 2.1.1 Keyboard

(Level A)

> All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") of the content is operable through a [keyboard interface](https://www.w3.org/TR/WCAG22/#dfn-keyboard-interface "interface used by software to obtain keystroke input") without requiring specific timings for individual keystrokes, except where the underlying function requires input that depends on the path of the user's movement and not just the endpoints.
> 
> Note 1
> 
> This exception relates to the underlying function, not the input technique. For example, if using handwriting to enter text, the input technique (handwriting) requires path-dependent input but the underlying function (text input) does not.
> 
> Note 2
> 
> This does not forbid and should not discourage providing mouse input or other input methods in addition to keyboard operation.

###### Applying SC 2.1.1 Keyboard to Non-Web Documents

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard#intent).

###### Applying SC 2.1.1 Keyboard to Non-Web Software

Where ICT is or includes non-web software that can be run on a software platform that provides a device-independent keyboard interface service, this applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard#intent).

Note 1 (Added) (for non-web software)

Keyboard interface does not refer to a physical device but to the service of [platform software](https://www.w3.org/TR/wcag2ict-22/#platform-software) (e.g. operating system, browser, etc.) that provides the software with keystrokes from any keyboard or keyboard substitute. When the [non-web software](https://www.w3.org/TR/wcag2ict-22/#software) supports such a device-independent service of the platform software, and the non-web software functionality is made fully operable through the service, then this success criterion would be satisfied.

Note 2 (Added) (for non-web software)

A "device-independent keyboard interface service" refers to the platform service that provides keystrokes to any software running on the platform.

Note 3 (Added) (for non-web software)

Inclusion of an on-screen keyboard can be done as well but does not satisfy this requirement since it does not allow for the use of keyboard alternatives whereas support of input from the device-independent keyboard interface service does.

Note 4 (Added) (for non-web software)

This success criterion does not imply that non-web software always needs to directly support a keyboard or “keyboard interface” if one is not provided by the platform software. But if one is provided, the software needs to make all functionality available through it - unless the exception applies.

Note 5 (Added) (for non-web software)

This success criterion also does not imply that non-web software always needs to provide its own [virtual keyboard](https://www.w3.org/TR/wcag2ict-22/#virtual-keyboard). But if it does, then the non-web software still needs to support keyboard input from any keyboard interface provided by the platform software.

Note 6 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.1.2 No Keyboard Trap

(Level A)

> If keyboard focus can be moved to a component of the page using a [keyboard interface](https://www.w3.org/TR/WCAG22/#dfn-keyboard-interface "interface used by software to obtain keystroke input"), then focus can be moved away from that component using only a keyboard interface, and, if it requires more than unmodified arrow or tab keys or other standard exit methods, the user is advised of the method for moving focus away.
> 
> Note
> 
> Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether it is used to meet other success criteria or not) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).

###### Applying SC 2.1.2 No Keyboard Trap to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.2](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap#intent), replacing “page” with “non-web document or software” and “on the web page” with "in the non-web document or software"; removing “See Conformance Requirement 5: Non-Interference”; and adjusting Note 1 to avoid the use of the normative term "must".

With these substitutions, it would read:

**2.1.2 No Keyboard Trap:** If keyboard focus can be moved to a component of the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> using a [keyboard interface](https://www.w3.org/TR/wcag2ict-22/#dfn-keyboard-interface), then focus can be moved away from that component using only a keyboard interface, and, if it requires more than unmodified arrow or tab keys or other standard exit methods, the user is advised of the method for moving focus away.

Note 1

Since any content that does not meet this success criterion can interfere with a user's ability to use the whole <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins>, <ins>[it would be necessary for]</ins> all content <ins>[in the non-web document or software]</ins> (whether it is used to meet other success criteria or not) <ins>[to]</ins> meet this success criterion.

Note 2 (Added)

Standard exit methods may vary by platform. For example, on many desktop platforms, the Escape key is a standard method for exiting.

Note 3 (Added) (for non-web software)

This criterion applies when focus can be moved using a keyboard interface. Some software may accept input from a keyboard, keypad, or controller, yet not offer any mechanism for focus; for example, the keys are mapped directly to functions without moving focus between on-screen controls. In this case, there is no concept of focus, and therefore keyboard traps cannot exist and this success criterion would be satisfied.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.1.4 Character Key Shortcuts

(Level A)

> If a [keyboard shortcut](https://www.w3.org/TR/WCAG22/#dfn-keyboard-shortcuts "alternative means of triggering an action by the pressing of one or more keys") is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:
> 
> Turn off
> 
> A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to turn the shortcut off;
> 
> Remap
> 
> A mechanism is available to remap the shortcut to include one or more non-printable keyboard keys (e.g., Ctrl, Alt);
> 
> Active only on focus
> 
> The keyboard shortcut for a [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") is only active when that component has focus.

###### Applying SC 2.1.4 Character Key Shortcuts to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.4](https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html).

Note 1 (Added) (for non-web software)

The WCAG2ICT interpretation is that a long press of a key (2 seconds or more) and other accessibility features provided by the platform do not meet the WCAG definition of a keyboard shortcut. See the [keyboard shortcut](https://www.w3.org/TR/wcag2ict-22/#dfn-keyboard-shortcuts) definition for more details.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

#### 2.2 Enough Time

> Provide users enough time to read and use content.

##### Applying Guideline 2.2 Enough Time to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.2 applies directly as written.

##### 2.2.1 Timing Adjustable

(Level A)

> For each time limit that is set by the content, at least one of the following is true:
> 
> Turn off
> 
> The user is allowed to turn off the time limit before encountering it; or
> 
> Adjust
> 
> The user is allowed to adjust the time limit before encountering it over a wide range that is at least ten times the length of the default setting; or
> 
> Extend
> 
> The user is warned before time expires and given at least 20 seconds to extend the time limit with a simple action (for example, "press the space bar"), and the user is allowed to extend the time limit at least ten times; or
> 
> Real-time Exception
> 
> The time limit is a required part of a [real-time event](https://www.w3.org/TR/WCAG22/#dfn-real-time-events "event that a) occurs at the same time as the viewing and b) is not completely generated by the content") (for example, an auction), and no alternative to the time limit is possible; or
> 
> Essential Exception
> 
> The time limit is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") and extending it would invalidate the activity; or
> 
> 20 Hour Exception
> 
> The time limit is longer than 20 hours.
> 
> Note
> 
> This success criterion helps ensure that users can complete tasks without unexpected changes in content or context that are a result of a time limit. This success criterion should be considered in conjunction with [Success Criterion 3.2.1](https://www.w3.org/TR/WCAG22/#on-focus), which puts limits on changes of content or context as a result of user action.

###### Applying SC 2.2.1 Timing Adjustable to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable#intent), replacing “ content” with “non-web document or software”.

With this substitution, it would read:

**2.2.1 Timing Adjustable:** For each time limit that is set by the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins>, at least one of the following is true:

Turn off

The user is allowed to turn off the time limit before encountering it; or

Adjust

The user is allowed to adjust the time limit before encountering it over a wide range that is at least ten times the length of the default setting; or

Extend

The user is warned before time expires and given at least 20 seconds to extend the time limit with a simple action (for example, “press the space bar”), and the user is allowed to extend the time limit at least ten times; or

Real-time Exception

The time limit is a required part of a real-time event (for example, an auction), and no alternative to the time limit is possible; or

Essential Exception

The time limit is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential) and extending it would invalidate the activity; or

20 Hour Exception

The time limit is longer than 20 hours.

Note

This success criterion helps ensure that users can complete tasks without unexpected changes in content or context that are a result of a time limit. This success criterion should be considered in conjunction with [Success Criterion 3.2.1](https://www.w3.org/TR/WCAG22/#on-focus), which puts limits on changes of content or context as a result of user action.

##### 2.2.2 Pause, Stop, Hide

(Level A)

> For moving, [blinking](https://www.w3.org/TR/WCAG22/#dfn-blinking "switch back and forth between two visual states in a way that is meant to draw attention"), scrolling, or auto-updating information, all of the following are true:
> 
> Moving, blinking, scrolling
> 
> For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") for the user to [pause](https://www.w3.org/TR/WCAG22/#dfn-pause "stopped by user request and not resumed until requested by user"), stop, or hide it unless the movement, blinking, or scrolling is part of an activity where it is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform"); and
> 
> Auto-updating
> 
> For any auto-updating information that (1) starts automatically and (2) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it or to control the frequency of the update unless the auto-updating is part of an activity where it is essential.
> 
> Note 1
> 
> For requirements related to flickering or flashing content, refer to [Guideline 2.3](https://www.w3.org/TR/WCAG22/#seizures-and-physical-reactions).
> 
> Note 2
> 
> Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether it is used to meet other success criteria or not) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).
> 
> Note 3
> 
> Content that is updated periodically by software or that is streamed to the user agent is not required to preserve or present information that is generated or received between the initiation of the pause and resuming presentation, as this may not be technically possible, and in many situations could be misleading to do so.
> 
> Note 4
> 
> An animation that occurs as part of a preload phase or similar situation can be considered essential if interaction cannot occur during that phase for all users and if not indicating progress could confuse users or cause them to think that content was frozen or broken.

###### Applying SC 2.2.2 Pause, Stop, Hide to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide#intent), replacing “page” with “non-web document or software” and “on the web page” with “in the non-web document or software”; removing “See Conformance Requirement 5: Non-Interference” in Note 2 of the success criterion; and adjusting Note 2 to avoid the use of the normative term "must".

With these substitutions, it would read:

**2.2.2 Pause, Stop, Hide:** For moving, [blinking](https://www.w3.org/TR/WCAG22/#dfn-blinking), scrolling, or auto-updating information, all of the following are true:

Moving, blinking, scrolling

For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a mechanism for the user to [pause](https://www.w3.org/TR/WCAG22/#dfn-pause)), stop, or hide it unless the movement, blinking, or scrolling is part of an activity where it is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential); and

Auto-updating

For any auto-updating information that (1) starts automatically and (2) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it or to control the frequency of the update unless the auto-updating is part of an activity where it is essential.

Note 1

For requirements related to flickering or flashing content, refer to [Guideline 2.3](https://www.w3.org/TR/WCAG22/#seizures-and-physical-reactions).

Note 2

Since any content that does not meet this success criterion can interfere with a user's ability to use the whole <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins>, <ins>[it would be necessary for]</ins> all content <ins>[in the non-web document or software]</ins> (whether it is used to meet other success criteria or not) <ins>[to]</ins> meet this success criterion.

Note 3

Content that is updated periodically by software or that is streamed to the user agent is not required to preserve or present information that is generated or received between the initiation of the pause and resuming presentation, as this may not be technically possible, and in many situations could be misleading to do so.

Note 4

An animation that occurs as part of a preload phase or similar situation can be considered essential if interaction cannot occur during that phase for all users and if not indicating progress could confuse users or cause them to think that content was frozen or broken.

Note 5 (Added)

While the success criterion uses the term “information”, the WCAG 2 [Intent from Understanding Success Criterion 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide#intent) makes it clear that this is to be applied to all content. Any [content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web), even if just decorative, that is updated automatically, blinks, or moves may create an accessibility barrier.

#### 2.3 Seizures and Physical Reactions

> Do not design content in a way that is known to cause seizures or physical reactions.

##### Applying Guideline 2.3 Seizures and Physical Reactions to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.3 applies directly as written.

##### 2.3.1 Three Flashes or Below Threshold

(Level A)

> [Web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") do not contain anything that flashes more than three times in any one second period, or the [flash](https://www.w3.org/TR/WCAG22/#dfn-flashes "a pair of opposing changes in relative luminance that can cause seizures in some people if it is large enough and in the right frequency range") is below the [general flash and red flash thresholds](https://www.w3.org/TR/WCAG22/#dfn-general-flash-and-red-flash-thresholds "a flash or rapidly changing image sequence is below the threshold (i.e., content passes) if any of the following are true:").
> 
> Note
> 
> Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether it is used to meet other success criteria or not) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).

###### Applying SC 2.3.1 Three Flashes or Below Threshold to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold#intent), replacing “web pages” with “non-web documents or software” , “page” with “non-web document or software”, and “on the web page” with “in the non-web document or software”; removing “See Conformance Requirement 5: Non-Interference”; and adjusting Note 1 to avoid the use of the normative term "must".

With these substitutions, it would read:

**2.3.1 Three Flashes or Below Threshold:** <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">Non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> do not contain anything that flashes more than three times in any one second period, or the [flash](https://www.w3.org/TR/WCAG22/#dfn-flashes) is below the [general flash and red flash thresholds](https://www.w3.org/TR/wcag2ict-22/#dfn-general-flash-and-red-flash-thresholds).

Note 1

Since any content that does not meet this success criterion can interfere with a user's ability to use the whole <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins>, <ins>[it would be necessary for]</ins> all content <ins>[in the non-web document or software]</ins> (whether it is used to meet other success criteria or not) <ins>[to]</ins> meet this success criterion.

Note 2 (Added) (for non-web software)

This requirement applies to flashing of content on a screen and flashing of any other type caused by the ICT.

Note 3 (Added) (for non-web software)

This requirement applies to those visual elements produced by the ICT itself. Content from an external source that is presented through the ICT, is the responsibility of the source. The requirement does not require the ICT to examine or modify such externally supplied content in any way.

Example (Added) (for non-web software): Examples of ICT that presents content from an external source include TVs playing broadcast programs and media players that are playing content provided by the user.

#### 2.4 Navigable

> Provide ways to help users navigate, find content, and determine where they are.

##### Applying Guideline 2.4 Navigable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.4 applies directly as written.

##### 2.4.1 Bypass Blocks

(Level A)

> A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to bypass blocks of content that are repeated on multiple [web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent").

###### Applying SC 2.4.1 Bypass Blocks to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 2.4.1](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks#intent), replacing “on multiple web pages” with “in multiple non-web documents in a set of non-web documents, or in multiple software programs in a set of software programs” to explicitly state that the multiple documents (or software programs) are part of a set rather than any two documents or pieces of software.

With these substitutions, this success criterion would read:

**2.4.1 Bypass Blocks:** A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to bypass blocks of content that are repeated <ins>[in multiple <strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> in a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-documents">set of non-web documents</a></strong>, or in multiple <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software programs</a></strong> in a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs">set of software programs</a></strong>]</ins>.

Note 1 (Added)

See [set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents) and [set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](https://www.w3.org/TR/wcag2ict-22/#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

Individual documents or software programs (not in a set) would automatically satisfy this success criterion because this success criterion applies only to things that appear in a set.

Note 3 (Added)

Although not required by the success criterion, being able to bypass blocks of content that are repeated _within_ non-web documents or software directly addresses user needs identified in the Intent section for this success criterion, and is generally considered best practice.

Note 4 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 5 (Added) (for non-web software)

Many software user interface components have built-in mechanisms to navigate directly to / among them, which also have the effect of skipping over or bypassing blocks of content.

Note 6 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.4.2 Page Titled

(Level A)

> [Web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") have titles that describe topic or purpose.

###### Applying SC 2.4.2 Page Titled to Non-Web Documents

This success criterion is problematic to apply directly to non-web documents through simple word substitution because not all document formats provide support for a programmatically determinable Title property, and document titles don't always describe the topic or purpose of the document. File names, as the WCAG 2 Understanding document specifies, also rarely describe the topic or purpose of the document – especially where the document names are not under the author’s control. However, where the document authoring tool or technology provides the capability to supply a title or name for a document, when the non-web document utilizes the Title property to provide a unique title or name inside of each document, and/or when a meaningful file name can be supplied, the user can more easily find it or understand its purpose. This would address the user needs identified in the [Intent from Understanding Success Criterion 2.4.2](https://www.w3.org/WAI/WCAG22/Understanding/page-titled#intent). The following criterion is recommended as a substitute for the WCAG language:

**2.4.2 Non-web Document Titled:** In non-web documents implemented in a format that supports a programmatically determinable Title property that is editable using common authoring tools for that document format, the non-web document has a title that describes the name, topic, or purpose.

Note (Added) (for non-web documents)

The Title property is specified as "editable through that document format’s common authoring tools" so that authors can view and edit the Title without requiring specialized or external metadata utilities. “Common authoring tools" are the most readily available tools used for editing a particular document type.

###### Applying SC 2.4.2 Page Titled to Non-Web Software

This success criterion is problematic to apply directly to non-web software through simple word substitution because application titles rarely describe the topic or purpose of the software. However, where the platform supports a programmatic title or name for a software window or screen, when a software application utilizes that feature to provide a unique title or name for each window or screen, the user can more easily find it or understand its purpose. This would address the user needs identified in the [Intent from Understanding Success Criterion 2.4.2](https://www.w3.org/WAI/WCAG22/Understanding/page-titled#intent). The following criterion is recommended as a substitute for the WCAG language:

**2.4.2 Non-web Software Titled:** In non-web software implemented on a platform that supports a Title property for windows or screens, the non-web software provides titles that describe the name, topic or purpose of each window or screen.

##### 2.4.3 Focus Order

(Level A)

> If a [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") can be [navigated sequentially](https://www.w3.org/TR/WCAG22/#dfn-navigated-sequentially "navigated in the order defined for advancing focus (from one element to the next) using a keyboard interface") and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability.

###### Applying SC 2.4.3 Focus Order to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.3](https://www.w3.org/WAI/WCAG22/Understanding/focus-order#intent) replacing “a web page” with “non-web documents or software”.

With this substitution, it would read:

**2.4.3 Focus Order:** If <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> can be [navigated sequentially](https://www.w3.org/TR/WCAG22/#dfn-navigated-sequentially) and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability.

##### 2.4.4 Link Purpose (In Context)

(Level A)

> The [purpose of each link](https://www.w3.org/TR/WCAG22/#dfn-purpose-of-each-link "nature of the result obtained by activating a hyperlink") can be determined from the link text alone or from the link text together with its [programmatically determined link context](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determined-link-context "additional information that can be programmatically determined from relationships with a link, combined with the link text, and presented to users in different modalities"), except where the purpose of the link would be [ambiguous to users in general](https://www.w3.org/TR/WCAG22/#dfn-ambiguous-to-users-in-general "the purpose cannot be determined from the link and all information of the web page presented to the user simultaneously with the link (i.e., readers without disabilities would not know what a link would do until they activated it)").

###### Applying SC 2.4.4 Link Purpose (In Context) to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context#intent).

Note 1 (Added)

In non-web documents or software, a “link” is any user interface control that behaves like a hypertext link.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.4.5 Multiple Ways

(Level AA)

> More than one way is available to locate a [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization") except where the web page is the result of, or a step in, a [process](https://www.w3.org/TR/WCAG22/#dfn-processes "series of user actions where each action is required in order to complete an activity").

###### Applying SC 2.4.5 Multiple Ways to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 2.4.5](https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways#intent), replacing “web page within a set of web pages” with “non-web document within a set of non-web documents, or a set of software programs within a set of software programs” and "the web page" with "the non-web document or software program".

With these substitutions, this success criterion would read:

**2.4.5 Multiple Ways:** More than one way is available to locate a <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> within a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-documents">set of non-web documents</a></strong>, or a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software program</a></strong> within a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs">set of software programs</a></strong>]</ins> except where <ins>[the non-web document or software program]</ins> is the result of, or a step in, a [process](https://www.w3.org/TR/WCAG22/#dfn-processes).

Note 1 (Added)

See [set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents) and [set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](https://www.w3.org/TR/wcag2ict-22/#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

The definitions of “[set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents)” and “[set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs)” in the Key Terms section are predicated on the ability to navigate from each element of the set to each other, and navigation is a type of locating. So the mechanism used to navigate between elements of the set will be one way of locating information in the set. Non-web environments, generally major operating systems with browse and search capabilities, often provide infrastructure and tools that provide mechanisms for locating content in a set of non-web documents or a set of software programs. For example, it may be possible to browse through the files or programs that make up a set, or search within members of the set for the names of other members. A file directory would be the equivalent of a site map for documents in a set, and a search function in a file system would be equivalent to a web search function for web pages. Such facilities may provide additional ways of locating information in the set.

Note 3 (Added)

While some users may find it useful to have multiple ways to locate some groups of user interface elements within a non-web document or software program, this is not required by the success criterion (and may pose difficulties in some situations).

Note 4 (Added)

The definitions of “[set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents)” and “[set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs)” in WCAG2ICT require every item in the set to be independently reachable, and so nothing in such a set can be a “step in a process” that can't be reached any other way. The purpose of the exception—that items in a process are exempt from satisfying this success criterion—is achieved by the definition of set.

Note 5 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 6 (Added) (for non-web software)

An example of the use of “a software program that is part of process”, that would meet the exception for this success criterion, would be one where programs are interlinked but the interlinking depends on program A being used before program B, for validation or to initialize the dataset, etc.

Note 7 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.4.6 Headings and Labels

(Level AA)

> Headings and [labels](https://www.w3.org/TR/WCAG22/#dfn-labels "text or other component with a text alternative that is presented to a user to identify a component within web content") describe topic or purpose.

###### Applying SC 2.4.6 Headings and Labels to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.6](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels#intent).

Note (Added) (for non-web software)

In non-web [software](https://www.w3.org/TR/wcag2ict-22/#software), headings and labels are used to describe sections of [content](https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web) and controls respectively. In some cases it may be unclear whether a piece of static text is a heading or a label. But whether treated as a label or a heading, the requirement is the same: that if they are present they describe the topic or purpose of the item(s) they are associated with.

##### 2.4.7 Focus Visible

(Level AA)

> Any keyboard operable user interface has a mode of operation where the keyboard [focus indicator](https://www.w3.org/TR/WCAG22/#dfn-focus-indicator "New") is visible.

###### Applying SC 2.4.7 Focus Visible to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.4.11 Focus Not Obscured (Minimum)

(Level AA)

> When a [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") receives keyboard focus, the component is not entirely hidden due to author-created content.
> 
> Note 1
> 
> Where content in a configurable interface can be repositioned by the user, then only the initial positions of user-movable content are considered for testing and conformance of this success criterion.
> 
> Note 2
> 
> Content opened by the _user_ may obscure the component receiving focus. If the user can reveal the focused component without advancing the keyboard focus, the component with focus is not considered visually hidden due to author-created content.

###### Applying SC 2.4.11 Focus not Obscured to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum#intent).

#### 2.5 Input Modalities

> Make it easier for users to operate functionality through various inputs beyond keyboard.

##### Applying Guideline 2.5 Input Modalities to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.5 applies directly as written.

##### 2.5.1 Pointer Gestures

(Level A)

> All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that uses multipoint or path-based gestures for operation can be operated with a [single pointer](https://www.w3.org/TR/WCAG22/#dfn-single-pointer "an input modality that only targets a single point on the page/screen at a time – such as a mouse, single finger on a touch screen, or stylus.") without a path-based gesture, unless a multipoint or path-based gesture is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform").
> 
> Note
> 
> This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

###### Applying SC 2.5.1 Pointer Gestures to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.1](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures#intent), making changes to the notes for non-web documents by replacing “web content” with "content", for non-web software by replacing "web content that interprets" with "non-web software that interprets" and "user agent" with "underlying platform software".

With these substitutions, the notes would read:

Note 1 (for non-web documents)

This requirement applies to <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web">content</a></strong>]</ins> that interprets pointer actions (i.e., this does not apply to actions that are required to operate the [user agent](https://www.w3.org/TR/wcag2ict-22/#user-agent) or [assistive technology](https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies)).

Note 2 (Added) (for non-web documents)

Multipoint and path-based gestures are less common in non-web documents. An example where a non-web document author could add such gestures is an interactive prototype document created in a software design tool.

Note 3 (for non-web software)

This requirement applies to <ins>[non-web <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong> that interprets]</ins> pointer actions (i.e., this does not apply to actions that are required to operate the <ins>[underlying <strong><a href="https://www.w3.org/TR/wcag2ict-22/#platform-software">platform software</a></strong>]</ins> or assistive technology).

Note 4 (Added) (for non-web software)

This requirement also applies to platform software, such as user agents, assistive technology software, and operating systems. Each layer is responsible for its own pointer actions only, not for those in an underlying layer.

##### 2.5.2 Pointer Cancellation

(Level A)

> For [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that can be operated using a [single pointer](https://www.w3.org/TR/WCAG22/#dfn-single-pointer "an input modality that only targets a single point on the page/screen at a time – such as a mouse, single finger on a touch screen, or stylus."), at least one of the following is true:
> 
> No Down-Event
> 
> The [down-event](https://www.w3.org/TR/WCAG22/#dfn-down-event "platform event that occurs when the trigger stimulus of a pointer is depressed") of the pointer is not used to execute any part of the function;
> 
> Abort or Undo
> 
> Completion of the function is on the [up-event](https://www.w3.org/TR/WCAG22/#dfn-up-event "platform event that occurs when the trigger stimulus of a pointer is released"), and a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to abort the function before completion or to undo the function after completion;
> 
> Up Reversal
> 
> The up-event reverses any outcome of the preceding down-event;
> 
> Essential
> 
> Completing the function on the down-event is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform").
> 
> Note 1
> 
> Functions that emulate a keyboard or numeric keypad key press are considered essential.
> 
> Note 2
> 
> This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

###### Applying SC 2.5.2 Pointer Cancellation to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.2](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html#intent), making changes to the notes for non-web documents by replacing “web content” with "content", for non-web software by replacing "web content that interprets" with "non-web software that interprets" and "user agent" with "underlying platform software".

With these substitutions, the notes would read:

Note 1 (for non-web documents)

Functions that emulate a keyboard or numeric keypad key press are considered essential.

Note 2 (for non-web documents)

This requirement applies to <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web">content</a></strong>]</ins> that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

Note 3 (Added) (for non-web documents)

Content that interprets pointer actions and controls which events are used for executing functionality is less common in non-web documents. An example where a non-web document author could add such functionality is an interactive prototype document created in a software design tool.

Note 4 (for non-web software)

Functions that emulate a keyboard or numeric keypad key press are considered essential.

Example (Added) (for non-web software): Examples of essential functionality for non-web software are features for meeting environmental energy usage requirements (like waking a device from sleep, power saver mode, and low power state).

Note 5 (for non-web software)

This requirement applies to <ins>[non-web <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong> that interprets]</ins> pointer actions (i.e., this does not apply to actions that are required to operate the <ins>[underlying <strong><a href="https://www.w3.org/TR/wcag2ict-22/#platform-software">platform software</a></strong>]</ins> or assistive technology).

Note 6 (Added) (for non-web software)

This requirement also applies to platform software, such as user agents, assistive technology software, and operating systems. Each layer is responsible for its own pointer actions only, not for those in an underlying layer.

Note 7 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.5.3 Label in Name

(Level A)

> For [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") with [labels](https://www.w3.org/TR/WCAG22/#dfn-labels "text or other component with a text alternative that is presented to a user to identify a component within web content") that include [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") or [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect"), the [name](https://www.w3.org/TR/WCAG22/#dfn-name "text by which software can identify a component within web content to the user") contains the text that is presented visually.
> 
> Note
> 
> A best practice is to have the text of the label at the start of the name.

###### Applying SC 2.5.3 Label in Name to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 2.5.4 Motion Actuation

(Level A)

> [Functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that can be operated by device motion or user motion can also be operated by [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") and responding to the motion can be disabled to prevent accidental actuation, except when:
> 
> Supported Interface
> 
> The motion is used to operate functionality through an [accessibility supported](https://www.w3.org/TR/WCAG22/#dfn-accessibility-supported "supported by users' assistive technologies as well as the accessibility features in browsers and other user agents") interface;
> 
> Essential
> 
> The motion is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") for the function and doing so would invalidate the activity.

###### Applying SC 2.5.4 Motion Actuation to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.4](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html#intent).

##### 2.5.7 Dragging Movements

(Level AA)

> All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that uses a [dragging movement](https://www.w3.org/TR/WCAG22/#dfn-dragging-movements "New") for operation can be achieved by a [single pointer](https://www.w3.org/TR/WCAG22/#dfn-single-pointer "an input modality that only targets a single point on the page/screen at a time – such as a mouse, single finger on a touch screen, or stylus.") without dragging, unless dragging is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") or the functionality is determined by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and not modified by the author.
> 
> Note
> 
> This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

###### Applying SC 2.5.7 Dragging Movements to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html#intent), replacing "user agent" with "user agent or other platform software" and by making changes to the notes for non-web documents by replacing “web content” with "content", and for non-web software by replacing "web content that interprets" with "non-web software that interprets" and "user agent" with "underlying platform software".

With these substitutions, it would read:

**2.5.7 Dragging Movements:** All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality) that uses a [dragging movement](https://www.w3.org/TR/WCAG22/#dfn-dragging-movements) for operation can be achieved by a [single pointer](https://www.w3.org/TR/wcag22/#dfn-single-pointer) without dragging, unless dragging is [essential](https://www.w3.org/TR/wcag22/#dfn-essential) or the functionality is determined by the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#user-agent">user agent</a></strong> or other <strong><a href="https://www.w3.org/TR/wcag2ict-22/#platform-software">platform software</a></strong>]</ins> and not modified by the author.

Note 1 (for non-web documents)

This requirement applies to <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web">content</a></strong>]</ins> that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

Note 2 (Added) (for non-web documents)

Dragging movements for operation are less common in non-web documents. An example where a document author could add dragging functionality is an interactive prototype document created in a software design tool.

Note 3 (for non-web software)

This requirement applies to <ins>[non-web <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong> that interprets]</ins> pointer actions (i.e., this does not apply to actions that are required to operate the <ins>[underlying platform software]</ins> or assistive technology).

Note 4 (Added) (for non-web software)

This requirement also applies to platform software, such as user agents, assistive technology software, and operating systems. Each layer is responsible for its own pointer actions only, not for those in an underlying layer.

##### 2.5.8 Target Size (Minimum)

(Level AA)

> The size of the [target](https://www.w3.org/TR/WCAG22/#dfn-targets "region of the display that will accept a pointer action, such as the interactive area of a user interface component") for [pointer inputs](https://www.w3.org/TR/WCAG22/#dfn-pointer-inputs "input from a device that can target a specific coordinate (or set of coordinates) on a screen, such as a mouse, pen, or touch contact") is at least 24 by 24 [CSS pixels](https://www.w3.org/TR/WCAG22/#dfn-css-pixels "visual angle of about 0.0213 degrees"), except when:
> 
> Spacing
> 
> Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the [bounding box](https://www.w3.org/TR/WCAG22/#dfn-bounding-boxes "New") of each, the circles do not intersect another target or the circle for another undersized target;
> 
> Equivalent
> 
> The function can be achieved through a different control on the same page that meets this criterion;
> 
> Inline
> 
> The target is in a sentence or its size is otherwise constrained by the line-height of non-target text;
> 
> User Agent Control
> 
> The size of the target is determined by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and is not modified by the author;
> 
> Essential
> 
> A particular [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation "rendering of the content in a form to be perceived by users") of the target is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") or is legally required for the information being conveyed.
> 
> Note 1
> 
> Targets that allow for values to be selected spatially based on position within the target are considered one target for the purpose of the success criterion. Examples include sliders, color pickers displaying a gradient of colors, or editable areas where you position the cursor.
> 
> Note 2
> 
> For inline targets the line-height should be interpreted as perpendicular to the flow of text. For example, in a language displayed vertically, the line-height would be horizontal.

###### Applying SC 2.5.8 Target Size (Minimum) to Non-Web Documents and Software:

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html#intent), replacing "user agent" with "user agent or other platform software" and "on the same page" with "in the same non-web document or software".

With these substitutions, it would read:

**2.5.8 Target Size (Minimum):** The size of the [target](https://www.w3.org/TR/wcag2ict-22/#dfn-targets) for [pointer inputs](https://www.w3.org/TR/WCAG22/#dfn-pointer-inputs) is at least 24 by 24 [CSS pixels](https://www.w3.org/TR/wcag2ict-22/#dfn-css-pixels), except when:

Spacing

Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the [bounding box](https://www.w3.org/TR/WCAG22/#dfn-bounding-boxes) of each, the circles do not intersect another target or the circle for another undersized target;

Equivalent

The function can be achieved through a different control <ins>[in the same <strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> that meets this criterion.

Inline

The target is in a sentence or its size is otherwise constrained by the line-height of non-target text;

<ins>[User agent or other platform software]</ins> control

The size of the target is determined by the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#user-agent">user agent</a></strong> or other <strong><a href="https://www.w3.org/TR/wcag2ict-22/#platform-software">platform software</a></strong>]</ins> and is not modified by the author;

Essential

A particular [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation) of the target is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential) or is legally required for the information being conveyed.

Note 1

Targets that allow for values to be selected spatially based on position within the target are considered one target for the purpose of the success criterion. Examples include sliders, color pickers displaying a gradient of colors, or editable areas where you position the cursor.

Note 2

For inline targets the line-height should be interpreted as perpendicular to the flow of text. For example, in a language displayed vertically, the line-height would be horizontal.

Note 3 (Added)

In technologies where CSS is not used, the definition of 'CSS pixel' applies as described in [Applying “CSS pixel” to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-css-pixel-to-non-web-documents-and-software).

Note 4 (Added) (for non-web documents)

Some non-web document formats are designed for viewing at a wide range of zoom levels provided by the user agent. However, the commonly available user agents for these formats may lack a consistent base zoom level from which to evaluate this criterion. For such documents, evaluate target sizes at a zoom level that aligns with the intended usage of the content.

Note 5 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

### 3\. Understandable

> Information and the operation of the user interface must be understandable.

#### Applying Principle 3 Understandable to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 3 applies directly as written.

#### 3.1 Readable

> Make text content readable and understandable.

##### Applying Guideline 3.1 Readable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 3.1 applies directly as written.

##### 3.1.1 Language of Page

(Level A)

> The default [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s "language that is spoken, written or signed (through visual or tactile means) to communicate with humans") of each [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities").

###### Applying SC 3.1.1 Language of Page to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.1.1](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page#intent) replacing “each web page” with “non-web documents or software”.

With this substitution, it would read:

**3.1.1 Language of Page:** The default [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s) of <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> can be [programmatically determined](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-determinable).

Note 1 (Added) (for non-web software)

Where software platforms provide a “locale / language” setting, applications that use that setting and render their interface in that “locale / language” would satisfy this success criterion. Applications that do not use the platform “locale / language” setting but instead use an [accessibility-supported](https://www.w3.org/TR/wcag2ict-22/#dfn-accessibility-supported) method for exposing the human language of the [non-web software](https://www.w3.org/TR/wcag2ict-22/#software) would also satisfy this success criterion. Applications implemented in technologies where [assistive technologies](https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies) cannot determine the human language and that do not support the platform “locale / language” setting may not be able to satisfy this success criterion in that locale / language.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 3.1.2 Language of Parts

(Level AA)

> The [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s "language that is spoken, written or signed (through visual or tactile means) to communicate with humans") of each passage or phrase in the content can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") except for proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the immediately surrounding [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language").

###### Applying SC 3.1.2 Language of Parts to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.1.2](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts#intent) replacing “content” with “non-web document or software”.

With this substitution, it would read:

**3.1.2 Language of Parts:** The [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s) of each passage or phrase in the <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> can be [programmatically determined](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-determinable) except for proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the immediately surrounding [text](https://www.w3.org/TR/WCAG22/#dfn-text).

Note 1 (Added)

Examples of programmatic identification include language metadata or markup. There are some [non-web software](https://www.w3.org/TR/wcag2ict-22/#software) and [non-web document](https://www.w3.org/TR/wcag2ict-22/#document) technologies where there is no assistive technology supported method for marking the language for the different passages or phrases in the non-web document or software, and it would not be possible to satisfy this success criterion with those technologies.

Note 2 (Added) (for non-web documents)

Inheritance is one common method. For example, where the primary language of a non-web document is programmatically determinable, it can be assumed that all of the text or user interface elements within that document will be using the same language unless it is indicated.

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

#### 3.2 Predictable

> Make web pages appear and operate in predictable ways.

##### Applying Guideline 3.2 Predictable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 3.2 applies directly as written, replacing “web pages” with “non-web documents or software”.

With this substitution, it would read:

**Guideline 3.2 Predictable:** Make <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> appear and operate in predictable ways.

##### 3.2.1 On Focus

(Level A)

> When any [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") receives focus, it does not initiate a [change of context](https://www.w3.org/TR/WCAG22/#dfn-change-of-context "major changes that, if made without user awareness, can disorient users who are not able to view the entire page simultaneously").

###### Applying SC 3.2.1 On Focus to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.2.1](https://www.w3.org/WAI/WCAG22/Understanding/on-focus#intent).

Note (Added)

Some compound documents and their user agents are designed to provide significantly different viewing and editing functionality depending upon what portion of the compound document is being interacted with (e.g. a presentation that contains an embedded spreadsheet, where the menus and toolbars of the user agent change depending upon whether the user is interacting with the presentation content, or the embedded spreadsheet content). If the user uses a mechanism other than putting focus on that portion of the compound document with which they mean to interact (e.g. by a menu choice or special keyboard gesture), any resulting [change of context](https://www.w3.org/TR/wcag2ict-22/#dfn-change-of-context) wouldn't be subject to this success criterion because it was not caused by a change of focus.

##### 3.2.2 On Input

(Level A)

> Changing the setting of any [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") does not automatically cause a [change of context](https://www.w3.org/TR/WCAG22/#dfn-change-of-context "major changes that, if made without user awareness, can disorient users who are not able to view the entire page simultaneously") unless the user has been advised of the behavior before using the component.

###### Applying SC 3.2.2 On Input to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input#intent).

##### 3.2.3 Consistent Navigation

(Level AA)

> Navigational mechanisms that are repeated on multiple [web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization") occur in the [same relative order](https://www.w3.org/TR/WCAG22/#dfn-same-relative-order "same position relative to other items") each time they are repeated, unless a change is initiated by the user.

###### Applying SC 3.2.3 Consistent Navigation to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 3.2.3](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation#intent), replacing "on multiple web pages within a set of web pages" with "in multiple non-web documents within a set of non-web documents, or in multiple non-web software programs within a set of software programs”.

With these substitutions, it would read:

**3.2.3 Consistent Navigation:** Navigational mechanisms that are repeated <ins>[in multiple <strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> within a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-documents">set of non-web documents</a></strong>, or in multiple <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software programs</a></strong> within a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs">set of software programs</a></strong>]</ins> occur in the [same relative order](https://www.w3.org/TR/WCAG22/#dfn-same-relative-order) each time they are repeated, unless a change is initiated by the user.

Note 1 (Added)

See [set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents) and [set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](https://www.w3.org/TR/wcag2ict-22/#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

Although not required by this success criterion, ensuring that navigation elements have consistent order when repeated within non-web documents or software programs directly addresses user needs identified in the Intent section for this success criterion, and is generally considered best practice.

Note 3 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 3.2.4 Consistent Identification

(Level AA)

> Components that have the [same functionality](https://www.w3.org/TR/WCAG22/#dfn-same-functionality "same result when used") within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization") are identified consistently.

###### Applying SC 3.2.4 Consistent Identification to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 3.2.4](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification#intent), replacing “set of web pages” with “set of non-web documents or a set of software programs”.

With these substitutions, it would read:

**3.2.4 Consistent Identification:** Components that have the [same functionality](https://www.w3.org/TR/wcag2ict-22/#dfn-same-functionality) within a <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-documents">set of non-web documents</a></strong> or a <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs">set of software programs</a></strong>]</ins> are identified consistently.

Note 1 (Added)

See [set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents) and [set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](https://www.w3.org/TR/wcag2ict-22/#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

Although not required by this success criterion, ensuring that component identification be consistent when they occur more than once _within_ non-web documents or software programs directly addresses user needs identified in the Intent section for this success criterion, and is generally considered best practice.

Note 3 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 3.2.6 Consistent Help

(Level A)

> If a [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") contains any of the following help [mechanisms](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result"), and those mechanisms are repeated on multiple web pages within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization"), they occur in the same order relative to other page content, unless a change is initiated by the user:
> 
> -   Human contact details;
> -   Human contact mechanism;
> -   Self-help option;
> -   A fully automated contact mechanism.
> 
> Note 1
> 
> Help mechanisms may be provided directly on the page, or may be provided via a direct link to a different page containing the information.
> 
> Note 2
> 
> For this success criterion, "the same order relative to other page content" can be thought of as how the content is ordered when the page is serialized. The visual position of a help mechanism is likely to be consistent across pages for the same page variation (e.g., CSS break-point). The user can initiate a change, such as changing the page's zoom or orientation, which may trigger a different page variation. This criterion is concerned with relative order across pages displayed in the same page variation (e.g., same zoom level and orientation).

###### Applying SC 3.2.6 Consistent Help to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help#intent), replacing "web page(s)" and "page(s)" with "non-web document(s) or software program(s)", "set of web pages" with "set of non-web documents or set of software programs", "page content" with "content", "on the page" with "in the non-web document or software", "page is serialized" with "non-web document or software content is serialized", "different page" with "different non-web document, software, or web page", and "page variation" with "content layout variation".

With these substitutions, it would read:

**3.2.6 Consistent Help:** If a <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> contains any of the following help [mechanisms](https://www.w3.org/TR/WCAG22/#dfn-mechanism), and those mechanisms are repeated <ins>[in multiple non-web documents or software]</ins> within a <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-documents">set of non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs">set of software programs</a></strong>]</ins>, they occur in the same order relative to other <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#content-on-and-off-the-web">content</a></strong>]</ins>, unless a change is initiated by the user:

-   Human contact details;
-   Human contact mechanism;
-   Self-help option;
-   A fully automated contact mechanism

Note 1

Help mechanisms may be provided directly <ins>[in the non-web document or software]</ins>, or may be provided via a direct link to a <ins>[different non-web document, software, or web page]</ins> containing the information.

Note 2

For this success criterion, "the same order relative to other <ins>[content]</ins>" can be thought of as how the content is ordered when the <ins>[non-web document or software content is serialized]</ins>. The visual position of a help mechanism is likely to be consistent across <ins>[non-web documents or software]</ins> for the same <ins>[content layout variation]</ins> (e.g., CSS break-point). The user can initiate a change, such as changing the <ins>[non-web document’s or software's]</ins> zoom or orientation, which may trigger a different <ins>[content layout variation]</ins>. This criterion is concerned with relative order across <ins>[non-web documents or software]</ins> displayed in the same <ins>[content layout variation]</ins> (e.g., same zoom level and orientation).

Note 3 (Added)

See [set of documents](https://www.w3.org/TR/wcag2ict-22/#set-of-documents) and [set of software programs](https://www.w3.org/TR/wcag2ict-22/#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](https://www.w3.org/TR/wcag2ict-22/#interpretation-of-web-terminology-in-a-non-web-context).

Note 4 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

#### 3.3 Input Assistance

> Help users avoid and correct mistakes.

##### Applying Guideline 3.3 Input Assistance to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 3.3 applies directly as written.

##### 3.3.1 Error Identification

(Level A)

> If an [input error](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") is automatically detected, the item that is in error is identified and the error is described to the user in text.

###### Applying SC 3.3.1 Error Identification to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 3.3.2 Labels or Instructions

(Level A)

> [Labels](https://www.w3.org/TR/WCAG22/#dfn-labels "text or other component with a text alternative that is presented to a user to identify a component within web content") or instructions are provided when content requires user input.

###### Applying SC 3.3.2 Labels or Instructions to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.2](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions#intent).

##### 3.3.3 Error Suggestion

(Level AA)

> If an [input error](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") is automatically detected and suggestions for correction are known, then the suggestions are provided to the user, unless it would jeopardize the security or purpose of the content.

###### Applying SC 3.3.3 Error Suggestion to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion#intent).

##### 3.3.4 Error Prevention (Legal, Financial, Data)

(Level AA)

> For [web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") that cause [legal commitments](https://www.w3.org/TR/WCAG22/#dfn-legal-commitments "transactions where the person incurs a legally binding obligation or benefit") or financial transactions for the user to occur, that modify or delete [user-controllable](https://www.w3.org/TR/WCAG22/#dfn-user-controllable "data that is intended to be accessed by users") data in data storage systems, or that submit user test responses, at least one of the following is true:
> 
> Reversible
> 
> Submissions are reversible.
> 
> Checked
> 
> Data entered by the user is checked for [input errors](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") and the user is provided an opportunity to correct them.
> 
> Confirmed
> 
> A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available for reviewing, confirming, and correcting information before finalizing the submission.

###### Applying SC 3.3.4 Error Prevention (Legal, Financial, Data) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.4](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data#intent) replacing “web pages” with “non-web documents or software”.

With this substitution, it would read:

**3.3.4 Error Prevention (Legal, Financial, Data):** For <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins> that cause [legal commitments](https://www.w3.org/TR/WCAG22/#dfn-legal-commitments) or financial transactions for the user to occur, that modify or delete [user-controllable](https://www.w3.org/TR/WCAG22/#dfn-user-controllable) data in data storage systems, or that submit user test responses, at least one of the following is true:

Reversible

Submissions are reversible.

Checked

Data entered by the user is checked for input errors and the user is provided an opportunity to correct them.

Confirmed

A mechanism is available for reviewing, confirming, and correcting information before finalizing the submission.

##### 3.3.7 Redundant Entry

(Level A)

> Information previously entered by or provided to the user that is required to be entered again in the same [process](https://www.w3.org/TR/WCAG22/#dfn-processes "series of user actions where each action is required in order to complete an activity") is either:
> 
> -   auto-populated, or
> -   available for the user to select.
> 
> Except when:
> 
> -   re-entering the information is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform"),
> -   the information is required to ensure the security of the content, or
> -   previously entered information is no longer valid.

###### Applying SC 3.3.7 Redundant Entry to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry#intent).

##### 3.3.8 Accessible Authentication (Minimum)

(Level AA)

> A [cognitive function test](https://www.w3.org/TR/WCAG22/#dfn-cognitive-function-test "New") (such as remembering a password or solving a puzzle) is not required for any step in an authentication [process](https://www.w3.org/TR/WCAG22/#dfn-processes "series of user actions where each action is required in order to complete an activity") unless that step provides at least one of the following:
> 
> Alternative
> 
> Another authentication method that does not rely on a cognitive function test.
> 
> Mechanism
> 
> A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to assist the user in completing the cognitive function test.
> 
> Object Recognition
> 
> The cognitive function test is to recognize objects.
> 
> Personal Content
> 
> The cognitive function test is to identify [non-text content](https://www.w3.org/TR/WCAG22/#dfn-non-text-content "any content that is not a sequence of characters that can be programmatically determined or where the sequence is not expressing something in human language") the user provided to the website.
> 
> Note 1
> 
> "Object recognition" and "Personal content" may be represented by images, video, or audio.
> 
> Note 2
> 
> Examples of mechanisms that satisfy this criterion include:
> 
> -   support for password entry by password managers to reduce memory need, and
> -   copy and paste to reduce the cognitive burden of re-typing.

###### Applying SC 3.3.8 Accessible Authentication (Minimum) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html), replacing “the website” with “a website, non-web document, or software”.

With this substitution, it would read:

**3.3.8 Accessible Authentication (Minimum):** A [cognitive function test](https://www.w3.org/TR/wcag2ict-22/#dfn-cognitive-function-test) (such as remembering a password or solving a puzzle) is not required for any step in an authentication [process](https://www.w3.org/TR/WCAG22/#dfn-processes) unless that step provides at least one of the following:

Alternative

Another authentication method that does not rely on a cognitive function test.

Mechanism

A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to assist the user in completing the cognitive function test.

Object Recognition

The cognitive function test is to recognize objects.

Personal Content

The cognitive function test is to identify [non-text content](https://www.w3.org/TR/WCAG22/#dfn-non-text-content) the user provided to <ins>[a website, <strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web document</a></strong>, or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins>.

Note 1

"Object recognition" and "Personal content" may be represented by images, video, or audio.

Note 2

Examples of mechanisms that satisfy this criterion include:

1.  support for password entry by password managers to reduce memory need, and
2.  copy and paste to reduce the cognitive burden of re-typing.

Note 3 (Added) (for non-web software)

Any passwords used to unlock underlying [platform software](https://www.w3.org/TR/wcag2ict-22/#platform-software) (running below the non-web software) are out of scope for this requirement since these are not under control of the non-web software’s author.

Note 4 (Added) (for non-web software)

There are cases where non-web software has an authentication process and no alternative or assistance mechanism is feasible, for example when entering a password when starting, powering on / turning on an ICT (device or otherwise). In such situations, it may not be possible for the non-web software to satisfy this success criterion.

Note 5 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

### 4\. Robust

> Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.

#### Applying Principle 4 Robust to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 4 applies directly as written replacing “user agents, including assistive technologies” with “assistive technologies and accessibility features of software”.

With this substitution, it would read:

**Principle 4 Robust:** Content must be robust enough that it can be interpreted by a wide variety of <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies">assistive technologies</a></strong> and accessibility features of software]</ins>.

#### 4.1 Compatible

> Maximize compatibility with current and future user agents, including assistive technologies.

##### Applying Guideline 4.1 Compatible to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 4.1 applies directly as written, replacing “user agents, including assistive technologies” with “assistive technologies and accessibility features of software”.

With this substitution, it would read:

**Guideline 4.1 Compatible:** Maximize compatibility with current and future <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies">assistive technologies</a></strong> and accessibility features of software]</ins>.

##### 4.1.1 Parsing (WCAG 2.1)

(Level A)

> In content implemented using markup languages, elements have complete start and end tags, elements are nested according to their specifications, elements do not contain duplicate attributes, and any IDs are unique, except where the specifications allow these features.
> 
> Note 1
> 
> This success criterion should be considered as always satisfied for any content using HTML or XML.
> 
> Note 2
> 
> Since this criterion was written, the HTML Living Standard has adopted specific requirements governing how user agents must handle incomplete tags, incorrect element nesting, duplicate attributes, and non-unique IDs. \[[HTML](https://www.w3.org/TR/WCAG21/#bib-html "HTML Standard")\]
> 
> Although the HTML standard treats some of these cases as non-conforming for authors, it is considered to "allow these features" for the purposes of this success criterion because the specification requires that user agents support handling these cases consistently. In practice, this criterion no longer provides any benefit to people with disabilities in itself.
> 
> Issues such as missing roles due to inappropriately nested elements or incorrect states or names due to a duplicate ID are covered by different success criteria and should be reported under those criteria rather than as issues with 4.1.1.

###### Applying SC 4.1.1 Parsing (WCAG 2.0 and 2.1) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 4.1.1](https://www.w3.org/WAI/WCAG21/Understanding/parsing#intent), replacing “In content implemented using markup languages” with “For non-web documents or software that use markup languages, in such a way that the markup is separately exposed and available to assistive technologies and accessibility features of software or to a user-selectable user agent” and replacing the WCAG notes with notes applicable to non-web documents and software.

With this substitution, it would read:

**4.1.1 Parsing:** <ins>[For <strong><a href="https://www.w3.org/TR/wcag2ict-22/#document">non-web documents</a></strong> or <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong> that use markup languages, in such a way that the markup is separately exposed and available to <strong><a href="https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies">assistive technologies</a></strong> and accessibility features of software or to a user-selectable <strong><a href="https://www.w3.org/TR/wcag2ict-22/#user-agent">user agent</a></strong>]</ins>, elements have complete start and end tags, elements are nested according to their specifications, elements do not contain duplicate attributes, and any IDs are unique, except where the specifications allow these features.

Note 1 (Added)

Markup is not always available to [assistive technologies](https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies) or to user selectable [user agents](https://www.w3.org/TR/wcag2ict-22/#user-agent) such as browsers. Software sometimes uses markup languages internally for persistence of the software user interface, in ways where the markup is never available to assistive technology (either directly or through a document object model (DOM)), or to a user agent (such as a browser). In such cases, conformance to this provision would have no impact on accessibility as it can have for web content where it is exposed.

Accessibility issues introduced through poor markup would surface as errors in the programmatic information and would be reported using success criteria that rely on that information, such as 1.3.1 Info and Relationships and 4.1.2 Name, Role, Value.

Note 2 (Added)

This success criterion would be satisfied in cases where:

-   Content is implemented using HTML or XML (as outlined in the [WCAG 2.1 note on 4.1.1](https://www.w3.org/TR/WCAG21/#h-note-27) and the [WCAG 2.0 editorial errata](https://www.w3.org/WAI/WCAG20/errata/#editorial) in the thirteenth list item)
-   Non-web documents or software are not authored using a markup language.
-   Non-web documents or software are authored using a markup language, but accessibility information is exposed via platform accessibility APIs, not by making the markup itself available to assistive technologies.

Example (Added): Examples where 4.1.1 Parsing would be satisfied:

-   An HTML page embedded inside a desktop application (as outlined in the [WCAG 2.1 note on 4.1.1](https://www.w3.org/TR/WCAG21/#h-note-27) and the [WCAG 2.0 editorial errata](https://www.w3.org/WAI/WCAG20/errata/#editorial) in the thirteenth list item)
-   A PDF document (not authored using a markup language)
-   Android or iOS apps which use a markup language to specify UI layout (accessibility information is exposed via platform accessibility APIs, not the markup)

Examples of markup that might be separately exposed and available to assistive technologies and to user agents include:

-   LaTeX documents
-   Markdown documents

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 4.1.1 Parsing (WCAG 2.2)

(Obsolete and removed)

> Note
> 
> This criterion was originally adopted to address problems that assistive technology had directly parsing HTML. Assistive technology no longer has any need to directly parse HTML. Consequently, these problems either no longer exist or are addressed by other criteria. This criterion no longer has utility and is removed.

###### Applying SC 4.1.1 Parsing (Obsolete and removed) (WCAG 2.2) to Non-Web Documents and Software

Note (Added)

WCAG 2.2 has made this success criterion obsolete and removed it as a requirement in the standard. Therefore, the interpretation of this success criterion for [non-web documents](https://www.w3.org/TR/wcag2ict-22/#document) and [software](https://www.w3.org/TR/wcag2ict-22/#software) has been removed.

##### 4.1.2 Name, Role, Value

(Level A)

> For all [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") (including but not limited to: form elements, links and components generated by scripts), the [name](https://www.w3.org/TR/WCAG22/#dfn-name "text by which software can identify a component within web content to the user") and [role](https://www.w3.org/TR/WCAG22/#dfn-role "text or number by which software can identify the function of a component within Web content") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities"); [states](https://www.w3.org/TR/WCAG22/#dfn-states "dynamic property expressing characteristics of a user interface component that may change in response to user action or automated processes"), properties, and values that can be set by the user can be [programmatically set](https://www.w3.org/TR/WCAG22/#dfn-programmatically-set "set by software using methods that are supported by user agents, including assistive technologies"); and notification of changes to these items is available to [user agents](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users"), including [assistive technologies](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents").
> 
> Note
> 
> This success criterion is primarily for web authors who develop or script their own user interface components. For example, standard HTML controls already meet this success criterion when used according to specification.

###### Applying SC 4.1.2 Name, Role, Value to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value#intent), replacing “user agents, including assistive technologies", with “assistive technologies and accessibility features of underlying software” and the note with: “This success criterion is primarily for software developers who develop or use custom user interface components. For example, standard user interface components on most accessibility-supported platforms already satisfy this success criterion when used according to specification.”

With this substitution, it would read:

**4.1.2 Name, Role, Value:** For all [user interface components](https://www.w3.org/TR/wcag2ict-22/#dfn-user-interface-components) (including but not limited to: form elements, links and components generated by scripts), the [name](https://www.w3.org/TR/wcag2ict-22/#dfn-name) and [role](https://www.w3.org/TR/wcag2ict-22/#dfn-role) can be [programmatically determined](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-determinable); [states](https://www.w3.org/TR/WCAG22/#dfn-states), properties, and values that can be set by the user can be [programmatically set](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-set); and notification of changes to these items is available to <ins>[<strong><a href="https://www.w3.org/TR/wcag2ict-22/#dfn-assistive-technologies">assistive technologies</a></strong> and accessibility features of underlying <strong><a href="https://www.w3.org/TR/wcag2ict-22/#software">software</a></strong>]</ins>.

Note 1 (Added) (for non-web documents)

For non-web document formats that support interoperability with assistive technology, standard user interface components often satisfy this success criterion when used according to the general design and accessibility guidance for the document format.

Note 2 (Replaced) (for non-web software)

This success criterion is primarily for software developers who develop or use custom user interface components. Standard user interface components on most [accessibility-supported](https://www.w3.org/TR/wcag2ict-22/#dfn-accessibility-supported) platforms already satisfy this success criterion when used according to specification.

Note 3 (Added) (for non-web software)

For conforming to this success criterion, it is usually best practice for software user interfaces to use the [accessibility services of platform software](https://www.w3.org/TR/wcag2ict-22/#accessibility-services-of-platform-software). These accessibility services enable interoperability between software user interfaces and both assistive technologies and accessibility features of software in standardized ways. Most platform accessibility services go beyond programmatic exposure of name and role, and programmatic setting of states, properties and values (and notification of same), and specify additional information that could be exposed and / or set (for instance, a list of the available actions for a given user interface component, and a means to programmatically execute one of the listed actions).

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

##### 4.1.3 Status Messages

(Level AA)

> In content implemented using markup languages, [status messages](https://www.w3.org/TR/WCAG22/#dfn-status-messages "change in content that is not a change of context, and that provides information to the user on the success or results of an action, on the waiting state of an application, on the progress of a process, or on the existence of errors") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") through [role](https://www.w3.org/TR/WCAG22/#dfn-role "text or number by which software can identify the function of a component within Web content") or properties such that they can be presented to the user by [assistive technologies](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents") without receiving focus.

###### Applying SC 4.1.3 Status Messages to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html#intent).

Note 1 (Added)

For [non-web documents](https://www.w3.org/TR/wcag2ict-22/#document) and [software](https://www.w3.org/TR/wcag2ict-22/#software) where status messages are not implemented using markup languages, there is still a user need to have status messages be programmatically exposed so that they can be presented to the user by assistive technologies without receiving focus. This is typically enabled through the use of accessibility services of the [user agent](https://www.w3.org/TR/wcag2ict-22/#user-agent) or other [platform software](https://www.w3.org/TR/wcag2ict-22/#platform-software).

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality).

## Privacy Considerations

_This section is non-normative._

This Working Group Note does not introduce any new privacy considerations. However, when implementing WCAG 2 success criteria in the context of non-web ICT, information about a user’s accessibility needs or preferences might be exposed; a user could be harmed by disclosure and misuse of that information. It is best practice to choose implementations that reduce the potential for fingerprinting or other identification and tracking of users, and that the only data collected is data necessary to enable the accessibility features.

## Security Considerations

_This section is non-normative._

This Working Group Note does not introduce any new security considerations. Since any software feature has the potential to compromise security, take care when implementing non-web ICT features added to meet WCAG 2 success criteria.

## A. Success Criteria Problematic for Closed Functionality

There are success criteria that can be problematic for developers of ICT with closed functionality. Some criteria discuss making information available in text (which can be read by assistive technologies), making it “programmatically determinable” (rendered by a user agent and readable by assistive technologies), or doing something else to make content compatible with assistive technologies. Where ICT with closed functionality doesn’t support use of assistive technology or the platform does not have an accessibility API, providing equivalent information and operation through another mechanism, such as functions built into the software that behave like assistive technology, would help meet the intent of these success criteria. See also the [Comments on Closed Functionality](https://www.w3.org/TR/wcag2ict-22/#comments-on-closed-functionality) section.

Other success criteria would apply to ICT with closed functionality either if they are partially closed or if they allow for the connection of some types of devices. As an example, Success Criterion 2.1.1 Keyboard would apply to ICT that is closed to screen readers, but have a physical keyboard, a connector for standard keyboards, or allow the installation of alternate keyboards. While these criteria, as written, are not always applicable to ICT with closed functionality, most of them can inform and aid development of built-in features needed to make ICT with closed functionality accessible.

For non-web software on ICT with closed functionality, those who implement this document (WCAG2ICT) should consider the applicability of individual WCAG 2 success criteria on a criterion-by-criterion basis. Alternate accessibility provisions might be needed to cover the user needs addressed by the following success criteria:

-   [1.1.1 Non-text Content](https://www.w3.org/TR/wcag2ict-22/#non-text-content) — Depends upon text (or a text alternative) being in a programmatically determinable form.
-   [1.2.1 Pre-recorded video](https://www.w3.org/TR/wcag2ict-22/#audio-only-and-video-only-prerecorded) — One of the options available to authors for Success Criterion 1.2.1 is providing a media alternative that is text which, in the absence of connected assistive technology, would need to be made available in different modalities.
-   [1.2.3 Audio description or Media Alternative](https://www.w3.org/TR/wcag2ict-22/#audio-description-or-media-alternative-prerecorded) — One of the options available to authors for Success Criterion 1.2.3 is providing a media alternative that is text which, in the absence of connected assistive technology, would need to be made available in different modalities.
-   [1.3.1 Info and Relationships](https://www.w3.org/TR/wcag2ict-22/#info-and-relationships) — Requires that information be in a programmatically determinable form or in text (that is programmatically determinable).
-   [1.3.2 Meaningful Sequence](https://www.w3.org/TR/wcag2ict-22/#meaningful-sequence) — Requires information (i.e, a correct reading sequence) in a programmatically determinable form. An equivalent for ICT with closed functionality would be to provide a meaningful reading sequence through auditory output or some other non-visual means that helps users correlate the output with the corresponding information displayed on the screen.
-   [1.3.4 Orientation](https://www.w3.org/TR/wcag2ict-22/#orientation) — ICT with closed functionality that has fixed-in-place displays or other limitations that prevent modifying the physical display orientation should be considered as examples that are covered under the essential exception. See the note in the section [Applying SC 1.3.4 Orientation to Non-Web Software](https://www.w3.org/TR/wcag2ict-22/#applying-sc-1-3-4-orientation-to-non-web-software).
-   [1.3.5 Identify Input Purpose](https://www.w3.org/TR/wcag2ict-22/#identify-input-purpose) — Depends upon information in a programmatically determinable form; in the absence of programmatic capabilities, text labels need to be specific and be provided to the user in other modalities (e.g. auditory).
-   [1.4.2 Audio Control](https://www.w3.org/TR/wcag2ict-22/#audio-control) — The intent of this success criterion is to avoid interference of audio with assistive products, which are not available in ICT with closed functionality. If the built-in accessibility features of the ICT with closed functionality provide speech output, then the interference may happen and this success criterion applies. In addition, there are existing requirements in regulations (e.g., the EN 301 549 and U.S. Revised 508 Standards) that address volume control for ICT with closed functionality.
-   [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/wcag2ict-22/#contrast-minimum) — There are cases where applying this success criterion to non-web software on ICT with closed functionality is problematic:
    -   When the contrast of the content is determined by the hardware and not modifiable by the software author, it may not be possible to meet this success criterion.
        
        Note 1
        
        Contrast requirements for hardware are out of scope for WCAG2ICT (and this success criterion).
        
    -   When the color contrast ratio cannot be programmatically measured due to system limitations (e.g. lockdown), precise quantifiable testing of color contrast cannot be performed by a third party. In such cases, the software author would need to confirm that the color combinations used meet the contrast requirement.
        
        Note 2
        
        Photographs (e.g., of a hardware display) are not sufficient for testing that content meets this success criterion. This is because the quality of the lighting, camera, and physical aspects of the hardware display can dramatically affect the ability to capture the content for testing purposes.
        
-   [1.4.4 Resize Text](https://www.w3.org/TR/wcag2ict-22/#resize-text) — Non-web software on ICT with closed functionality may offer more limited text rendering support than the support found in user agents for the Web. As a result, meeting Success Criterion 1.4.4 in a closed environment may place a much heavier burden on the content author.
-   [1.4.5 Images of Text](https://www.w3.org/TR/wcag2ict-22/#images-of-text) — To enable assistive technology to modify displayed text (e.g., adjusting contrast, increasing font size), machine-readable text is needed, as opposed to mere images of text. Not all ICT with closed functionality has the capability to support visual modification of displayed text or images of text, given there is no interoperability with assistive technology and/or lack of platform support.
-   [1.4.10 Reflow](https://www.w3.org/TR/wcag2ict-22/#reflow) — Some non-web software on ICT with closed functionality does not support scrolling content, or zooming, or changing the size of a viewport or scrollable content area to the specified width/height (examples include, but are not limited to, software for self-service transaction machines or kiosks). Therefore, some other non-WCAG requirements would be needed for ICT with closed functionality to ensure that content is readable by persons with low vision without scrolling in two dimensions.
    
    Note 3
    
    Some ICT with closed functionality does not display large chunks of text and only has UI controls. In such cases, two-dimensional scrolling to access the text and UI controls may be considered essential, thus meeting an exception, and the success criterion would be satisfied.
    
-   [1.4.11 Non-text Contrast](https://www.w3.org/TR/wcag2ict-22/#non-text-contrast) — There are cases where applying this success criterion to non-web software on ICT with closed functionality is problematic:
    -   When the contrast of the content is determined by the hardware and not modifiable by the software author, it may not be possible to meet this success criterion.
        
        Note 4
        
        Contrast requirements for hardware are out of scope for WCAG2ICT (and this success criterion).
        
    -   When the color contrast ratio cannot be programmatically measured due to system limitations (e.g. lockdown), precise quantifiable testing of color contrast cannot be performed by a third party. In such cases, the software author would need to confirm that the color combinations used meet the contrast requirement.
        
        Note 5
        
        Photographs are not sufficient for testing that content meets this success criterion. This is because the quality of the lighting, camera, and physical aspects of the hardware display can dramatically affect the ability to capture the content for testing purposes.
        
-   [1.4.12 Text Spacing](https://www.w3.org/TR/wcag2ict-22/#text-spacing) — In non-web software on ICT with closed functionality the ability for users to modify line, paragraph, letter, or word spacing is rarely supported. Regardless, the success criterion applies as written and as noted in the [Applying SC 1.4.12 Text Spacing to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-sc-1-4-12-text-spacing-to-non-web-documents-and-software).
-   [2.1.1 Keyboard](https://www.w3.org/TR/wcag2ict-22/#keyboard) — Assumes operation via a keyboard interface which also allows for alternative input devices. It may not be possible to satisfy this success criterion when the ICT does not have a built-in keyboard, and it also does not support an alternative input method (hardware or software) that provides keyboard-like access to all functionality.
    
    Note 6
    
    A keypad that provides full access to functionality might be considered a keyboard.
    
-   [2.1.2 No Keyboard Trap](https://www.w3.org/TR/wcag2ict-22/#no-keyboard-trap) — This criterion applies when focus can be moved using a keyboard interface. In some ICT with closed functionality, tactile input like numeric keypads or other functional groups of keys may be available, but there is no mechanism for onscreen focus; for example, the keys are mapped directly to functions without moving focus between on-screen controls. In this case, there is no concept of focus, and therefore keyboard traps cannot exist and this success criterion would be satisfied.
-   [2.1.4 Character Key Shortcuts](https://www.w3.org/TR/wcag2ict-22/#character-key-shortcuts) — ICT with closed functionality might lack a mechanism for keyboard shortcuts because their mode of operation revolves around a single key performing a single function. For such systems, this success criterion is satisfied.
-   [2.4.1 Bypass Blocks](https://www.w3.org/TR/wcag2ict-22/#bypass-blocks) — The WCAG2ICT interpretation of this success criterion replaces "sets of Web pages" with "sets of software programs" which are extremely rare - especially for non-web software on ICT with closed functionality. However, being able to bypass blocks of content that are repeated within software is generally considered best practice.
-   [2.4.4 Link Purpose (In Context)](https://www.w3.org/TR/wcag2ict-22/#link-purpose-in-context) — This success criterion relies upon text and context being made available in a programmatically determinable form.
-   [2.4.5 Multiple Ways](https://www.w3.org/TR/wcag2ict-22/#multiple-ways) — The WCAG2ICT interpretation of this success criterion replaces "set of Web pages" with "set of software programs". Such sets, particularly in the context of non-web software on ICT with closed functionality, are exceedingly rare. There are a number of notes in the section [Applying SC 2.4.5 Multiple Ways to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-sc-2-4-5-multiple-ways-to-non-web-documents-and-software) that are applicable to non-web software on ICT with closed functionality.
-   [2.4.7 Focus Visible](https://www.w3.org/TR/wcag2ict-22/#focus-visible) — Presumes that there is a mode of operation where focus can be moved and controlled by keyboard. Some ICT with closed functionality may offer tactilely discernible input such as a numeric keypad or other functional groups of keys, but do not offer any mechanism for conveying focus because the user interface is designed not to need that. For example, the keys are used to select options from a spoken menu rather than to move an onscreen focus element between multiple options. In this case, there is no concept of focus, thus there is no need for a visible indicator and this success criterion would be satisfied.
-   [2.5.2 Pointer Cancellation](https://www.w3.org/TR/wcag2ict-22/#pointer-cancellation) — As noted in the section [Applying SC 2.5.2 Pointer Cancellation to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-sc-2-5-2-pointer-cancellation-to-non-web-documents-and-software), examples of ‘essential’ functionality are features for meeting environmental energy usage requirements (like waking a device from sleep, power saver mode, and low power state).
-   [2.5.3 Label in Name](https://www.w3.org/TR/wcag2ict-22/#label-in-name) — Requires information in a programmatically determinable form; specifically, the programmatic name contains the text of the visual label.
-   [2.5.8 Target Size (Minimum)](https://www.w3.org/TR/wcag2ict-22/#target-size-minimum) — This success criterion uses CSS pixels for defining the target size. ICT with closed functionality may not use CSS pixels as a standard measurement, but the definition of ‘CSS pixel’ still applies as described in [Applying “CSS pixel” to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-css-pixel-to-non-web-documents-and-software). If the system supports a density-independent pixel measurement, it should be used in place of CSS pixels.
    
    Note 7
    
    If the viewing distance and pixel density of the system are unknown, approximating the reference pixel as described in Applying “CSS pixel” to Non-Web Documents and Software is not possible.
    
    Note 8
    
    For non-web software designed to run on specific known hardware, a physical size standard would be more straightforward to apply, as calculations for a CSS pixel are dependent on the viewing distance or pixel density of the display.
    
-   [3.1.1 Language of Page](https://www.w3.org/TR/wcag2ict-22/#language-of-page) — Depends upon language information being in a programmatically determinable form intended to drive correct pronunciation. Where another mechanism achieves correct pronunciation for ICT with closed functionality, such as self-voicing, the intent of this success criterion would be met.
-   [3.1.2 Language of Parts](https://www.w3.org/TR/wcag2ict-22/#language-of-parts) — Depends upon language information in a programmatically determinable form intended to drive correct pronunciation. Where another mechanism achieves correct pronunciation for ICT with closed functionality, such as self-voicing, the intent of this success criterion would be met.
-   [3.2.3 Consistent Navigation](https://www.w3.org/TR/wcag2ict-22/#consistent-navigation) — This success criterion is interpreted to only apply to “sets of software programs” which are very rare. See the second note in the section [Applying SC 3.2.3 Consistent Navigation to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-sc-3-2-3-consistent-navigation-to-non-web-documents-and-software).
-   [3.2.4 Consistent Identification](https://www.w3.org/TR/wcag2ict-22/#consistent-identification) — This success criterion is interpreted to only apply to “sets of software programs” which are very rare. See the second note in the section [Applying SC 3.2.4 Consistent Identification to Non-Web Documents and Software](https://www.w3.org/TR/wcag2ict-22/#applying-sc-3-2-4-consistent-identification-to-non-web-documents-and-software).
-   [3.2.6 Consistent Help](https://www.w3.org/TR/wcag2ict-22/#consistent-help) — The WCAG2ICT interpretation of this success criterion replaces "sets of Web pages" with "sets of software programs" which are extremely rare - especially for non-web software on ICT with closed functionality. However, providing consistent access to help is generally considered best practice.
-   [3.3.1 Error Identification](https://www.w3.org/TR/wcag2ict-22/#error-identification) — Requires error information to be provided as text, noting that the WCAG definition of text is that it be "programmatically determinable".
-   [3.3.8 Accessible Authentication (Minimum)](https://www.w3.org/TR/wcag2ict-22/#accessible-authentication-minimum) — There are situations where meeting this success criterion is problematic for ICT with closed functionality:
    -   Systems that are designed for shared use (such as in a public library) or have closed functionality might block mechanisms typically used to assist the user, such as copying authentication information from a password manager. Instead, an alternative authentication method might be needed, such as an identity card scanner.
    -   Where standards for banking or security have authentication requirements that are regulated or strictly enforced, those requirements may be judged to take legal precedence over Success Criterion 3.3.8 Accessible Authentication (Minimum).
-   [4.1.1 Parsing](https://www.w3.org/TR/wcag2ict-22/#parsing21)
    -   When WCAG 2.0 and 2.1 were written, the [Intent of Success Criterion 4.1.1](https://www.w3.org/TR/2013/NOTE-UNDERSTANDING-WCAG20-20130905/ensure-compat-parses.html#ensure-compat-parses-intent-head) was to provide consistency so that different user agents or assistive technologies would yield the same result.
    -   In WCAG 2.2, Success Criterion 4.1.1 Parsing was made obsolete and WCAG 2.2 removed it as a requirement, so this success criterion is not applicable.
-   [4.1.2 Name, Role, Value](https://www.w3.org/TR/wcag2ict-22/#name-role-value) — Requires information in a programmatically determinable form.
-   [4.1.3 Status Messages](https://www.w3.org/TR/wcag2ict-22/#status-messages) — Depends upon status messages being programmatically determinable using role or properties.
    
    Note 9
    
    Non-web software on ICT with closed functionality would need equivalent facilitation to provide access to status messages.
    

## B. Background on Text / Command-Line / Terminal Applications and Interfaces

### B.1 How Text Interfaces Are Realized

The interface of a text application is realized through a server application directing which characters should be placed on the screen, along with either a hardware terminal or a terminal application that displays the characters. The client terminal application for text applications is analogous to a web user agent for web pages. Also, like web applications, text applications may execute primarily on a remote server or execute locally.

Some text applications render like a TeleTYpewriter (TTY); their output is always appended, like an ever-growing file. Such text applications are often called “command-line applications” or occasionally “TTY-applications”, and their output can optionally be redirected to a file for later review. Others explicitly place text into a matrix of fixed width character cells on a screen (sometimes with specific foreground and background colors).

Historically, input to the text application itself is provided exclusively through a keyboard interface, though Automatic Speech Recognition (ASR) based voice input is sometimes now an alternative option - especially on mobile devices.

### B.2 How Text Applications Have Been Made Accessible Via Assistive Technology

Strategies for making text applications accessible through assistive technology involve two key tasks: (1) obtaining all of the text displayed in the interface, and (2) performing an analysis on that text to detect screen updates and attempt to discern structural elements.

For example, a text application screen reader might directly access the matrix of character cells in the interface and provide a screen review mechanism for the user to review that matrix of characters (by sending the output to synthetic speech and/or a braille display). Alternately, a text application screen reader might directly consume the output rendered (perhaps by acting as its own terminal application or by analyzing the “TTY” output). A text application screen reader might also attempt to analyze the spacing and layout of the text in the matrix, to provide features such as reading columns of text in a multi-column layout; discerning headers through analysis of line spacing, indentation, and capitalization; and discerning input fields or user interface components by scanning for the use of inverse video, for text appearing in brackets, or for text from the character graphics codepage (ASCII codes greater than ‘0x7F’). Some of this analysis might also be done through the use of filter tools that transform the output of a program (e.g., through reformatting “TTY” output rendered to a file or as direct input to a filter tool).

Similarly, a text application screen magnifier would gain access to the matrix of character cells to magnify them or re-display them in a larger font. It would scan for screen refreshes and updates and then apply heuristics to what had changed in order to decide what sub-matrix of character cells should appear in a magnified view. It would also scan for inverse video and a moving text cursor to track text being input by the user (and might combine the text matrix scanning with scanning of the keyboard input to match user input to what is appearing on the screen).

### B.3 Applying WCAG 2 to Text Applications

To apply WCAG to text applications, it is necessary to apply the glossary terms [accessibility supported](https://www.w3.org/TR/wcag2ict-22/#dfn-accessibility-supported) and [programmatically determined](https://www.w3.org/TR/wcag2ict-22/#dfn-programmatically-determinable) in the context of how text applications are rendered and the history of assistive technologies that made them accessible.

As noted above, in a text interface the terminal application renders the characters on the screen, just as a web browser typically renders content for a web application. As an example, for success criterion [1.4.4 Resize Text](https://www.w3.org/TR/WCAG22/#resize-text), a text application could achieve 200 percent resizing when the terminal application client that is rendering it has this capability (cf. WCAG 2 Technique [G142 Using a technology that has commonly-available user agents that support zoom](https://www.w3.org/WAI/WCAG22/Techniques/general/G142)). Many web pages and web applications use this approach to meet success criterion [1.4.4 Resize Text](https://www.w3.org/TR/WCAG22/#resize-text) through no explicit action of their own.

A similar approach could also be used for success criterion [1.4.3 Contrast (minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum) (cf. WCAG 2 Technique [G148: Not specifying background color, not specifying text color, and not using technology features that change those defaults](https://www.w3.org/WAI/WCAG22/Techniques/general/G148)): relying on the terminal application client to render the text with sufficient contrast against the background. In fact, many terminal applications allow the user to force all text to share a single user-chosen foreground color (and a single user-chosen background color), overriding the text application's specified colors to meet the user's desires or needs.

Since many assistive technology analysis techniques depend upon discerning the location of the text input cursor, terminal application use of “soft cursors” and “highlight bars” may bypass those analysis techniques and cause failures of success criteria.

Note 1

It is outside of the scope of this document to define WCAG techniques for non-web ICT. These examples are simply illustrations of how WCAG 2 success criteria can be applied to this class of non-web software applications.

The way to think about "accessibility supported" and "programmatically determined" may seem a little different for text applications, but the definitions are unchanged. Unlike the semantic objects of graphical user interfaces and web pages, the output of text-based applications consists of plain text. A terminal emulator acts as the user agent for text-based applications; it might render some content such as escape codes as semantic elements, but otherwise exposes only lines of text to assistive technology. Where assistive technology is able to interpret the text and any semantic objects accurately, the content is "programmatically determinable"—even though no explicit markup was necessarily used to make it so.

Note 2

The terminal application itself is “traditional” non-web software ICT. It is only for the text application that there is a need to take this approach with these glossary terms.

## C. Acknowledgements

### C.1 Active Participants of the WCAG2ICT Task Force Involved in the Development of This Document

-   Shadi Abou-Zahra (Amazon)
-   Bruce Bailey (Invited Expert)
-   Phil Day (NCR Atleos)
-   Tamsin Ewing (W3C Staff)
-   Loïc Martínez Normand (Universidad Politécnica de Madrid)
-   Laura Miller (US General Services Administration)
-   Daniel Montalvo (W3C Staff)
-   Mary Jo Mueller (IBM Corporation)
-   Mike Pluke (Invited Expert)
-   Gregg Vanderheiden (W3C Invited Expert)

### C.2 Participants in the AG Working Group that Actively Reviewed and Contributed

-   Jonathan Avila (Level Access)
-   Daniel Bjorge (Deque Systems, Inc.)
-   Alastair Campbell (Nomensa)
-   Laura Carlson (Invited Expert)
-   DJ Chase (Invited Expert)
-   Azlan Cuttilan (Invited Expert)
-   Jennifer Delisi (Invited Expert)
-   Steve Faulkner (TetraLogical Services Ltd.)
-   Wilco Fiers (Deque Systems, Inc.)
-   Detlev Fischer (Invited Expert)
-   Mike Gifford (Invited Expert)
-   Michael Gower (IBM Corporation)
-   Jan Jaap de Groot (Abra)
-   Shawn Henry (W3C Staff)
-   Andrew Kirkpatrick (Evinced Inc.)
-   Patrick Lauke (TetraLogical)
-   Todd Libby (Invited Expert)
-   David MacDonald (Invited Expert)
-   Rachael Bradley Montgomery (Library of Congress)
-   Lori Oakley (Oracle Corporation)
-   Scott O'Hara (Microsoft Corporation)
-   Kimberly Patch (Invited Expert)
-   Melanie Philipp (Invited Expert)
-   Julie Rawe (Understood)
-   Roberto Scano (Invited Expert)
-   Lisa Seeman-Horwitz (Invited Expert)
-   Poornima Badhan Subramanian (Invited Expert)
-   Ben Tillyer (University of Oxford)
-   Kevin White (W3C Staff)
-   Frankie Wolf (Invited Expert)

WCAG2ICT Task Force participants are also in the AG working group, but are not repeated here.

### C.3 Other Participants of the WCAG2ICT Task Force

-   Charles Adams (Oracle Corporation)
-   Fernanda Bonnin (Microsoft Corporation)
-   Devanshu Chandra (Deque Systems, Inc.)
-   Mitchell Evan (TPGi)
-   Thorsten Katzmann (IBM Corporation)
-   Sam Ogami (Invited Expert)
-   Jennifer Strickland (MITRE Corporation)
-   Shawn Thompson (Shared Services Canada)
-   Bryan Trogdon (Google LLC)

### C.4 Previous Contributors

The following people contributed to the development of the WCAG2ICT Note:

Charles Adams, Matthew Atkinson, Fernanda Bonnin, Judy Brewer, Devanshu Chandra, Michael Cooper, Mitchell Evan, Anastasia Lanz, Janina Sajka, Olivia Hogan-Stark, Thorsten Katzmann, Chris Loiselle, Sam Ogami, Shawn Thompson, Jason White

### C.5 Enabling Funders

This publication has been funded in part with U.S. Federal funds from the Health and Human Services, National Institute on Disability, Independent Living, and Rehabilitation Research (NIDILRR), initially under contract number ED-OSE-10-C-0067 and now under HHS75P00120P00168. The content of this publication does not necessarily reflect the views or policies of the U.S. Department of Health and Human Services or the U.S. Department of Education, nor does mention of trade names, commercial products, or organizations imply endorsement by the U.S. Government.

Work on this publication was part of the [WAI-CooP Project](https://www.w3.org/WAI/about/projects/wai-coop/), a European Commission (EC) co-funded project, Horizon 2020 Program (101004794).

-   2025-12-04 [sotd updates](https://github.com/w3c/wcag2ict/pull/819)
-   2025-10-30 [2.4.2 Page Titled - Not all non-web docs and SW have titles that describe the topic or purpose](https://github.com/w3c/wcag2ict/pull/793)
-   2025-10-30 [2.4.4 Link Purpose: Adjust "link" note to apply to non-web docs as well](https://github.com/w3c/wcag2ict/pull/806)
-   2025-10-24 [1.3.4 Orientation: update guidance for non-web documents and software and add examples](https://github.com/w3c/wcag2ict/pull/780)
-   2025-10-09 [1.4.4 Resize Text: Remove note regarding minimum text size](https://github.com/w3c/wcag2ict/pull/792)
-   2025-09-18 [1.4.13 Content on Hover or Focus: additional word substitutions](https://github.com/w3c/wcag2ict/pull/778)
-   2025-09-16 [1.4.4 Resize text: updates to resolve issue 772 and incorporate EN note](https://github.com/w3c/wcag2ict/pull/776)
-   2025-10-22 [2.3.1 Three Flashes or Below Threshold: Add 2 new notes](https://github.com/w3c/wcag2ict/pull/794)
-   2025-10-10 [1.2.3 and 1.2.5: Add note describing audio descriptions](https://github.com/w3c/wcag2ict/pull/789)
-   2025-09-26 [1.4.13 Content on Hover or Focus: Update note for "links" word replacement](https://github.com/w3c/wcag2ict/pull/785)
-   2025-09-11 [2.4.4 Link Purpose: Update Note 1 to simplify and remove "outside a user interface control,"](https://github.com/w3c/wcag2ict/pull/777)

-   2025-07-31 [Add note describing device-independent keyboard interface services](https://github.com/w3c/wcag2ict/pull/744)
-   2025-08-19 [1.4.10 Reflow: Remove Note 5 from non-web documents](https://github.com/w3c/wcag2ict/pull/768)
-   2025-08-12 [2.1.1 Keyboard - Reinstate interpretation for non-web documents](https://github.com/w3c/wcag2ict/pull/764)
-   2025-08-12 [1.4.4 Resize text - add note from EN 301 549](https://github.com/w3c/wcag2ict/pull/765)
-   2025-07-31 [Make adjustments to 1.4.1 where platforms provide text scaling for all text, but not to 200% for some text](https://github.com/w3c/wcag2ict/pull/748)
-   2025-04-25 [Update note 1 of 2.1.1 Keyboard guidance to make it more understandable](https://github.com/w3c/wcag2ict/pull/629)
-   2025-07-17 [2.1.1 Keyboard - Updates to notes prompted by the EN 301 549](https://github.com/w3c/wcag2ict/pull/718)
-   2025-07-17 [3.1.2 Language of Parts - Add modified EN 301 549 note](https://github.com/w3c/wcag2ict/pull/714)
-   2025-06-19 [Simplify word replacement in "target" definition to use "content" as word replacement for "page"](https://github.com/w3c/wcag2ict/pull/698)
-   2025-06-12 [More consistency changes for note used in 1.4.2, 2.1.2, 2.2.2, and 2.3.1](https://github.com/w3c/wcag2ict/pull/683)
-   2025-06-21 [Update 4.1.2 to have a word replacement for "user agent"](https://github.com/w3c/wcag2ict/pull/632)
-   2025-06-16 [Adjust note in 1.4.2, 2.1.2, 2.2.2, and 2.3.1 to be consistent verbiage and avoid use of "must"](https://github.com/w3c/wcag2ict/pull/682)
-   2025-04-29 [Add Notes 2 and 3 to key term "content"](https://github.com/w3c/wcag2ict/pull/630)
-   2025-06-20 [SC 2.2.2: Update Note 5 to give full understanding doc name and link and not use "informative" which has a specific meaning in WCAG](https://github.com/w3c/wcag2ict/pull/697)
-   2025-06-27 [1.4.10: Add note for non-web doc from first 2 paragraphs of non-web software note](https://github.com/w3c/wcag2ict/pull/709)
-   2025-07-03 [1.3.1: Add note for non-web documents from the EN 301 549](https://github.com/w3c/wcag2ict/pull/715)

\[etsi-en-301-549\]

[ETSI EN 301 549 V3.2.1 (2021-03): Accessibility requirements for ICT products and services](http://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf). ETSI. March 2021. Published. URL: [http://www.etsi.org/deliver/etsi\_en/301500\_301599/301549/03.02.01\_60/en\_301549v030201p.pdf](http://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf)

\[ISO\_9241-171\]

[Ergonomics of human-system interaction Part 171: Guidance on software accessibility](https://www.iso.org/standard/39080.html). International Standards Organization. 2008. URL: [https://www.iso.org/standard/39080.html](https://www.iso.org/standard/39080.html)

\[ISO/IEC\_13066-1\]

[Information technology - Interoperability with assistive technology (AT) Part 1: Requirements and recommendations for interoperability](https://www.iso.org/standard/53770.html). International Standards Organization. 2011. URL: [https://www.iso.org/standard/53770.html](https://www.iso.org/standard/53770.html)

\[UNDERSTANDING-WCAG22\]

[Understanding Web Content Accessibility Guidelines 2.2](https://www.w3.org/WAI/WCAG22/Understanding/). URL: [https://www.w3.org/WAI/WCAG22/Understanding/](https://www.w3.org/WAI/WCAG22/Understanding/)

\[WCAG20\]

[Web Content Accessibility Guidelines (WCAG) 2.0](https://www.w3.org/TR/WCAG20/). Ben Caldwell; Michael Cooper; Loretta Guarino Reid; Gregg Vanderheiden et al. W3C. 11 December 2008. W3C Recommendation. URL: [https://www.w3.org/TR/WCAG20/](https://www.w3.org/TR/WCAG20/)

\[WCAG21\]

[Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/). Michael Cooper; Andrew Kirkpatrick; Joshue O'Connor; Alastair Campbell. W3C. 6 May 2025. W3C Recommendation. URL: [https://www.w3.org/TR/WCAG21/](https://www.w3.org/TR/WCAG21/)

\[WCAG22\]

[Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). Michael Cooper; Andrew Kirkpatrick; Alastair Campbell; Rachael Bradley Montgomery; Charles Adams. W3C. 12 December 2024. W3C Recommendation. URL: [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/)

\[WCAG22-TECHS\]

[Techniques for WCAG 2.2](https://www.w3.org/WAI/WCAG22/Techniques/). URL: [https://www.w3.org/WAI/WCAG22/Techniques/](https://www.w3.org/WAI/WCAG22/Techniques/)
