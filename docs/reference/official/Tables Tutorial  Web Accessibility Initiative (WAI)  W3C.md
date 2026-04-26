---
created: 2026-04-26T13:11:48 (UTC -05:00)
tags: []
source: https://www.w3.org/WAI/tutorials/tables/
author: W3C Web Accessibility Initiative (WAI)
---

# Tables Tutorial | Web Accessibility Initiative (WAI) | W3C

> ## Excerpt
> Accessibility resources free online from the international standards organization: W3C Web Accessibility Initiative (WAI).

---
in [Tutorials](https://www.w3.org/WAI/tutorials/)

Data tables are used to organize data with a logical relationship in grids. Accessible tables need HTML markup that indicates header cells and data cells and defines their relationship. Assistive technologies use this information to provide context to users.

Header cells must be marked up with `<th>`, and data cells with `<td>` to make tables accessible. For more complex tables, explicit associations may be needed using `scope`, `id`, and `headers` attributes.

This tutorial shows you how to apply appropriate structural markup to tables. It includes the following pages:

-   **[Tables with one header![](https://www.w3.org/WAI/content-images/tutorials/tables/img-simple.png)](https://www.w3.org/WAI/tutorials/tables/one-header/)** for rows or columns: For tables with content that is easy to distinguish, mark up header cells with `<th>` and data cells with `<td>` elements.
    
-   **[Tables with two headers![](https://www.w3.org/WAI/content-images/tutorials/tables/img-multidir.png)](https://www.w3.org/WAI/tutorials/tables/two-headers/)** have a simple row header and a simple column header: For tables with unclear header directions, define the direction of each header by setting the `scope` attribute to `col` or `row`.
    
-   **[Tables with irregular headers![](https://www.w3.org/WAI/content-images/tutorials/tables/img-irreg.png)](https://www.w3.org/WAI/tutorials/tables/irregular/)** have header cells that span multiple columns and/or rows: For these tables, define column and row groups and set the range of the header cells using the `colgroup` and `rowgroup` values of the scope attribute.
    
-   **[Tables with multi-level headers![](https://www.w3.org/WAI/content-images/tutorials/tables/img-multi.png)](https://www.w3.org/WAI/tutorials/tables/multi-level/)** have multiple header cells associated per data cell: For tables that are so complex that header cells can’t be associated in a strictly horizontal or vertical way, use `id` and `headers` attributes to associate header and data cells explicitly.
    
-   **[Caption & Summary![](https://www.w3.org/WAI/content-images/tutorials/tables/img-caption.png)](https://www.w3.org/WAI/tutorials/tables/caption-summary/):** A caption identifies the overall topic of a table and is useful in most situations. A summary provides orientation or navigation hints in complex tables.
    

Some document formats other than HTML, such as PDF, provide similar mechanisms to markup table structures. Word processing applications may also provide mechanisms to markup tables. Tables markup is often lost when converting from one format to another, though some programs may provide functionality to assist converting table markup.

Many web authoring tools and content management systems (CMS) provide functions to define header cells during table creation without having to edit the code manually.

## Why is this important?

Tables without structural markup to differentiate and properly link between header and data cells, create accessibility barriers. Relying on visual cues alone is not sufficient to create an accessible table. With structural markup, headers and data cells can be programmatically determined by software, which means that:

-   **People using screen readers** can have the row and column headers read aloud as they navigate through the table. Screen readers speak one cell at a time and reference the associated header cells, so the reader doesn’t lose context.
    
-   **Some people use alternative ways to render the data**, for example by using custom stylesheets to display header cells more prominently. Techniques like this enable them to change text size and colors and display the information as lists rather than grids. The table code needs to be properly structured to allow alternative renderings.
    

[Back to Top](https://www.w3.org/WAI/tutorials/tables/#top)
