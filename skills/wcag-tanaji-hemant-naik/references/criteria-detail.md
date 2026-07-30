# WCAG 2.2 Success Criteria — Detailed Reference

This file provides detailed guidance for all WCAG 2.2 Level A and AA success criteria. Read only the sections relevant to the current task.

## Table of Contents

- [1.1 Text Alternatives](#11-text-alternatives)
- [1.2 Time-based Media](#12-time-based-media)
- [1.3 Adaptable](#13-adaptable)
- [1.4 Distinguishable](#14-distinguishable)
- [2.1 Keyboard Accessible](#21-keyboard-accessible)
- [2.2 Enough Time](#22-enough-time)
- [2.3 Seizures and Physical Reactions](#23-seizures-and-physical-reactions)
- [2.4 Navigable](#24-navigable)
- [2.5 Input Modalities](#25-input-modalities)
- [3.1 Readable](#31-readable)
- [3.2 Predictable](#32-predictable)
- [3.3 Input Assistance](#33-input-assistance)
- [4.1 Compatible](#41-compatible)
- [WCAG 2.2 New Criteria Summary](#wcag-22-new-criteria-summary)
- [Testing Tools Reference](#testing-tools-reference)

---

## 1.1 Text Alternatives

### SC 1.1.1 Non-text Content (Level A)

**Requirement:** All non-text content has a text alternative that serves the equivalent purpose.

**Sufficient techniques:**
- `G94`: Providing short text alternative for non-text content that serves the same purpose
- `H37`: Using `alt` attributes on `<img>` elements
- `H36`: Using `alt` attributes on images used as submit buttons
- `ARIA6`: Using `aria-label` to provide labels for objects
- `H67`: Using null alt text and no title attribute on img for images that AT should ignore

**Common failures:**
- F3: Using CSS background images to convey information with no text equivalent
- F13: Using text alternatives that do not include information conveyed by color or position in an image
- F20: Not updating text alternatives when non-text content changes
- F30: Using text alternatives that are not alternatives (same as filename, placeholder text, etc.)
- F38: Not marking up decorative images so they can be ignored by AT
- F65: Omitting the alt attribute or text alternative on img elements, area elements, or input elements of type "image"

**Scope:**
- Informative images → meaningful alt text
- Decorative images → `alt=""` with no title
- Functional images (buttons, links) → alt describes function, not appearance
- Complex images (charts, diagrams) → short alt + long description via `aria-describedby`, `longdesc`, or adjacent text
- Captchas → provide audio captcha or text alternative explaining what captcha is for
- Purely decorative text or text part of a logo → may be treated as decorative

---

## 1.2 Time-based Media

### SC 1.2.1 Audio-only and Video-only — Pre-recorded (Level A)
Provide a text transcript for pre-recorded audio-only. Provide a text alternative or audio track for pre-recorded video-only.

### SC 1.2.2 Captions — Pre-recorded (Level A)
All pre-recorded audio content in synchronised media has captions. Auto-generated captions alone do not satisfy this unless they are accurate and reviewed.

**Key requirements for captions:**
- Synchronised with the audio
- Verbatim (or close equivalent for edited captions)
- Identify speakers
- Include relevant sound effects [applause], [laughter] when they convey meaning

### SC 1.2.3 Audio Description or Media Alternative — Pre-recorded (Level A)
An alternative for time-based media or audio description of the prerecorded video content in synchronized media is provided, except where the media is a media alternative for text and is clearly labeled as such.

### SC 1.2.4 Captions — Live (Level AA)
Captions are provided for all live audio content in synchronised media. Live captions may be provided by CART (Communication Access Realtime Translation) services.

### SC 1.2.5 Audio Description — Pre-recorded (Level AA)
Audio description is provided for all prerecorded video content in synchronised media. Describes visual information not conveyed in the audio track: actions, scene changes, on-screen text.

---

## 1.3 Adaptable

### SC 1.3.1 Info and Relationships (Level A)

**Requirement:** Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text.

**Key patterns:**
- Use `<h1>`–`<h6>` for headings — not styled `<div>` or `<p>` elements
- Use `<table>` with `<th scope="col|row">` for data tables; use `<caption>` for table title
- Use `<label for="id">` to associate form labels, or `aria-labelledby`/`aria-label`
- Use `<fieldset>` and `<legend>` for groups of related inputs (radio buttons, checkboxes)
- Use `<ul>`, `<ol>`, `<dl>` for lists; don't fake lists with dashes and line breaks
- Required fields: mark with `aria-required="true"` or `required`; don't rely on colour alone

**Common failures:**
- F2: Using changes in text presentation to convey information without using the appropriate markup
- F17: Relying on CSS visual placement to associate labels with form controls
- F33: Using white space characters to create multiple columns in plain text
- F34: Using white space characters to format tables in plain text
- F42: Using scripting events to emulate links without appropriate semantic markup
- F43: Using structural markup in a way that does not represent relationships in the content
- F46: Using `summary` attribute on layout table (misrepresents it as data table)
- F48: Using the `pre` element to markup tabular information
- F68: Association between a label and control not programmatically determined
- F87: Inserting spacer images with no alt text into tables used for layout
- F91: Not marking up table headers correctly

### SC 1.3.2 Meaningful Sequence (Level A)
The reading sequence can be determined programmatically when the presentation sequence affects meaning. DOM order should match visual reading order; CSS positioning must not reorder meaningful content.

### SC 1.3.3 Sensory Characteristics (Level A)
Instructions do not rely solely on sensory characteristics such as shape, colour, size, visual location, orientation, or sound. Example failure: "click the round button" or "see the form in the right column."

### SC 1.3.4 Orientation (Level AA — WCAG 2.1)
Content does not restrict its view and operation to a single display orientation unless essential. Mobile sites should support both portrait and landscape unless orientation is essential (e.g., piano app).

### SC 1.3.5 Identify Input Purpose (Level AA — WCAG 2.1)
The purpose of each input field collecting information about the user can be programmatically determined using the HTML `autocomplete` attribute with defined token values.

**Key autocomplete tokens:**
- `name`, `given-name`, `family-name`
- `email`, `tel`
- `street-address`, `address-line1`, `address-line2`, `postal-code`, `country`
- `bday`, `sex`
- `current-password`, `new-password`
- `cc-name`, `cc-number`, `cc-exp`

---

## 1.4 Distinguishable

### SC 1.4.1 Use of Colour (Level A)
Colour is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

**Fixes:** Add text labels, icons, patterns, or other non-colour differentiators alongside colour.

### SC 1.4.2 Audio Control (Level A)
Auto-playing audio longer than 3 seconds can be paused or stopped by the user, or the volume can be adjusted independently from the system volume.

### SC 1.4.3 Contrast — Minimum (Level AA)
- Normal text (below 18pt or 14pt bold): **4.5:1** minimum contrast ratio
- Large text (18pt/24px+ regular OR 14pt/18.67px+ bold): **3:1** minimum
- Logotypes, inactive UI components, decorative text: exempt

**Formula:** Contrast ratio = (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter luminance and L2 is the darker relative luminance. Relative luminance uses the sRGB colour model.

**Tools:** WebAIM Contrast Checker, Colour Contrast Analyser (desktop app), browser DevTools > Accessibility > Contrast.

**Edge cases:**
- Placeholder text in inputs: often fails — must meet 4.5:1 if it's the only content visible
- Text in images: must meet contrast requirements
- Text over gradient/image backgrounds: check at the worst-case overlap area

### SC 1.4.4 Resize Text (Level AA)
Text can be resized without assistive technology up to 200 percent without loss of content or functionality. Use relative units (`rem`, `em`, `%`) rather than `px` for font sizes and container heights. Test at 200% browser zoom with no horizontal scrollbar for single-column content.

### SC 1.4.5 Images of Text (Level AA)
Text is used to convey information rather than images of text, except for logotypes or where the image of text is essential to the information conveyed.

### SC 1.4.10 Reflow (Level AA — WCAG 2.1)
Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
- Vertical-scrolling content at a width equivalent to 320 CSS pixels
- Horizontal-scrolling content at a height equivalent to 256 CSS pixels

**Exception:** Content that requires two-dimensional layout for its usage or meaning (data tables, maps, diagrams, videos, games).

**Test method:** Set browser viewport to 320px width (or zoom to 400% on 1280px display) and verify no horizontal scrollbar appears.

### SC 1.4.11 Non-text Contrast (Level AA — WCAG 2.1)
UI components (form fields, buttons, focus indicators) and informational graphics have a contrast ratio of at least **3:1** against adjacent colours.

**Scope:**
- Input borders against background
- Checkbox/radio outlines
- Focus indicators (custom)
- Chart lines, graph bars, data points
- Icons that convey meaning (not decorative)

**Exempt:** Inactive/disabled components; logotypes; purely decorative graphics.

### SC 1.4.12 Text Spacing (Level AA — WCAG 2.1)
No loss of content or functionality when all the following text spacing properties are overridden simultaneously:
- Line height ≥ 1.5 × font size
- Letter spacing ≥ 0.12 × font size
- Word spacing ≥ 0.16 × font size
- Spacing following paragraphs ≥ 2 × font size

**Test:** Use the Text Spacing bookmarklet to apply all four properties at once and check for clipped/overlapping text.

### SC 1.4.13 Content on Hover or Focus (Level AA — WCAG 2.1)
Additional content that appears on hover or keyboard focus must be:
1. **Dismissable** — user can dismiss it without moving the pointer or focus (typically via Escape)
2. **Hoverable** — if the trigger is hover, the pointer can move over the additional content without it disappearing
3. **Persistent** — the content stays visible until the user dismisses it, moves focus/pointer away, or the information is no longer valid

**Common failures:** Tooltips that disappear when pointer moves toward them; tooltips with no way to dismiss.

---

## 2.1 Keyboard Accessible

### SC 2.1.1 Keyboard (Level A)
All functionality is available via keyboard without requiring specific timings for individual keystrokes.

**Required keyboard patterns (ARIA Authoring Practices Guide):**
- Dropdown menus: Arrow keys to navigate, Enter/Space to activate, Escape to close
- Dialogs/modals: Tab within modal, Escape to close, focus returns to trigger on close
- Tabs: Arrow keys between tabs, Tab into tabpanel content
- Sliders: Arrow keys to change value, Home/End for min/max
- Date pickers: Arrow keys for day navigation, Page Up/Down for month/year
- Tree views: Arrow keys, Enter to activate
- Autocomplete: Arrow keys, Enter to select, Escape to close

**Common failures:** Mouse-only `onclick`, `onmouseover` handlers on non-focusable elements; drag-and-drop without keyboard alternative; inaccessible custom widgets.

### SC 2.1.2 No Keyboard Trap (Level A)
Keyboard focus can be moved from any component using standard keys (Tab, Shift+Tab, arrow keys). If non-standard keys are needed, the user is informed.

**Modal dialogs:** Focus may be intentionally constrained to the modal, but there must be a way to close and return focus to the trigger.

### SC 2.1.4 Character Key Shortcuts (Level A — WCAG 2.1)
If single-character key shortcuts are implemented, at least one of: the shortcut can be turned off, remapped, or only active on focus.

---

## 2.2 Enough Time

### SC 2.2.1 Timing Adjustable (Level A)
For time limits set by the content: the user can turn off, adjust, or extend the limit. Exception: real-time events (auctions), essential time limits, >20 hours.

**Best practice:** Warn users 20 seconds before session timeout with an option to extend.

### SC 2.2.2 Pause, Stop, Hide (Level A)
For moving, blinking, scrolling, or auto-updating information that starts automatically and lasts more than 5 seconds: provide controls to pause, stop, or hide it. Exception: essential movement.

---

## 2.3 Seizures and Physical Reactions

### SC 2.3.1 Three Flashes or Below (Level A)
No content flashes more than three times per second OR the flash is below the general flash and red flash thresholds. Applies to video, animations, GIFs, and scripted effects.

---

## 2.4 Navigable

### SC 2.4.1 Bypass Blocks (Level A)
A mechanism to skip blocks of content repeated on multiple pages. Typically implemented as a skip link ("Skip to main content") or via ARIA landmark regions (`main`, `nav`, `header`, `footer`, `aside`).

**Best practice:** Provide both a visible skip link and proper landmark structure. Skip link should be the first focusable element and should become visible on focus.

### SC 2.4.2 Page Titled (Level A)
Web pages have titles that describe topic or purpose. Titles should be unique across the site and follow the pattern "Page-specific title — Site name."

### SC 2.4.3 Focus Order (Level A)
Focusable components receive focus in an order that preserves meaning and operability. DOM order should match visual reading order; avoid `tabindex` values greater than 0 which disrupt natural tab order.

### SC 2.4.4 Link Purpose — In Context (Level A)
The purpose of each link can be determined from the link text alone, or from the link text plus its programmatic context (enclosing sentence, list item, table cell, or associated header).

**Failures:** "Click here", "Read more", "Learn more" with no accessible context.

**Fix:** Use descriptive link text ("Read our WCAG 2.2 guide") or supplement with `aria-label` or `aria-describedby`.

### SC 2.4.5 Multiple Ways (Level AA)
More than one way to locate a page within a set of pages. At least two of: site navigation, site search, site map, table of contents, list of related pages. Exception: pages that are the result of a process (checkout confirmation).

### SC 2.4.6 Headings and Labels (Level AA)
Headings and labels describe the topic or purpose of the content they apply to. Headings must be meaningful — not "Section 1" or "Content."

### SC 2.4.7 Focus Visible (Level AA)
Any keyboard operable interface has a mode of operation where the keyboard focus indicator is visible. Do not use `outline: none` without a replacement focus style.

**Best practice:** Use `focus-visible` CSS pseudo-class to show focus only for keyboard users (not mouse clicks).

### SC 2.4.11 Focus Not Obscured — Minimum (Level AA — WCAG 2.2)
When a UI component receives keyboard focus, it is not entirely hidden due to author-created content (sticky headers, banners, cookie notices, chat bubbles). The component may be partially obscured; it just must not be completely hidden.

**Fix:** Ensure `scroll-margin-top` or equivalent compensates for sticky header height; or use `position: sticky` with sufficient top offset.

### SC 2.4.12 Focus Not Obscured — Enhanced (Level AAA — WCAG 2.2)
The focused component is not hidden by any author-created content. The entire component is fully visible when focused.

### SC 2.4.13 Focus Appearance (Level AAA — WCAG 2.2)
The focus indicator area: (a) encloses the UI component or its text; (b) has a contrast ratio of at least 3:1 between focused and unfocused states; (c) has a contrast ratio of at least 3:1 against adjacent colours; and (d) is not entirely obscured.

---

## 2.5 Input Modalities

### SC 2.5.1 Pointer Gestures (Level A — WCAG 2.1)
All functionality using multipoint (pinch/zoom) or path-based gestures (swipe) has a single-pointer alternative that doesn't require a specific path.

### SC 2.5.2 Pointer Cancellation (Level A — WCAG 2.1)
For functionality activated with a single pointer: at least one of: no down-event activation; up-event can abort/undo; up-event reverses down-event; down-event essential.

**Failure:** Click action fires on `mousedown` rather than `mouseup`, preventing users from cancelling by moving the pointer away.

### SC 2.5.3 Label in Name (Level A — WCAG 2.1)
For UI components with visible text labels, the accessible name (computed name from `aria-label`, `aria-labelledby`, or native label) contains the visible label text.

**Failure:** Button visually labelled "Submit form" but `aria-label="Send"` — voice control users saying "click Submit form" will not activate it.

### SC 2.5.4 Motion Actuation (Level A — WCAG 2.1)
Functionality triggered by device motion (shaking, tilting) can also be operated via UI components and motion response can be disabled (except where motion is essential).

### SC 2.5.7 Dragging Movements (Level AA — WCAG 2.2)
All functionality that uses a dragging movement for operation can also be achieved with a single pointer without dragging.

**Examples:** Sortable list with drag handles — must have up/down buttons; range slider with drag — must have text input or increment buttons; kanban card drag-and-drop — must have a keyboard-accessible alternative.

### SC 2.5.8 Target Size — Minimum (Level AA — WCAG 2.2)
The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except where:
- **Spacing:** Undersized targets are offset from other targets by at least 24px in all directions
- **Equivalent:** The function can be achieved through an equivalent control that meets the criterion
- **Inline:** Target is in a sentence or its size is constrained by the line-height of non-target text
- **User agent:** The target size is determined by the user agent and not modified by the author
- **Essential:** A particular presentation is essential to the information conveyed

**Recommendation:** Aim for at least 44×44 CSS pixels for all touch targets (iOS/Android HIG recommendation).

---

## 3.1 Readable

### SC 3.1.1 Language of Page (Level A)
The default human language of each web page can be programmatically determined. Set `lang` attribute on `<html>` element (e.g., `<html lang="en">`). Use valid BCP 47 language tags.

### SC 3.1.2 Language of Parts (Level AA)
Human language of each passage or phrase in the content can be programmatically determined except for proper names, technical terms, indeterminate language, and words that have become part of the vernacular.

**Fix:** `<span lang="fr">Bonjour</span>` for inline foreign language content.

---

## 3.2 Predictable

### SC 3.2.1 On Focus (Level A)
When a UI component receives focus, it does not initiate a change of context (new window, form submission, significant page change).

### SC 3.2.2 On Input (Level A)
Changing the setting of a UI component does not automatically cause a change of context unless the user has been advised before using the component.

**Failure:** Selecting a radio button or option in a select element immediately navigates to a new page without a submit button.

### SC 3.2.3 Consistent Navigation (Level AA)
Navigational mechanisms that are repeated on multiple pages appear in the same relative order each time they are repeated, unless a change is initiated by the user.

### SC 3.2.4 Consistent Identification (Level AA)
Components that have the same functionality within a set of web pages are identified consistently.

**Failure:** Search feature labelled "Search" on most pages but "Find" on others; or "Go" instead of "Submit" for the same form action.

### SC 3.2.6 Consistent Help (Level A — WCAG 2.2)
If a web page provides help mechanisms (contact details, human contact, self-help option, automated contact mechanism), those mechanisms appear in the same location relative to other page content across a set of web pages, unless a change is initiated by the user.

---

## 3.3 Input Assistance

### SC 3.3.1 Error Identification (Level A)
If an input error is automatically detected, the item in error is identified and the error is described to the user in text.

**Requirements:**
- Error messages must be in text (not just colour or icon)
- Must identify which field is in error
- Must describe the error
- Must be programmatically associated with the field (`aria-describedby` or adjacent text)

### SC 3.3.2 Labels or Instructions (Level A)
Labels or instructions are provided when content requires user input. Format hints (e.g., "MM/DD/YYYY") must be provided before or within the form field.

### SC 3.3.3 Error Suggestion (Level AA)
If an input error is automatically detected and suggestions for correction are known, then the suggestion is provided to the user.

**Not sufficient:** "Invalid input" — the error must explain what is wrong.

**Sufficient:** "Please enter a date in MM/DD/YYYY format" or "Password must be at least 8 characters and include a number."

### SC 3.3.4 Error Prevention — Legal, Financial, Data (Level AA)
For pages that cause legal commitments, financial transactions, modify/delete user-controlled data, or submit test responses, at least one of:
1. **Reversible** — submission is reversible
2. **Checked** — data entered is checked for errors and user is given opportunity to correct them
3. **Confirmed** — mechanism is available for reviewing, confirming, and correcting information before finalising

### SC 3.3.7 Redundant Entry (Level A — WCAG 2.2)
Information previously entered by or provided to the user that is required again in the same process is either auto-populated or available for the user to select.

**Exception:** Re-entering information essential for security reasons (e.g., password confirmation) or when the previously entered information is no longer valid.

### SC 3.3.8 Accessible Authentication — Minimum (Level AA — WCAG 2.2)
A cognitive function test (remember a password, solve a puzzle, recognise objects) is not required for any step in an authentication process unless the step provides an alternative that does not rely on cognitive function test, a mechanism to assist the user in completing the cognitive function test, or the cognitive function test is to recognise objects.

**Common failure:** CAPTCHA with no accessible alternative (audio CAPTCHA, support contact option, or single-use login link).

**Passes:** Email magic link (no cognitive test); passkey/biometric authentication; CAPTCHA with audio alternative and support option.

---

## 4.1 Compatible

### SC 4.1.1 Parsing (Level A — Removed in WCAG 2.2)
In WCAG 2.0 and 2.1, required valid markup (no duplicate IDs, complete start/end tags, proper nesting). Removed from WCAG 2.2 because modern browsers handle parsing errors gracefully. Still relevant for WCAG 2.0/2.1 conformance claims and Section 508 compliance.

**Remaining concern:** Duplicate IDs still cause failures for `aria-labelledby` and `aria-describedby` associations.

### SC 4.1.2 Name, Role, Value (Level A)
For all UI components, the name and role can be programmatically determined; states, properties, and values that can be set by the user can be programmatically determined; and notification of changes to these items is available to user agents, including assistive technologies.

**Key ARIA patterns:**

| Widget | Required ARIA |
|--------|--------------|
| Accordion | `role="button"`, `aria-expanded`, `aria-controls` |
| Alert | `role="alert"` or `aria-live="assertive"` |
| Autocomplete | `role="combobox"`, `aria-expanded`, `aria-autocomplete`, `aria-activedescendant` |
| Button (toggle) | `role="button"`, `aria-pressed` |
| Checkbox (custom) | `role="checkbox"`, `aria-checked` |
| Dialog | `role="dialog"`, `aria-modal`, `aria-labelledby` |
| Menu | `role="menu"`, `role="menuitem"`, `aria-haspopup`, `aria-expanded` |
| Progressbar | `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax` |
| Radio (custom) | `role="radio"`, `aria-checked`, within `role="radiogroup"` |
| Slider | `role="slider"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax` |
| Tab/Tabpanel | `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls` |
| Tooltip | `role="tooltip"`, triggered by `aria-describedby` |

### SC 4.1.3 Status Messages (Level AA — WCAG 2.1)
Status messages can be programmatically determined through role or properties so they can be presented by assistive technologies without receiving focus.

**ARIA live region patterns:**
- `aria-live="polite"`: non-urgent status messages (form saved, item added to cart)
- `aria-live="assertive"`: urgent messages (error, session expiring soon) — use sparingly
- `role="status"`: polite live region (same as `aria-live="polite"`)
- `role="alert"`: assertive live region (same as `aria-live="assertive"`)
- `role="log"`: chat, activity log — items added in order
- `aria-atomic="true"`: announce entire region content when any change occurs

**Common failures:**
- Success banner injected into DOM without a live region role — screen readers don't announce it
- Error summary appended to form without focus management or live region
- "Loading…" spinner with no accessible live region update when loading completes

---

## WCAG 2.2 New Criteria Summary

WCAG 2.2 (October 2023) added 9 new success criteria and removed SC 4.1.1 Parsing.

| SC | Name | Level | Change |
|----|------|-------|--------|
| 2.4.11 | Focus Not Obscured (Minimum) | AA | New |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | New |
| 2.4.13 | Focus Appearance | AAA | New |
| 2.5.7 | Dragging Movements | AA | New |
| 2.5.8 | Target Size (Minimum) | AA | New |
| 3.2.6 | Consistent Help | A | New |
| 3.3.7 | Redundant Entry | A | New |
| 3.3.8 | Accessible Authentication (Minimum) | AA | New |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | New |
| 4.1.1 | Parsing | — | Removed |

---

## Testing Tools Reference

### Automated Testing Tools

| Tool | Type | Catches | Notes |
|------|------|---------|-------|
| axe-core | Browser ext / CI | ~35% of WCAG 2.x | Zero false positives philosophy; use axe DevTools for browser |
| Lighthouse | Browser (Chrome DevTools) | ~20–30% | Good for quick audits; part of PageSpeed Insights |
| WAVE | Browser ext | ~30–35% | Good visual overlay; highlights structural issues |
| IBM Equal Access Checker | Browser ext | ~40% | Strong for ARIA and dynamic content |
| Deque aXe-cli | CLI | ~35% | Good for CI pipelines |
| Pa11y | CLI | ~30% | Uses axe or htmlcs under the hood |
| Colour Contrast Analyser | Desktop | Contrast only | Essential for SC 1.4.3 and 1.4.11 |

Automated tools combined typically find 30–40% of all WCAG failures. Manual testing is essential.

### Manual Testing Checklist

1. **Keyboard navigation** — Tab through entire page; verify all interactive elements reachable; verify focus order is logical; verify no traps
2. **Screen reader** — NVDA+Chrome, JAWS+Chrome, VoiceOver+Safari (macOS), VoiceOver+Safari (iOS), TalkBack+Chrome (Android)
3. **Colour contrast** — Use Colour Contrast Analyser on all text, UI components, informational graphics
4. **Zoom/Reflow** — Browser zoom to 200% (SC 1.4.4); set viewport to 320px (SC 1.4.10)
5. **Text spacing** — Apply text spacing bookmarklet (SC 1.4.12)
6. **Forms** — Verify all inputs labelled; verify error messages associated; verify autocomplete attributes
7. **Dynamic content** — Verify live regions announce updates; verify modal focus management
8. **Images** — Check alt text quality; verify decorative images are hidden from AT
9. **Videos** — Verify captions; verify audio descriptions
10. **Touch/pointer** — Verify touch target sizes; verify no drag-only interactions

### Screen Reader + Browser Pairings

| Screen Reader | Best Browser | Usage |
|--------------|-------------|-------|
| JAWS (Windows) | Chrome or Edge | Federal/enterprise standard; most used SR in US |
| NVDA (Windows) | Chrome or Firefox | Free; widely used for testing; good coverage |
| VoiceOver (macOS) | Safari | Required for Mac conformance testing |
| VoiceOver (iOS) | Safari | Mobile web and native iOS |
| TalkBack (Android) | Chrome | Android web and native apps |
| Narrator (Windows) | Edge | Windows built-in; test if targeting Edge users |

### Bookmarklets and Extensions

- **Text Spacing Bookmarklet** (by Steve Faulkner) — applies all SC 1.4.12 spacing properties simultaneously
- **NoCoffee Vision Simulator** — simulates various visual impairments
- **Landmarks browser extension** — shows ARIA landmark structure
- **HeadingsMap** — shows heading hierarchy
- **Accessibility Insights** (Microsoft) — guided manual testing workflows
