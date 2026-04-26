---
created: 2026-04-26T13:13:05 (UTC -05:00)
tags: []
source: https://www.w3.org/TR/wcag-3.0/
author: Rachael Bradley Montgomery (Library of Congress)
---

# W3C Accessibility Guidelines (WCAG) 3.0

> ## Excerpt
> W3C Accessibility Guidelines (WCAG) 3.0 W3C Working Draft 03 March 2026 More details about this document This version: https://www.w3.org/TR/2026/WD-wcag-3.0-20260303/ Latest published version: https:

---
# W3C Accessibility Guidelines (WCAG) 3.0

[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

[W3C Working Draft](https://www.w3.org/standards/types#WD) 03 March 2026

More details about this document

This version:

[https://www.w3.org/TR/2026/WD-wcag-3.0-20260303/](https://www.w3.org/TR/2026/WD-wcag-3.0-20260303/)

Latest published version:

[https://www.w3.org/TR/wcag-3.0/](https://www.w3.org/TR/wcag-3.0/)

Latest editor's draft:

[https://w3c.github.io/wcag3/guidelines/](https://w3c.github.io/wcag3/guidelines/)

History:

[https://www.w3.org/standards/history/wcag-3.0/](https://www.w3.org/standards/history/wcag-3.0/)

[Commit history](https://github.com/w3c/wcag3/commits/)

Editors:

[Alastair Campbell](mailto:acampbell@nomensa.com) (Nomensa)

[Chuck Adams](mailto:charles.adams@oracle.com) (Oracle)

[Kevin White](mailto:kevin@w3.org) (W3C)

[Giacomo Petri](mailto:giacomo.petri@usablenet.com) (UsableNet)

[Julie Rawe](mailto:jrawe@understood.org) (Understood.org)

[Francis Storr](mailto:francis.storr@intel.com) (Intel Corporation)

[Makoto Ueki](mailto:makoto.ueki@gmail.com) (Invited Expert)

[Hidde de Vries](mailto:hidde@hiddedevries.nl) (Logius)

Former editors:

[Jeanne Spellman](mailto:jspellman@spellmanconsulting.com) (TetraLogical)

Michael Cooper, Staff Contact, 2016-2023 (W3C)

Shawn Lauriat, Editor, 2016-2023 (Google, Inc.)

Wilco Fiers, Project Manager, 2021-2023 (Deque Systems, Inc.)

Feedback:

[GitHub w3c/wcag3](https://github.com/w3c/wcag3/) ([pull requests](https://github.com/w3c/wcag3/pulls/), [new issue](https://github.com/w3c/wcag3/issues/new/choose), [open issues](https://github.com/w3c/wcag3/issues/))

[public-agwg-comments@w3.org](mailto:public-agwg-comments@w3.org?subject=%5Bwcag-3.0%5D%20YOUR%20TOPIC%20HERE) with subject line \[wcag-3.0\] _… message topic …_ ([archives](https://lists.w3.org/Archives/Public/public-agwg-comments))

[Copyright](https://www.w3.org/policies/#copyright) © 2021-2026 [World Wide Web Consortium](https://www.w3.org/). W3C<sup>®</sup> [liability](https://www.w3.org/policies/#Legal_Disclaimer), [trademark](https://www.w3.org/policies/#W3C_Trademarks) and [document use](https://www.w3.org/copyright/document-license/ "W3C Document License") rules apply.

___

## Abstract

W3C Accessibility Guidelines (WCAG) 3.0 will provide a wide range of recommendations for making web content more accessible to users with disabilities. Following these guidelines will address many of the needs of users with blindness, low vision and other vision impairments; deafness and hearing loss; limited movement and dexterity; speech disabilities; sensory disorders; cognitive and learning disabilities; and combinations of any of these disabilities. These guidelines address the accessibility of web content on desktops, laptops, tablets, mobile devices, wearable devices, and other Web of Things devices. The guidelines apply to various types of web content, including static, dynamic, interactive, and streaming content; audiovisual media; virtual and augmented reality; and alternative access presentation and control. These guidelines also address related web tools such as user agents (browsers and assistive technologies), content management systems, authoring tools, and testing tools.

Each [guideline](https://www.w3.org/TR/wcag-3.0/#dfn-guideline) in this standard provides information on accessibility practices that address documented [user needs](https://www.w3.org/TR/wcag-3.0/#dfn-user-need) of people with disabilities. Guidelines are supported by multiple [requirements](https://www.w3.org/TR/wcag-3.0/#dfn-requirement) and [assertions](https://www.w3.org/TR/wcag-3.0/#dfn-assertion) to determine whether the need has been met. Guidelines are also supported by technology-specific [methods](https://www.w3.org/TR/wcag-3.0/#dfn-method) to meet each requirement or assertion.

To keep pace with changing technology, this specification is expected to be updated regularly with updates to and new methods, requirements, and guidelines that address new needs as technologies evolve. For entities that make formal claims of [conformance](https://www.w3.org/TR/wcag-3.0/#dfn-conformance) to these guidelines, several levels of conformance are available to address the diverse nature of digital content and the type of testing that is performed.

For an overview of WCAG 3 and links to WCAG technical and educational material, see [WCAG 3 Introduction](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/).

## Status of This Document

_This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C standards and drafts index](https://www.w3.org/TR/)._

This is an update to W3C Accessibility Guidelines (WCAG) 3.0. It includes all requirements that have reached the developing status.

To comment, [file an issue in the wcag3 GitHub repository](https://github.com/w3c/wcag3/issues/new). Create separate GitHub issues for each comment, rather than commenting on multiple topics in a single issue. It is free to create a GitHub account to file issues. If filing issues in GitHub is not feasible, email [public-agwg-comments@w3.org](mailto:public-agwg-comments@w3.org?subject=WCAG%203.0%20public%20comment) ([comment archive](https://lists.w3.org/Archives/Public/public-agwg-comments/)).

In-progress updates to the guidelines can be viewed in the [public Editor's Draft](https://w3c.github.io/wcag3/guidelines/).

This document was published by the [Accessibility Guidelines Working Group](https://www.w3.org/groups/wg/ag) as a Working Draft using the [Recommendation track](https://www.w3.org/policies/process/20250818/#recs-and-notes).

Publication as a Working Draft does not imply endorsement by W3C and its Members.

This is a draft document and may be updated, replaced, or obsoleted by other documents at any time. It is inappropriate to cite this document as other than a work in progress.

This document was produced by a group operating under the [W3C Patent Policy](https://www.w3.org/policies/patent-policy/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/groups/wg/ag/ipr) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent that the individual believes contains [Essential Claim(s)](https://www.w3.org/policies/patent-policy/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/policies/patent-policy/#sec-Disclosure).

This document is governed by the [18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/).

## Table of Contents

1.  [Abstract](https://www.w3.org/TR/wcag-3.0/#abstract)
2.  [Status of This Document](https://www.w3.org/TR/wcag-3.0/#sotd)
3.  [1\. Introduction](https://www.w3.org/TR/wcag-3.0/#introduction)
    1.  [1.1 About this draft](https://www.w3.org/TR/wcag-3.0/#about-this-draft)
        1.  [1.1.1 Draft requirements](https://www.w3.org/TR/wcag-3.0/#draft-requirements)
        2.  [1.1.2 Section status levels](https://www.w3.org/TR/wcag-3.0/#section-status-levels)
    2.  [1.2 About WCAG 3](https://www.w3.org/TR/wcag-3.0/#about-wcag-3)
4.  [2\. Guidelines](https://www.w3.org/TR/wcag-3.0/#guidelines)
    1.  [2.1 Images and media](https://www.w3.org/TR/wcag-3.0/#images-and-media)
        1.  [2.1.1 Image alternatives](https://www.w3.org/TR/wcag-3.0/#image-alternatives)
            1.  [Images detectable](https://www.w3.org/TR/wcag-3.0/#images-detectable)
            2.  [Decorative images hidden](https://www.w3.org/TR/wcag-3.0/#decorative-images-hidden)
            3.  [Image alternatives available](https://www.w3.org/TR/wcag-3.0/#image-alternatives-available)
        2.  [2.1.2 Media alternatives](https://www.w3.org/TR/wcag-3.0/#media-alternatives)
            1.  [Transcripts available](https://www.w3.org/TR/wcag-3.0/#transcripts-available)
            2.  [Media alternatives equivalent](https://www.w3.org/TR/wcag-3.0/#media-alternatives-equivalent)
            3.  [Media alternatives findable](https://www.w3.org/TR/wcag-3.0/#media-alternatives-findable)
            4.  [Speakers identified](https://www.w3.org/TR/wcag-3.0/#speakers-identified)
            5.  [Speaker language identified](https://www.w3.org/TR/wcag-3.0/#speaker-language-identified)
            6.  [Sounds identified](https://www.w3.org/TR/wcag-3.0/#sounds-identified)
            7.  [Visual information identified](https://www.w3.org/TR/wcag-3.0/#visual-information-identified)
            8.  [Sign language available (prerecorded)](https://www.w3.org/TR/wcag-3.0/#sign-language-available-prerecorded)
            9.  [Sign language available (live)](https://www.w3.org/TR/wcag-3.0/#sign-language-available-live)
            10.  [Media alternatives style guide](https://www.w3.org/TR/wcag-3.0/#media-alternatives-style-guide)
            11.  [Accessible video player selected](https://www.w3.org/TR/wcag-3.0/#accessible-video-player-selected)
            12.  [Media alternatives usability testing](https://www.w3.org/TR/wcag-3.0/#media-alternatives-usability-testing)
            13.  [Reviewed by content authors](https://www.w3.org/TR/wcag-3.0/#reviewed-by-content-authors)
        3.  [2.1.3 Non-text alternatives](https://www.w3.org/TR/wcag-3.0/#non-text-alternatives)
            1.  [Non-text content not relied on](https://www.w3.org/TR/wcag-3.0/#non-text-content-not-relied-on)
        4.  [2.1.4 Captions](https://www.w3.org/TR/wcag-3.0/#captions)
            1.  [Captions adjustable](https://www.w3.org/TR/wcag-3.0/#captions-adjustable)
            2.  [Captions available (prerecorded)](https://www.w3.org/TR/wcag-3.0/#captions-available-prerecorded)
            3.  [Captions available (live)](https://www.w3.org/TR/wcag-3.0/#captions-available-live)
            4.  [Captions unobstructed](https://www.w3.org/TR/wcag-3.0/#captions-unobstructed)
            5.  [Captions synchronized](https://www.w3.org/TR/wcag-3.0/#captions-synchronized)
            6.  [Captions centered (immersive)](https://www.w3.org/TR/wcag-3.0/#captions-centered-immersive)
            7.  [Captions controllable](https://www.w3.org/TR/wcag-3.0/#captions-controllable)
            8.  [Direction indicated (immersive)](https://www.w3.org/TR/wcag-3.0/#direction-indicated-immersive)
        5.  [2.1.5 Audio descriptions](https://www.w3.org/TR/wcag-3.0/#audio-descriptions)
            1.  [Audio descriptions available (prerecorded)](https://www.w3.org/TR/wcag-3.0/#audio-descriptions-available-prerecorded)
            2.  [Audio descriptions synchronized](https://www.w3.org/TR/wcag-3.0/#audio-descriptions-synchronized)
            3.  [Audio descriptions available (live)](https://www.w3.org/TR/wcag-3.0/#audio-descriptions-available-live)
            4.  [Extended audio descriptions available](https://www.w3.org/TR/wcag-3.0/#extended-audio-descriptions-available)
            5.  [Audio description language adjustable](https://www.w3.org/TR/wcag-3.0/#audio-description-language-adjustable)
        6.  [2.1.6 Figure captions](https://www.w3.org/TR/wcag-3.0/#figure-captions)
        7.  [2.1.7 Single sense](https://www.w3.org/TR/wcag-3.0/#single-sense)
            1.  [Hue not relied on](https://www.w3.org/TR/wcag-3.0/#hue-not-relied-on)
            2.  [Graphical object contrast sufficient](https://www.w3.org/TR/wcag-3.0/#graphical-object-contrast-sufficient)
            3.  [Visual depth not relied on](https://www.w3.org/TR/wcag-3.0/#visual-depth-not-relied-on)
            4.  [Sound not relied on](https://www.w3.org/TR/wcag-3.0/#sound-not-relied-on)
            5.  [Spatial audio not relied on](https://www.w3.org/TR/wcag-3.0/#spatial-audio-not-relied-on)
    2.  [2.2 Text and wording](https://www.w3.org/TR/wcag-3.0/#text-and-wording)
        1.  [2.2.1 Text appearance](https://www.w3.org/TR/wcag-3.0/#text-appearance)
            1.  [Text size adjustable](https://www.w3.org/TR/wcag-3.0/#text-size-adjustable)
            2.  [Text color adjustable](https://www.w3.org/TR/wcag-3.0/#text-color-adjustable)
            3.  [Text customizations retained](https://www.w3.org/TR/wcag-3.0/#text-customizations-retained)
        2.  [2.2.2 Text-to-speech](https://www.w3.org/TR/wcag-3.0/#text-to-speech)
            1.  [Text detectable](https://www.w3.org/TR/wcag-3.0/#text-detectable)
            2.  [Human language detectable](https://www.w3.org/TR/wcag-3.0/#human-language-detectable)
            3.  [Numerical metadata available](https://www.w3.org/TR/wcag-3.0/#numerical-metadata-available)
        3.  [2.2.3 Clear language](https://www.w3.org/TR/wcag-3.0/#clear-language)
            1.  [Abbreviations explained](https://www.w3.org/TR/wcag-3.0/#abbreviations-explained)
            2.  [Non-literal language explained](https://www.w3.org/TR/wcag-3.0/#non-literal-language-explained)
            3.  [Diacritics available](https://www.w3.org/TR/wcag-3.0/#diacritics-available)
            4.  [No nested clauses](https://www.w3.org/TR/wcag-3.0/#no-nested-clauses)
            5.  [No unnecessary words](https://www.w3.org/TR/wcag-3.0/#no-unnecessary-words)
            6.  [Clear language review](https://www.w3.org/TR/wcag-3.0/#clear-language-review)
            7.  [Visual aids review](https://www.w3.org/TR/wcag-3.0/#visual-aids-review)
    3.  [2.3 Interactive components](https://www.w3.org/TR/wcag-3.0/#interactive-components)
        1.  [2.3.1 Keyboard focus appearance](https://www.w3.org/TR/wcag-3.0/#keyboard-focus-appearance)
            1.  [Default focus indicator used](https://www.w3.org/TR/wcag-3.0/#default-focus-indicator-used)
            2.  [Focus indicator contrast sufficient](https://www.w3.org/TR/wcag-3.0/#focus-indicator-contrast-sufficient)
            3.  [Focus indicator size sufficient](https://www.w3.org/TR/wcag-3.0/#focus-indicator-size-sufficient)
            4.  [Focus indicator style guide](https://www.w3.org/TR/wcag-3.0/#focus-indicator-style-guide)
        2.  [2.3.2 Pointer focus appearance](https://www.w3.org/TR/wcag-3.0/#pointer-focus-appearance)
            1.  [Pointer activation indicated (minimum)](https://www.w3.org/TR/wcag-3.0/#pointer-activation-indicated-minimum)
            2.  [Pointer activation indicated (enhanced)](https://www.w3.org/TR/wcag-3.0/#pointer-activation-indicated-enhanced)
            3.  [Pointer contrast sufficient](https://www.w3.org/TR/wcag-3.0/#pointer-contrast-sufficient)
            4.  [Default pointer used](https://www.w3.org/TR/wcag-3.0/#default-pointer-used)
            5.  [Pointer focus indicated](https://www.w3.org/TR/wcag-3.0/#pointer-focus-indicated)
            6.  [Pointer visible](https://www.w3.org/TR/wcag-3.0/#pointer-visible)
            7.  [Enhanced pointer available](https://www.w3.org/TR/wcag-3.0/#enhanced-pointer-available)
        3.  [2.3.3 Navigating content](https://www.w3.org/TR/wcag-3.0/#navigating-content)
            1.  [Focus relevant](https://www.w3.org/TR/wcag-3.0/#focus-relevant)
            2.  [Focus retained](https://www.w3.org/TR/wcag-3.0/#focus-retained)
            3.  [Focus order meaningful](https://www.w3.org/TR/wcag-3.0/#focus-order-meaningful)
        4.  [2.3.4 Expected behavior](https://www.w3.org/TR/wcag-3.0/#expected-behavior)
            1.  [Consistent interactions](https://www.w3.org/TR/wcag-3.0/#consistent-interactions)
            2.  [Conventional pattern used](https://www.w3.org/TR/wcag-3.0/#conventional-pattern-used)
        5.  [2.3.5 Control information](https://www.w3.org/TR/wcag-3.0/#control-information)
            1.  [Interactive element contrast sufficient](https://www.w3.org/TR/wcag-3.0/#interactive-element-contrast-sufficient)
            2.  [Interactive element names available](https://www.w3.org/TR/wcag-3.0/#interactive-element-names-available)
            3.  [Changes to elements notified](https://www.w3.org/TR/wcag-3.0/#changes-to-elements-notified)
            4.  [Input constraints used](https://www.w3.org/TR/wcag-3.0/#input-constraints-used)
            5.  [Label included in programmatic name](https://www.w3.org/TR/wcag-3.0/#label-included-in-programmatic-name)
            6.  [Roles, values, states, properties available](https://www.w3.org/TR/wcag-3.0/#roles-values-states-properties-available)
    4.  [2.4 Input / operation](https://www.w3.org/TR/wcag-3.0/#input-operation)
        1.  [2.4.1 Keyboard interface input](https://www.w3.org/TR/wcag-3.0/#keyboard-interface-input)
            1.  [Keyboard operable](https://www.w3.org/TR/wcag-3.0/#keyboard-operable)
            2.  [Keyboard accessible](https://www.w3.org/TR/wcag-3.0/#keyboard-accessible)
            3.  [Bidirectional navigation](https://www.w3.org/TR/wcag-3.0/#bidirectional-navigation)
            4.  [Custom keys documented](https://www.w3.org/TR/wcag-3.0/#custom-keys-documented)
            5.  [No keyboard conflicts](https://www.w3.org/TR/wcag-3.0/#no-keyboard-conflicts)
            6.  [Keyboard navigable if responsive](https://www.w3.org/TR/wcag-3.0/#keyboard-navigable-if-responsive)
            7.  [Focus placed](https://www.w3.org/TR/wcag-3.0/#focus-placed)
            8.  [No keyboard traps](https://www.w3.org/TR/wcag-3.0/#no-keyboard-traps)
            9.  [Focus user-controlled](https://www.w3.org/TR/wcag-3.0/#focus-user-controlled)
            10.  [Focus movement relevant](https://www.w3.org/TR/wcag-3.0/#focus-movement-relevant)
        2.  [2.4.2 Physical or cognitive effort when using keyboard](https://www.w3.org/TR/wcag-3.0/#physical-or-cognitive-effort-when-using-keyboard)
            1.  [Navigation keys described](https://www.w3.org/TR/wcag-3.0/#navigation-keys-described)
            2.  [No repetitive links](https://www.w3.org/TR/wcag-3.0/#no-repetitive-links)
            3.  [Keyboard effort comparable](https://www.w3.org/TR/wcag-3.0/#keyboard-effort-comparable)
        3.  [2.4.3 Pointer input](https://www.w3.org/TR/wcag-3.0/#pointer-input)
            1.  [Pointer activation controllable](https://www.w3.org/TR/wcag-3.0/#pointer-activation-controllable)
            2.  [Simple pointer input available](https://www.w3.org/TR/wcag-3.0/#simple-pointer-input-available)
            3.  [Consistent pointer cancellation](https://www.w3.org/TR/wcag-3.0/#consistent-pointer-cancellation)
            4.  [Pointer pressure not relied on](https://www.w3.org/TR/wcag-3.0/#pointer-pressure-not-relied-on)
            5.  [Pointer speed not relied on](https://www.w3.org/TR/wcag-3.0/#pointer-speed-not-relied-on)
        4.  [2.4.4 Speech and voice input](https://www.w3.org/TR/wcag-3.0/#speech-and-voice-input)
            1.  [Speech not relied on](https://www.w3.org/TR/wcag-3.0/#speech-not-relied-on)
            2.  [Real-time text available](https://www.w3.org/TR/wcag-3.0/#real-time-text-available)
            3.  [Generated speech testing](https://www.w3.org/TR/wcag-3.0/#generated-speech-testing)
        5.  [2.4.5 Input operation](https://www.w3.org/TR/wcag-3.0/#input-operation-0)
            1.  [Hover or focus content dismissible](https://www.w3.org/TR/wcag-3.0/#hover-or-focus-content-dismissible)
            2.  [Hover content persistent](https://www.w3.org/TR/wcag-3.0/#hover-content-persistent)
            3.  [Hover or focus content persistent](https://www.w3.org/TR/wcag-3.0/#hover-or-focus-content-persistent)
            4.  [Path-based gesture not relied on](https://www.w3.org/TR/wcag-3.0/#path-based-gesture-not-relied-on)
            5.  [Input method flexible](https://www.w3.org/TR/wcag-3.0/#input-method-flexible)
            6.  [Body movements not relied on](https://www.w3.org/TR/wcag-3.0/#body-movements-not-relied-on)
            7.  [Eye tracking not relied on](https://www.w3.org/TR/wcag-3.0/#eye-tracking-not-relied-on)
            8.  [Pointer accessible](https://www.w3.org/TR/wcag-3.0/#pointer-accessible)
        6.  [2.4.6 Authentication](https://www.w3.org/TR/wcag-3.0/#authentication)
            1.  [Biometrics not relied on](https://www.w3.org/TR/wcag-3.0/#biometrics-not-relied-on)
            2.  [Voice identification not relied on](https://www.w3.org/TR/wcag-3.0/#voice-identification-not-relied-on)
    5.  [2.5 Error handling](https://www.w3.org/TR/wcag-3.0/#error-handling)
        1.  [2.5.1 Correct errors](https://www.w3.org/TR/wcag-3.0/#correct-errors)
            1.  [Error notifications available](https://www.w3.org/TR/wcag-3.0/#error-notifications-available)
            2.  [Error suggestions provided](https://www.w3.org/TR/wcag-3.0/#error-suggestions-provided)
            3.  [Errors indicated in multiple ways](https://www.w3.org/TR/wcag-3.0/#errors-indicated-in-multiple-ways)
            4.  [Error messages persistent](https://www.w3.org/TR/wcag-3.0/#error-messages-persistent)
            5.  [Errors associated](https://www.w3.org/TR/wcag-3.0/#errors-associated)
            6.  [Error messages collocated](https://www.w3.org/TR/wcag-3.0/#error-messages-collocated)
        2.  [2.5.2 Prevent errors](https://www.w3.org/TR/wcag-3.0/#prevent-errors)
            1.  [Errors preventable](https://www.w3.org/TR/wcag-3.0/#errors-preventable)
            2.  [Submission status notified](https://www.w3.org/TR/wcag-3.0/#submission-status-notified)
            3.  [Data entry validated](https://www.w3.org/TR/wcag-3.0/#data-entry-validated)
            4.  [Error prevention review](https://www.w3.org/TR/wcag-3.0/#error-prevention-review)
    6.  [2.6 Animation and movement](https://www.w3.org/TR/wcag-3.0/#animation-and-movement)
        1.  [2.6.1 Avoid physical harm](https://www.w3.org/TR/wcag-3.0/#avoid-physical-harm)
            1.  [No flashing](https://www.w3.org/TR/wcag-3.0/#no-flashing)
            2.  [No flashing (no exceptions)](https://www.w3.org/TR/wcag-3.0/#no-flashing-no-exceptions)
            3.  [No visual motion](https://www.w3.org/TR/wcag-3.0/#no-visual-motion)
            4.  [No visual motion (no exceptions)](https://www.w3.org/TR/wcag-3.0/#no-visual-motion-no-exceptions)
            5.  [Trigger warning available](https://www.w3.org/TR/wcag-3.0/#trigger-warning-available)
            6.  [Haptic stimulation adjustable](https://www.w3.org/TR/wcag-3.0/#haptic-stimulation-adjustable)
            7.  [Audio shifting adjustable](https://www.w3.org/TR/wcag-3.0/#audio-shifting-adjustable)
            8.  [Safe content review](https://www.w3.org/TR/wcag-3.0/#safe-content-review)
    7.  [2.7 Layout](https://www.w3.org/TR/wcag-3.0/#layout)
        1.  [2.7.1 Recognizable layouts](https://www.w3.org/TR/wcag-3.0/#recognizable-layouts)
            1.  [Conventional layout review](https://www.w3.org/TR/wcag-3.0/#conventional-layout-review)
        2.  [2.7.2 User orientation](https://www.w3.org/TR/wcag-3.0/#user-orientation)
            1.  [Page/view title available](https://www.w3.org/TR/wcag-3.0/#page-view-title-available)
            2.  [Location within product review](https://www.w3.org/TR/wcag-3.0/#location-within-product-review)
            3.  [All steps listed](https://www.w3.org/TR/wcag-3.0/#all-steps-listed)
            4.  [Current step indicated](https://www.w3.org/TR/wcag-3.0/#current-step-indicated)
            5.  [Page/view change notified](https://www.w3.org/TR/wcag-3.0/#page-view-change-notified)
            6.  [Return to start supported](https://www.w3.org/TR/wcag-3.0/#return-to-start-supported)
            7.  [Return to start prominent](https://www.w3.org/TR/wcag-3.0/#return-to-start-prominent)
        3.  [2.7.3 Structure](https://www.w3.org/TR/wcag-3.0/#structure)
            1.  [Relationships detectable](https://www.w3.org/TR/wcag-3.0/#relationships-detectable)
            2.  [Blocks of content available (minimum)](https://www.w3.org/TR/wcag-3.0/#blocks-of-content-available-minimum)
            3.  [Sections labeled](https://www.w3.org/TR/wcag-3.0/#sections-labeled)
            4.  [Heading structure available](https://www.w3.org/TR/wcag-3.0/#heading-structure-available)
            5.  [Order detectable](https://www.w3.org/TR/wcag-3.0/#order-detectable)
            6.  [Blocks of content available (enhanced)](https://www.w3.org/TR/wcag-3.0/#blocks-of-content-available-enhanced)
            7.  [Clear structure review](https://www.w3.org/TR/wcag-3.0/#clear-structure-review)
            8.  [Key information usability testing](https://www.w3.org/TR/wcag-3.0/#key-information-usability-testing)
        4.  [2.7.4 No obstruction](https://www.w3.org/TR/wcag-3.0/#no-obstruction)
            1.  [Overlay content dismissible](https://www.w3.org/TR/wcag-3.0/#overlay-content-dismissible)
    8.  [2.8 Consistency across views](https://www.w3.org/TR/wcag-3.0/#consistency-across-views)
        1.  [2.8.1 Consistency](https://www.w3.org/TR/wcag-3.0/#consistency)
            1.  [Consistent structural order](https://www.w3.org/TR/wcag-3.0/#consistent-structural-order)
            2.  [Consistent navigation order](https://www.w3.org/TR/wcag-3.0/#consistent-navigation-order)
            3.  [Consistent navigation labels](https://www.w3.org/TR/wcag-3.0/#consistent-navigation-labels)
    9.  [2.9 Process and task completion](https://www.w3.org/TR/wcag-3.0/#process-and-task-completion)
        1.  [2.9.1 Avoid exclusionary cognitive tasks](https://www.w3.org/TR/wcag-3.0/#avoid-exclusionary-cognitive-tasks)
            1.  [Automated entry allowed](https://www.w3.org/TR/wcag-3.0/#automated-entry-allowed)
            2.  [Cognitive test alternatives available](https://www.w3.org/TR/wcag-3.0/#cognitive-test-alternatives-available)
        2.  [2.9.2 Adequate time](https://www.w3.org/TR/wcag-3.0/#adequate-time)
            1.  [Timeout adjustable](https://www.w3.org/TR/wcag-3.0/#timeout-adjustable)
            2.  [No time limits](https://www.w3.org/TR/wcag-3.0/#no-time-limits)
            3.  [No unnecessary time limits](https://www.w3.org/TR/wcag-3.0/#no-unnecessary-time-limits)
            4.  [Time limits conveyed](https://www.w3.org/TR/wcag-3.0/#time-limits-conveyed)
        3.  [2.9.3 Avoid deception](https://www.w3.org/TR/wcag-3.0/#avoid-deception)
            1.  [Preselections visible](https://www.w3.org/TR/wcag-3.0/#preselections-visible)
            2.  [Deceptive practices usability testing](https://www.w3.org/TR/wcag-3.0/#deceptive-practices-usability-testing)
            3.  [Deceptive messaging expert review](https://www.w3.org/TR/wcag-3.0/#deceptive-messaging-expert-review)
        4.  [2.9.4 Retain information](https://www.w3.org/TR/wcag-3.0/#retain-information)
            1.  [Going back supported](https://www.w3.org/TR/wcag-3.0/#going-back-supported)
            2.  [No redundant entry](https://www.w3.org/TR/wcag-3.0/#no-redundant-entry)
            3.  [Progress saved](https://www.w3.org/TR/wcag-3.0/#progress-saved)
        5.  [2.9.5 Complete tasks](https://www.w3.org/TR/wcag-3.0/#complete-tasks)
            1.  [Required action available](https://www.w3.org/TR/wcag-3.0/#required-action-available)
            2.  [Information requirements available at start](https://www.w3.org/TR/wcag-3.0/#information-requirements-available-at-start)
            3.  [Process instructions available](https://www.w3.org/TR/wcag-3.0/#process-instructions-available)
        6.  [2.9.6 Unnecessary steps](https://www.w3.org/TR/wcag-3.0/#unnecessary-steps)
            1.  [Usability testing for unnecessary steps](https://www.w3.org/TR/wcag-3.0/#usability-testing-for-unnecessary-steps)
    10.  [2.10 Policy and protection](https://www.w3.org/TR/wcag-3.0/#policy-and-protection)
        1.  [2.10.1 Risk](https://www.w3.org/TR/wcag-3.0/#risk)
            1.  [Consequences of choices explained](https://www.w3.org/TR/wcag-3.0/#consequences-of-choices-explained)
            2.  [Consequences explained before agreement](https://www.w3.org/TR/wcag-3.0/#consequences-explained-before-agreement)
            3.  [Diverse disabilities considered](https://www.w3.org/TR/wcag-3.0/#diverse-disabilities-considered)
            4.  [Algorithm inclusivity review](https://www.w3.org/TR/wcag-3.0/#algorithm-inclusivity-review)
        2.  [2.10.2 Algorithms](https://www.w3.org/TR/wcag-3.0/#algorithms)
            1.  [Inclusive data set](https://www.w3.org/TR/wcag-3.0/#inclusive-data-set)
            2.  [No harm from algorithms](https://www.w3.org/TR/wcag-3.0/#no-harm-from-algorithms)
    11.  [2.11 Help and feedback](https://www.w3.org/TR/wcag-3.0/#help-and-feedback)
        1.  [2.11.1 Help available](https://www.w3.org/TR/wcag-3.0/#help-available)
            1.  [Consistent help available](https://www.w3.org/TR/wcag-3.0/#consistent-help-available)
            2.  [Contextual help available](https://www.w3.org/TR/wcag-3.0/#contextual-help-available)
            3.  [Disabled controls explained](https://www.w3.org/TR/wcag-3.0/#disabled-controls-explained)
            4.  [Sensory characteristics not relied on](https://www.w3.org/TR/wcag-3.0/#sensory-characteristics-not-relied-on)
            5.  [Supported decision-making review](https://www.w3.org/TR/wcag-3.0/#supported-decision-making-review)
            6.  [Help usability testing](https://www.w3.org/TR/wcag-3.0/#help-usability-testing)
        2.  [2.11.2 Feedback](https://www.w3.org/TR/wcag-3.0/#feedback)
            1.  [Feedback mechanism available](https://www.w3.org/TR/wcag-3.0/#feedback-mechanism-available)
    12.  [2.12 User control](https://www.w3.org/TR/wcag-3.0/#user-control)
        1.  [2.12.1 Assistive technology control](https://www.w3.org/TR/wcag-3.0/#assistive-technology-control)
            1.  [Assistive technology supported](https://www.w3.org/TR/wcag-3.0/#assistive-technology-supported)
            2.  [User settings supported](https://www.w3.org/TR/wcag-3.0/#user-settings-supported)
            3.  [Virtual cursor supported](https://www.w3.org/TR/wcag-3.0/#virtual-cursor-supported)
            4.  [Notifications adjustable](https://www.w3.org/TR/wcag-3.0/#notifications-adjustable)
        2.  [2.12.2 Control text](https://www.w3.org/TR/wcag-3.0/#control-text)
        3.  [2.12.3 Adjustable viewport](https://www.w3.org/TR/wcag-3.0/#adjustable-viewport)
            1.  [Orientation supported (minimum)](https://www.w3.org/TR/wcag-3.0/#orientation-supported-minimum)
            2.  [Orientation supported (enhanced)](https://www.w3.org/TR/wcag-3.0/#orientation-supported-enhanced)
            3.  [Text reflow supported](https://www.w3.org/TR/wcag-3.0/#text-reflow-supported)
            4.  [Layout reflow supported](https://www.w3.org/TR/wcag-3.0/#layout-reflow-supported)
        4.  [2.12.4 Media control](https://www.w3.org/TR/wcag-3.0/#media-control)
            1.  [Page/view audio adjustable](https://www.w3.org/TR/wcag-3.0/#page-view-audio-adjustable)
            2.  [Media alternatives searchable](https://www.w3.org/TR/wcag-3.0/#media-alternatives-searchable)
            3.  [Media alternatives controllable](https://www.w3.org/TR/wcag-3.0/#media-alternatives-controllable)
        5.  [2.12.5 Content changes](https://www.w3.org/TR/wcag-3.0/#content-changes)
            1.  [Change of content notified](https://www.w3.org/TR/wcag-3.0/#change-of-content-notified)
            2.  [Change of focus notified](https://www.w3.org/TR/wcag-3.0/#change-of-focus-notified)
            3.  [Change of user agent notified](https://www.w3.org/TR/wcag-3.0/#change-of-user-agent-notified)
5.  [3\. Conformance](https://www.w3.org/TR/wcag-3.0/#conformance)
    1.  [3.1 Interpreting normative provisions](https://www.w3.org/TR/wcag-3.0/#interpreting-normative-provisions)
        1.  [3.1.1 Types of provision](https://www.w3.org/TR/wcag-3.0/#types-of-provision)
        2.  [3.1.2 Best practices](https://www.w3.org/TR/wcag-3.0/#best-practices)
    2.  [3.2 Conformance requirements](https://www.w3.org/TR/wcag-3.0/#conformance-requirements)
        1.  [3.2.1 Conformance level](https://www.w3.org/TR/wcag-3.0/#conformance-level)
        2.  [3.2.2 Accessibility supported](https://www.w3.org/TR/wcag-3.0/#accessibility-supported)
            1.  [3.2.2.1 Accessibility support set](https://www.w3.org/TR/wcag-3.0/#accessibility-support-set)
        3.  [3.2.3 Defined conformance scope](https://www.w3.org/TR/wcag-3.0/#defined-conformance-scope)
    3.  [3.3 Functional performance statements (expanded)](https://www.w3.org/TR/wcag-3.0/#function-performance-statements)
6.  [4\. Glossary](https://www.w3.org/TR/wcag-3.0/#glossary)
7.  [A. Privacy Considerations](https://www.w3.org/TR/wcag-3.0/#privacy-considerations)
8.  [B. Security Considerations](https://www.w3.org/TR/wcag-3.0/#security-considerations)
9.  [C. Change log](https://www.w3.org/TR/wcag-3.0/#change-log)
10.  [D. Acknowledgements](https://www.w3.org/TR/wcag-3.0/#acknowledgements)
    1.  [D.1 Contributors to the development of this document](https://www.w3.org/TR/wcag-3.0/#contributors-to-the-development-of-this-document)
    2.  [D.2 Previous contributors to the development of this document](https://www.w3.org/TR/wcag-3.0/#previous-contributors-to-the-development-of-this-document)
    3.  [D.3 Research Partners](https://www.w3.org/TR/wcag-3.0/#research-partners)
    4.  [D.4 Enabling funders](https://www.w3.org/TR/wcag-3.0/#enabling-funders)
11.  [E. References](https://www.w3.org/TR/wcag-3.0/#references)
    1.  [E.1 Normative references](https://www.w3.org/TR/wcag-3.0/#normative-references)
    2.  [E.2 Informative references](https://www.w3.org/TR/wcag-3.0/#informative-references)

## 1\. Introduction

_This section (with its subsections) provides advice only and does not specify guidelines, meaning it is [informative](https://www.w3.org/TR/wcag-3.0/#dfn-informative) or non-normative._

Plain language summary of Introduction

-   W3C Accessibility Guidelines (WCAG) 3.0 shows ways to make web content and apps usable by people with disabilities. WCAG 3 is a newer standard than the Web Content Accessibility Guidelines (WCAG) 2.
-   WCAG 3 does not replace WCAG 2. WCAG 2 is used around the world and will still be required by different countries for a long time to come.
-   Meeting WCAG 2 at AA level means you will be close to meeting WCAG 3, but there may be differences.
-   This draft only includes requirements that have reached the developing status. This means that we have a general agreement on the topic but not all the details are worked out.
-   We would like feedback on this draft. You can raise a [GitHub issue](https://github.com/w3c/wcag3/issues) or email [public-agwg-comments@w3.org](mailto:public-agwg-comments@w3.org?subject=WCAG%203.0%20public%20comment).

End of summary for Introduction

### 1.1 About this draft

This draft includes an updated list of the potential guidelines, requirements, and assertions that have progressed to [Developing status](https://www.w3.org/TR/wcag-3.0/#section-status-levels). While this draft has moved closer towards completion, it still has several years of work. Details will change and we encourage comments based on the questions below.

Requirements and assertions at the Exploratory status are not included in this Working Draft. If you would like to see the complete list, please review the [Editor's Draft](https://w3c.github.io/wcag3/guidelines/).

Please consider the following questions when reviewing this draft:

-   Are there user needs which are not covered?
-   The conformance model has been updated, there are several questions in the [conformance section](https://www.w3.org/TR/wcag-3.0/#conformance)
-   Is the "applies when" and "except when" format for requirements understandable and useful?
-   Does the increased granularity of the requirements help understanding and application or would consolidating requirements be a better approach?

To provide feedback, please open a new issue in the [WCAG 3 GitHub repository](https://github.com/w3c/wcag3/issues). Create a separate GitHub issue for each topic, rather than commenting on multiple topics in a single issue.

If it's not feasible for you to use GitHub, email your comments to [public-agwg-comments@w3.org](mailto:public-agwg-comments@w3.org?subject=WCAG%203.0%20public%20comment) ([comment archive](https://lists.w3.org/Archives/Public/public-agwg-comments/)). Please put your comments in the body of the message, not as an attachment.

#### 1.1.1 Draft requirements

The list of requirements is longer than the list of success criteria in WCAG 2. This is because:

-   the intent at this stage is to be as inclusive as possible of potential requirements, and
-   WCAG 3 requirements are more granular than WCAG 2 success criteria.

The final set of requirements in WCAG 3 will be different from what is in this draft. Requirements are likely to be added, combined, and removed. We also expect changes to the text of the requirements. Not all of the requirements will be used to meet the base level of conformance.

#### 1.1.2 Section status levels

As part of the WCAG 3 drafting process, each [normative](https://www.w3.org/TR/wcag-3.0/#dfn-normative) section of this document is given a status. This status is used to indicate how far along in the development this section is, how ready it is for experimental adoption, and what kind of feedback the Accessibility Guidelines Working Group is looking for.

-   **Placeholder**: This content is temporary. It showcases the type of content to expect here. All of this is expected to be replaced. No feedback is needed on placeholder content.
-   **Exploratory**: This content is not refined; details and definitions may be missing. The working group is exploring what direction to take with this section. Feedback should be about the proposed direction.
-   **Developing**: This content has been roughly agreed on in terms of what is needed for this section, although not all high-level concerns have been settled. Details have been added, but are yet to be worked out. Feedback should be focused on ensuring the section is usable and reasonable, in a broad sense.
-   **Refining**: This content is ready for wide public review and experimental adoption. The working group has reached consensus on this section. Feedback should be focused on the feasibility of implementation.
-   **Mature**: This content is believed by the working group to be ready for recommendation. Feedback on this section should be focused on edge-case scenarios that the working group may not have anticipated.

### 1.2 About WCAG 3

This specification presents a new model and guidelines to make web content and applications accessible to people with disabilities. W3C Accessibility Guidelines (WCAG) 3.0 supports a wide set of user needs, uses new approaches to testing, and allows frequent maintenance of guidelines and related content to keep pace with accelerating technology changes. WCAG 3 supports this evolution by focusing on the [functional needs](https://www.w3.org/TR/wcag-3.0/#dfn-functional-need) of users. These needs are then supported by guidelines that are written as outcome statements, requirements, assertions, and technology-specific methods to meet those needs.

WCAG 3 is a successor to [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) \[[WCAG22](https://www.w3.org/TR/wcag-3.0/#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")\] and previous versions, but does not [deprecate](https://www.w3.org/TR/wcag-3.0/#dfn-deprecate) WCAG 2. It will also incorporate some content from and partially extend [User Agent Accessibility Guidelines 2.0](https://www.w3.org/TR/UAAG20/) \[[UAAG20](https://www.w3.org/TR/wcag-3.0/#bib-uaag20 "User Agent Accessibility Guidelines (UAAG) 2.0")\] and [Authoring Tool Accessibility Guidelines 2.0](https://www.w3.org/TR/ATAG20/) \[[ATAG20](https://www.w3.org/TR/wcag-3.0/#bib-atag20 "Authoring Tool Accessibility Guidelines (ATAG) 2.0")\]. These earlier versions provided a flexible model that kept them relevant for over 15 years. However, changing technology and changing needs of people with disabilities have led to the need for a new model to address content accessibility more comprehensively and flexibly.

There are many differences between WCAG 2 and WCAG 3. The WCAG 3 guidelines address the accessibility of web content on desktops, laptops, tablets, mobile devices, wearable devices, and other Web of Things devices. The guidelines apply to various types of web content, including static, dynamic, interactive, and streaming content; visual and auditory media; virtual and augmented reality; and alternative access presentation and control methods. These guidelines also address related web tools such as user agents (browsers and assistive technologies), content management systems, authoring tools, and testing tools.

Each [guideline](https://www.w3.org/TR/wcag-3.0/#dfn-guideline) in this standard provides information on accessibility practices that address documented [user needs](https://www.w3.org/TR/wcag-3.0/#dfn-user-need) of people with disabilities. Guidelines are supported by multiple [requirements](https://www.w3.org/TR/wcag-3.0/#dfn-requirement) to determine whether the need has been met. Guidelines are also supported by technology-specific [methods](https://www.w3.org/TR/wcag-3.0/#dfn-method) to meet each requirement.

Content that conforms to WCAG 2.2 Level A and Level AA is expected to meet most of the minimum conformance level of this new standard but, since WCAG 3 includes additional tests and different scoring mechanics, additional work will be needed to reach full conformance. Since the new standard will use a different conformance model, the Accessibility Guidelines Working Group expects that some organizations may wish to continue using WCAG 2, while others may wish to migrate to the new standard. For those that wish to migrate to WCAG 3, the Working Group will provide transition support materials, which may use mapping and other approaches to facilitate migration.

## 2\. GuidelinesDeveloping

_This section (with its subsections) provides requirements which must be followed to conform to the specification, meaning it is [normative](https://www.w3.org/TR/wcag-3.0/#dfn-normative)._

Plain language summary of Guidelines

The following guidelines are being considered for WCAG 3. They are currently a list of topics which we expect to explore more thoroughly in future drafts. The list includes current WCAG 2 guidance and additional requirements. The list will change in future drafts.

Unless otherwise stated, requirements assume the content described is provided both visually and [programmatically](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable).

End of summary for Guidelines

Editor's note

The individuals and organizations that use WCAG vary widely and include web designers and developers, policy makers, purchasing agents, teachers, and students. To meet the varying needs of this audience, several layers of guidance will be provided including guidelines written as outcome statements, requirements that can be tested, assertions, a rich collection of methods, resource links, and code samples.

**The following list is an initial set of potential guidelines and requirements that the Working Group will be exploring. The goal is to guide the next phase of work. They should be considered drafts and should not be considered as final content of WCAG 3.0**.

Ordinarily, exploratory content includes editor's notes listing concerns and questions for each item. Because this Guidelines section is very early in the process of working on WCAG 3, this editor's note covers most of the content in this section. Unless otherwise noted, all items in the list are exploratory at this point. It is a list of all possible topics for consideration. Not all items listed will be included in the final version of WCAG 3.0.

The guidelines and requirements listed below came from analysis of user needs that the Working Group has been studying, examining, and researching. They have not been refined and do not include essential exceptions or methods. Some requirements may be best addressed by authoring tools or at the platform level. Many requirements need additional work to better define the scope and to ensure they apply correctly to multiple languages, cultures, and writing systems. We will address these questions as we further explore each requirement.

**Additional Research**

One goal of publishing this list is to identify gaps in current research and request assistance filling those gaps.

Editor's notes indicate the requirements within this list where the Working Group has not found enough research to fully validate the guidance and create methods to support it or additional work is needed to evaluate existing research. If you know of existing research or if you are interested in conducting research in this area, please file a [GitHub issue](https://github.com/w3c/wcag3/issues) or send email to [public-agwg-comments@w3.org](mailto:public-agwg-comments@w3.org?subject=WCAG%203.0%20public%20comment) ([comment archive](https://lists.w3.org/Archives/Public/public-agwg-comments/)).

### 2.1 Images and mediaDeveloping

#### Guideline 2.1.1 Image alternatives

Users have equivalent alternatives for images.

##### Core requirement: Images detectableDeveloping

Non-[decorative](https://www.w3.org/TR/wcag-3.0/#dfn-decorative) images are detectable.

**Applies when**

-   content includes non-[decorative](https://www.w3.org/TR/wcag-3.0/#dfn-decorative) images.

Tests

_This section is non-normative._

**Procedure**

For each non-decorative image:

1.  Check the code to see if it has been marked up in a way that makes it detectable; or
2.  For technologies where the code cannot be checked, use a screen reader to test that the image is detectable.

**Expected results**

-   #1 or #2 is true.

##### Core requirement: Decorative images hiddenDeveloping

[Decorative](https://www.w3.org/TR/wcag-3.0/#dfn-decorative) images are [programmatically](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable) hidden.

Tests

_This section is non-normative._

_(General) No accessible name_

**Procedure**

1.  Check for any images that add no information to the content.
2.  Check that the image has no accessible name.

**Expected results**

-   #2 is true.

_(HTML) Using an empty `alt` attribute for an `image` element_

**Procedure**

For any image that adds no information to the content:

1.  Check that `title`, `aria-label`, `aria-labelledby` etc. is either absent or empty.
2.  Check that an `alt` attribute is present and empty.

**Expected results**

-   #1 is true.
-   #2 is true.

##### Core requirement: Image alternatives availableDeveloping

[Equivalent](https://www.w3.org/TR/wcag-3.0/#dfn-equivalent) [text alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-text-alternative) are [available](https://www.w3.org/TR/wcag-3.0/#dfn-available) for images that convey [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

Tests

_This section is non-normative._

Provide a text alternative for the image in a way that conveys the equivalent meaning or content that’s displayed visually.

_(General) Equivalent text alternative_

**Procedure**

For each non-decorative image:

1.  Remove, hide, or mask the image.
2.  Replace it with the text alternative.
3.  Check that the meaningful content in the image is described by the text alternative.
4.  If the image includes words that are important to understanding the content, check that those words are included in the text alternative.

**Expected results**

-   #3 is true.
-   #4 is also true, if the image includes words that are important to understanding the content.

#### Guideline 2.1.2 Media alternatives

Users have equivalent alternatives for [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) and [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

##### Core requirement: Transcripts availableDeveloping

[Transcripts](https://www.w3.org/TR/wcag-3.0/#dfn-transcript) are [available](https://www.w3.org/TR/wcag-3.0/#dfn-available) for all [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) and [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

**Except when**

-   The audio or video content is an alternative for text and clearly labelled as such.
-   It is a background video with no spoken content.

Tests

_This section is non-normative._

_(General) Transcript is available_

**Procedure**

For each instance of audio or video:

1.  Check that a transcript is available.

**Expected results**

-   #1 is true.

##### Core requirement: Media alternatives equivalentDeveloping

[Equivalent](https://www.w3.org/TR/wcag-3.0/#dfn-equivalent) [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative) are [available](https://www.w3.org/TR/wcag-3.0/#dfn-available) for [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) and [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) content.

**Except when**

-   It is a background video with no spoken content.

Tests

_This section is non-normative._

_Media alternative is equivalent_

**Procedure**

For each instance of audio or video content:

1.  Check that a media alternative is available for that content.
2.  Check that the content of the media alternative is equivalent to the meaningful information in the media content.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: Media alternatives findableDeveloping

A [mechanism](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) is [available](https://www.w3.org/TR/wcag-3.0/#dfn-available) within the page/view to access the [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative) for audio and video.

**Except when**

-   It is a decorative audio or video.

Tests

_This section is non-normative._

_Link to text description of audio or video content_

**Procedure**

For each instance of audio or video:

1.  Check that a text description or link to a text description is provided for each audio or video.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Speakers identifiedDeveloping

Speakers are identified understandably within all [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative).

**Except when**

-   The speaker has a hidden identity as part of narrative structure.
-   Identity is identifiable within the context of use.

**Applies when**

-   There are multiple speakers in the video.

Tests

_This section is non-normative._

_Consistent speaker name in transcript_

**Procedure**

For each media alternative:

1.  Check that each speaker in the audio or video is consistently identified.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Speaker language identifiedDeveloping

When more than one language is spoken in [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content), the language spoken by each speaker is identified in all [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative).

**Except when**

-   Words are used incidentally.

Tests

_This section is non-normative._

_Language identified in transcripts_

**Procedure**

For each transcript that includes multiple languages:

1.  Check that part(s) using a language different from the original language is programmatically determined in the media alternatives.

**Expected results**

-   #2 is true.

##### Core requirement: Sounds identifiedDeveloping

Sounds needed to understand the media are identified or described in [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) and [transcripts](https://www.w3.org/TR/wcag-3.0/#dfn-transcript).

Editor's note

This includes sound effects and other non-spoken [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

**Except when**

-   it is a decorative video.

**Applies when**

-   there is sound.

Tests

_This section is non-normative._

_Meaningful sounds in captions_

**Procedure**

For all audio content:

1.  Identify meaningful non-verbal audio (sounds).
2.  Check that captions include a description of the meaningful non-verbal audio.

**Expected results**

-   #2 is true.

##### Core requirement: Visual information identifiedDeveloping

Visual information needed to understand the media is described in the [transcript](https://www.w3.org/TR/wcag-3.0/#dfn-transcript) and [audio description](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description).

Editor's note

-   This includes actions, charts or [informative](https://www.w3.org/TR/wcag-3.0/#dfn-informative) visuals, scene changes, and on-screen [text](https://www.w3.org/TR/wcag-3.0/#dfn-text),

Tests

_This section is non-normative._

_Meaningful visual information in transcripts and audio descriptions_

**Procedure**

For each transcript:

1.  Check that the transcript includes a description of any visual information needed to understand the content of the audio or video.
2.  Check that the audio description includes a description of any visual information needed to understand the content of the audio or video.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Sign language available (prerecorded)Developing

[Sign language interpretation](https://www.w3.org/TR/wcag-3.0/#dfn-sign-language-interpretation) is provided for all [prerecorded](https://www.w3.org/TR/wcag-3.0/#dfn-prerecorded) [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) content in the primary sign language of the intended audience or region.

**Except when**

-   It is a decorative background sound.

Tests

_This section is non-normative._

_Sign language for audio only_

**Procedure**

For each instance of prerecorded audio content:

1.  Check that a sign language translation is available.
2.  Check that the sign language translation conveys all the auditory information needed to understand the full context and meaning in the pre-recorded audio content.

**Expected results**

-   #1 and #2 are true.

##### Assertion: Sign language available (live)Developing

\[Title, role, or organization\] asserts that:

-   We provide [Sign language interpretation](https://www.w3.org/TR/wcag-3.0/#dfn-sign-language-interpretation) for all [live](https://www.w3.org/TR/wcag-3.0/#dfn-live) [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) content in the primary sign language of the intended audience or region.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of assertion (if different from the date of the conformance claim).
-   Example recording of a signed live event.

Recommended internal documentation (Informative):

-   Procurement procedure for sign language interpreters.

##### Assertion: Media alternatives style guideDeveloping

\[Title, role, or organization\] asserts that:

-   Our organization has a style guide that includes guidance on [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative) and a policy and/or processes that the style guide must be followed

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the style guide was published.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Summary of the needs of users involved.
-   Identified issues and details of solutions applied.
-   Section labels relevant to image alternatives, or
-   Copy or snapshot of the style guide

##### Assertion: Accessible video player selectedDeveloping

\[Title, role, or organization\] asserts that:

-   We provide a [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) player that supports appropriate [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative). The video player includes the following features \[list all that apply\]:
    -   Supports closed [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) in a standard caption format;
    -   Turning captions on and off;
    -   Turning [audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) on and off;
    -   Adjusting caption styles, including but not limited to: font size, font weight, font style, font color, background color, background transparency, and placement;
    -   Changing the location of captions; and
    -   Changing the language of the audio descriptions.

**Applies when**

-   a video is used that does not play in standard browsers.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of assertion (if different from the date of the conformance claim).
-   Feature included from the list

Recommended internal documentation (Informative):

-   Video player documentation detailing functional support for media alternatives.

##### Assertion: Media alternatives usability testingDeveloping

\[Title, role, or organization\] asserts that:

-   We have conducted usability testing with users who need [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative), and changes were made to fix or mitigate the issues found.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the usability testing was conducted.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Scope
-   Types of disabilities each user had
-   Number of users (for each type of disability)
-   Date of testing
-   Identified issues and details of solutions applied.

##### Assertion: Reviewed by content authorsDeveloping

\[Title, role, or organization\] asserts that:

-   We have reviewed the [media alternatives](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative).

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of the review
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Role of the creator
-   Number of creators (for each Role)
-   Date (Period) of review
-   Examples of fixed issues based on the review

#### Guideline 2.1.3 Non-text alternatives

Users have alternatives available for non-[text](https://www.w3.org/TR/wcag-3.0/#dfn-text), non-image [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that conveys context or meaning.

##### Core requirement: Non-text content not relied onDeveloping

All [non-text content](https://www.w3.org/TR/wcag-3.0/#dfn-non-text-content) that is not decorative includes a programmatically determinable equivalent text alternatives.

Tests

_This section is non-normative._

_HTML alternative text for images_

**Procedure**

1.  Examine the source code of the HTML document to identify all non-decorative `img` elements.
2.  Each img element has an `alt` attribute.
3.  The `alt` attribute provides a text alternative which conveys meaning or content that is displayed visually.
4.  If the image includes words that are important to understanding the content, the words are included in the text alternative.

**Expected results**

-   #2, #3 and #4 are true.

_(Mobile) Videos include accessible name_

**Procedure**

For each instance of non-text content:

1.  Using native mobile screen reader to review all videos in the app.
2.  When videos are navigated to an accessible name is read out.
3.  The accessible name includes the title of the video.

**Expected results**

-   #2 and #3 are true.

#### Guideline 2.1.4 Captions

Users have [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) for the [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

##### Supplemental requirement: Captions adjustableDeveloping

The appearance of [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions), including associated visual indicators, is adaptable including font size, font weight, font style, font color, background color, background transparency, and placement.

Tests

_This section is non-normative._

**Procedure**

For each caption:

1.  Check that the appearance of captions and associated visual indicators is adaptable including font size, font weight, font style, font color, background color, background transparency, and placement

**Expected results**

-   #1 is true.

##### Core requirement: Captions available (prerecorded)Developing

[Captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) are available for all prerecorded [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

**Except when**

-   The audio content is an alternative for text and clearly labelled as such.

Tests

_This section is non-normative._

**Procedure**

For each pre-recorded media asset:

1.  If the captions format is closed captions:
    -   Turn on the closed caption feature of the media player
    -   View the synchronized media content
    -   Check that captions (of all dialogue and important sounds) are visible and in the human language of the video
2.  If the captions format is open captions:
    -   Check that captions (of all dialogue and important sounds) are visible and in the human language of the video

**Expected results**

-   #1 or #2 is true.

##### Core requirement: Captions available (live)Developing

[Captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) are available for all live [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

Tests

_This section is non-normative._

**Procedure**

For all live audio content:

1.  Check that captions are provided

**Expected results**

-   #1 is true.

##### Supplemental requirement: Captions unobstructedDeveloping

[Captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) are placed on the screen so that they do not hide visual information needed to understand the [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

Tests

_This section is non-normative._

**Procedure**

For each caption:

1.  Check if caption doesn’t hide visual information needed to understand the video content

**Expected results**

-   #1 is true.

##### Core requirement: Captions synchronizedDeveloping

[Captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) are synchronized with the [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) of [synchronized media](https://www.w3.org/TR/wcag-3.0/#dfn-synchronized-media).

Tests

_This section is non-normative._

**Procedure**

For each caption:

1.  Check if it is in sync with video content

**Expected results**

-   #1 is true.

##### Core requirement: Captions centered (immersive)Developing

In 360-degree digital environments, [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) remain directly in front of the user.

**Applies when**

-   the position of the captions is controlled by the user.

Tests

_This section is non-normative._

**Procedure**

For each caption in 360-degree environments:

1.  Check that captions remain directly in front of the user.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Captions controllableDeveloping

A [mechanism](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) is available to turn [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) on and off.

**Except when**

-   Captions are hard coded into the video content.

Tests

_This section is non-normative._

**Procedure**

For each caption:

1.  Check that content with captions provides a mechanism to turn on and off the captions. **Expected results**

-   #1 is true.

##### Core requirement: Direction indicated (immersive)Developing

In 360-degree digital environments, the direction of a sound or speech is indicated when [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) is heard from outside the current [view](https://www.w3.org/TR/wcag-3.0/#dfn-view).

Tests

_This section is non-normative._

**Procedure**

For each instance of audio that is heard from outside the current view in a 360-degree digital environment:

1.  Check that the captions indicate the direction of a sound or speech.

**Expected results**

-   #1 is true.

#### Guideline 2.1.5 Audio descriptions

Users have [audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) for [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

##### Core requirement: Audio descriptions available (prerecorded)Developing

[Audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) are available in prerecorded [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) for visual [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) needed to understand the media.

Editor's note

-   WCAG 3 needs to specify how to handle video content with [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) that does not include gaps to insert audio descriptions. Two possible solutions are providing an exception that allows the [content author(s)](https://www.w3.org/TR/wcag-3.0/#dfn-content-author) to use [descriptive transcripts](https://www.w3.org/TR/wcag-3.0/#dfn-descriptive-transcript) instead or requiring content authors to provide an [extended audio description](https://www.w3.org/TR/wcag-3.0/#dfn-extended-audio-description).

**Except when**

-   the video content is an alternative for text and clearly labelled as such.

Tests

_This section is non-normative._

**Procedure**

For prerecorded video:

1.  Check that audio description is available for visual content needed to understand the media

**Expected results**

-   #1 is true.

##### Core requirement: Audio descriptions synchronizedDeveloping

[Audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) are synchronized with [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) without overlapping dialogue and meaningful [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) content.

**Except when**

-   There are no audio descriptions.

Tests

_This section is non-normative._

**Procedure**

For synchronized media with audio description:

1.  Check that audio description is in sync with video content in synchronized media.
2.  Check that audio description doesn’t overlap with dialogue and meaningful audio content.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Audio descriptions available (live)Developing

[Audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) are available in live [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) for visual [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) needed to understand the media.

Tests

_This section is non-normative._

**Procedure**

For each live media broadcast:

1.  Check that a secondary audio option exists that provides live audio description of the broadcast.

**Expected results**

-   #1 is true.

##### Core requirement: Extended audio descriptions availableDeveloping

The [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) pauses to extend the [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) track and provides an [extended audio description](https://www.w3.org/TR/wcag-3.0/#dfn-extended-audio-description) to describe visual information needed to understand the media.

**Applies when**

-   the existing pauses in a soundtrack are not long enough.

Tests

_This section is non-normative._

**Procedure**

For each media asset with visual content:

1.  Play the media with the extended audio description on.
2.  Check that the extended audio description includes all important visual information that cannot be understood from the main soundtrack alone.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Audio description language adjustableDeveloping

A [mechanism](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) is available that allows users to change the [audio description](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) language if multiple languages are available.

Tests

_This section is non-normative._

**Procedure**

For each media asset with audio content:

1.  Check that a version of the media has audio description available in alternative languages and the language of audio description can be changed by the user.
2.  Alternatively, check that alternative versions of the media exist that have audio description available in alternative languages.

**Expected results**

-   #1 or #2 is true.

#### Guideline 2.1.6 Figure captions

Users can view [figure captions](https://www.w3.org/TR/wcag-3.0/#dfn-figure-caption) even if not focused at figure.

Editor's note

Requirements and assertions for this guideline do not appear here because they have not yet progressed beyond exploratory. See the [Editor's Draft](https://w3c.github.io/wcag3/guidelines/) for the complete list of potential requirements and assertions.

#### Guideline 2.1.7 Single sense

Users have [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that does not rely on a single sense or perception.

##### Core requirement: Hue not relied onDeveloping

Information is not conveyed by hue alone.

Note

Information conveyed includes presenting data or meaning, indicating an action, prompting a response, distinguishing between items, conveying boundaries, etc. Artistic expression is not part of information conveyed.

**Except when**

-   Content is artistic or expressive.
-   Content is designed only for a device that is limited to presenting hues.

Tests

_This section is non-normative._

**Procedure**

For each instance where information is conveyed by hue:

1.  Check that at least one additional visual indicator is present that conveys the same information.

**Expected results**

-   #1 is true.

##### Core requirement: Graphical object contrast sufficientDeveloping

Parts of graphical object required to understand the content meet a minimum [contrast ratio test](https://www.w3.org/TR/wcag-3.0/#dfn-contrast-ratio-test)

**Except when**

-   a particular presentation of graphical objects is essential to the information being conveyed.

Tests

_This section is non-normative._

**Procedure**

For each part of a graphical object that conveys information:

1.  Check that these parts meet the minimum contrast ratio with adjacent colors.

**Expected results**

-   #1 is true.

##### Core requirement: Visual depth not relied onDeveloping

Information is not conveyed through visual depth perception alone.

Tests

_This section is non-normative._

**Procedure**

For each instance where information is conveyed by visual depth:

1.  Check that at least one additional visual indicator is present that conveys the same information.

**Expected results**

-   #1 is true.

##### Core requirement: Sound not relied onDeveloping

Information is not conveyed by sound alone.

**Except when**

-   Content is audio-based media.

Note

Information conveyed includes presenting data or meaning, indicating an action, prompting a response, distinguishing between items, conveying boundaries, etc. Artistic expression is not part of information conveyed.

Tests

_This section is non-normative._

**Procedure**

For each instance where information is conveyed by sound:

1.  Check that the information is also conveyed in a way that does not use sound, for instance with a visual, text, or haptic indicator.

**Expected results**

-   #2 is true.

##### Core requirement: Spatial audio not relied onDeveloping

Information is not conveyed by [spatial audio](https://www.w3.org/TR/wcag-3.0/#dfn-spatial-audio) alone.

Note

Information conveyed includes presenting data or meaning, indicating an action, prompting a response, distinguishing between items, conveying boundaries, etc. Artistic expression is not part of information conveyed.

Tests

_This section is non-normative._

**Procedure**

For each instance where information is conveyed by spatial audio:

1.  Check that the information is also conveyed in a way that does not use sound, for instance with a visual text, or haptic indicator.

**Expected results**

-   #1 is true for all instances.

### 2.2 Text and wording

#### Guideline 2.2.1 Text appearance

Users can read visually rendered [text](https://www.w3.org/TR/wcag-3.0/#dfn-text).

Editor's note

AGWG remains committed to providing Text Appearance guidance for multiple scripts and/or languages. To support our internationalization goals, AGWG is exploring ways to:

-   not require WCAG 3 to be republished when metrics are added for more scripts/languages,
-   make script/language-specific metrics normative,
-   meet the needs of different scripts and languages by allowing flexibility in which metrics are required and in their values, and
-   preserve backward compatibility.

##### Core requirement: Text size adjustableDeveloping

Text can be increased in size to at least 200% of the platform’s default body-text size.

**Except when**

-   the same text is available elsewhere in the page/view which can be increased to at least 200% of the platform’s default body-text size.

Tests

_This section is non-normative._

**Procedure**

For each block of text:

1.  Use each platform mechanism for increasing text size.
2.  Check that at least one mechanism can achieve a 200% text-size increase.

**Expected results**

-   #2 is true.

##### Core requirement: Text color adjustableDeveloping

The foreground and background color of text can be adjusted without losing content or functionality.

Note

The requirement is that the text is manipulable and the colors can be overridden. That could be achieved by the user-agent (including operating system, browser, and assistive technology), or provided by the content author.

**Applies when**

-   text is presented, including text embedded in an image format.

**Except when**

-   the text is:
    -   also present elsewhere in the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) which meets the requirement,
    -   part of an inactive Interactive element,
    -   pure decoration,
    -   not visible to anyone,
    -   part of a picture that includes significant other visual content,
    -   part of a logo.

Tests

_This section is non-normative._

**Procedure**

For each block of text:

1.  Adjust the foreground and background color to a high-contrast light-on-dark theme.
2.  Check that content and functionality is not lost.
3.  Adjust the foreground and background color to a high-contrast dark-on-light theme.
4.  Check that content and functionality is not lost.

**Expected results**

-   #2 and #4 are true.

##### Supplemental requirement: Text customizations retainedDeveloping

Content that is exported, saved, or printed retains user-applied text-appearance customizations.

**Applies when**

-   the page/view can be exported, saved, or printed.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Adjust aspects of the text appearance, such as size, style, and color.
2.  Export, save, and print the content.
3.  Check that the customizations in #1 remain intact in the exported/saved/printed version. If there are multiple export options, check that at least one preserves the customizations.

**Expected results**

-   #3 is true.

#### Guideline 2.2.2 Text-to-speech

Users can access [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content) and its meaning with text-to-speech tools.

##### Core requirement: Text detectableDeveloping

All visible [text](https://www.w3.org/TR/wcag-3.0/#dfn-text) has a [programmatically determinable](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable) equivalent.

**Except when**

-   making visible text programmatically determinable would lead to duplication within the view.

Tests

_This section is non-normative._

**Procedure** For all visible text: 2. If the text is embedded in an image, check that the text has a [text alternative](https://www.w3.org/TR/wcag-3.0/#dfn-text-alternative) or can be accurately read using the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set). 3. If text content, check that the text is not hidden using code such as the `aria-hidden` attribute.

**Expected results**

-   #2 and #3 are true.

##### Core requirement: Human language detectableDeveloping

The [human language](https://www.w3.org/TR/wcag-3.0/#dfn-human-language) of all [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) within the [view](https://www.w3.org/TR/wcag-3.0/#dfn-view) is [programmatically determinable](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable).

**Except when**

-   a language tag is not available in ISO 639 language codes, or
-   the technology used to create the view does not support indicating languages.

Tests

_This section is non-normative._

**Procedure**

For text content:

1.  Establish which language is used.
2.  Check that the content’s language is identified in the HTML code with a lang attribute.

**Expected results**

-   #2 is true.

##### Core requirement: Numerical metadata availableDeveloping

Numerical information includes sufficient context in written text and a programmatic equivalent to avoid confusion when presenting dates, temperatures, time, and Roman numerals.

Note

Numerical metadata is information that provides context about the numbers presented. This context helps users understand what the numbers represent and how they should be read. Without these cues, numbers can be ambiguous or misleading, making it harder for users to understand the intended meaning—especially across different regions, disciplines, or assistive technologies.

Tests

_This section is non-normative._

**Procedure**

For each date, temperature, time, or Roman numeral presented visually:

1.  Check that it uses an unambiguous format.
2.  Check that it provides an alternative in an unambiguous format within the same page/view.

**Expected results**

-   #1 or #2 are true.

#### Guideline 2.2.3 Clear languageDeveloping

Users can understand the content without having to process complex or unclear language.

Editor's note

This [guideline](https://www.w3.org/TR/wcag-3.0/#dfn-guideline) will include exceptions for poetic, scriptural, artistic, and other content whose main goal is expressive rather than [informative](https://www.w3.org/TR/wcag-3.0/#dfn-informative).

Editor's note

See also: [Structure](https://www.w3.org/TR/wcag-3.0/#structure) as these guidelines are closely related.

Editor's note

To ensure this guideline works well across different languages, members of AGWG, Cognitive and Learning Disabilities Accessibility Task Force (COGA), and internationalization (i18n) agreed on an initial set of languages to pressure-test the guidance.

The five “guardrail” languages are:

-   Arabic
-   English
-   Hindi
-   Mandarin
-   Russian

We started with the six official languages of the United Nations (UN). Then we removed French and Spanish because they are similar to English. We added Hindi because it is the most commonly spoken language that is not on the UN list.

The group of five languages includes a wide variety of language features, such as:

-   Right-to-left [text](https://www.w3.org/TR/wcag-3.0/#dfn-text) layout
-   Vertical text layout
-   Tonal sounds that affect meaning

This list doesn’t include every language, but it helps keep the work manageable while making the guidance more useful for a wide audience.

We will work with W3C’s Global Inclusion community group, the Internationalization (i18n) task force, and others to review and refine the testing and techniques for these [requirements](https://www.w3.org/TR/wcag-3.0/#dfn-requirement). We also plan to create guidance for translating the guidelines into more languages in the future.

##### Core requirement: Abbreviations explainedDeveloping

Explanations of [abbreviations](https://www.w3.org/TR/wcag-3.0/#dfn-abbreviation) are available when first used.

**Except when**

-   the abbreviation is:
    -   used so often it has become a word with its own dictionary entry, such as “scuba,” “info,” and “HTML”
    -   used in a logo
    -   included in a longer phrase, such as “brand DNA,” whose meaning needs to be defined to meet the [non-literal language requirement](https://www.w3.org/TR/wcag-3.0/#non-literal-language-explained).

Tests

_This section is non-normative._

**Procedure**

For any abbreviation in the content:

1.  Check that an explanation is available for the first use of the abbreviation.
2.  For an abbreviation that has no explanation available, check that it is included in a dictionary intended for the general public.

**Expected result**

-   #1 or #2 is true.

##### Supplemental requirement: Non-literal language explainedDeveloping

Explanations or unambiguous alternatives are available in [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content) for [non-literal language](https://www.w3.org/TR/wcag-3.0/#dfn-non-literal-language), such as idioms and metaphors.

**Except when**

text content is:

-   poetic,
-   scriptural,
-   artistic, or
-   expressive rather than informational.

Editor's note

Translation software and other tools can aid [content authors](https://www.w3.org/TR/wcag-3.0/#dfn-content-author) in identifying non-literal language.

Tests

_This section is non-normative._

**Procedure**

For each phrase of [non-literal language](https://www.w3.org/TR/wcag-3.0/#dfn-non-literal-language) in [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content):

1.  Check that access is provided to an unambiguous alternative or to an explanation of the non-literal text.
2.  Check that the non-literal text is presented in a way that is available to [user agents](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent), including [assistive technologies](https://www.w3.org/TR/wcag-3.0/#dfn-assistive-technology) (AT).
3.  Check that the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set) meets ‘Non-literal language explained’.

**Expected results**

-   #1 and #2 are true, or
-   #3 is true.

##### Core requirement: Diacritics availableDeveloping

Diacritics required to identify the correct meaning of each word are available.

**Applies when**

-   a [human language](https://www.w3.org/TR/wcag-3.0/#dfn-human-language) has a version that removes diacritics for proficient readers.

Note 1

A diacritic is a small mark that is added to a letter or character that changes how it is pronounced or what it means. Diacritics may appear above, below, within, or between letters or characters.

Note 2

Hebrew and Arabic are examples of human languages that omit diacritics for proficient readers.

Tests

_This section is non-normative._

**Procedure**

For all text content:

1.  Check for content that has missing diacritics.
2.  Check that an alternative version to text identified in #1 is provided that includes diacritics needed to identify the correct meaning of each word.
3.  Check that the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set) meets ‘Diacritics available’.

**Expected results**

-   #2 or #3 is true.

##### Supplemental requirement: No nested clausesDeveloping

Sentences do not include [nested clauses](https://www.w3.org/TR/wcag-3.0/#dfn-nested-clause).

**Except when**

-   [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content):
    -   is poetic, scriptural, artistic, or expressive rather than informational, or
    -   provides [legal information](https://www.w3.org/TR/wcag-3.0/#dfn-legal-information).

Tests

_This section is non-normative._

**Procedure**

For each sentence: For all nested clauses in the sentence (introduced by nesting conjunctions such as ‘because’, ‘although’, ‘if’, ‘that’, ‘which’, ‘who’, ‘when’, and ‘where’).

1.  Check that each initial nested clause does not contain other nested clauses within it.
2.  Check that a technology in the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set) meets ‘No nested clauses’.

**Expected results**

-   #1 or #2 is true.

##### Supplemental requirement: No unnecessary wordsDeveloping

Sentences do not include [unnecessary words](https://www.w3.org/TR/wcag-3.0/#dfn-unnecessary-words).

**Except when**

-   [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content) is:
    -   poetic,
    -   scriptural,
    -   artistic, or
    -   expressive rather than informational.

Note

Automated tools can help [content authors](https://www.w3.org/TR/wcag-3.0/#dfn-content-author) identify unnecessary words in many languages, including Arabic, English, Hindi, Mandarin, and Russian.

Tests

_This section is non-normative._

**Procedure**

For each sentence:

1.  Identify any words that may be unnecessary.
2.  Remove or replace the phrase with a simpler alternative.
3.  Check that no meaning is lost.
4.  Check that a technology in the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set) meets ‘No unnecessary words.’

**Expected results**

-   #3 or #4 is true.

##### Assertion: Clear language reviewDeveloping

\[Title, role, or organization\] asserts that:

-   Our organization has a process and policy to review [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content) for [clear language](https://www.w3.org/TR/wcag-3.0/#dfn-clear-language) before publication. The process includes confirming:
    -   All of the core requirements in the ‘Clear Language’ guideline are met.
    -   Verb tense is chosen for ease of understanding.
    -   Content uses short paragraphs.
    -   Paragraphs that convey information begin with a sentence stating the main point or purpose (often called a topic sentence).
    -   If a style guide is used by [content authors](https://www.w3.org/TR/wcag-3.0/#dfn-content-author), it must provide guidance on these aspects of clear language.
    -   If author training is provided, it must provide guidance on these aspects of clear language.

Information that needs to be included publicly:

-   Title, role, or organization making the assertion (if different from the conformance claim).
-   Date of when the policy was implemented.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Copy of the policy implementing the clear language review.
-   Date author training was provided (if any).
-   Number or proportion of authors who completed the training.
-   Copy of the style guide (if any) where clear language review has been defined.

##### Assertion: Visual aids reviewDeveloping

\[Title, role, or organization\] asserts that:

-   Our organization has a process and policy for reviewing [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content) to identify complex ideas such as processes, workflows, relationships, or chronological information, and adding [visual aids](https://www.w3.org/TR/wcag-3.0/#dfn-visual-aids) to help readers understand them.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim)
-   Date of when the policy was implemented
-   Date of assertion (if different from the date of the conformance claim)

Recommended internal documentation (Informative):

-   Copy of the policy implementing the use of visual aids
-   Date author training was provided (if any)
-   Number or proportion of authors who completed the training
-   Copy of the style guide (if any) where visual aids have been defined

### 2.3 Interactive components

#### Guideline 2.3.1 Keyboard focus appearanceDeveloping

Users can see which element has [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus).

##### Supplemental requirement: Default focus indicator usedDeveloping

The focusable [item](https://www.w3.org/TR/wcag-3.0/#dfn-items) uses the [user agent](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent) default [focus indicator](https://www.w3.org/TR/wcag-3.0/#dfn-focus-indicator).

Tests

_This section is non-normative._

**Procedure**

For user agents that allow the customization of focus indicators:

1.  Use the keyboard to move focus onto the item.
2.  Check that the focus indicator is the user agent’s default indicator.
3.  For platform display changes, check that the focus indicator’s color is correct for the type of element.

**Expected results**

-   #2 and #3 are true.

##### Core requirement: Focus indicator contrast sufficientDeveloping

If a custom [focus indicator](https://www.w3.org/TR/wcag-3.0/#dfn-focus-indicator) is used, it has sufficient adjacent contrast and change of contrast.

**Applies when**

-   the user agent’s default focus indicator is replaced by a custom focus indicator.

Tests

_This section is non-normative._

**Procedure**

For each element able to attain focus:

1.  Using a keyboard, tab to the component.
2.  Check that the focus indicator contrast meets the minimum contrast ratio test.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Focus indicator size sufficientDeveloping

If a custom [focus indicator](https://www.w3.org/TR/wcag-3.0/#dfn-focus-indicator) is used, it has sufficient size and adjacency.

**Applies when**

-   the user agent’s default focus indicator is replaced by a custom focus indicator.

Tests

_This section is non-normative._

**Procedure**

For each custom focus indicator:

1.  Check that the focus indicator is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component or sub-component, and
2.  Check that the focus indicator has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states.

**Except when**

-   the focus indicator is determined by the user agent and cannot be adjusted by the author, or the focus indicator and the indicator’s background color are not modified by the author.

**Expected results**

-   #1 and #2 are true.

##### Assertion: Focus indicator style guideDeveloping

\[Title, role, or organization\] asserts that:

-   Our organization has a style guide that includes guidance on focus indicators and a policy and/or processes that the style guide must be followed.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the design style guide was published.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Copy of the policy implementing the use of design style guide on focus style.
-   Whether training was provided for authors
    -   Date training was provided.
    -   Number or proportion of authors who completed the training.
-   A copy of the design style guide (if any) where focus style has been defined.

#### Guideline 2.3.2 Pointer focus appearance

Users can see the location of the [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) focus.

##### Core requirement: Pointer activation indicated (minimum)Developing

There is a visible indication of the activation of an interactive element when selected by the [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer).

**Applies when**

-   The platform does not use a visible pointer indicator.

Note

This is primarily aimed at touch-interfaces and VR where you don’t have a pointer indicator, but do need to know when something has been selected.

Tests

_This section is non-normative._

**Procedure**

Where the platform does not use a visible pointer indicator, for each interactive element:

1.  Check that there is an indicator of activation.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Pointer activation indicated (enhanced)Developing

The user can choose to always have a visible [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) indicator.

**Applies when**

-   The platform does not use a visible pointer indicator.

Note

This is primarily aimed at eye-tracking and touch-screens, where it is useful for the user to be able to have a visible indicator, but it wouldn’t be universal (i.e., it might get in the way for some users).

Tests

_This section is non-normative._

**Procedure**

For each pointer indicator:

1.  Check the settings of the [platform](https://www.w3.org/TR/wcag-3.0/#dfn-platform) or [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) for the ability to have an always-visible pointer indicator.

**Expected results**

-   #1 is true.

##### Core requirement: Pointer contrast sufficientDeveloping

The default pointer meets the @@\[non-text-contrast\] requirement, and is at least as large as the platform default.

Note

There can be multiple types of pointer indicator (e.g. arrow, hand, caret). The size requirement applies to whichever type of indicator would be the default for that scenario.

**Applies when**

-   the pointer indicator appearance can be adjusted from the platform default.

Tests

_This section is non-normative._

**Procedure**

For each custom pointer indicator:

1.  Identify which visual information defines the boundaries of the interactive area.
2.  Check if the visual information meets the minimum contrast ratio test.
3.  For each possible state, repeat step 1 and 2.

**Expected results**

-   #3 is true for each state.

##### Supplemental requirement: Default pointer usedDeveloping

The user can ensure that the appearance of the [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) is not overridden by the authored interface.

**Except when**

-   Changing the pointer appearance is essential.

Editor's note

Methods & best practices:

-   No scripting or styling overrides the pointer indicator appearance.
-   A setting is provided so that the pointer indicator appearance is not overridden.

Tests

_This section is non-normative._

**Procedure**

For each pointer indicator:

1.  Check that the pointer uses the standard platform indicator.
2.  Check for a setting that the user can enable to use the standard platform indicator.

**Expected results**

-   #1 or #2 is true.

##### Core requirement: Pointer focus indicatedDeveloping

There is a visible [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) indicator.

**Except when**

-   The pointer is on a video - it can be hidden if there is a pointer mechanism to un-hide the pointer indicator.
-   The pointer controls the direction of view in a virtual or real world environment.

Note 1

Examples of pointers which do not always show the pointer indicator:

-   A touch-screen interface does not need to have an indicator as the pointer is not on an element before activating it.
-   An eye-tracking interface highlights the element under the gaze of the user, but otherwise does not have a pointer indicator.
-   A game where you use the pointer to move the entire view around a virtual environment.

Note 2

Methods & best practices:

-   Method: Interactive elements are highlighted when the pointer is on the element. For example, a set of image-links are shown, and the one under the pointer is highlighted with an outline or size-change.

Tests

_This section is non-normative._

**Procedure**

With appropriate user-settings enabled:

1.  Move the pointer (mouse, eye tracker, hand gesture in VR space, …).
2.  Check that there is some form of indication of where the user is pointing to.

**Expected results**

-   #2 is true.

##### Core requirement: Pointer visibleDeveloping

The [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) indicator is always visible.

**Except when**

-   The pointer is on a video and is not moving.
-   The pointer controls the direction of view in a virtual or real world environment.

Note

Methods & best practices

-   Method: No styling or scripting hides the pointer indicator.

Tests

_This section is non-normative._

**Procedure**

If the pointer is ever not visible:

1.  Check that it meets one of the exceptions.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Enhanced pointer availableDeveloping

Provide a more visible [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) indicator than the platform default. The enhanced pointer indicator can be enabled in a setting, and be visible temporarily (for a few seconds) or permanently.

Note

Methods & best practices:

-   Provide a setting to adjust the pointer indicator.

Tests

_This section is non-normative._

**Procedure**

For each pointer indicator:

1.  Check for a setting that increases the visibility.
2.  Check that it works in the conformance scope of web pages/views.

**Expected results**

-   #1 and #2 are true.

#### Guideline 2.3.3 Navigating content

Users can determine where they are and move through [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) (including [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element)) in a systematic and meaningful way regardless of input or movement [method](https://www.w3.org/TR/wcag-3.0/#dfn-method).

##### Core requirement: Focus relevantDeveloping

The focus order does not include hidden, static, or groups of repeated interactive elements.

Tests

_This section is non-normative._

**Procedure**

For groups of repeated interactive elements (for example, a site-wide navigation bar on a website):

1.  Check that a method of skipping them is available.
2.  Check that hidden interactive elements do not receive focus.
3.  Check that static elements do not receive focus.

**Expected results**

-   #1, #2, and #3 are true.

##### Supplemental requirement: Focus retainedDeveloping

A user can focus on a [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) “area”, such as a modal or popup, then resume their view of all content using a limited number of steps.

Tests

_This section is non-normative._

**Procedure**

For each situation where the keyboard focus is removed:

1.  Check that the keyboard focus moves to its previous location, or, if that no longer exists, to another meaningful location.

**Expected results**

-   #1 is true.

##### Core requirement: Focus order meaningfulDeveloping

The [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) moves sequentially through [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) in an order and way that preserves meaning and operability.

Note

-   The [Common Keyboard Navigation Techniques](https://www.w3.org/TR/wcag-3.0/#dfn-common-keyboard-navigation-technique) are considered logical by default
-   Having the navigation follow a consistent pattern on the page would be an indication of logic (if it is not consistently random).
-   A strictly start-to-end order is not required.
-   Linear means in a single direction (forward/backward) - and is not required as long the non-linear (x-y) technique is in the Common Keyboard Navigation Techniques or is described on the page or where the user will encounter it prior.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Determine the logical order of the interactive elements.
2.  Starting with the first focusable element in the page/view, tab through the interactive elements in the content.
3.  Check that the focus order of the interactive elements in the content is the same as the logical order in #1.

**Expected results**

-   #3 is true.

#### Guideline 2.3.4 Expected behavior

Users can interact with [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) that behave as expected.

##### Assertion: Consistent interactionsDeveloping

\[Title, role, or organization\] asserts that:

-   A review has been conducted and changes made (when necessary) to ensure that [Components](https://www.w3.org/TR/wcag-3.0/#dfn-component) with the same functionality behave consistently:
    -   Components that perform the same function behave in the same way and use the same visual indicators.
    -   Within the component, [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) with the same function have consistent labels.
    -   Standard user interface designs for the platform are used when applicable.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the review was completed.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Results from the review.
-   Process or policy for maintaining the review.

##### Assertion: Conventional pattern usedDeveloping

\[Title, role, or organization\] asserts that:

-   A review has been conducted and changes made (when necessary) to ensure that [Components](https://www.w3.org/TR/wcag-3.0/#dfn-component) follow established conventions:
    -   Each component follows applicable platform conventions for how users interact with that type of component.
    -   If a component library is used, then each component in the library:
        -   is tested for accessibility before being used
        -   follows applicable platform conventions for how users interact with that type of component

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the review was completed.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Results from the review.
-   Process or policy for maintaining the review.

Note

#### Guideline 2.3.5 Control information

Users have information about [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) that is identifiable and usable visually and using [assistive technology](https://www.w3.org/TR/wcag-3.0/#dfn-assistive-technology).

##### Core requirement: Interactive element contrast sufficientDeveloping

Visual information required to identify [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) and states meet a minimum [contrast ratio test](https://www.w3.org/TR/wcag-3.0/#dfn-contrast-ratio-test)

**Except when**

-   the interactive element is inactive, or
-   when the appearance of the component is determined by the [user agent](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent) and not modified by the content author.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Identify which visual information defines the boundaries of the interactive area.
2.  Check if the visual information meets the minimum contrast ratio test.
3.  For each possible state, repeat step 1 and 2.

**Expected results**

-   #2 and #3 are true.

##### Core requirement: Interactive element names availableDeveloping

Persistent names (including labels) that identify the purpose of the interactive element are visually and programmatically available.

Note

Visible labels can be text or non-text, for instance icons.

Editor's note

Methods & best practices

-   Method: Provide unique, descriptive text or image (icon) for each interactive element.
-   Best Practice: Ensure clarity by pairing an icon with a persistent visible text label or only use a persistent visible text label.
-   Best Practice: When an icon is the only visual label, provide a tooltip (hover label) with the text description.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Confirm it has a visual label that describes the element.
2.  Confirm the visual label persists during use.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: Changes to elements notifiedDeveloping

Changes to [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element)’ names, roles, values or states are visually and [programmatically indicated](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable).

Editor's note

Methods & best practices:

-   Method: Add code that clearly defines the name, role, value and state.
-   Method: visually indicate the names, roles and values of the interactive element.
-   Method: HTML - html tags or aria

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Confirm that the role, value, and state (when applicable) are visually indicated in all states.
2.  Inspect the code and accessibility tree (when available) to confirm that the name, role, value and state (when applicable) are indicated.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: Input constraints usedDeveloping

Field constraints and conditions (required line length, date format, password format, etc.) are available.

Editor's note

Methods & best practices

-   Method (HTML): to programmatically indicate, use the pattern attribute or write the information in a label; to visually indicate, add the requirements to the page near the input.

Best practice: the constraints remain persistent

Tests

_This section is non-normative._

**Procedure**

For each input:

1.  Confirm it has a visual information that describes the constraint.
2.  Inspect the code and accessibility tree (when applicable) and confirm that the constraint is programmatically listed in the code and associated with the input.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: Label included in programmatic nameDeveloping

The programmatic name includes the visual label.

Editor's note

Methods & best practices

-   Method: Code the same name as you display.
-   Best Practice: Use unique names and keep the programmatic and visual names the same.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Identify the interactive elements’ programmatic name.
2.  Identify the interactive element’s visual name.
3.  Check that #1 includes all of #2.

**Expected results**

-   #3 is true.

##### Core requirement: Roles, values, states, properties availableDeveloping

Accurate names, roles, values, and [states](https://www.w3.org/TR/wcag-3.0/#dfn-state) are available for [interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element).

Editor's note

Methods & best practices

-   Method (HTML): use HTML elements according to specification.
-   Method (ARIA): add roles, values, states, and properties according to specification.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Inspect the code and accessibility tree (when available) to confirm that the role, value, state, and properties (when applicable) are indicated.

**Expected results**

-   #1 is true.

### 2.4 Input / operation

#### Guideline 2.4.1 Keyboard interface input

Users can navigate and operate [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) using only the keyboard.

##### Core requirement: Keyboard operableDeveloping

All [components](https://www.w3.org/TR/wcag-3.0/#dfn-component) on the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) that can be operated by [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer), [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) (voice or other), [gesture](https://www.w3.org/TR/wcag-3.0/#dfn-gesture), camera, or other means can be operated using [keyboard interface](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-interface) only.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Check that it can be operated using only the keyboard and keyboard actions in the [Standard Keyboard Navigation & Operation Keys and Techniques](https://github.com/w3c/wcag3/wiki/Standard-Keyboard-Navigation-&-Operation-Keys-and-Techniques) or described on the page where it is required or on a page earlier in the process where it is required.

**Expected results**

-   #1 is true.

##### Core requirement: Keyboard accessibleDeveloping

All [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that can be accessed by other input modalities can be accessed using [keyboard interface](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-interface) only.

Note 1

All content includes content made available via hovers, right clicks, etc.

Note 2

Other input modalities include [pointing devices](https://www.w3.org/TR/wcag-3.0/#dfn-pointer), voice and speech recognition, [gesture](https://www.w3.org/TR/wcag-3.0/#dfn-gesture), camera, and any other means of input or control.

Note 3

The [“Keyboard operable” requirement](https://www.w3.org/TR/wcag-3.0/#keyboard-operable) allows you to navigate to all actionable elements, but if the next element is 5 screens down, you also need to be able to access all the content. Also, if the content is in expanding [sections](https://www.w3.org/TR/wcag-3.0/#dfn-section), you need to not only open them but also access all of the content, not just its actionable elements.

Tests

_This section is non-normative._

**Procedure** For all content on the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view):

1.  Check that the content can be viewed using the keyboard and keyboard actions in the [Standard Keyboard Navigation & Operation Keys and Techniques](https://github.com/w3c/wcag3/wiki/Standard-Keyboard-Navigation-&-Operation-Keys-and-Techniques);
2.  Check that the content can be viewed using keyboard actions described on the page where it is required or on a page earlier in the process where it is required.

**Expected results**

-   #1 or 2 is true.

##### Core requirement: Bidirectional navigationDeveloping

The keyboard interface can always move forward to the next interactive element and back to the previous interactive element.

Note 1

Although keyboard navigation is required to be bidirectional, it is not required that it be symmetrical, even though this is usually best practice.

Note 2

Methods & best practices:

-   Method: Use standard HTML to create interactive elements.
-   Avoid modifying the tab order to be in only one direction.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Check that when tabbing forwards, you can navigate to the interactive element and then to the next interactive element.
2.  Check that when tabbing backwards, you can navigate to the interactive element and then to the previous interactive element.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Custom keys documentedDeveloping

Non-standard keyboard commands provided by content authors are documented and that documentation is programmatically and visually available from any [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) to which they apply.

Tests

_This section is non-normative._

**Procedure**

For each non-standard (custom) keyboard command that works on a page/view:

1.  Check that documentation of keyboard commands exists.
2.  Check that the documentation is available from the page/view.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: No keyboard conflictsDeveloping

Keyboard commands provided by content authors do not conflict with [standard platform keyboard commands](https://www.w3.org/TR/wcag-3.0/#dfn-standard-platform-keyboard-commands) or they can be remapped.

Tests

_This section is non-normative._

**Procedure**

For each author generated keyboard command:

1.  Check that it does not conflict against the standard platform keyboard commands.
2.  Check that it can be remapped.

**Expected results**

-   #1 or #2 is true.

##### Core requirement: Keyboard navigable if responsiveDeveloping

If the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) uses responsive design, the page / view remains fully keyboard navigable.

Tests

_This section is non-normative._

**Procedure**

For each breakpoint defined by the author and at minimum width:

1.  Check that all keyboard input tests work.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Focus placedDeveloping

When [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) moves from one context to another within a [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view), whether automatically or by user request, the keyboard focus is preserved so that, when the user returns to the previous context, the keyboard focus is restored to its previous location unless that location no longer exists.

Editor's note

Method: When removing interactive elements such as filters, dialogs, or popups that currently contain focus, actively place the focus back on the element that led to that element, the previous element within the focus order, or another meaningful location.

Best Practice: Conduct usability testing with screen reader users to evaluate the focus movement.

Tests

_This section is non-normative._

**Procedure**

For each situation where elements that have or contain keyboard focus are removed:

1.  Check that the keyboard focus moves to its previous location, or, if that no longer exists, to another meaningful location.

**Expected results**

-   #1 is true for each situation.

##### Core requirement: No keyboard trapsDeveloping

Components that can be activated or entered using the keyboard interface, can be deactivated or exited using a standard keyboard navigation-operation technique, standard platform keyboard commands.

**Except when**

-   The non-standard keyboard navigation technique is described on the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) or earlier in the [process](https://www.w3.org/TR/wcag-3.0/#dfn-process).

Tests

_This section is non-normative._

**Procedure**

For each interface element:

1.  Check that you can exit from it in a forward or backward direction.

**Expected results**

-   #1 is true.

##### Core requirement: Focus user-controlledDeveloping

The [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) only moves as a result of user interaction.

**Except when**

-   The keyboard focus automatically moves to the next interactive elements in keyboard navigation order on completion of some user action, such when the focus moves between the fields for a time-based one-time password (TOTP) code.
-   The keyboard focus results from security or emergency situations, such as warning about an imminent session timeout that would cause the user to lose their work.
-   The user is informed of the potential keyboard focus move before it happens and given the chance to avoid the move.

Tests

_This section is non-normative._

**Procedure**

For each time the keyboard focus changes:

1.  Check that one of the following is true:
    -   The focus was moved under direct user control
    -   A new page / view such as a dialog is introduced and the focus is moved to it
    -   The user is informed of the potential move and given the chance to avoid the move
    -   The keyboard focus moves to the next item in keyboard navigation order

**Expected results**

-   #1 is true.

##### Supplemental requirement: Focus movement relevantDeveloping

Except for skip links and other elements that are hidden but specifically added to aid keyboard navigation, tabbing does not move the [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) onto [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that was not visible before the tab action.

Note

Accordions, dropdown menus, and [ARIA tab panels](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) are examples of expandable content. According to this [requirement](https://www.w3.org/TR/wcag-3.0/#dfn-requirement), these would not expand simply because they include an element in the tab-order contained in them. They would either not expand or would not have any tab-order elements in them.

Tests

_This section is non-normative._

**Procedure**

For any interactive element:

1.  Check that keyboard focus does not disappear into content that is not visible.
2.  Check that hidden element does not automatically expand (become visible) when the keyboard focus is on it (unless it is a visually hidden element specifically added to aid keyboard navigation) (e.g. skip to main content).

**Expected results**

-   #1 and #2 are true.

#### Guideline 2.4.2 Physical or cognitive effort when using keyboard

Users can use keyboard without unnecessary physical or cognitive effort.

##### Supplemental requirement: Navigation keys describedDeveloping

If any keyboard action needed to navigate, perceive, and operate the full [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) of the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) is not a [common keyboard navigation technique](https://www.w3.org/TR/wcag-3.0/#dfn-common-keyboard-navigation-technique), then it is described in the page/view where it is required or on a page/view earlier in the [process](https://www.w3.org/TR/wcag-3.0/#dfn-process) where it is used.

Note

Any [platform](https://www.w3.org/TR/wcag-3.0/#dfn-platform)\-related functions are not the responsibility of the author as long as they are not overridden by the content. Examples:

-   Tab and Shift + Tab to move through elements
-   Sticky Keys functionality that allows single key activation of multi-key commands

Tests

_This section is non-normative._

**Procedure**

For each keyboard command needed to operate functionality:

1.  Check that it is in the list of common keyboard navigation techniques.
2.  Check that it is described on the page / view where it is required or on a page / view earlier in the process where it is used.

**Expected results**

-   #1 or #2 are true.

##### Supplemental requirement: No repetitive linksDeveloping

Repetitive adjacent links that have the same destination are avoided.

Editor's note

Supplemental if applicable to all [content](https://www.w3.org/TR/wcag-3.0/#dfn-content), else best practice.

Note 1

A common pattern is having a [component](https://www.w3.org/TR/wcag-3.0/#dfn-component) that includes a linked image and some linked [text](https://www.w3.org/TR/wcag-3.0/#dfn-text), where both links go to the same content. Someone using screen reading software can be disoriented from the unnecessary chatter, and a keyboard user has to navigate through more tab stops than should be necessary. Combining adjacent links that go to the same content improves the user experience.

Note 2

Methods & best practices

-   Method: When repetitive links are used, remove them from the focus and reading order.
-   Method: Use a single link instead of multiple links to the same destination.
-   Best practice: Combine repetitive links into a single interactive element.

Tests

_This section is non-normative._

**Procedure**

For set of adjacent links that go to the same destination:

1.  Check that only one of the links is in the focus and reading order.

**Expected Results**

-   #1 is true.

##### Assertion: Keyboard effort comparableDeveloping

\[Title, role, or organization\] asserts that:

-   A review has been conducted and changes made (when necessary) to ensure that there is minimal difference between the number of input commands required when using the [keyboard interface](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-interface) only and the number of commands when using other input modalities.

Note

Other input modalities include [pointing devices](https://www.w3.org/TR/wcag-3.0/#dfn-pointer), voice and speech recognition, [gesture](https://www.w3.org/TR/wcag-3.0/#dfn-gesture), camera, and any other means of input or control.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the review was conducted.
-   Date of assertion (if different from the date of the conformance claim).
-   Scope of assertion (if different from the conformance claim).

Recommended internal documentation (Informative):

-   Copy of the review implementing the use of user interface design principles that include minimizing the difference between the number of input commands required when using the keyboard interface only and the number of commands when using other input modalities.
-   Whether training was provided for authors.
-   Date training was provided.
-   Number or proportion of authors who completed the training.
-   A copy of the user interface design principles document.

#### Guideline 2.4.3 Pointer input

[Pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) input is consistent and all functionality can be done with [simple pointer input](https://www.w3.org/TR/wcag-3.0/#dfn-simple-pointer-input) in a time and pressure insensitive way.

##### Core requirement: Pointer activation controllableDeveloping

At least one of the following is true for functionality that can be activated using a [simple pointer input](https://www.w3.org/TR/wcag-3.0/#dfn-simple-pointer-input):

No Down Event

The [down event](https://www.w3.org/TR/wcag-3.0/#dfn-down-event) of the [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) is not used to execute any part of the function.

Cancel or Undo

Completion of the function is on the [up event](https://www.w3.org/TR/wcag-3.0/#dfn-up-event) and a [mechanism](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) is available to cancel the function before completion, or there is a mechanism to undo the function after completion.

Up Reversal

The [up event](https://www.w3.org/TR/wcag-3.0/#dfn-up-event) reverses any outcome of the preceding down event.

**Except when**

-   Completing the function on the down event is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome).

Tests

_This section is non-normative._

**Procedure**

For each element that can be activated with a simple pointer:

1.  Check that the down-event of the pointer is not used to execute any part of the function.
2.  Check that completion of the function is on the up-event, and a mechanism is available to abort the function before completion or to undo the function after completion.
3.  Check that the up-event reverses any outcome of the preceding down-event.
4.  Check that completing the function on the down-event is essential.

**Expected results**

-   Any of #1, #2, #3, or #4 is true.

##### Core requirement: Simple pointer input availableDeveloping

All functionality and content available using [complex pointer inputs](https://www.w3.org/TR/wcag-3.0/#dfn-complex-pointer-input) is also available using a [simple pointer input](https://www.w3.org/TR/wcag-3.0/#dfn-simple-pointer-input) or a sequence of simple pointer inputs that do not require timing.

Note 1

Complex pointer inputs are not banned, but they cannot be the only way to accomplish an action.

Note 2

Simple pointer input is different than [single pointer input](https://www.w3.org/TR/wcag-3.0/#dfn-single-pointer-input) and is more restrictive than simply using a single pointer.

Tests

_This section is non-normative._

**Procedure**

For each functionality that uses pointer input other than simple pointer input:

1.  Check that it can also be operated by a simple pointer input or a sequence of simple pointer inputs that do not require timing.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Consistent pointer cancellationDeveloping

The [method](https://www.w3.org/TR/wcag-3.0/#dfn-method) of [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) cancellation is consistent for each type of interaction within a set of [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view).

**Except when**

-   It is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to be different.

Note

Where it is essential to be different, it can be helpful to alert the user.

Tests

_This section is non-normative._

**Procedure**

For each type of pointer interaction:

1.  Check that it can be cancelled with a consistent interaction.

**Expected results**

-   #1 is true.

##### Core requirement: Pointer pressure not relied onDeveloping

Specific [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) pressure is not the only way of achieving any functionality.

**Except when**

-   Specific pressure is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to the functionality.

Note

Methods & best practices:

Method: When building in functionality that relies on pointer pressure, add a slider or other control that can complete the same functionality.

Tests

_This section is non-normative._

**Procedure**

For each instance of interactive content:

1.  Check that pointer pressure is not the only way to achieve any functionality.

**Expected results**

-   #1 is true.

##### Core requirement: Pointer speed not relied onDeveloping

Functionality does not rely solely on specific [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) speed.

**Except when**

-   Specific pointer speed is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to the functionality.

Tests

_This section is non-normative._

**Procedure**

For each instance of functionality that uses a pointer:

1.  Check that pointer speed is not the only way to achieve any functionality.

**Expected results**

-   #1 is true.

#### Guideline 2.4.4 Speech and voice input

Provide alternatives to speech input and facilitate speech control.

##### Core requirement: Speech not relied onDeveloping

Content or functionality does not rely on speech alone.

**Except when**

-   Speech input is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to the functionality.

Editor's note

Methods & best practices

Method: When speech input is supported, an additional way of providing input is also supported.

Tests

_This section is non-normative._

**Procedure**

For each functionality or content that is accessed using speech input:

1.  Check that there is another way to complete the functionality.

**Expected results**

-   #1 is true.

##### Core requirement: Real-time text availableDeveloping

A real-time text option is available for real-time bidirectional voice communication.

Editor's note

Methods & best practices

Method: Provide a chat option for any voice communication

Tests

_This section is non-normative._

**Procedure**

For each places where speech is used for communication (with human or AI):

1.  Check that there is an alternative way to achieve the same function using real-time text.

**Expected results**

-   #1 is true.

##### Assertion: Generated speech testingDeveloping

\[Title, role, or organization\] asserts that:

-   We have tested voice input and communication systems with generated speech to ensure the systems work with artificial speech as well as human speech.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the policy was implemented.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Systems tested.
-   Accuracy rates.

#### Guideline 2.4.5 Input operation

Users have the option to use different input techniques and combinations and switch between them.

##### Core requirement: Hover or focus content dismissibleDeveloping

A [mechanism](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) is available to dismiss [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that appears on [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) hover or [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) without moving pointer hover or keyboard focus, unless the additional content does not obscure or replace other content

**Applies when**

-   Receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, and the visual presentation of the additional content is controlled by the author and not by the [user agent](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent).

Note

This applies to content that appears in addition to the triggering of the [interactive element](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) itself. Since hidden interactive elements that are made visible on keyboard focus (such as links used to skip to another part of a [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view)) do not present additional content, they are not covered by this [requirement](https://www.w3.org/TR/wcag-3.0/#dfn-requirement).

Tests

_This section is non-normative._

**Procedure**

For additional content that appears on hover:

1.  Check that the content can be closed without moving the pointer way from the trigger. Either by pressing Esc, by pressing another documented keyboard shortcut, or by activating the trigger.

For additional content that appears on focus:

1.  Check that the content can be closed without moving the focus away from the trigger. Either by pressing Esc, by pressing another other documented keyboard shortcut, or by activating the trigger.

**Expected results**

-   For additional content that appears on hover: #1 is true.
-   For additional content that appears on focus: #1 is true.

##### Core requirement: Hover content persistentDeveloping

If pointer hover can trigger [content](https://www.w3.org/TR/wcag-3.0/#dfn-content), then the pointer can be moved over the additional content without the additional content disappearing.

**Applies when**

-   Receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, and the visual presentation of the additional content is controlled by the author and not by the [user agent](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent).

Note

This applies to content that appears in addition to the triggering of the [interactive element](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) itself. Since hidden interactive elements that are made visible on keyboard focus (such as links used to skip to another part of a [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view)) do not present additional content, they are not covered by this [requirement](https://www.w3.org/TR/wcag-3.0/#dfn-requirement).

Tests

_This section is non-normative._

**Procedure**

For additional content that appears on hover:

1.  Check that the pointer can be moved over the additional content without the additional content disappearing.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Hover or focus content persistentDeveloping

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that appears on [pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer) hover or [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) remains visible until the hover or keyboard focus trigger is removed, the user dismisses it, or its information is no longer valid.

**Applies when**

-   Receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, and the visual presentation of the additional content is controlled by the author and not by the [user agent](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent).

Note

This applies to content that appears in addition to the triggering of the [interactive element](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) itself. Since hidden interactive elements that are made visible on keyboard focus (such as links used to skip to another part of a [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view)) do not present additional content, they are not covered by this [requirement](https://www.w3.org/TR/wcag-3.0/#dfn-requirement).

Tests

_This section is non-normative._

**Procedure**

For additional content or focus that appears on hover:

1.  Check that the additional content stays visible and does not automatically close after a time.

**Expected results**

-   #1 is true.

##### Core requirement: Path-based gesture not relied onDeveloping

[Path-based gestures](https://www.w3.org/TR/wcag-3.0/#dfn-path-based-gesture) are not the only way of achieving any functionality.

**Except when**

-   A path-based gesture is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to the functionality.

Tests

_This section is non-normative._

**Procedure**

For each path-based gesture:

1.  Check that the functionality is available without a path-based gesture.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Input method flexibleDeveloping

The ability to switch between input [methods](https://www.w3.org/TR/wcag-3.0/#dfn-method) is available at any time.

Note

This does not mean that all input technologies ([pointer](https://www.w3.org/TR/wcag-3.0/#dfn-pointer), keyboard, voice, [gesture](https://www.w3.org/TR/wcag-3.0/#dfn-gesture)) need to be supported, but if an input modality is supported, it is supported everywhere in the [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) except where a particular input method is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to the functionality.

Tests

_This section is non-normative._

**Procedure**

For each input:

1.  Set up multiple input types (pointer, keyboard, voice, gesture, etc.)
2.  Check that you can switch between inputs and complete functionality

**Expected results**

-   #2 is true.

##### Core requirement: Body movements not relied onDeveloping

Functionality does not rely solely on full or gross body movement.

**Except where**

-   Full or gross body movement is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) to the functionality.

Note

This includes both detection of body movement and actions to the device, such as shaking, that require body movement.

Tests

_This section is non-normative._

**Procedure**

For each instance of functionality that uses body movement:

1.  Check that the body movement is not the only way to achieve any functionality.

**Expected results**

-   #1 is true.

##### Core requirement: Eye tracking not relied onDeveloping

Content and functionality does not rely solely on eye tracking.

**Except when**

-   Eye tracking is essential.

Note 1

This is primarily aimed at ensuring there is an alternative for people who cannot use eye-tracking (but do have sight) due to eye conditions.

Note 2

Some platforms may only allow eye tracking. Ideally the platforms allow additional mechanisms for control.

Tests

_This section is non-normative._

**Procedure**

For platforms that use eye-tracking for pointer use:

1.  Check that alternative, such as using a switch control, is available.

**Expected results**

-   #1 is true.

##### Core requirement: Pointer accessibleDeveloping

Pointer selection of elements moves the [keyboard focus](https://www.w3.org/TR/wcag-3.0/#dfn-keyboard-focus) to that element, even if the user selects an [interactive element](https://www.w3.org/TR/wcag-3.0/#dfn-interactive-element) and drags away from the element without activation.

**Applies when**

-   Content can interfere with pointer or keyboard focus behavior.

Tests

_This section is non-normative._

**Procedure**

For every interactive element that allows pointer selection (including click events on non-interactive elements):

1.  Check that the keyboard focus moves when the pointer selects the element.

**Expected results**

-   #1 is true.

#### Guideline 2.4.6 Authentication

Users have alternative authentication [methods](https://www.w3.org/TR/wcag-3.0/#dfn-method) available to them.

##### Core requirement: Biometrics not relied onDeveloping

[Biometric](https://www.w3.org/TR/wcag-3.0/#dfn-biometric) identification is not the only way to identify or authenticate.

Note 1

Biometrics includes facial recognition software, fingerprinting, vocal patterns and other voice characteristics.

Note 2

Methods & best practices

-   Method: When requiring biometric information for authentication, provide an additional way to authenticate that is not biometric. For example, if a finger print is required for authentication, then a password must also be supported.

Tests

_This section is non-normative._

**Procedure**

For each method of biometric user authentication:

1.  Check that there is at least one other method of non-biometric authentication.

**Expected results**

-   #1 is true.

##### Core requirement: Voice identification not relied onDeveloping

Voice identification is not the only way to identify or authenticate.

Tests

_This section is non-normative._

**Procedure**

For each place where voice is used for identification:

1.  Check that there is an alternative way to achieve authentication.

**Expected results**

-   #1 is true.

### 2.5 Error handling

#### Guideline 2.5.1 Correct errors

Users know about and can correct errors.

##### Core requirement: Error notifications availableDeveloping

Errors that are [programmatically determined](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable) are identified and the problem is described to the user in text.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Trigger errors.
2.  For each error, check that the nature of the problem is identified and described.

**Expected results**

-   #2 is true for each error.

##### Supplemental requirement: Error suggestions providedDeveloping

Error messages include suggestions for corrections.

**Applies when**

-   Errors require corrections by the user.

**Except when**

-   including suggestions would jeopardize the security or purpose of the [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

Tests

_This section is non-normative._

**Procedure**

For each error message:

1.  Check that the error needs correction by the user.
2.  Check that the error message includes suggestions for how to fix the error.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Errors indicated in multiple waysDeveloping

Error messages are visually indicated using at least two of the following:

-   A symbol that is consistent throughout the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope).
-   Color that differentiates the error message from surrounding [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).
-   Text that clearly indicates the error.

Tests

_This section is non-normative._

**Procedure**

For each validation error:

1.  Check that it meets at least two of the listed indicators (symbol, color or text).

**Expected results**

-   #1 is true.

##### Supplemental requirement: Error messages persistentDeveloping

Error messages persist at least until the error is resolved or the user dismisses them.

Editor's note

Methods & best practices

-   Method: Keep track of the state of the error and make visibility of the error message depending on this state.
-   Method: In a form, revalidate all fields when the form is submitted and remove all error messages that are no longer relevant.
-   Method: Add a “Dismiss” button to the error that makes the error message disappear.
-   Best Practice: \[1-2 sentence description or a link to an example\]

Tests

_This section is non-normative._

**Procedure**

For each error messages:

1.  Check that the error message persists until the user fixes the error or dismisses the message.

**Expected results**

-   #1 is true.

##### Core requirement: Errors associatedDeveloping

When input validation fails, the errors are visually and programmatically associated with the element that caused the error or that can resolve it.

Tests

_This section is non-normative._

**Procedure**

For each validation error:

1.  Check that validation error is indicated visually.
2.  Check that validation error is indicated programmatically.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Error messages collocatedDeveloping

Error messages are [visually collocated with](https://www.w3.org/TR/wcag-3.0/#dfn-visually-collocated-with) the error source or the focus is moved to the error message and a mechanism is available to move to the input that is in error.

**Applies when**

-   Error messages relate to user input.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Zoom in 400%
2.  Trigger errors
3.  Check that the error is visible next to the trigger or that the focus moves to the error.

**Expected results**

-   #3 is true.

#### Guideline 2.5.2 Prevent errors

Users can review, confirm and fix information they submit in order to prevent errors.

##### Core requirement: Errors preventableDeveloping

Data entry interfaces allow for users to do at least one of the following before submission:

-   Review, confirm, and correct all information; or
-   Review and correct input errors found during validation.

**Except when**

-   entered data is auto-saved and/or reversible.

Editor's note

Editors are looking at removing the grey area that may exist in this requirement due to interpretations of the word “submission“ (pressing “Submit” in the UI or receiving information server-side).

Tests

_This section is non-normative._

**Procedure**

For each data entry point:

1.  Check that users can return at any point in the process to correct data they entered.
2.  If it’s not possible to go back and correct the data during the process, check that the information being submitted can be reviewed and corrected before submission, or that it’s validated and can be fixed before submission.

**Expected results**

-   #1 is true, or
-   #2 is true.

##### Supplemental requirement: Submission status notifiedDeveloping

Data entry interfaces notify users of submission status at the time of submission.

**Applies when**

-   data submission has succeeded or failed.

Tests

_This section is non-normative._

**Procedure**

For each data submission:

1.  Check that the user is notified about the submission immediately afterwards.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Data entry validatedDeveloping

Data entered is validated after the user enters data, either:

-   when the user leaves the field, or
-   when the form is submitted.

Tests

_This section is non-normative._

**Procedure**

1.  Check that no validation has not occurred before data entry.
2.  Enter data.
3.  Check that validation is provided immediately after data entry or occurs before submission.

**Expected results**

-   #1 and #2 are true.

##### Assertion: Error prevention reviewDeveloping

\[Title, role or organization\] asserts that:

-   For each form in the conformance claim, we have reviewed the form designs to reduce the possibility of users making mistakes.

This review includes checking to make sure that we:

-   make the user enter as little information as possible,
-   clearly indicate required fields, for long numbers, divide input fields into chunks (supporting autocomplete across fields),
-   use an interface where only valid input can be selected,
-   use autocomplete and personalization of form controls,
-   use common words and metrics or units that users are likely to be familiar with,
-   automatically correct input errors when possible and reliable, and
-   provide the user with known suggestions and corrections.

Information that needs to be included publicly:

-   Title, role or organization making the assertion
-   Date of assertion (if different from the date of the conformance claim)

Recommended internal documentation (Informative):

-   Documentation of which forms were reviewed
-   Documentation of any changes made as a result of the review
-   Date of usability testing, if applicable

### 2.6 Animation and movement

Users do not experience physical harm from [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

##### Core requirement: No flashingDeveloping

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) does not include [flashing](https://www.w3.org/TR/wcag-3.0/#dfn-flash).

**Except when**

-   The flashing is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome).

Editor's note

**Method(s)**

-   Consider if flashing is essential and, if it is not, refrain from including it.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Check if content includes flashing.
2.  For each instance of flashing, check that the flashing is essential.

**Expected results**

-   #1 is false, or
-   #2 is true.

##### Supplemental requirement: No flashing (no exceptions)Developing

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) does not include [flashing](https://www.w3.org/TR/wcag-3.0/#dfn-flash).

Editor's note

**Method(s)**

-   Design content without using [flashing](https://www.w3.org/TR/wcag-3.0/#dfn-flash).

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Check if content includes flashing.

**Expected results**

-   #1 is false.

##### Core requirement: No visual motionDeveloping

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) does not include [pseudo-motion](https://www.w3.org/TR/wcag-3.0/#dfn-pseudo-motion) or visual motion lasting longer than 5 seconds.

**Except when**

-   The motion or pseudo-motion is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome).

Editor's note

**Method(s)**

-   Consider if motion or pseudo-motion is essential, and if it is not, refrain from including it.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Check if content includes visual motion or pseudo-motion.
2.  For each instance, check that the visual motion or pseudo-motion is essential.

**Expected results**

-   #1 is false, or
-   #2 is true.

##### Supplemental requirement: No visual motion (no exceptions)Developing

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) does not include [pseudo-motion](https://www.w3.org/TR/wcag-3.0/#dfn-pseudo-motion) or visual motion lasting longer than 5 seconds.

Editor's note

**Method(s)**

-   Design content without using visual motion or pseudo-motion.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Check if content includes visual motion or pseudo-motion.

**Expected results**

-   #1 is false.

##### Core requirement: Trigger warning availableDeveloping

A warning is provided before users encounter triggers and a mechanism is available to access the same information without the triggering [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

**Applies when**

-   triggers are present

Note

Note: Triggers are flashing, motion lasting more than 5 seconds, and pseudo-motion.

Editor's note

**Method(s)**

-   Provide a warning for triggers and provide an option without the triggers.

Tests

_This section is non-normative._

**Procedure**

For each trigger:

1.  Check if a warning is provided before the user encounters the trigger.
2.  Check that the same information is available without triggers.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: Haptic stimulation adjustableDeveloping

Haptic feedback can be reduced or turned off.

**Applies when**

-   content triggers haptic feedback.

**Except when**

-   the operating system or user agent converts non-haptic feedback to haptics at user request.

Editor's note

**Method(s)**

-   Add a setting to reduce haptic feedback or turn it off.

Tests

_This section is non-normative._

**Procedure**

For haptic feedback caused by the digital content (vs. the operating system or user agent).

1.  Check if there is a setting that allows for reducing or turning off the haptic feedback.

**Expected results**

-   #1 is true.

##### Core requirement: Audio shifting adjustableDeveloping

Audio shifting designed to create a perception of motion can be paused or turned off.

**Applies when**

-   content includes audio shifting.

**Except when**

-   operating system or user agent triggers audio shifting.

Editor's note

**Method(s)**

-   Add a setting to pause audio-shifting or turn it off.

Tests

_This section is non-normative._

**Procedure**

For audio shifting caused by the digital content (vs. the operating system or user agent):

1.  Check that there is a setting to pause or turn off the audio shifting.

**Expected results**

-   #1 is true.

##### Assertion: Safe content reviewDeveloping

\[Title, role, or organization\] asserts that:

-   We have reviewed content for violent, explicit, or troubling content and provided appropriate warnings before accessing the content.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the review was conducted.
-   Date of assertion (if different from the date of the conformance claim).

Note

Troubling content will vary based on culture or individual situations, and reviews should take target audiences into consideration.

### 2.7 Layout

#### Guideline 2.7.1 Recognizable layouts

Users have consistent and recognizable layouts available.

##### Assertion: Conventional layout reviewDeveloping

\[Title, role, or organization\] asserts that:

-   We have reviewed layout conventions for similar products or processes.
-   The layout used follows a conventional pattern or a tested non-conventional pattern was used.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Report covering review of layouts for similar products or processes.
-   Design log capturing decision to use specific layouts.
-   If a non-convention layout is used, usability testing results that demonstrate the utility of the approach taken.

#### Guideline 2.7.2 User orientation

Users can determine their location in [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) both visually and using assistive technologies.

##### Core requirement: Page/view title availableDeveloping

[Pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view) have a title that describes the name, topic or purpose.

**Except when**

-   The presented content has no way to include a title.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Examine the source code of the HTML document and check that the first `title` element is not-empty.
2.  Check that the title element describes the document.

**Expected results**

-   #1 and #2 are true.

##### Assertion: Location within product reviewDeveloping

\[Title, role, or organization\] asserts that:

-   We have reviewed conventions for presenting current location within the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope).
-   The presentation of current location within the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) uses appropriate visually and programmatically patterns.

Note

It is often helpful for users to understand where within a digital product they are. There are many ways to achieve this, for example, a breadcrumb. Ideally this is consistently presented throughout the conformance scope but for some pages/views it may make less sense to include. For example, including a breadcrumb trail on the homepage or on pages that sit outside the hierarchy, for example a shopping cart.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Design log capturing decision to use specific approaches to current location patterns used within the conformance scope.
-   If a non-convention design pattern is used, usability testing results that demonstrate the utility of the design approach taken.

##### Core requirement: All steps listedDeveloping

A list of all steps in a multi-step process is visually and programmatically available at each step.

**Except when**

-   The total number of steps is unknown, or the sequence of steps depends on user actions.

Tests

_This section is non-normative._

_Visual multi-step listing_

**Procedure**

For each multi-step process:

1.  Review the content within each stage of a multi-step process.
2.  A list of steps in the process is included on each stage.

**Expected results**

-   #2 is true.

_HTML multi-step listing_

**Procedure**

For each multi-step process:

1.  Examine the HTML source code for each step of the process.
2.  An `<ol>` is included with a `<li>` for each step of the process at each step.
3.  The `<ol>` is included in the accessibility tree.

**Expected results**

-   #2 and #3 are true.

##### Core requirement: Current step indicatedDeveloping

The current step within a multi-step process is visually and programmatically indicated.

Tests

_This section is non-normative._

_ARIA current_

**Procedure**

For each multi-step process:

1.  Examine the source code of the HTML document.
2.  Process navigation steps are included.
3.  Current process step is identified using `aria-current="step"`.

**Expected results**

-   Check #2 and #3 are true.

_Current step visually identifiable_

**Procedure**

For each multi-step process:

1.  Visually examine the content.
2.  Process navigation steps are viewable.
3.  The current process step is visually distinguishable from other steps.

**Expected results**

-   Check #2 and #3 are true.

##### Core requirement: Page/view change notifiedDeveloping

When content triggers a change of page/view there is a visual change within the view and programmatic notification of the change.

Tests

_This section is non-normative._

_Opening new page_

**Procedure**

For each change of page/view triggered by content:

1.  Check that the change is conveyed in the view.
2.  Check that the change is conveyed programmatically using the assistive technology in the accessibility support set.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Return to start supportedDeveloping

A visual and programmatically available mechanism exists that allows users to return to the [starting point](https://www.w3.org/TR/wcag-3.0/#dfn-starting-point) of the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope).

**Except when**

-   The [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) is the starting point of the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope).
-   It is essential to the functionality not to provide this mechanism.

Note

Where the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) is a sub-part of larger digital product, then the starting point should be the conformance scope starting point. For example, an organization’s careers website that is separate from the main website.

Tests

_This section is non-normative._

_HTML homepage link_

**Procedure**

For each page/view that is not the website’s home page:

1.  Check that there is a link that points to the website’s home page.

**Expected results**

-   #1 is true.

##### Best practice: Return to start prominentDeveloping

Mechanisms that return the user to the [starting point](https://www.w3.org/TR/wcag-3.0/#dfn-starting-point) of the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) are available in prominent positions both programmatically and visually.

Note

For HTML, a good programmatic positioning of such a mechanism would be early in the DOM.

#### Guideline 2.7.3 Structure

Users can understand and navigate through the [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) using structure.

Editor's note

See also: [Clear Language](https://www.w3.org/TR/wcag-3.0/#clear-language) as these guidelines are closely related.

##### Supplemental requirement: Relationships detectableDeveloping

[Relationships of meaning](https://www.w3.org/TR/wcag-3.0/#dfn-relationship-of-meaning) between elements are conveyed programmatically.

Tests

_This section is non-normative._

_HTML hierarchical relationship_

**Procedure**

1.  Determine the contextual hierarchy of the content either visually or through the meaning of the content.
2.  Examine the source code of the HTML document to identify each hierarchical section.
3.  Check that each section uses an appropriate semantic HTML element that reflects its position in the hierarchy.

**Expected results**

-   #3 is true.

_HTML input field/label relationship_

**Procedure** For each input field within the unit of conformance:

1.  Check that each `<input>`, `<select>` and `<textarea>` in the source code has a programmatically associated `<label>` using `for` and `id` attributes.

**Expected results**

-   #1 is true.

_HTML list relationship_

**Procedure**

For each list within the unit of conformance:

1.  Check that each list consists of a `<ul>`, `<ol>` or `<dl>`.
2.  Check that each list item within the list is contained within an `<li>` element (for `<ul>` and `<ol>`) or `<dt>`/`<dd>` pair (for `<dl>`).
3.  Check that the immediate child element of the list is an `<li>` element (for `<ul>` and `<ol>`) or `<dt>`/`<dd>` pair (for `<dl>`).

**Expected results**

-   #1, #2 and #3 are true.

_HTML nested list relationship_

**Procedure**

For each nested list within the unit of conformance:

1.  Check that all child lists are contained within a `<li>` of the parent list.

**Expected results**

-   #1 is true.

##### Core requirement: Blocks of content available (minimum)Developing

[Meaningful blocks of content](https://www.w3.org/TR/wcag-3.0/#dfn-meaningful-blocks-of-content) are programmatically determinable and visually presented with sufficient surrounding space.

Tests

_This section is non-normative._

_HTML sufficient space_

**Procedure**

1.  Identify meaningful blocks of content in the page/view that are not bounded by a visual border.
2.  Examine the computed style to determine the total of margin, padding and border spacing.
3.  The spacing between all adjacent meaningful blocks of content is sufficient.

**Expected results**

-   #3 is true.

_Programmatically identifiable meaningful blocks of content_

**Procedure**

For each meaningful blocks of content in the page/view:

1.  Check that an appropriate role is being used for the meaningful blocks of content in the source code.
2.  Check using assistive technology that an appropriate role is being used for the meaningful blocks of content.

**Expected results**

-   #1 or #2 is true.

##### Core requirement: Sections labeledDeveloping

[Meaningful blocks of content](https://www.w3.org/TR/wcag-3.0/#dfn-meaningful-blocks-of-content) have a semantically appropriate [label](https://www.w3.org/TR/wcag-3.0/#dfn-label) that defines their purpose.

**Except when**

-   A label is not needed to understand the purpose of the content within the context of use.

Editor's note

-   Add example(s) of labels and heading usage

Tests

_This section is non-normative._

_Meaningful label_

**Procedure**

1.  Review content and identify meaningful blocks with labels.
2.  Each label correctly describes the block.

**Expected results**

-   #2 is true.

_Label exists_

**Procedure**

1.  Review content and identify meaningful blocks.
2.  Each block has a label that describes the block.

**Expected results**

-   #2 is true.

_HTML heading semantics_

**Procedure**

1.  Visually identify each meaningful blocks.
2.  Heading text is marked up using an `<h?>` element.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Heading structure availableDeveloping

[Meaningful blocks of content](https://www.w3.org/TR/wcag-3.0/#dfn-meaningful-blocks-of-content) are organized with a logical hierarchy of headings.

**Except when**

-   The technology does not support heading levels.

Tests

_This section is non-normative._

_Headings set at right level_

**Procedure**

For the hierarchy of headings:

1.  Check that headings for sibling content blocks have the same heading level.
2.  Check that headings for immediate child content blocks should be at most one level higher than parent content blocks.

**Expected results**

-   #1 and #2 are true.

_HTML Heading levels not skipped_

**Procedure**

For each page/view:

1.  Review the hierarchy of headings.
2.  Each heading level should be at most one numerical level higher than the preceding heading.

**Expected results**

-   #2 is true.

##### Core requirement: Order detectableDeveloping

Ordered content includes programmatically determinable markers that indicate the position of each item.

**Except when**

-   The nature of the ordering of the content is presented immediately prior.

Note

This includes lists and processes

Tests

_This section is non-normative._

_Process steps_

**Procedure**

For each ordered process:

1.  Check that each step in the process includes an indicator of its position within the process.

**Expected results**

-   #1 is true.

_HTML ordered lists_

**Procedure**

For each ordered list:

1.  Examine the HTML code and check that each ordered list is marked up with an `<ol>` element.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Blocks of content available (enhanced)Developing

Styling is used to enhance the visual separation between [meaningful blocks of content](https://www.w3.org/TR/wcag-3.0/#dfn-meaningful-blocks-of-content).

Tests

_This section is non-normative._

_Visually identifiable meaningful blocks of content_

**Procedure**

For each meaningful block of content in the page/view:

1.  Check that each meaningful block of content is grouped by one or more of the following characteristics:
    -   Color or lightness — the same color scheme is used (Note that this should also meet requirements for ‘Color alone’ and ‘Contrast’)
    -   Borders — blocks are contained within the same borders
    -   Spacing — blocks are grouped based on their proximity to others within the same area, while spacing is used to separate different sections of content
    -   Font — blocks are presented with similar font families
    -   Position — blocks are located in the same area of the page/view (for example, header, navigation, footer)
    -   Repeated visual feature — blocks contain a consistent visual feature (for example, bullets in a list, checkbox)

**Expected results**

-   #1 is true.

##### Assertion: Clear structure reviewDeveloping

\[Title, role, or organization\] asserts that:

-   Our organization has a process and policy for reviewing written content for clear structure before publication. The process includes confirming:
    -   all of the core requirements in the Structure guideline are met
    -   content sections are as concise as possible
    -   icons are considered as possible ways to help users understand the content structure and identify key parts, and
    -   authors consider when to turn sentences into lists to make the information easier to understand and remember
-   If a style guide is used by authors, it must provide guidance on these aspects of clear structure.
-   If author training is provided, it must provide guidance on these aspects of clear structure.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the policy was implemented.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Copy of the policy implementing the clear structure review.
-   Whether training was provided for authors
    -   Date training was provided.
    -   Number or proportion of authors who completed the training.
-   A copy of the style guide (if any) where clear structure review has been defined.

##### Assertion: Key information usability testingDeveloping

\[Title, role or organization\] asserts that:

-   We conducted usability testing to ensure that a diverse group of users, including people with cognitive and mental health challenges, understand the site’s information hierarchy and menu organization and are able to find key information.

Information that needs to be included publicly:

-   Title, role or organization making the assertion
-   Date of assertion
-   Date of the testing

Recommended internal documentation (Informative):

-   Documentation of usability testing and results
-   Scope of testing
-   Number of participants and disabilities represented
-   Documentation of changes made as a result of usability findings

#### Guideline 2.7.4 No obstruction

Users can perceive and operate user interface [components](https://www.w3.org/TR/wcag-3.0/#dfn-component) and navigation without obstruction.

##### Core requirement: Overlay content dismissibleDeveloping

When new content becomes visible and covers the main content, a mechanism is available to dismiss the new content.

Editor's note

Methods

-   The ‘Escape’ (Esc) key closes new content.
-   An accessible ‘close’ button is provided to close the new content.

Tests

_This section is non-normative._

_Modal dialogs on interaction_

**Procedure**

For each element that opens a modal dialog when interacted with:

1.  Open the dialog.
2.  Check that the dialog includes a mechanism to allow the dialog to be dismissed.

**Expected results**

-   #2 is true.

### 2.8 Consistency across views

Users have consistent and alternative [methods](https://www.w3.org/TR/wcag-3.0/#dfn-method) for navigation.

##### Supplemental requirement: Consistent structural orderDeveloping

The relative order of [structural components](https://www.w3.org/TR/wcag-3.0/#dfn-structural-component) remains consistent throughout each variation of [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view) in the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope).

**Applies when**

-   In a set of [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view)

Note

Relative order means that content can be added or removed, but repeated items are in the same order relative to each other.

Tests

_This section is non-normative._

_Consistent relative order for website_

**Procedure**

For each variation of [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view) in the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope):

1.  Identify common structural components across multiple pages/views.
2.  Check that components are presented in the same order within each page/view.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Consistent navigation orderDeveloping

The relative order of navigation items is consistent within blocks of navigation that are repeated on multiple pages/views of the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) or process.

**Applies when**

-   In a set of [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view)

Editor's note

This relates to consistency and terminology within blocks of navigation. The consistent ordering of blocks of navigation within a page/view is covered by ‘Consistent relative order’.

Tests

_This section is non-normative._

_Consistent main navigation relative order_

**Procedure**

For each repeated blocks of navigation across multiple pages/views of the conformance scope or process:

1.  Check that the navigation items within each block of navigation have the same relative order across all pages/views of the conformance scope or process.

**Expected results**

-   #1 is true.

##### Supplemental requirement: Consistent navigation labelsDeveloping

The labelling of navigation items within blocks of navigation that are repeated on multiple pages/views in the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) or process is consistent.

**Except when**

-   Labels for navigation items that are marked as ‘current’ within the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) or process.

Editor's note

This relates to consistency and terminology within blocks of navigation. The consistent ordering of blocks of navigation within a page/view is covered by ‘Consistent relative order’.

Tests

_This section is non-normative._

_Consistent main navigation labels_

**Procedure**

For each repeated block of navigation across multiple pages/views of the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) or process:

1.  Check that the navigation items within each block of navigation have the same names across all pages/views of the conformance scope or process.

**Expected results**

-   #1 is true.

### 2.9 Process and task completion

#### Guideline 2.9.1 Avoid exclusionary cognitive tasks

Users can complete tasks without needing to memorize nor complete advanced cognitive tasks.

##### Core requirement: Automated entry allowedDeveloping

Automated input of personal information from user agents, third-party tools, or paste is not prevented.

Note

Personal information includes names, passwords, et cetera.

Tests

_This section is non-normative._

**Procedure**

For each form that requests personal information:

1.  Ensure there is a test identity set up in the browser.
2.  Navigate to a form requiring the input of personal information.
3.  Check that the browser tools automatically populate personal information into the form.

**Expected results**

-   #3 is true.

##### Core requirement: Cognitive test alternatives availableDeveloping

[Processes](https://www.w3.org/TR/wcag-3.0/#dfn-process), including authentication, can be completed without a [cognitive function test](https://www.w3.org/TR/wcag-3.0/#dfn-cognitive-function-test).

Tests

_This section is non-normative._

**Procedure**

For each form requiring the completion of a complex test, such as a puzzle, image identification, gesture reproduction, math question, or character recognition/entry:

1.  Check that there is an alternative provided that does not require completion of a cognitive function test.

**Expected results**

-   #2 is true.

#### Guideline 2.9.2 Adequate time

Users have enough time to read and use [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

##### Supplemental requirement: Timeout adjustableDeveloping

A mechanism exists to extend the time limit before timeout, or the time limit can be disabled.

**Applies when**

-   Time limit(s) exist.

**Except when**

-   The time limit is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome).

Tests

_This section is non-normative._

_Extend or disable at timeout_

**Procedure**

For each time limit:

1.  Check if there is a way to disable it.
2.  Wait for the timeout.
3.  Check that before the timeout, an option is given to extend the time limit.

**Expected results**

-   #3 is true.

##### Supplemental requirement: No time limitsDeveloping

The completion of a [process](https://www.w3.org/TR/wcag-3.0/#dfn-process) does not include time limits.

**Except when**

-   the time limit is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome), such as in an auction or timed exam.

Note

Implying to a user that they will lose a benefit if they don’t act immediately is not an essential time limit.

Tests

_This section is non-normative._

**Procedure**

For each page/view:

1.  Check if content includes time limits.

**Expected results**

-   #1 is false.

##### Assertion: No unnecessary time limitsDeveloping

\[Title, role, or organization\] asserts that:

-   Products and processes in scope have no non-essential time limits for engagement or completion.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of assertion.

##### Supplemental requirement: Time limits conveyedDeveloping

Users are informed at the start of the process or session that a time limit exists, its length, and that it can be adjusted.

**Applies when**

-   [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view) within the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) have a time limit

**Except when**

-   hiding the existence of the time limit is essential

Tests

_This section is non-normative._

**Procedure**

For each time limit:

1.  Check that a notification is provided to the user at the start of a process that the time limit exists, its length and that it can be adjusted.

**Expected results**

-   #1 is true.

#### Guideline 2.9.3 Avoid deception

Users do not encounter deception when completing tasks.

##### Core requirement: Preselections visibleDeveloping

During the completion of a [process](https://www.w3.org/TR/wcag-3.0/#dfn-process), preselected options that impact finance, privacy or safety are visibly and programmatically available to the user, by default.

Tests

_This section is non-normative._

**Procedure**

For all options that affect finance, privacy and safety”

1.  Check that the options are visible when completing a process.
2.  Check that that they are programmatically available before completing the process.

**Expected results**

-   #1 and #2 are true.

##### Assertion: Deceptive practices usability testingDeveloping

\[Title, role, or organization\] asserts that:

-   We conducted a usability test that included participants with cognitive disabilities and/or mental health based disabilities to evaluate content for misleading wording, artificial pressure, misdirection, and other deceptive practices
-   We removed any deceptive practices found.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of assertion.

Recommended internal documentation (Informative):

-   Number of participants.
-   The deceptive practices evaluated.
-   Maintain records of usability testing protocol, and results,
-   Disabilities represented within the group of participants.

##### Assertion: Deceptive messaging expert reviewDeveloping

\[Title, role, or organization\] asserts that:

-   We conducted an expert review to evaluate content for misleading wording, artificial pressure, misdirection, and other deceptive practices
-   We removed any deceptive practices found.

Information that needs to be included publicly:

-   Title, role or organization making the assertion.
-   Date of assertion.

Recommended internal documentation (Informative):

-   The deceptive practices evaluated.
-   Maintain records of deceptive practices found, and resolutions.

#### Guideline 2.9.4 Retain information

Users do not have to reenter information or redo work.

##### Supplemental requirement: Going back supportedDeveloping

In a multi-step [process](https://www.w3.org/TR/wcag-3.0/#dfn-process), the interface supports stepping backwards in a process and returning to the current point without data loss.

**Except when**

-   It is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome) that the user cannot step back in a process.

Tests

_This section is non-normative._

**Procedure**

For multi-step processes:

1.  Check that the user is prompted to review and confirm data.
2.  Check that the user is allowed to return to previous steps to review and change the data.
3.  Check that if a summary of all data input by the user is provided before the transaction is committed, and that a method is provided to correct errors, if necessary.

**Expected results**

-   #1, #2, or #3 is true.

##### Supplemental requirement: No redundant entryDeveloping

Information previously entered by or provided to the user that is required to be entered again in the same [process](https://www.w3.org/TR/wcag-3.0/#dfn-process) is either auto-populated, or available for the user to select.

**Except when**

-   re-entering the information is essential,
-   the information is required to ensure the security of the content, or
-   previously entered information is no longer valid.

Tests

_This section is non-normative._

**Procedure**

For any process that requires the user to enter information:

1.  Check whether the information has already been requested ion a previous step of the process.
2.  Check that the information entered previously is prepopulated in the respective field(s) or is displayed on the page for copying.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Progress savedDeveloping

Data entry and other task completion [processes](https://www.w3.org/TR/wcag-3.0/#dfn-process) allow saving and resuming from the current step in the task.

**Except when**

-   The task completion is part of a real-time event (for example, an auction or concert ticket purchase), and no alternative to the time limit is possible.

Tests

_This section is non-normative._

**Procedure**

For any processes that require the user to enter information:

1.  Log in, if needed, and begin the timed activity.
2.  Allow the session to time out.
3.  Submit or save the data.
4.  Log out if logged in.
5.  Re-authenticate and log back in.
6.  Check that the process can continue from where you left off and be completed without loss of data, including the original data and any changes made after re-authentication.
7.  Check that the process used to save the information submitted in step 3 is not stored on the server. (Note: This requires knowledge of the technology and features used to implement the technique.)

**Expected results**

-   #7 is true.

#### Guideline 2.9.5 Complete tasks

Users understand how to complete tasks.

##### Supplemental requirement: Required action availableDeveloping

The interface indicates when user input or action is required in order to proceed to the next step.

**Applies when**

-   The user needs to complete an action in order to proceed to the next step. For example: the user needs to agree to the terms and conditions before they can submit the form.

Tests

_This section is non-normative._

**Procedure**

For any parts of a process that cannot be completed without the user doing a required action:

1.  Enter in all the information except for the required action(s).
2.  Try to complete the process.
3.  Check that there is a notification that explains what the user needs to do before the process can be completed.

**Expected results**

-   #3 is true.

##### Supplemental requirement: Information requirements available at startDeveloping

Information and resources that are needed to complete a multi-step [process](https://www.w3.org/TR/wcag-3.0/#dfn-process) are provided at the start of the process, including the:

-   number of steps it might take (if known in advance),
-   details of any resources needed to perform the task, and
-   overview of the process and next step.

**Applies when**

-   the user needs to complete a multi-step process.

Tests

_This section is non-normative._

**Procedure**

At the start of each process:

1.  Identify any multi-step processes.
2.  If it can be determined in advance, check that the number of steps it will take to complete the process is provided at the start of the process.
3.  Check that the details of any information and resources that are needed to perform the task are provided at the start of the process.
4.  Check that an overview of the process and next steps are provided at the start of the process.

**Expected results**

-   #2 is true.
-   #3 is true.
-   #4 is true.

##### Supplemental requirement: Process instructions availableDeveloping

The instructions needed to complete a multi-step [process](https://www.w3.org/TR/wcag-3.0/#dfn-process) are available.

**Applies when**

-   The user needs to complete a multi-step process.

Tests

_This section is non-normative._

**Procedure**

For each multi-step process:

1.  Check that the steps and instructions needed to complete a multi-step process are provided.
2.  Check that any breadcrumb navigation correctly communicates the current step in the process.

**Expected results**

-   #1 and #2 are true.

#### Guideline 2.9.6 Unnecessary steps

Users can complete tasks without unnecessary steps.

##### Assertion: Usability testing for unnecessary stepsDeveloping

\[Title, role, or organization\] asserts that:

-   Usability testing has been conducted to review for unnecessary steps in the process or unnecessary information being requested.
-   The sample of test participants included people with cognitive disabilities and/or mental health based disabilities.

Information that needs to be included publicly:

-   Title, role or organization making the assertion.
-   Date of assertion.

Recommended internal documentation (Informative):

-   Maintain records of usability testing protocol, scope of the testing, and results.
-   Number of participants and disabilities represented within the group of participants.
-   Record of actions taken to address identified issues.

### 2.10 Policy and protection

#### Guideline 2.10.1 Risk

Users understand the benefits, risks, and consequences of options they select.

##### Core requirement: Consequences of choices explainedDeveloping

Choices with legal, financial, privacy, or security consequences are accompanied by a description of the benefits, risks, and potential consequences when users make the choice.

Tests

_This section is non-normative._

**Procedure**

For any choices being made by the user:

1.  Identify any potential legal, financial, privacy and security consequences to the user as a result of the choice.
2.  Check that the consequences are provided when the user makes the choice.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Consequences explained before agreementDeveloping

Legal, financial, privacy, and security consequences are provided before finalizing an agreement.

**Applies when**

-   Entering an agreement is required.

Tests

_This section is non-normative._

**Procedure**

For any agreements being made by the user:

1.  Identify any potential legal, financial, privacy and security consequences to the user as a result of the agreement.
2.  Check that the consequences are provided before the user enters into the agreement.

**Expected results**

-   #2 is true.

##### Assertion: Diverse disabilities consideredDeveloping

\[Title, role, or organization\] asserts that:

-   When considering the safety and security of our users, we considered use cases of people with diverse disabilities. For example, people with cognitive or learning disabilities are sometimes targeted on social media for sexual exploitation and other bad intent.
-   Research has been conducted on risks to safety, wellbeing, and mental health for users with diverse disabilities and, when risks are found, all reasonable practical steps have been identified and taken to mitigate the risk.

Information that needs to be included publicly:

-   Title, role or organization making the assertion
-   Date of assertion

Recommended internal documentation (Informative):

-   List of steps that have been taken
-   List of use cases used

##### Assertion: Algorithm inclusivity reviewDeveloping

\[Title, role, or organization\] asserts that:

-   We have a policy and process to review — and have reviewed — the data set, results, and/or algorithm in order to minimize the possibility that algorithms are disadvantageous for people with disabilities.

Information that needs to be included publicly:

-   Title, role or organization making the assertion
-   Date of assertion
-   Disabilities considered
-   What was reviewed (data set, results, or algorithm itself)
-   Review scope

Recommended internal documentation (Informative):

-   Results
-   Copy of any process and policy
-   Copy of usability testing, if conducted
-   Steps taken to resolve the issues found

#### Guideline 2.10.2 Algorithms

Users are not disadvantaged or harmed by algorithms.

##### Assertion: Inclusive data setDeveloping

\[Title, role, or organization\] asserts that:

-   [Content author(s)](https://www.w3.org/TR/wcag-3.0/#dfn-content-author) train AI models using representative and unbiased disability-related information that is proportional to the general population.

##### Assertion: No harm from algorithmsDeveloping

\[Title, role, or organization\] asserts that:

-   [Content author(s)](https://www.w3.org/TR/wcag-3.0/#dfn-content-author) conduct [usability testing](https://www.w3.org/TR/wcag-3.0/#dfn-usability-testing) and ethics reviews to minimize the possibility that algorithms disadvantage people with disabilities.

### 2.11 Help and feedback

#### Guideline 2.11.1 Help available

Users have help available.

##### Supplemental requirement: Consistent help availableDeveloping

Help is labeled consistently and is available in a consistent location relative to other content.

**Applies when**

-   human contact information, a human contact mechanism, a self-help option, or a fully automated contact mechanism is available.

Tests

_This section is non-normative._

**Procedure**

For each help item in a page / view:

1.  Check that it is labeled consistently
2.  Check that it remains in the same relative visual and programmatic location.

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Contextual help availableDeveloping

[Context-sensitive help](https://www.w3.org/TR/wcag-3.0/#dfn-context-sensitive-help) is available.

Tests

_This section is non-normative._

**Procedure**

For each interactive element:

1.  Check for potentially confusing or difficult interactions such as formatting restrictions or interdependencies.
2.  For any element identified in #1, check that context-sensitive help is available.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Disabled controls explainedDeveloping

Information explaining why a visible interactive element is disabled is available and, if the user can take action(s) to enable the element, those action(s) are described.

Tests

_This section is non-normative._

**Procedure**

For each visible disabled control:

1.  Check that instructions are available that explain how to enable it.

**Expected results**

-   #1 is true.

##### Core requirement: Sensory characteristics not relied onDeveloping

Instructions and help do not rely on sensory characteristics such as shape, color, size, visual location, orientation, or sound.

Tests

_This section is non-normative._

**Procedure**

For each reference to shape, size, or position of an object:

1.  Check that the reference includes additional information that allows the item to be located and identified without any knowledge of its shape, size, or relative position.

**Expected results**

-   #1 is true.

##### Assertion: Supported decision-making reviewDeveloping

\[Title, role, or organization\] asserts that:

-   We have conducted a review to identify when users need to make substantial decisions about money, privacy, or well-being. In these situations, additional support was provided such as:
    -   a clear layout of options advantages and disadvantages
    -   aids for comprehension such as icons and graphics
    -   reduced distractions

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the policy was implemented.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Results of review
-   Documentation of decisions and changes made as a result.

##### Assertion: Help usability testingDeveloping

\[Title, role, or organization\] asserts that:

-   Help and training was added based on usability testing with people with cognitive and mental health disabilities to identify gaps.

Information that needs to be included publicly:

-   Title, role or organization making the assertion (if different from the conformance claim).
-   Date of when the usability testing was conducted.
-   Date of assertion (if different from the date of the conformance claim).

Recommended internal documentation (Informative):

-   Usability findings
-   Solutions added

#### Guideline 2.11.2 Feedback

Users can provide feedback to [content author(s)](https://www.w3.org/TR/wcag-3.0/#dfn-content-author).

##### Supplemental requirement: Feedback mechanism availableDeveloping

A [mechanism](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) is available to provide feedback to authors.

Tests

_This section is non-normative._

**Procedure**

Within the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope):

1.  Check that a feedback mechanism exists.
2.  Check that the feedback is sent to authors.

**Expected results**

-   #1 and #2 are true.

### 2.12 User control

#### Guideline 2.12.1 Assistive technology control

Users can control [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) settings from their [user agents](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent) including [assistive technology](https://www.w3.org/TR/wcag-3.0/#dfn-assistive-technology).

##### Core requirement: Assistive technology supportedDeveloping

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) can be controlled using assistive and adaptive technology.

Tests

_This section is non-normative._

**Procedure**

For each page view:

1.  Check that each control can be operated using assistive technology and that operating the controls achieves the same results with and without assistive technology.
2.  Check that reading or experiencing non-interactive content produces the same results with and without assistive technology.

**Expected results**

-   #1 and #2 are true.

##### Core requirement: User settings supportedDeveloping

[Content](https://www.w3.org/TR/wcag-3.0/#dfn-content) responds to users’ platform and user agent accessibility-related settings.

Note

Accessibility-related user settings include font size, icon size, color scheme, magnification, and motion.

Tests

_This section is non-normative._

**Procedure**

For each setting:

1.  Change an accessibility-related setting in a platform or user agent in the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set).
2.  Check content to see that the setting has been applied.

**Expected results**

-   #2 is true.

##### Core requirement: Virtual cursor supportedDeveloping

Assistive technologies can access [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) and interactions when using [mechanisms](https://www.w3.org/TR/wcag-3.0/#dfn-mechanism) that convey alternative [points of regard](https://www.w3.org/TR/wcag-3.0/#dfn-point-of-regard) or focus (i.e. virtual cursor).

Tests

_This section is non-normative._

**Procedure**

For each setting:

1.  Access content and interactions by using mechanisms that convey alternative points of regard or focus
2.  Check that content is readable and interactions are operable.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Notifications adjustableDeveloping

The timing or positioning of notifications can be changed, suppressed or saved.

**Applies when**

-   Notifications or other interruptions are present.

**Except when**

-   The notification involves an emergency or is essential.

Tests

_This section is non-normative._

**Procedure**

For each notification:

1.  Check that settings allow the timing or location to be changed.

**Expected results**

-   #1 is true.

#### Guideline 2.12.2 Control text

Users can control [text](https://www.w3.org/TR/wcag-3.0/#dfn-text) presentation.

Editor's note

Requirements and assertions for this guideline do not appear here because they have not yet progressed beyond exploratory. See the [Editor's Draft](https://w3c.github.io/wcag3/guidelines/) for the complete list of potential requirements and assertions.

#### Guideline 2.12.3 Adjustable viewport

Users can adjust the size and orientation of the [viewport](https://www.w3.org/TR/wcag-3.0/#dfn-viewport), adjust text size of [content](https://www.w3.org/TR/wcag-3.0/#dfn-content), or zoom content without loss of legibility or functionality.

##### Core requirement: Orientation supported (minimum)Developing

If the platform has a [default orientation](https://www.w3.org/TR/wcag-3.0/#dfn-default-orientation), content supports that orientation. If the platform does not have a default orientation, content supports both portrait and landscape orientations.

**Except when**

-   Content is aligned with the physical world.
-   The orientation is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome).

Note 1

For extended reality, the platform default orientation aligns with the real world orientation.

Note 2

Content does not have to re-layout or change aspect ratio in a different orientation, it just needs to display in the device orientation.

Tests

_This section is non-normative._

**Procedure**

For platforms which have a default orientation:

1.  Open the content.
2.  Check that the orientation aligns with the platform default.

For platforms which do not have a default orientation:

1.  Open the content
2.  Check that the orientation can align with both portrait and landscape orientations.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Orientation supported (enhanced)Developing

Content supports both portrait and landscape orientations.

**Except when**

-   Content is aligned with the physical world.
-   The orientation is [essential](https://www.w3.org/TR/wcag-3.0/#dfn-essential-to-outcome).

Tests

_This section is non-normative._

**Procedure**

For platforms which do not have a default orientation:

1.  Open the content
2.  Check that the orientation can align with both portrait and landscape orientations.

**Expected results**

-   #2 is true.

##### Supplemental requirement: Text reflow supportedDeveloping

[Blocks of text](https://www.w3.org/TR/wcag-3.0/#dfn-block-of-text) are legible at 320 [CSS pixels](https://www.w3.org/TR/wcag-3.0/#dfn-css-pixel) in the orientation of text, without the need to scroll in the orientation of text.

**Except when**

-   The meaning of text relies on a two dimensional structure. For example, preformatted text such as code, poems, maps, or comics.

Editor's note

Tests

_This section is non-normative._

_HTML paragraph reflow without requiring scrolling in two dimensions_

**Procedure**

For each page/view:

1.  Set the viewport at 320 CSS pixels in the direction of text.
2.  Identify all the blocks of text within the scope.
3.  Check that each block of text does not require scrolling into two dimensions.
4.  Check that the text in each block of text is legible.

**Expected results**

-   #3 and #4 are true.

##### Supplemental requirement: Layout reflow supportedDeveloping

All content fits within 320 [CSS pixels](https://www.w3.org/TR/wcag-3.0/#dfn-css-pixel) in the default orientation of text without requiring scrolling in more than one direction. Sections of content within the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) that scroll in a different direction to the page/view fit within 320 CSS pixels of the page-scrolling direction.

**Except when**

-   2D relationships. For example, tables, electronic program guides.
-   Canvases of presentational content. For example, slides.
-   Multiple palettes or panels that act on content. For example, Photoshop, IDE.

Editor's note

All block-level elements fit within a 320px inline-size without requiring scrolling in more than one direction.

Tests

_This section is non-normative._

**Procedure**

1.  Set the viewport at 320px in the direction of text.
2.  Check that each section of content fits within 320 CSS pixels.

**Expected results**

-   #2 is true.

#### Guideline 2.12.4 Media control

Users can control media and media alternatives.

##### Core requirement: Page/view audio adjustableDeveloping

There are mechanisms to pause, stop, and adjust the volume independently of the overall system volume level, of any automatically playing [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) in a page / view.

**Applies when**

-   Notifications or other interruptions are present.

Note

Mechanisms include controls on each instance of content, or a single app-wide control that disables audio, for example: app-wide earcons.

Tests

_This section is non-normative._

**Procedure**

For each page / view:

1.  Check for audio that starts automatically.
2.  For audio content in a media player, check that the media player has controls that can pause, stop, or adjust the audio volume.
3.  For audio content set at an application level, check that there is a central setting that enables or disables audio across the application.
4.  Check that one of these are present: a. There is a mechanism within the first three elements in the page / view for the user to pause, stop, or adjust the audio volume; b. There are keyboard controls that can pause, stop, or adjust the audio volume.

**Expected results**

-   #2, #3, or #4 is true.

##### Supplemental requirement: Media alternatives searchableDeveloping

Alternatives for media can be searched and queried.

Tests

_This section is non-normative._

**Procedure**

For each instance of media with captions and / or transcripts:

1.  Check that a mechanism to search the captions or transcripts is available.
2.  Check that a mechanism to search and look up terms in transcripts is available. This can be:
    1.  copying and pasting content from the transcript into a dictionary; or
    2.  allowing a platform or application dictionary to show a definition of the term.
        -   Example: VoiceOver on MacOS includes a feature to look up terms for what is under a ‘mouse cursor point’

**Expected results**

-   #1 and #2 are true.

##### Supplemental requirement: Media alternatives controllableDeveloping

Closed [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions) and [audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) can be turned on and off.

Tests

_This section is non-normative._

**Procedure**

For each media asset with audio content:

1.  Check that a mechanism is available so that users can turn on and off the closed captions.
2.  Check that a mechanism is available so that users can change the audio track from a non-audio-described one to an audio-described.

**Expected results**

-   #1 and #2 are true.

#### Guideline 2.12.5 Content changes

Users know when [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) changes.

##### Core requirement: Change of content notifiedDeveloping

Meaningful changes in visual [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) are conveyed programmatically.

**Applies when**

-   The changes appear before the user’s current position in reader order.
-   The changes appear earlier in the process.
-   Notifications, status or error messages appear.
-   The amount of content changes.
-   The change affects the content’s meaning.
-   The audience changes.

**Except when**

-   changes are continuous, without pause.

Tests

_This section is non-normative._

**Procedure**

For each meaningful change of visual content:

1.  Check that the change is conveyed programmatically using the assistive technology in the accessibility support set.

**Expected results**

-   #1 is true.

##### Core requirement: Change of focus notifiedDeveloping

When the focus changes on-focus or automatically, the user is notified visually and programmatically.

Tests

_This section is non-normative._

**Procedure**

For each instance of focus being changed by the content:

1.  Check that the change is conveyed visually and programmatically using the assistive technology in the accessibility support set.

**Expected results**

-   #1 is true.

##### Core requirement: Change of user agent notifiedDeveloping

When content triggers a device change or an automatic user agent change, the user is notified before the change occurs.

Tests

_This section is non-normative._

**Procedure**

For each instance where the content triggers a change of device or user agent change:

1.  Check that the change is conveyed before the chance occurs.

**Expected results**

-   #1 is true.

## 3\. ConformanceExploratory

_This section (with its subsections) provides requirements which must be followed to conform to the specification, meaning it is [normative](https://www.w3.org/TR/wcag-3.0/#dfn-normative)._

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words _MAY_, _MUST_, _MUST NOT_, _NOT RECOMMENDED_, _RECOMMENDED_, _SHOULD_, and _SHOULD NOT_ in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) \[[RFC2119](https://www.w3.org/TR/wcag-3.0/#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")\] \[[RFC8174](https://www.w3.org/TR/wcag-3.0/#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")\] when, and only when, they appear in all capitals, as shown here.

Plain language summary of Interpreting normative provisions

You might want to make a claim that your [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) or digital product meets the WCAG 3 guidelines. When it meets the guidelines, you can make a "conformance claim".

To make a formal conformance claim, you must use the process described in this document. Conformance claims are not required. Your content can conform to WCAG 3, even if you don't want to make a claim.

WCAG 3 has two types of content:

-   **Normative:** Rules you _must_ follow to meet the guidelines.
-   **Informative:** Information that helps you understand or apply those rules — This is also called [non-normative](https://www.w3.org/TR/wcag-3.0/#dfn-informative).

The guidelines use three kinds of provisions that set out what must be done:

-   **Core requirements:** The main things you _must_ do
-   **Supplemental requirements:** Additional things that you can do to make things more accessible
-   **Assertions:** Things that you can say you did or do to improve the accessibility of your content or product

In addition, WCAG 3 provides Best Practices. These provide important guidance that often save time and improve accessibility but may not always apply in every situation.

The methods you use to satisfy WCAG 3 must be [accessibility supported](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-supported). This means a method only counts toward conformance if browsers and assistive technologies in general use support it. WCAG 3 uses defined accessibility-support sets to identify which technologies are tested against to check whether the methods used meet a requirement. The initial accessibility-support set in WCAG 3 is for HTML methods.

When evaluating accessibility, WCAG 3 applies to a clearly defined part of your content — such as specific [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view), or [processes](https://www.w3.org/TR/wcag-3.0/#dfn-process) — so you can scope your claim to exactly what was tested.

Each core requirement, supplemental requirement, and assertion is linked to different functional limitations. These cover a broad range of disabilities and help explain who benefits from the work to meet them.

End of summary for Interpreting normative provisions

This section lists requirements for conformance to WCAG 3.0. It also gives information about how to make conformance claims, which are optional. Finally, it describes what it means to be [accessibility supported](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-supported), since only accessibility-supported ways of using technologies can be relied upon for conformance.

Editor's note: Goals for a new conformance model

In this draft, AG is exploring a model based on Core Requirements, Supplemental Requirements, and Assertions. We ask reviewers to consider the following questions:

-   Should the core set of requirements provide approximately the same coverage as WCAG 2.2 A & AA? If not, should it be smaller or larger? If you think it should be a different size, what rules would you use to select the set?
-   Should we include assertions within the core set? Would organizations be willing to make public, attributable assertions about processes they completed?
-   Should there be additional levels within the core set of requirements? If yes, what and why?
-   In WCAG 2, every provision within the minimum conformance level has to be met to conform at the lowest level of conformance. To conform at the lowest level in WCAG 3, every provision within the core set must be met AND then additional effort must be done to better support people with disabilities but WCAG 3 allows some flexibility on what and how that effort is provided. Does this approach work or would a stricter set of requirements with more flexibility within the methods be a preferred approach?
-   The proposed conformance model ties conformance to functional performance statements. This list is expanded from the one currently used in legislation. What do you see as the positive and negative aspects of this approach? What statements should be added or changed?

### 3.1 Interpreting normative provisions

The main content of WCAG 2.2 is [normative](https://www.w3.org/TR/wcag-3.0/#dfn-normative) and defines requirements that impact conformance claims. Introductory material, appendices, sections marked as "non-normative", diagrams, examples, and notes are [informative](https://www.w3.org/TR/wcag-3.0/#dfn-informative) (non-normative). Non-normative material provides advisory information to help interpret the guidelines but does not create requirements that impact a conformance claim.

The key words __MAY__, __MUST__, __MUST NOT__, __NOT RECOMMENDED__, __RECOMMENDED__, __SHOULD__, and __SHOULD NOT__ are to be interpreted as described in \[[RFC2119](https://www.w3.org/TR/wcag-3.0/#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")\].

#### 3.1.1 Types of provision

WCAG 3 consists of three types of provisions.

**Core Requirements** — Requirements that must be met in order to conform. These include requirements that ensure:

-   content is detectable by user agents and AT,
-   content is conveyed to multiple senses and can be used by multiple inputs,
-   content does not cause immediate, physical harm, and
-   necessary support is available such as captions, text alternatives, and expanded forms of abbreviations.

**Supplemental Requirements** — Requirements that build on the core set. These include:

-   quality checks,
-   stricter or higher levels than those in a comparable core requirement,
-   requirements that are currently more difficult or expensive to implement, and
-   requirements that may apply in certain situations.

**Assertions** — Documented statements you can make about specific accessibility practices your organization follows to improve the accessibility of your content or product.

#### 3.1.2 Best practices

In addition to requirements and assertions, WCAG 3 includes best practices. These are listed at the provision and method level. They provide important guidance that often saves time and improve accessibility but may not always apply in every situation. These are integrated with requirements, assertions and methods and are clearly marked as best practice.

Best practices do not need to be satisfied to conform.

### 3.2 Conformance requirements

In order for a web page to conform to WCAG 3.0, all of the following conformance requirements must be satisfied:

#### 3.2.1 Conformance level

One of the following levels of conformance is met in full.

-   For Bronze conformance (the minimum level of conformance), all of the [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view) and [processes](https://www.w3.org/TR/wcag-3.0/#dfn-process) within the conformance scope _MUST_ satisfy all the core requirements and some portion (to be determined) of the supplemental requirements and assertions within each [functional performance statement](https://www.w3.org/TR/wcag-3.0/#function-performance-statements).
-   For Silver conformance, all of the pages/views and processes within the conformance scope _MUST_ satisfy all the core requirements and a larger portion of the supplemental requirements and assertions than in Bronze within each functional performance statement.
-   For Gold conformance, all of the pages/views and processes within the conformance scope satisfy all the core requirements and a larger portion of the supplemental requirements and assertions than in Silver within each functional performance statement.

#### 3.2.2 Accessibility supported

Many methods, such as those using ARIA or CSS, are only effective when they are supported by the [user agents](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent) (UA) and [assistive technologies](https://www.w3.org/TR/wcag-3.0/#dfn-assistive-technology) (AT) of real users.

The UA and AT used vary by language and region, and may be restricted in closed environments such as behind firewalls or on kiosks. As a result, it is important to understand which UA and AT support which methods and clearly state what UA and AT are assumed on conformance statements. The concept that methods must be supported by users' assistive technologies as well as the accessibility features in browsers and other user agents is referred to as "accessibility supported".

![diagram of the conformace model showing the core and supplemental requirements with lines for bronze, silver and gold level](https://www.w3.org/TR/wcag-3.0/img/conformance-model.png)

##### 3.2.2.1 Accessibility support set

WCAG 3 includes the concept of "accessibility-support sets". This is the set of UAs, ATs, and accessibility settings that AGWG will test against when determining methods that support a requirement.

WCAG 3 will use two accessibility support sets:

1.  **Default accessibility-support set** — A set of common browsers and assistive technology and accessibility supported settings support English content. The default accessibility-support set will be for HTML methods. Additional sets may be created for technologies such as mobile or VR.
2.  **Alternative accessibility support set** — People, organizations or regional regulators can also specify an alternative accessibility support set. This is a different set of browsers, assistive technology, and accessibility settings that support the intended languages, regions and technologies when the default accessibility-set does not provide that support.

While the AGWG will strive to ensure that requirements have as broad support as possible, it may not be possible for every requirement to be met on every combination of UA and AT. AGWG will only include core requirements if they include at least one HTML method that works with the default accessibility-support set at the time of publication.

The accessibility support set must be included in conformance claims. If you are working in a closed environment, with non-HTML technologies, or are in a region that relies on UA and AT outside the AG default accessibility-support set defined in WCAG 3, we also recommend including your accessibility support set in public accessibility statements. For example, if you claim conformance against a kiosk that uses a non-standard way to provide text to speech, then the accessibility-support set you are using should be included in your conformance claim and we recommend including it in public statements about the kiosk accessibility.

Editor's note

-   The default accessibility support set has not yet been defined.
-   Informative documentation will be needed to specify how people can create their own alternative accessibility support set.
-   Maintenance of the accessibility support set over time needs additional discussion.
-   An exception for long-present bugs in assistive technology is still under discussion.

#### 3.2.3 Defined conformance scope

When evaluating the accessibility of content, WCAG 3 requires the guidelines apply to a specific scope.

WCAG 3 defines two ways to scope content: [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view) and [processes](https://www.w3.org/TR/wcag-3.0/#dfn-process). Evaluation is done on one or more complete pages/views or processes, and conformance is determined on the basis of one or more complete pages/views or processes.

Conformance is defined only for clearly defined pages/views and processes. However, a conformance claim may be made to cover one pages/views and processes, a series of pages/views and processes, or multiple related pages/views and processes. All unique steps in a process __MUST__ be represented in the set of views. Views outside of the process __MAY__ also be included in the scope.

Editor's note

We recognize that representative sampling is an important strategy that large and complex sites use to assess accessibility. While it is not addressed within this document at this time, our intent is to later address it within this document or in a separate document before the guidelines reach the Candidate Recommendation stage. We welcome your suggestions and feedback about the best way to incorporate representative sampling in WCAG 3.

### 3.3 Functional performance statements (expanded)

Each core requirement, supplemental requirement, and assertion will be tagged with one or more of the expanded functional performance statements below. The statements are intended to describe the functional performance of ICT enabling people to locate, identify, and operate ICT functions, and to access the information provided, regardless of physical, cognitive or sensory abilities.

This is not a list of disabilities. Different disabilities may lead to the need for use with one or more of the limitations listed below. For example, a visual impairment or an inability to process visual information may require usage with limited vision.

-   Usage without vision
-   Usage with limited vision
-   Usage without perception of color
-   Usage without hearing
-   Usage with limited hearing
-   Usage without vocal capability
-   Usage with limited vocal capability
-   Usage with limited manipulation or strength
-   Usage with limited reach
-   Usage with sensitivity to sensory stimuli
-   Usage with limited executive function (includes self-regulation, task management, planning, organization and social skills)
-   Usage with limited reasoning (includes problem solving, abstraction, mathematical intelligence, recognition, and crystallized intelligence)
-   Usage with limited attention (includes the ability to concentrate, multitask, and focus over time)
-   Use with sensitivity to certain content (includes anxiety and content-based triggers)
-   Usage with limited language processing (includes the ability to process spoken language, sign language, written language, and image based language.)
-   Usage with limited memory
-   Usage with atypical physical attributes

Note

The difference between this list and the one currently used in legislation is:

-   Limited cognition has been broken apart to better reflect the diversity of needs within cognition-related disabilities.
-   An alternative breakdown to usage with limited cognition based on [FAST](https://w3c.github.io/fast/) would be:
    -   Usage with limited attention
    -   Usage with limited language and communication
    -   Usage with limited learning
    -   Usage with limited memory
    -   Usage with limited executive function
-   The following functional performance statements were added:
    -   Use with limited vocal capability
    -   Use with atypical physical attributes
    -   Use with sensitivity to certain content

## 4\. GlossaryDeveloping

_This section (with its subsections) provides requirements which must be followed to conform to the specification, meaning it is [normative](https://www.w3.org/TR/wcag-3.0/#dfn-normative)._

Note

Many of the terms defined here have common meanings. When terms appear with a link to the definition, the meaning is as formally defined here. When terms appear without a link to the definition, their meaning is not explicitly related to the formal definition here. These definitions are in progress and may evolve as the document evolves.

Editor's note

This glossary includes terms used by content that has reached a maturity level of Developing or higher. The definitions themselves include a maturity level and may mature at a different pace than the content that refers to them. The AGWG will work with other task forces and groups to harmonize terminology across documents as much as is possible.

abbreviationDeveloping

shortened form of a word, phrase, or name where the abbreviation has not become part of the language

Note 1

This includes initialisms, acronyms, and numeronyms.

1.  **initialisms** are shortened forms of a name or phrase made from the initial letters of words or syllables contained in that name or phrase. These are not defined in all languages.
2.  **acronyms** are abbreviated forms made from the initial letters or parts of other words (in a name or phrase) which may be pronounced as a word.
3.  **numeronyms** are shortened forms of a word that use the first and last letters, with a number in between showing the number of letters left out.

Note 2

Some companies have adopted what used to be an initialism as their company name. In these cases, the new name of the company is the letters (for example, Ecma) and the word is no longer considered an abbreviation.

accessibility support setDeveloping

group of user agents and assistive technologies you test with

Editor's note

The AGWG is considering defining a default set of user agents and assistive technologies that they use when validating guidelines.

Accessibility support sets may vary based on language, region, or situation.

If you are not using the default accessibility set, the conformance report should indicate what set is being used.

accessibility supportedDeveloping

available and working in the user agents and assistive technology in the [accessibility support set](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-support-set)

Editor's note

actively availableDeveloping

available for the user to perceive and use

ASCII artExploratory

picture created by a spatial arrangement of characters or glyphs (typically from the 95 printable characters defined by ASCII)

assertionDeveloping

formal claim of fact, attributed to a person or organization, regarding procedures practiced in the development and maintenance of the [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) or [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) to improve accessibility

assistive technologyDeveloping

hardware and/or software that acts as a [user agent](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent), or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents

Note 1

Functionality provided by assistive technology includes alternative presentations (e.g., as synthesized speech or magnified content), alternative input methods (e.g., voice), additional navigation or orientation mechanisms, and content transformations (e.g., to make tables more accessible).

Note 2

Assistive technologies often communicate data and messages with mainstream user agents by using and monitoring APIs.

Note 3

The distinction between mainstream user agents and assistive technologies is not absolute. Many mainstream user agents provide some features to assist individuals with disabilities. The basic difference is that mainstream user agents target broad and diverse audiences that usually include people with and without disabilities. Assistive technologies target narrowly defined populations of users with specific disabilities. The assistance provided by an assistive technology is more specific and appropriate to the needs of its target users. The mainstream user agent may provide important functionality to assistive technologies like retrieving web content from program objects or parsing markup into identifiable bundles.

audioDeveloping

live or recorded sound signal

audio descriptionDeveloping

narration added to the soundtrack to describe important visual details that cannot be understood from the main soundtrack alone

Note

For audiovisual media, audio description provides information about actions, characters, scene changes, on-screen text, and other visual content.

Audio description is also sometimes called “video description”, “described video”, “visual description”, or “descriptive narration”.

In standard audio description, narration is added during existing pauses in dialogue. See also [extended audio description](https://www.w3.org/TR/wcag-3.0/#dfn-extended-audio-description).

If all important visual information is already provided in the main audio track, no additional audio description track is necessary.

automated evaluationDeveloping

[evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-evaluation) conducted using software tools, typically evaluating code-level features and applying heuristics for other tests

Note

Automated testing is contrasted with other types of testing that involve human judgement or experience. [Semi-automated evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-semi-automated-evaluation) allows machines to guide humans to areas that need inspection. The emerging field of testing conducted via machine learning is not included in this definition.

availableExploratory

present and, in the context of alternatives, sufficient to understand the content

biometricDeveloping

behavioral or biological characteristics

Note

examples include but are not limited to voice, iris, appearance, fingerprint, face shape, or body movement

blinkingDeveloping

switching back and forth between two visual states in a way that is meant to draw attention

Note

See also [flash](https://www.w3.org/TR/wcag-3.0/#dfn-flash). It is possible for something to be large enough and blink brightly enough at the right frequency to be also classified as a flash.

block of textDeveloping

more than one sentence of [text](https://www.w3.org/TR/wcag-3.0/#dfn-text)

captionsDeveloping

synchronized visual and/or [text alternative](https://www.w3.org/TR/wcag-3.0/#dfn-text-alternative) for both the speech and non-speech [audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) portion of a work of audiovisual [content](https://www.w3.org/TR/wcag-3.0/#dfn-content)

Note 1

Closed captions are equivalents that can be turned on and off with some players and can often be read using assistive technology.

Note 2

Open captions are any captions that cannot be turned off in the player. For example, if the captions are visual equivalent images of text embedded in [video](https://www.w3.org/TR/wcag-3.0/#dfn-video).

Note 3

[Audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) can be, but do not need to be, captioned since they are descriptions of information that is already presented visually.

Note 4

In some countries, captions are called subtitles. The term ‘subtitles’ is often also used to refer to captions that present a translated version of the audio content.

clear languageExploratory

writing in a simple, direct way

Note

Clear language avoids unnecessary complexity and helps make content accessible to everyone, including people with cognitive disabilities, limited reading skills, and limited language proficiency.

cognitive function testDeveloping

task that requires the user to remember, manipulate, or transcribe information

Note

Examples include, but are not limited to:

-   memorization, such as remembering a username, password, set of characters, images, or patterns. The common identifiers name, email, and phone number are not considered cognitive function tests as they are personal to the user and consistent across websites;
-   transcription, such as typing in characters;
-   use of correct spelling;
-   performance of calculations;
-   solving of puzzles.

color contrastDeveloping

relationship of hue, saturation, and lightness values between two colors

common keyboard navigation techniqueDeveloping

keyboard navigation technique that is the same across most or all applications and platforms and can therefore be relied upon by users who need to navigate by keyboard alone

Note

complex numerical informationExploratory

numbers, statistics, or quantitative data that require interpretation, comparison, or multiple steps to understand.

Note

This includes mental calculation, proportional reasoning, or comparison against an unstated whole.

complex pointer inputDeveloping

any pointer input other than a [single pointer input](https://www.w3.org/TR/wcag-3.0/#dfn-single-pointer-input)

componentDeveloping

grouping of elements for a distinct function

conformanceDeveloping

satisfying all the requirements of the guidelines

Note

Conformance is an important part of following the guidelines even when not making a formal Conformance Claim

See the [Conformance section](https://www.w3.org/TR/wcag-3.0/#conformance) for more information.

conformance scopeDeveloping

A set of [Views](https://www.w3.org/TR/wcag-3.0/#dfn-view) and/or [Pages](https://www.w3.org/TR/wcag-3.0/#dfn-page) selected to be part of a conformance claim. Where a View or Page is part of a [Process](https://www.w3.org/TR/wcag-3.0/#dfn-process), all the Views or Pages in the process must be included.

Note

How a person or organization selects the set is not defined in WCAG3. There maybe informative guidance on selecting a suitable set in future (similar to [WCAG-EM](https://www.w3.org/TR/WCAG-EM/)), but regional laws or regulations may provide a methodology.

contentDeveloping

information, sensory experience and interactions conveyed

content authorExploratory

person or persons responsible for the content presented, including word choice, formatting, images, video, audio, and other elements

context-sensitive helpDeveloping

help text that provides information related to the function currently being performed

contrast ratio testExploratory

meeting a sufficient level of contrast between two colors using the relationship of hue, saturation, and lightness values

Editor's note

The contrast algorithm used in WCAG 3 is yet to be determined.

conversational supportExploratory

support that is provided in the form of interactive, bi-directional, context-sensitive conversations

css pixelDeveloping

visual angle of about 0.0213 degrees

Note

A CSS pixel is the canonical unit of measure for all lengths and measurements in CSS. This unit is density-independent, and distinct from actual hardware pixels present in a display. User agents and operating systems should ensure that a CSS pixel is set as closely as possible to the CSS Values and Units Module Level 3 reference pixel \[css3-values\], which takes into account the physical dimensions of the display and the assumed viewing distance (factors that cannot be determined by content authors).

decorativeDeveloping

serving only an aesthetic purpose, providing no information, and having no functionality

Note

Text is only purely decorative if the words can be rearranged or substituted without changing their purpose.

default orientationExploratory

the orientation of view that is preferred or enforced by the [platform](https://www.w3.org/TR/wcag-3.0/#dfn-platform)

default visual presentationExploratory

formatting of content defined by the author without any modifications or customizations by the end user

deprecateDeveloping

declare something outdated and in the process of being phased out, usually in favor of a specified replacement

Note

Deprecated documents are no longer recommended for use and may cease to exist in the future.

descriptive transcriptDeveloping

a text version of the speech and non-speech audio information and visual information needed to understand the content

down eventDeveloping

platform event that occurs when the trigger stimulus of a pointer is depressed

Note

The down event may have different names on different platforms, such as “touchstart” or “mousedown”.

equivalentExploratory

equal, and, in the context of alternatives, includes or conveys the same information as the original.

essential exceptionDeveloping

exception because there is no way to carry out the function without doing it this way or fundamentally changing the functionality

essential to outcomeDeveloping

always necessary to achieve the same result

Note

If something is essential to the outcome then: If it were removed, the information or functionality of the content would be fundamentally changed, and the information and functionality cannot be achieved in another way that would conform

evaluationDeveloping

process of examining [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) for [conformance](https://www.w3.org/TR/wcag-3.0/#dfn-conformance) to these guidelines

Note

Different approaches to evaluation include [automated evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-automated-evaluation), [semi-automated evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-semi-automated-evaluation), [human evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-human-evaluation), and [usability testing](https://www.w3.org/TR/wcag-3.0/#dfn-usability-testing).

extended audio descriptionDeveloping

[audio description](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description) that is added to audiovisual media by pausing the video to allow for additional time to fit in the audio description

Note

This technique is only used when the sense of the video would be lost without the additional audio description and the pauses between dialogue or narration are too short.

figure captionDeveloping

title, brief explanation, or comment that accompanies a work of visual media and is always visible on the page

flashDeveloping

a pair of opposing changes in [relative luminance](https://www.w3.org/TR/wcag-3.0/#dfn-relative-luminance) that can cause seizures in some people if it is large enough and in the right frequency range

Note 1

See [general flash and red flash thresholds](https://www.w3.org/TR/wcag-3.0/#dfn-general-flash-and-red-flash-thresholds) for information about types of flash that are not allowed.

focus indicatorDeveloping

pixels that are changed to visually indicate when a [user interface component](https://www.w3.org/TR/wcag-3.0/#dfn-user-interface-component) is in a focused [state](https://www.w3.org/TR/wcag-3.0/#dfn-state)

functional needDeveloping

statement that describes a specific gap in one’s ability, or a specific mismatch between ability and the designed environment or context

general flash and red flash thresholdsDeveloping

a [flash](https://www.w3.org/TR/wcag-3.0/#dfn-flash) or rapidly-changing image sequence is below the threshold (i.e., content **passes**) if any of the following are true:

-   there are no more than three **general flashes** and / or no more than three **red flashes** within any one-second period; or
-   the combined area of flashes occurring concurrently occupies no more than a total of .006 steradians within any 10 degree visual field on the screen (25% of any 10 degree visual field on the screen) at typical viewing distance

where:

-   A **general flash** is defined as a pair of opposing changes in [relative luminance](https://www.w3.org/TR/wcag-3.0/#dfn-relative-luminance) of 10% or more of the maximum relative luminance (1.0) where the relative luminance of the darker image is below 0.80; and where “a pair of opposing changes” is an increase followed by a decrease, or a decrease followed by an increase, and
-   A **red flash** is defined as any pair of opposing transitions involving a saturated red

_Exception:_ Flashing that is a fine, balanced, pattern such as white noise or an alternating checkerboard pattern with “squares” smaller than 0.1 degree (of visual field at typical viewing distance) on a side does not violate the thresholds.

Note 1

For general software or web content, using a 341 x 256 pixel rectangle anywhere on the displayed screen area when the content is viewed at 1024 x 768 pixels will provide a good estimate of a 10 degree visual field for standard screen sizes and viewing distances (e.g., 15-17 inch screen at 22-26 inches). This resolution of 75 - 85 ppi is known to be lower, and thus more conservative than the nominal CSS pixel resolution of 96 ppi in CSS specifications. Higher resolutions displays showing the same rendering of the content yield smaller and safer images so it is lower resolutions that are used to define the thresholds.

Note 2

A transition is the change in relative luminance (or relative luminance/color for red flashing) between adjacent peaks and valleys in a plot of relative luminance (or relative luminance/color for red flashing) measurement against time. A flash consists of two opposing transitions.

Note 3

The new working definition in the field for **“pair of opposing transitions involving a saturated red”** (from WCAG 2.2) is a pair of opposing transitions where, one transition is either to or from a state with a value R/(R + G + B) that is greater than or equal to 0.8, and the difference between states is more than 0.2 (unitless) in the CIE 1976 UCS chromaticity diagram. \[[ISO\_9241-391](https://www.w3.org/TR/wcag-3.0/#bib-iso_9241-391 "Ergonomics of human-system interaction—Part 391: Requirements, analysis and compliance test methods for the reduction of photosensitive seizures")\]

Note 4

Tools are available that will carry out analysis from video screen capture. However, no tool is necessary to evaluate for this condition if flashing is less than or equal to 3 flashes in any one second. Content automatically passes (see #1 and #2 above).

gestureDeveloping

motion made by the body or a body part used to communicate to technology

guidelineDeveloping

high-level, plain-language outcome statements used to organize [requirements](https://www.w3.org/TR/wcag-3.0/#dfn-requirement)

Note

Guidelines provide a high-level, plain-language outcome statements for managers, policy makers, individuals who are new to accessibility, and other individuals who need to understand the concepts but not dive into the technical details. They provide an easy-to-understand way of organizing and presenting the requirements so that non-experts can learn about and understand the concepts.

Each guideline includes a unique, descriptive name along with a high-level plain-language summary. Guidelines address functional needs on specific topics, such as contrast, forms, readability, and more.

Guidelines group related requirements and are technology-independent.

high-frequency corpusDeveloping

large collections of [text](https://www.w3.org/TR/wcag-3.0/#dfn-text) (corpora) used in linguistics to identify and analyze words and phrases that appear most often in a language

human evaluationDeveloping

[evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-evaluation) conducted by a human, typically to apply human judgement to tests that cannot be fully [automatically evaluated](https://www.w3.org/TR/wcag-3.0/#dfn-automated-evaluation)

Note

Human evaluation is contrasted with [automated evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-automated-evaluation) which is done entirely by machine, though it includes [semi-automated evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-semi-automated-evaluation) which allows machines to guide humans to areas that need inspection. Human evaluation involves inspection of content features, in contrast with [usability testing](https://www.w3.org/TR/wcag-3.0/#dfn-usability-testing) which directly tests the experience of users with [content](https://www.w3.org/TR/wcag-3.0/#dfn-content).

human languageExploratory

language that is spoken, written, or signed (through visual or tactile means) to communicate with humans

Note

See also [sign language](https://www.w3.org/TR/wcag-3.0/#dfn-sign-language).

imagePlaceholder

Editor's note

To be defined.

image rolePlaceholder

Editor's note

To be defined.

image typePlaceholder

Editor's note

To be defined.

infinite scrollingPlaceholder

Editor's note

To be defined.

informativeDeveloping

[content](https://www.w3.org/TR/wcag-3.0/#dfn-content) provided for information purposes and not required for [conformance](https://www.w3.org/TR/wcag-3.0/#dfn-conformance). Also referred to as non-normative

interactive elementDeveloping

element that responds to user input and has a distinct [programmatically determinable](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable) name

Note

In contrast to [non-interactive elements](https://www.w3.org/TR/wcag-3.0/#dfn-non-interactive-element). For example, headings or paragraphs.

itemsDeveloping

smallest testable unit for testing scope

Note

Items could be an interactive [component](https://www.w3.org/TR/wcag-3.0/#dfn-component) such as a drop down menu, a link, or a media player.

They could also be units of [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) such as a phrase, a paragraph, a label or error message, an icon, or an image.

keyboard focusDeveloping

point in the [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) where any keyboard actions would take effect

keyboard interfaceDeveloping

API (Application Programming Interface) where software gets “keystrokes” from

Note

“Keystrokes” that are passed to the software from the “keyboard interface” may come from a wide variety of sources including but not limited to a scanning program, sip-and-puff morse code software, speech recognition software, AI of all sorts, as well as other keyboard substitutes or special keyboards.

labelDeveloping

text or other component with a text alternative that is presented to a user to identify a component within web content

Note 1

A label is presented to all users whereas the name may be hidden and only exposed by assistive technology. In many (but not all) cases the name and the label are the same.

Note 2

The term label is not limited to the label element in HTML.

legal informationExploratory

content that must be provided to meet statutory or regulatory requirements, or that provides legal protection such as terms and conditions

liveDeveloping

information captured from a real-world event and transmitted to the receiver with no more than a broadcast delay

Note 1

A broadcast delay is a short (usually automated) delay, for example used in order to give the broadcaster time to cue or censor the audio (or video) feed, but not sufficient to allow significant editing.

Note 2

If information is completely computer generated, it is not live.

long-form text contentExploratory

written material made up of multiple [blocks of text](https://www.w3.org/TR/wcag-3.0/#dfn-block-of-text), along with structural elements such as headings and lists, that work together to explain, inform, or convey a narrative

Note

Long-form text content is meant to be read as a continuous piece of text, such as an article, report, essay, or guide, rather than as separate or standalone items like product listings on a shopping page.

meaningful blocks of contentExploratory

Group of related [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that represents a distinct topic or function, intended to be perceived as a single unit and capable of being programmatically identified and labelled.

Note

These blocks are required to be programmatically determinable so that assistive technologies can identify the boundaries and purpose of the information.

mechanismDeveloping

[process](https://www.w3.org/TR/wcag-3.0/#dfn-process) or technique for achieving a result

Note 1

The mechanism may be explicitly provided in the content, or may be relied upon to be provided by either the platform or by [user agents](https://www.w3.org/TR/wcag-3.0/#dfn-user-agent), including [assistive technologies](https://www.w3.org/TR/wcag-3.0/#dfn-assistive-technology).

Note 2

The mechanism needs to meet all requirements for the conformance level claimed.

media alternativeDeveloping

alternative formats, usually text, for audio, video, and audio-video content including [captions](https://www.w3.org/TR/wcag-3.0/#dfn-captions), [audio descriptions](https://www.w3.org/TR/wcag-3.0/#dfn-audio-description), and [descriptive transcripts](https://www.w3.org/TR/wcag-3.0/#dfn-descriptive-transcript)

methodDeveloping

detailed information, either technology-specific or technology-agnostic, on ways to satisfy the [requirement](https://www.w3.org/TR/wcag-3.0/#dfn-requirement)

minimum bounding boxDeveloping

the smallest enclosing rectangle aligned to the horizontal axis within which all the points of a shape lie

Note

For components which wrap onto multiple lines as part of a sentence or [block of text](https://www.w3.org/TR/wcag-3.0/#dfn-block-of-text), such as hypertext links, the bounding box is based on how the component would appear on a single line.

nested clauseDeveloping

clause that is embedded inside another clause and neither clause can stand alone as a sentence

Note

Nested clauses use groups of words that are sometimes called dependent clauses or subordinate clauses.

non-interactive elementDeveloping

element that does not respond to user input and does not include sub-parts

Note 1

If a paragraph included a link, the text either side of the link would be considered a static element, but not the paragraph as a whole.

Note 2

Letters within text do not constitute a “smaller part”.

non-literal languageDeveloping

words or phrases used in a way that are beyond their standard or dictionary meaning to express deeper, more complex ideas

Note

This is also called figurative language.

To understand the content, users have to interpret the implied meaning behind the words, rather than just their literal or direct meaning.

non-text contentExploratory

any content that is not a sequence of characters that can be [programmatically determinable](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable) or where the sequence is not expressing something in [human language](https://www.w3.org/TR/wcag-3.0/#dfn-human-language)

Note

This includes [ASCII art](https://www.w3.org/TR/wcag-3.0/#dfn-ascii-art) (which is a pattern of characters), emoticons, leetspeak (which uses character substitution), and images representing text

normativeDeveloping

[content](https://www.w3.org/TR/wcag-3.0/#dfn-content) whose instructions are required for [conformance](https://www.w3.org/TR/wcag-3.0/#dfn-conformance)

pageDeveloping

non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together

Note

Where a URI is available and represents a unique set of content, that would be the preferred conformance unit.

Path-based gestureDeveloping

gesture that depends on the path of the pointer input and not just its endpoints

Note

Path-based gesture includes both time dependent and non-time dependent path-based gestures.

platformDeveloping

software, or collection of layers of software, that lies below the subject software and provides services to the subject software and that allows the subject software to be isolated from the hardware, drivers, and other software below

Note 1

Platform software both makes it easier for subject software to run on different hardware, and provides the subject software with many services (e.g. functions, utilities, libraries) that make the subject software easier to write, keep updated, and work more uniformly with other subject software.

Note 2

A particular software component might play the role of a platform in some situations and a client in others. For example a browser is a platform for the content of the page but it also relies on the operating system below it.

Note 3

The platform is the context in which the [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) exists.

point of regardDeveloping

position in rendered [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that the user is presumed to be viewing, of which the dimensions can vary

Note

The point of regard is almost always within the viewport, but it can exceed the spatial or temporal dimensions of the viewport. See [rendered content](https://www.w3.org/TR/wcag-3.0/#dfn-rendered-content) for more information about viewport dimensions.

The point of regard can also refer to a particular moment in time for content that changes over time. For example, an audio-only presentation.

User agents can determine the point of regard in a number of ways, including based on viewport position in content, keyboard focus, and selection.

pointerDeveloping

a hardware-agnostic representation of input devices that can target a specific coordinate (or set of coordinates) on a screen, such as a mouse, pen, or touch contact

prerecordedExploratory

information that is not [live](https://www.w3.org/TR/wcag-3.0/#dfn-live)

presentationDeveloping

rendering of the [content](https://www.w3.org/TR/wcag-3.0/#dfn-content) in a form to be perceived by users

private and sensitive informationExploratory

private and sensitive information

processDeveloping

series of [views](https://www.w3.org/TR/wcag-3.0/#dfn-view) or [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page) associated with user actions, where actions required to complete an activity are performed, often in a certain order, regardless of the technologies used or whether it spans different sites or domains

programmatically determinableDeveloping

meaning of the content and all its important attributes can be determined by software functionality that is [accessibility supported](https://www.w3.org/TR/wcag-3.0/#dfn-accessibility-supported)

pseudo-motionExploratory

static content on the page that gives the user the perception or feeling of motion

relationship of meaningExploratory

Logical associations between elements that convey meaning and are necessary to understand the content

relative luminanceDeveloping

the relative brightness of any point in a colorspace, normalized to 0 for darkest black and 1 for lightest white

Note 1

For the sRGB colorspace, the relative luminance of a color is defined as L = 0.2126 \* **R** + 0.7152 \* **G** + 0.0722 \* **B** where **R**, **G** and **B** are defined as:

-   if RsRGB <= 0.04045 then **R** = RsRGB/12.92 else **R** = ((RsRGB+0.055)/1.055) ^ 2.4
-   if GsRGB <= 0.04045 then **G** = GsRGB/12.92 else **G** = ((GsRGB+0.055)/1.055) ^ 2.4
-   if BsRGB <= 0.04045 then **B** = BsRGB/12.92 else **B** = ((BsRGB+0.055)/1.055) ^ 2.4

and RsRGB, GsRGB, and BsRGB are defined as:

-   RsRGB = R8bit/255
-   GsRGB = G8bit/255
-   BsRGB = B8bit/255

The ”^” character is the exponentiation operator. (Formula taken from \[[SRGB](https://www.w3.org/TR/wcag-3.0/#bib-srgb "Multimedia systems and equipment - Colour measurement and management - Part 2-1: Colour management - Default RGB colour space - sRGB")\].)

Note 2

Before May 2021 the value of 0.04045 in the definition was different (0.03928). It was taken from an older version of the specification and has been updated. It has no practical effect on the calculations in the context of these guidelines.

Note 3

Almost all systems used today to view web content assume sRGB encoding. Unless it is known that another color space will be used to process and display the content, authors should evaluate using sRGB colorspace.

Note 4

If dithering occurs after delivery, then the source color value is used. For colors that are dithered at the source, the average values of the colors that are dithered should be used (average R, average G, and average B).

Note 5

Tools are available that automatically do the calculations when testing contrast and flash.

Editor's note

WCAG 2.2 includes a [separate page](https://www.w3.org/TR/WCAG22/relative-luminance.html) giving the relative luminance definition using MathML to display the formulas. This will need to be addressed for inclusion in WCAG 3.

rendered contentPlaceholder

Editor's note

To be defined.

requirementDeveloping

result of practices that reduce or eliminate barriers that people with disabilities experience

sectionDeveloping

self-contained portion of content that deals with one or more related topics or thoughts

Note

A section may consist of one or more paragraphs and include graphics, tables, lists and sub-sections.

semi-automated evaluationDeveloping

[evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-evaluation) conducted using machines to guide humans to areas that need inspection

Note

Semi-automated evaluation involves components of [automated evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-automated-evaluation) and [human evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-human-evaluation).

sign languageExploratory

a language using combinations of movements of the hands and arms, facial expressions, or body positions to convey meaning

sign language interpretationExploratory

translation of one language, generally a spoken language, into a sign language

Note

True sign languages are independent languages that are unrelated to the spoken language(s) of the same country or region.

simple pointer inputDeveloping

input event that involves only a single ‘click’ event or a ‘button down’ and ‘button up’ pair of events with no movement between

single pointer inputDeveloping

input modality that only targets a single point on the [page](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[view](https://www.w3.org/TR/wcag-3.0/#dfn-view) at a time – such as a mouse, single finger on a touch screen, or stylus

Note 1

Single pointer interactions include clicks, double clicks, taps, dragging motions, and single-finger swipe gestures. In contrast, multipoint interactions involve the use of two or more pointers at the same time, such as two-finger interactions on a touchscreen, or the simultaneous use of a mouse and stylus.

Note 2

Single pointer input is in contrast to multipoint input such as two, three or more fingers or pointers touching the surface, or gesturing in the air, at the same time.

Note 3

Activation is usually by click or tap but can also be by programmatic simulation of a click or tap or other similar simple activation.

spatial audioDeveloping

sounds that vary in volume and source location to create the illusion of different origin points

standard platform keyboard commandsDeveloping

keyboard commands that are the same across most or all platforms and are relied upon by users who need to navigate by keyboard alone

Note

starting pointDeveloping

the home page of a website or a set of web pages in a website

stateDeveloping

dynamic property expressing characteristics of a [user interface component](https://www.w3.org/TR/wcag-3.0/#dfn-user-interface-component) that may change in response to user action or automated processes

Note

States represent data associated with the component or user interaction possibilities. They do not affect the nature of the component. Examples include focus, hover, select, press, check, visited/unvisited, and expand/collapse.

structural componentExploratory

a [component](https://www.w3.org/TR/wcag-3.0/#dfn-component) that provides the same organizational or navigational purpose across multiple pages/views [pages](https://www.w3.org/TR/wcag-3.0/#dfn-page)/[views](https://www.w3.org/TR/wcag-3.0/#dfn-view)

supportPlaceholder

Editor's note

To be defined.

synchronized mediaDeveloping

[audio](https://www.w3.org/TR/wcag-3.0/#dfn-audio) or [video](https://www.w3.org/TR/wcag-3.0/#dfn-video) synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a [media alternative](https://www.w3.org/TR/wcag-3.0/#dfn-media-alternative) for text that is clearly labeled as such

task flowDeveloping

testing scope that includes a series views that support a specified user activity

Note

A task flow may include a subset of [items](https://www.w3.org/TR/wcag-3.0/#dfn-items) in a [view](https://www.w3.org/TR/wcag-3.0/#dfn-view) or a group of views. Only the part of the views that support the user activity are included in a test of the task flow.

testDeveloping

mechanism to evaluate implementation of a [method](https://www.w3.org/TR/wcag-3.0/#dfn-method)

textDeveloping

sequence of characters that can be [programmatically determined](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable), where the sequence is expressing something in [human language](https://www.w3.org/TR/wcag-3.0/#dfn-human-language)

text alternativeDeveloping

[text](https://www.w3.org/TR/wcag-3.0/#dfn-text) that is [programmatically associated](https://www.w3.org/TR/wcag-3.0/#dfn-programmatically-determinable) with [non-text content](https://www.w3.org/TR/wcag-3.0/#dfn-non-text-content) or referred to from text that is programmatically associated with non-text content

text contentDeveloping

[text](https://www.w3.org/TR/wcag-3.0/#dfn-text) and formatting that, together with the semantic or hierarchical structure provided by markup, communicate the content and meaning

transcriptExploratory

a text equivalent of the source material

unnecessary wordsExploratory

extra words or complicated phrases that can be removed or replaced with simpler ones without changing the meaning of the [text content](https://www.w3.org/TR/wcag-3.0/#dfn-text-content)

up eventDeveloping

platform event that occurs when the trigger stimulus of a pointer is released

Note

The up event may have different names on different platforms, such as “touchend” or “mouseup”.

usability testingDeveloping

[evaluation](https://www.w3.org/TR/wcag-3.0/#dfn-evaluation) of the experience of users using a [conformance scope](https://www.w3.org/TR/wcag-3.0/#dfn-conformance-scope) or [process](https://www.w3.org/TR/wcag-3.0/#dfn-process) by observation and feedback

user agentDeveloping

any software that retrieves and presents web content for users

user interface componentPlaceholder

Editor's note

To be defined.

user needDeveloping

end goal a user has when starting a process through digital means

user-manipulable textDeveloping

text which the user can adjust

Note

This could include, but is not limited to, changing:

-   Line, word or letter spacing
-   Color
-   Line length — being able to control width of block of text
-   Typographic alignment — justified, flushed right/left, centered
-   Wrapping
-   Columns — number of columns in one-dimensional content
-   Margins
-   Underlining, italics, bold
-   Font face, size, width
-   Capitalization — all caps, small caps, alternating case
-   End of line hyphenation
-   Links

variation of product or processPlaceholder

Editor's note

To be defined.

videoDeveloping

the technology of moving or sequenced pictures or images

Note

Video can be made up of animated or photographic images, or both.

viewDeveloping

[content](https://www.w3.org/TR/wcag-3.0/#dfn-content) that is [actively available](https://www.w3.org/TR/wcag-3.0/#dfn-actively-available) in a [viewport](https://www.w3.org/TR/wcag-3.0/#dfn-viewport) including that which can be scrolled or panned to, and any additional content that is included by expansion while leaving the rest of the content in the viewport actively available

Note

A modal dialog box would constitute a new view because the other content in the viewport is no longer actively available.

viewportDeveloping

object in which the [platform](https://www.w3.org/TR/wcag-3.0/#dfn-platform) presents content

Note 1

The author has no control of the viewport and almost always has no idea what is presented in a viewport (e.g. what is on screen) because it is provided by the platform. On browsers the hardware platform is isolated from the content.

Note 2

Content can be presented through one or more viewports. Viewports include windows, frames, loudspeakers, and virtual magnifying glasses. A viewport may contain another viewport. For example, nested frames. Interface components created by the user agent such as prompts, menus, and alerts are not viewports.

visual aidsDeveloping

diagrams, photos, illustrations, or a simplified step process to supplement complex ideas, such as processes, workflows, relationships, or chronological information presented in the text content

visually collocated withDeveloping

in reasonable proximity within the viewport, regardless of magnification or zoom level, to sufficiently associate the error message to the field in error

## A. Privacy Considerations

Editor's note

The content of this document has not matured enough to identify privacy considerations. Reviewers of this draft should consider whether requirements of the conformance model could impact privacy.

## B. Security Considerations

Editor's note

The content of this document has not matured enough to identify security considerations. Reviewers of this draft should consider whether requirements of the conformance model could impact security.

## C. Change log

This section shows substantive changes made in WCAG 3 since the First Public Working Draft was published in 21 January 2021.

The full [commit history to WCAG 3](https://github.com/w3c/wcag3/commits/main/guidelines) and [commit history to Silver](https://github.com/w3c/silver/commits/main/guidelines) is available.

-   2025-09-04: Published requirements and assertions that have reached developing; removed exploratory content from draft; and updated assertions section of [Explainer for WCAG 3.0](https://www.w3.org/TR/wcag-3.0-explainer/).
-   2024-12-12: Reorganized exploratory guidelines; added 3 developing guidelines and accessibility supported; added user agent support, updated conformance section, and moved explanatory content to the [Explainer for WCAG 3.0](https://www.w3.org/TR/wcag-3.0-explainer/)
-   2024-03-15: Updated placeholder guidelines with exploratory guidelines.
-   2023-07-24: Changed approach to WCAG 3 based feedback and removed old material that was not consistent with the new approach. Added WCAG 3 Guideline placeholders to indicate maturity level.
-   2021-12-07: Add Project Manager
-   2021-06-08: Moved explanatory information to [Explainer for W3C Accessibility Guidelines (WCAG) 3.0](https://www.w3.org/TR/wcag-3.0-explainer/)

## D. Acknowledgements

Additional information about participation in the Accessibility Guidelines Working Group (AG WG) can be found on the [Working Group home page](https://www.w3.org/groups/wg/ag/).

### D.1 Contributors to the development of this document

-   Adam Page (Invited Expert)
-   Alastair Campbell (Gain)
-   Alina Vayntrub (Understood.org)
-   Andrew Kirkpatrick (Evinced Inc.)
-   Ashley Firth (Invited Expert)
-   Atya Ratcliff (Google LLC)
-   Azlan Cuttilan (Invited Expert)
-   Ben Tillyer (University of Oxford)
-   Brian Elton (TPGi)
-   Bruce Bailey (Invited Expert)
-   Bryan Trogdon (Google LLC)
-   Carrie Hall (SAP SE)
-   Charu Pandhi (TPGi)
-   Chuck Adams (Oracle Corporation)
-   Claire Chang (Invited Expert)
-   Detlev Fischer (Invited Expert)
-   Eloisa Guerrero (Invited Expert)
-   Eric Hind (Google LLC)
-   Filippo Zorzi (UsableNet)
-   Francis Storr (Intel Corporation)
-   Frankie Wolf (Invited Expert)
-   Gez Lemon (TetraLogical Services Ltd)
-   Giacomo Petri (UsableNet)
-   Glenda Sims (Deque Systems, Inc.)
-   Graham Ritchie (Invited Expert)
-   Gregg Vanderheiden (Invited Expert)
-   Gundula Niemann (SAP SE)
-   Heather Bellis (Oracle Corporation)
-   Hidde de Vries (Logius)
-   Illai Zeevi (Evinced Inc.)
-   JaEun Jemma Ku (University of Illinois)
-   Jan Jaap de Groot (Abra)
-   Jan McSorley (Invited Expert)
-   Jaunita Flessas (Invited Expert)
-   Jen Goulden (Crawford Technologies)
-   Jennifer Delisi (Invited Expert)
-   Jeremy Katherman (Deque Systems, Inc.)
-   Jeroen Hulscher (Logius)
-   John Kirkwood (Invited Expert)
-   John Rochford (Invited Expert)
-   John Toles (Rhonda Weiss Center for Accessible IDEA Data)
-   Jon Avila (Level Access)
-   Jory Cunningham (Amazon)
-   Julie Rawe (Understood.org)
-   Kathy Eng (Invited Expert)
-   Ken Franqueiro (W3C)
-   Kevin White (W3C)
-   Kimberly McGee (SAP SE)
-   Laura Carlson (Invited Expert)
-   Len Beasley (CVS Pharmacy, Inc.)
-   Lisa Seeman-Kestenbaum (Invited Expert)
-   Lori Oakley (Oracle Corporation)
-   Makoto Murata (Information Accessibility Institute)
-   Makoto Ueki (Invited Expert)
-   Mary Jo Mueller (IBM Corporation)
-   Mike Beganyi (Invited Expert)
-   Mike Gower (IBM Corporation)
-   Patrick H. Lauke (TetraLogical Services Ltd)
-   Poornima Badhan Subramanian (Invited Expert)
-   Priti Rohra (BarrierBreak Solutions Private Limited)
-   Rachael Bradley Montgomery (Library of Congress)
-   Radostina (Ina) Tsvetkova (Invited Expert)
-   Rain Breaw Michaels (Google LLC)
-   Rashmi Katakwar (Invited Expert)
-   Rayianna Daniels-Wynn (Rhonda Weiss Center for Accessible IDEA Data)
-   Reinaldo Ferraz (NIC.br - Brazilian Network Information Center)
-   Roland Buss (SAP SE)
-   Ryan Romaine (Google LLC)
-   Sailesh Panchang (Deque Systems, Inc.)
-   Sam Hobson (Intopia)
-   Sarah Horton (Invited Expert)
-   Sazzad Mahamud (Google LLC)
-   Scott O’Hara (Microsoft Corporation)
-   Shadi Abou-Zahra (Amazon)
-   Shawn Thompson (Shared Services Canada)
-   Steve Faulkner (TetraLogical Services Ltd)
-   Steve Kerr (Google LLC)
-   Steven Hoober (Invited Expert)
-   Sydney Coleman (Google LLC)
-   Tamsin Ewing (W3C)
-   Tayef Farrar (CVS Pharmacy, Inc.)
-   Tiffany Burtin (Invited Expert)
-   Todd Libby (Invited Expert)
-   Venkata Vemuri (Oracle Corporation)
-   Wendy Reid (Invited Expert)
-   Wilco Fiers (Deque Systems, Inc.)

### D.2 Previous contributors to the development of this document

Abi James, Abi Roper, Adam Page, Alastair Campbell, Alexandra Yaneva, Alice Boxhall, Alina Vayntrub, Alistair Garrison, Amani Ali, Andrew Kirkpatrick, Andrew Somers, Andy Heath, Angela Hooker, Aparna Pasi, Ashley Firth, Atya Ratcliff, Avneesh Singh, Avon Kuo, Azlan Cuttilan, Ben Tillyer, Betsy Furler, Brooks Newton, Bruce Bailey, Bryan Trogdon, Carrie Hall, Caryn Pagel, Charles Hall, Charles Nevile, Chris Loiselle, Chris McMeeking, Christian Perera, Christy Owens, Chuck Adams, Cybele Sack, Daniel Bjorge, Daniel Henderson-Ede, Darryl Lehmann, David Fazio, David MacDonald, David Sloan, David Swallow, Dean Hamack, Detlev Fischer, DJ Chase, E.A. Draffan, Eleanor Loiacono, Eric Hind, Filippo Zorzi, Francis Storr, Frankie Wolf, Frederick Boland, Garenne Bigby, Gez Lemon, Giacomo Petri, Glenda Sims, Graham Ritchie, Greg Lowney, Gregg Vanderheiden, Gundula Niemann, Hidde de Vries, Imelda Llanos, Irfan Mukhtar, Jaeil Song, JaEun Jemma Ku, Jake Abma, Jamie Herrera, Jan Jaap de Groot, Jan McSorley, Janina Sajka, Jaunita Flessas, Jaunita George, Jeanne Spellman, Jedi Lin, Jeff Kline, Jen Goulden, Jennifer Chadwick, Jennifer Delisi, Jennifer Strickland, Jennison Asuncion, Jeroen Hulscher, Jill Power, Jim Allan, Joe Cronin, John Foliot, John Kirkwood, John McNabb, John Northup, John Rochford, John Toles, Jon Avila, Jory Cunningham, Joshue O’Connor, Judy Brewer, Julie Rawe, Justine Pascalides, Karen Schriver, Katharina Herzog, Kathleen Wahlbin, Katie Haritos-Shea, Katy Brickley, Kelsey Collister, Ken Franqueiro, Kevin White, Kim Dirks, Kimberly McGee, Kimberly Patch, Laura Carlson, Laura Miller, Len Beasley, Léonie Watson, Lisa Seeman-Kestenbaum, Lori Oakley, Lori Samuels, Lucy Greco, Luis Garcia, Lyn Muldrow, Makoto Ueki, Marc Johlic, Marie Bergeron, Mark Tanner, Mary Ann Jawili, Mary Jo Mueller, Matt Garrish, Matthew King, Melanie Philipp, Melina Maria Möhnle, Michael Cooper, Michael Crabb, Michael Elledge, Michael Fairchild, Michael Weiss, Michellanne Li, Michelle Lana, Mike Beganyi, Mike Crabb, Mike Gower, Nat Tarnoff, Nicaise Dogbo, Nicholas Trefonides, Nina Krauß, Omar Bonilla, Patrick H. Lauke, Paul Adam, Peter Korn, Peter McNally, Pietro Cirrincione, Poornima Badhan Subramanian, Rachael Bradley Montgomery, Rain Breaw Michaels, Ralph de Rooij, Rashmi Katakwar, Rebecca Monteleone, Rick Boardman, Roberto Scano, Roldon Brown, Ruoxi Ran, Ruth Spina, Ryan Hemphill, Sailesh Panchang, Sarah Horton, Sarah Pulis, Scott Hollier, Scott O’Hara, Shadi Abou-Zahra, Shannon Urban, Shari Butler, Shawn Henry, Shawn Lauriat, Shawn Thompson, Sheri Byrne-Haber, Shrirang Sahasrabudhe, Shwetank Dixit, Stacey Lumley, Stein Erik Skotkjerra, Stephen Repsher, Steve Faulkner, Steve Lee, Sukriti Chadha, Susi Pallero, Suzanne Taylor, sweta wakodkar, Takayuki Watanabe, Tananda Darling, Theo Hale, Thomas Logan, Thomas Westin, Tiffany Burtin, Tim Boland, Todd Libby, Todd Marquis Boutin, Victoria Clark, Wayne Dick, Wendy Chisholm, Wendy Reid, Wilco Fiers.

### D.3 Research Partners

These researchers selected a Silver research question, did the research, and graciously allowed us to use the results.

-   David Sloan and Sarah Horton, The Paciello Group, WCAG Success Criteria Usability Study
-   Scott Hollier et al, Curtin University, Internet of Things (IoT) Education: Implications for Students with Disabilities
-   Peter McNally, Bentley University, WCAG Use by UX Professionals
-   Dr. Michael Crabb, University of Dundee, Student research papers on Silver topics
-   Eleanor Loiacono, Worcester Polytechnic Institute Web Accessibility Perceptions (Student project from Worcester Polytechnic Institute)

### D.4 Enabling funders

This publication has been funded in part with U.S. Federal funds from the Health and Human Services, National Institute on Disability, Independent Living, and Rehabilitation Research (NIDILRR), initially under contract number ED-OSE-10-C-0067, then under contract number HHSP23301500054C, and now under HHS75P00120P00168. The content of this publication does not necessarily reflect the views or policies of the U.S. Department of Health and Human Services or the U.S. Department of Education, nor does mention of trade names, commercial products, or organizations imply endorsement by the U.S. Government.

\[RFC2119\]

[Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: [https://www.rfc-editor.org/rfc/rfc2119](https://www.rfc-editor.org/rfc/rfc2119)

\[RFC8174\]

[Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: [https://www.rfc-editor.org/rfc/rfc8174](https://www.rfc-editor.org/rfc/rfc8174)

\[ATAG20\]

[Authoring Tool Accessibility Guidelines (ATAG) 2.0](https://www.w3.org/TR/ATAG20/). Jan Richards; Jeanne F Spellman; Jutta Treviranus. W3C. 24 September 2015. W3C Recommendation. URL: [https://www.w3.org/TR/ATAG20/](https://www.w3.org/TR/ATAG20/)

\[ISO\_9241-391\]

[Ergonomics of human-system interaction—Part 391: Requirements, analysis and compliance test methods for the reduction of photosensitive seizures](https://www.iso.org/standard/56350.html). International Standards Organization. URL: [https://www.iso.org/standard/56350.html](https://www.iso.org/standard/56350.html)

\[SRGB\]

[Multimedia systems and equipment - Colour measurement and management - Part 2-1: Colour management - Default RGB colour space - sRGB](https://webstore.iec.ch/publication/6169). IEC. URL: [https://webstore.iec.ch/publication/6169](https://webstore.iec.ch/publication/6169)

\[UAAG20\]

[User Agent Accessibility Guidelines (UAAG) 2.0](https://www.w3.org/TR/UAAG20/). James Allan; Greg Lowney; Kimberly Patch; Jeanne F Spellman. W3C. 15 December 2015. W3C Working Group Note. URL: [https://www.w3.org/TR/UAAG20/](https://www.w3.org/TR/UAAG20/)

\[WCAG22\]

[Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). Michael Cooper; Andrew Kirkpatrick; Alastair Campbell; Rachael Bradley Montgomery; Charles Adams. W3C. 12 December 2024. W3C Recommendation. URL: [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/)
