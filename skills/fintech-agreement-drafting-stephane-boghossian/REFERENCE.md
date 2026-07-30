# Reference — Drafting & Finalising a Complex Multi-Pillar Fintech Agreement

> **Source manual** bundled with the `fintech-agreement-drafting` Claude skill.
> Methodology authored by **Abbas, Chief Legal Officer, HAQQ Legal AI**.
> Packaged as a skill by **Stephane Boghossian** (Head of Growth, HAQQ Legal AI).
> Licensed **AGPL-3.0**.
>
> This is the verbatim manual the skill operationalises. The skill
> (`SKILL.md`) is the executable workflow; this file is the underlying prose,
> worked tables, and callouts. Nothing here is legal or regulatory advice;
> every licence-specific value must be verified against the governing
> instrument.

---

**Drafting & Finalising a Complex**

**Multi-Pillar Fintech Agreement**

# How to Use This Manual

This manual sets out a repeatable, end-to-end method for drafting a multi-pillar fintech agreement and bringing it to execution. It is written for the drafting lawyer, not for the client. It assumes a deal in which a licensed payment-services provider engages a counterparty across several distinct service lines, each of which carries its own regulatory profile.

The structure follows the natural lifecycle of the matter: intake and regulatory mapping, architecture, core clause drafting, resolution of execution blockers, and iteration to signature. Each phase contains numbered steps with the analytical task, the drafting output, and the traps to watch. Callout boxes flag practice notes, drafting tips, and red flags. The worked example throughout is a payments framework bundling cash-in/cash-out agency, QR payments, wallet e-payments, and a marketplace integration, but the method generalises to any regulated, multi-service fintech contract.

|  |
| --- |
| **HOW TO READ THE CALLOUTS**  **Practice Note** — analytical guidance and reasoning to apply.  **Drafting Tip** — concrete clause-level technique.  **Red Flag** — a recurring failure mode that delays or defeats execution. |

# Contents

# Phase 1: Intake & Regulatory Mapping

Nothing is drafted in Phase 1. The work here is diagnostic. Drafting before the regulatory perimeter is mapped is the single most expensive mistake on a fintech matter, because a misclassified activity contaminates every downstream clause: the licence basis, the permitted commission, the KYC allocation, and the representations.

## Step 1: Identify the regulated activity and its licence basis

Classify what the client is actually doing before you classify what the contract says. In a payment-services context, isolate each activity and tie it to the specific provision of the central bank's licensing instrument that authorises it. Typical activities include e-money issuance, agent-based cash-in and cash-out, QR-code payments, and wallet-funded e-payments. Each activity has a different regulatory footprint, and a single deal frequently spans several at once.

|  |
| --- |
| **PRACTICE NOTE**  Build a one-page activity-to-licence matrix at intake. List every service the deal contemplates in the left column; in the right column, name the precise article or decision that licenses it. Any activity you cannot tie to a provision is either out of scope, requires a licence extension, or needs a regulator ruling. That blank cell is your earliest warning of an execution blocker. |

## Step 2: Resolve classification gates early

Some activities sit in a grey zone. The recurring example is the QR transaction: is it a peer-to-peer transfer between two onboarded wallet users, or is it merchant acquiring, payment facilitation, or gateway activity? The distinction is not academic. It changes the applicable commission ceiling, the KYC and onboarding obligations, and whether the existing licence covers the service or a separate authorisation is required.

Resolve the classification before drafting the pillar, by one of two routes: (*a*) a written non-objection or no-action position from the regulator, or (*b*) a reasoned written legal opinion that the activity falls within the licensed perimeter and records the basis for that conclusion. Treat the unresolved gate as an execution-blocking condition, not a drafting detail to be papered over.

|  |
| --- |
| **RED FLAG**  Do not let commercial momentum push a grey-zone activity into the contract on the assumption it will be sorted out later. If the QR pillar is classified as acquiring rather than P2P after signature, the commission terms may breach the cap and the pillar may be operating outside the licence. Gate it: the pillar does not go live until the classification is confirmed in writing. |

## Step 3: Map the parties' true roles

Pin down, in substance and not just in label, which party is the licensed financial institution, which is merely an agent or payment acceptor, and which bears no financial-institution status at all. This single determination governs the entire allocation of KYC and AML execution, transaction authority, float ownership, audit rights, and liability. Get it wrong and the agent inadvertently acquires regulated-entity obligations, or the licensed party silently disclaims duties it cannot lawfully delegate.

| **Party** | **Status** | **Core function** | **Must NOT do** |
| --- | --- | --- | --- |
| Licensed PSP | Financial institution | KYC/AML, authorisation, float, reporting | Delegate non-delegable regulatory duties |
| Counterparty / agent | Agent & acceptor only | Cash handling, physical operations | Act as financial intermediary; hold out as FI |
| Marketplace operator | Merchant | Sell goods/services via the rails | Touch the regulated payment flow |

# Phase 2: Architecture

With the perimeter mapped, choose the contractual structure before writing clauses. Architecture decisions made now determine whether pillars can launch, pause, and terminate independently, and whether regulatory risk in one service line can be quarantined from the others.

## Step 4: Use a framework plus sub-agreements for multi-pillar deals

When a deal bundles several independent services, do not draft one monolithic contract. Use a General Framework Agreement that sets the common terms, namely definitions, compliance obligations, liability allocation, term and termination, confidentiality, and governing law. Then attach a separate, separately executed sub-agreement for each pillar: cash-in/cash-out, QR payments, wallet e-payments, and marketplace integration. The framework binds the relationship; each sub-agreement operationalises one service.

|  |
| --- |
| **DRAFTING TIP**  Make the framework the single source of truth for shared terms and have every sub-agreement incorporate it by reference, with an express order-of-precedence clause. State that, in the event of conflict, the framework governs except where a sub-agreement expressly and specifically derogates from it for that pillar. This prevents a later sub-agreement from silently overriding a compliance term that must hold across the whole relationship. |
| **PRACTICE NOTE**  Independent execution is the commercial payoff of this structure. A regulator query, a failed condition precedent, or a commercial dispute confined to one pillar should not stall or unwind the others. Draft termination so that each pillar can be suspended or terminated on its own without collapsing the framework, and so that termination of the framework cascades to all pillars but not vice versa. |

## Step 5: Ring-fence the riskiest pillar

Where one pillar carries a materially different risk profile, give it a standalone agreement and keep it out of the regulated payment flow. The marketplace pillar is the usual candidate: it introduces product liability, delivery and fulfilment disputes, and third-party merchants whose conduct the licensed party cannot fully control. Treat the marketplace operator as it would any third-party merchant, under standard merchant terms, KYC, and onboarding, rather than folding it into the agency or wallet structure.

|  |
| --- |
| **RED FLAG**  Folding a marketplace into the payments rails imports consumer-goods liability into a regulated payments contract and blurs the line the regulator cares about most: who is performing the payment service. Ring-fence it. Product and delivery disputes belong with the marketplace operator; the payment rails should see the marketplace as just another merchant. |

# Cross-Cutting: The Regulatory–Commercial Balance

This section sits between architecture and drafting because that is where the balancing actually gets decided, but the principle runs through every phase of the matter. A fintech lawyer is rarely asked to choose between compliance and commerce. The real task is to find the structure that satisfies the regulator at the lowest friction to the business, and to know precisely which terms can flex to get there and which cannot.

## The core tension

Two failure modes bracket every regulated fintech deal. Compliance maximalism, in which every conceivable control is imposed regardless of proportionality, produces a contract so heavy that the product never launches or the counterparty walks away. Commercial maximalism, in which speed and frictionless onboarding override the licence conditions, produces a contract that closes fast and then breaches, exposing the licence itself. The drafter's value is in refusing both extremes: a document that a regulator would accept and a business would actually sign and operate.

|  |
| --- |
| **PRACTICE NOTE**  Reframe the question the business is really asking. When a commercial sponsor says “this is too restrictive,” they are usually not asking you to break a rule; they are asking whether the restriction is genuinely required or merely conservative drafting. Separate the two out loud. If a control is mandated by the licence, say so and stop negotiating it. If it is your own prudence, it is on the table, and treating it as negotiable builds the credibility you need when you hold firm on the things that are not. |

## Techniques for reconciling the two

Most apparent conflicts between compliance and commerce dissolve under one of three techniques, each of which lets the business move while keeping the licence intact.

* **Phased rollout.** Launch the clean pillars immediately and gate the contested ones. The business gets revenue and momentum on what is ready; the regulated grey zone activates only once its condition is satisfied. This is the commercial payoff of the framework-plus-sub-agreement architecture from Phase 2.
* **Proportionate controls.** Calibrate the obligation to the actual risk and to what the rules require, not to the most cautious reading. Do not impose bank-grade onboarding on a low-value, fully-traced P2P flow if the instrument does not demand it. Over-control is not free; it is friction that the business correctly resents and that may exceed the regulator’s own expectation.
* **Conditions precedent as “yes, but sequenced.”** A condition precedent converts a flat refusal into a structured timeline. Rather than telling the business it cannot have a feature, you tell it the feature switches on the moment a defined, achievable step is complete. This keeps the deal alive and gives the commercial team something concrete to chase.

## Pushing back commercially without breaching

The skill is not saying no; it is saying no in a way that redirects. When a commercial ask collides with a compliance condition, name the condition, explain the consequence of breaching it in business terms rather than legal ones, and offer the nearest compliant alternative. “We cannot raise the agent cap because that voids the licence basis; what we can do is prioritise the highest-volume locations within the existing cap” moves the conversation forward. A flat “no” stops it.

|  |
| --- |
| **DRAFTING TIP**  Frame every non-negotiable in terms of the business consequence, not the rule number. “This breaches Article X” persuades no one in a commercial meeting; “this puts the licence at risk, which stops every pillar, not just this one” lands. The most effective compliance argument is almost always the one expressed as commercial self-interest. |

## Negotiable versus non-negotiable

Keep an explicit line between what can flex and what cannot, and surface it early so the commercial team negotiates within the right perimeter. Terms that touch pricing and service generally flex; terms that touch the licence, the regulated core, or the accuracy of representations do not.

| **Negotiable (can flex)** | **Non-negotiable (compliance condition)** |
| --- | --- |
| Pricing and commission within the cap | The commission cap itself |
| Service levels and SLAs | KYC/AML ownership by the licensed party |
| Exclusivity and territory | Agent caps and mandatory regulator notification |
| Term, renewal, and termination notice | Prohibition on sub-agency without approval |
| Marketing, branding, and rollout sequence | Accuracy of representations and warranties |
| **RED FLAG**  The most dangerous moment is when commercial pressure reframes a non-negotiable as a “commercial point” to be split down the middle. Compliance conditions do not have a midpoint. Splitting the difference on an agent cap or a KYC obligation does not produce a moderate position; it produces a breach. Hold the line precisely because you gave ground freely on everything that genuinely was negotiable. |

# Phase 3: Core Clause Drafting

Now draft. The governing principle across every clause in this phase is that authority, money, and liability should each track control. Whoever controls a function bears its obligations and its risk; whoever is barred from a function must be expressly barred in the text.

## Step 6: Allocate authority asymmetrically and explicitly

The licensed entity must retain exclusive authority over the regulated core: KYC and AML, sanctions screening, transaction authorisation, float management, regulatory reporting, and audit. The counterparty receives cash handling and physical operations only. Crucially, the agent's exclusions must be stated affirmatively, not merely implied by the grant to the licensed party.

Draft an express prohibitions clause barring the agent from financial intermediation, from holding itself out as a financial institution, from initiating, approving, overriding, or manipulating transactions, from structuring transactions, and from handling sensitive customer credentials.

|  |
| --- |
| **DRAFTING TIP**  Write a closed list of agent prohibitions and a separate closed list of licensed-party reserved powers. Two explicit lists are far harder to misread than a single grant with everything else left to inference, and they give you a clean checklist for the regulator and for the agent's own compliance team. |

## Step 7: Engineer the money mechanics

Specify the float model in operational detail; vagueness here is where reconciliation disputes and regulatory findings originate. Address, at minimum, the prefunding source, segregation and non-commingling of funds, real-time monitoring with hard per-agent limits, the accounting treatment on each party's books, the reconciliation cadence and exception SLA, and which system is authoritative.

| **Mechanic** | **Drafting requirement** |
| --- | --- |
| Prefunding | Identify the funding party and the segregated, non-commingled account |
| Monitoring | Real-time monitoring with hard per-agent float limits |
| Accounting | Liability on the agent's books; restricted cash on the licensed party's |
| Reconciliation | Daily automated reconciliation of ledger, agent float, and bank accounts |
| Exceptions | Defined exception SLA (e.g., T+1 resolution) |
| Authority | System of record is authoritative; bank records are settlement reference only |
| **PRACTICE NOTE**  The most consequential single line in the money mechanics is the one naming the authoritative transactional record. When the licensed party's system and the bank statement disagree, the contract must already say which prevails for what purpose: the system of record governs the transactional truth; bank records govern settlement. Decide it in the text, not in the dispute. |

## Step 8: Build in the regulator's hard caps and obligations

Hard-code the licence conditions as non-negotiable terms, not as commercial variables. These typically include a maximum number of agents per branch and an aggregate cap across the network, mandatory notification to the regulator, a prohibition on sub-agency, delegation, or subcontracting without prior approval, and individual fit-and-proper vetting, training, and system-authorisation of every responsible person.

|  |
| --- |
| **RED FLAG**  Caps and approval requirements are compliance conditions, not points to trade in negotiation. If a commercial counterpart asks to raise an agent cap or to permit subcontracting, the answer is not a redline; it is a regulator question. Drafting these as ordinary negotiable terms invites a breach that voids the licence basis. |

## Step 9: Draft compliance, data, and audit provisions

Cover the supervisory and data obligations expressly. These commonly include a statutory data-retention period under local law, annual external-auditor reports addressing compliance, electronic operations, and AML/CFT at agent level, footage and CCTV service levels for suspicious transactions, privacy-aligned counter design so that one customer's data is not visible to others, a standing right to audit, and unannounced mystery-shopping at any agent location.

|  |
| --- |
| **DRAFTING TIP**  For every compliance obligation, draft three linked elements: the standard, the evidence the obliged party must produce, and the cadence on which it must produce it. An audit right without a defined evidence package and a reporting interval is unenforceable in practice. Tie the data-retention period to the specific statute so the clause survives a change in internal policy. |

## Step 10: Allocate liability along the operational seam

Liability should follow control, splitting at the operational seam between the parties. Cash handling and physical operations sit with the agent; system processing and regulatory compliance sit with the licensed party; product, delivery, and customer claims sit with the marketplace operator unless otherwise agreed. Reinforce the allocation with an ongoing agent risk-monitoring regime, scoring agents periodically on transaction-volume anomalies, cash discrepancies, and behavioural flags.

| **Risk** | **Owner** | **Rationale** |
| --- | --- | --- |
| Cash & physical handling | Agent | Agent controls the cash and the counter |
| System & regulatory | Licensed PSP | PSP controls the rails and holds the licence |
| Product / delivery / claims | Marketplace operator | Operator controls fulfilment |

# Phase 4: Solving Execution Blockers

By this phase you will have a substantively complete draft and a list of open points. Triage that list ruthlessly. Separate the points that are merely desirable from the points that prevent execution. Only the latter are blockers, and each blocker needs a recommended path and a fallback before the document can move to signature.

## Step 11: Identify and resolve the deal-killers

Two blockers recur on regulated payments matters. The first is a security requirement, such as a regulator-mandated bank guarantee, that the counterparty refuses or is unable to post. The workaround is to position the prefunded, segregated float as the sole security mechanism, demonstrating that the float already performs the protective function the guarantee was meant to serve, or alternatively to seek a management or regulator waiver. The second is the classification gate from Step 2, which must close by regulator non-objection or qualifying legal opinion before the affected pillar can go live.

|  |
| --- |
| **PRACTICE NOTE**  Present each blocker to the client as a short decision package: the obstacle in one sentence, the recommended path, the fallback if the path fails, and the consequence of leaving it unresolved. Clients can decide quickly when the options are framed this way; they stall when handed an undifferentiated list of open issues. |
| **Blocker** | **Recommended path** | **Fallback** |
| Bank guarantee refused | Position prefunded float as sole security | Seek management or regulator waiver |
| QR classification open | Obtain regulator non-objection | Qualifying written legal opinion |
| Reconciliation ownership | Assign in sub-agreement with SLA | Escalation and audit-right backstop |

# Phase 5: Iteration & Finalisation

Finalisation is a controlled process, not a single pass. Version deliberately, verify systematically, and convert any blocker that cannot be closed before signature into a condition precedent so the client can sign without absorbing unmanaged regulatory risk.

## Step 12: Draft in versioned rounds with tracked changes

Move through successive versions with tracked changes exchanged between the parties, maintaining an issues list that maps every open point to an owner and a resolution status. Quality improves measurably across rounds when each version closes a defined set of issues. Resist the urge to declare the document final while execution blockers remain open; a clean-looking draft with a live blocker is not finished.

|  |
| --- |
| **DRAFTING TIP**  Keep the issues list as a living annex to the working draft, not as scattered email threads. Each row should carry the issue, the owner, the current position, and the status. The list is what tells you, objectively, whether the document is ready, and it becomes the agenda for every negotiation call. |

## Step 13: Run a pre-signature compliance and consistency check

Before execution, run a structured verification pass. Confirm that internal cross-references resolve, that every pillar has its corresponding executed sub-agreement, that commission terms match the regulatory ceiling, and that every representation is accurate. In particular, never represent that something is done, such as a guarantee posted or a right secured, unless the executed evidence actually exists.

|  |
| --- |
| **RED FLAG**  Inaccurate representations are the highest-risk line in any deal that will face investor counsel or a regulator. A representation that all approvals are in place, or that security has been provided, is a discoverable misstatement the moment someone asks for the executed copy. If the evidence does not exist, disclose the gap; do not represent around it. |
| **Pre-signature check** | **Pass condition** |
| Cross-references | Every internal reference resolves to the right clause |
| Sub-agreement completeness | Each live pillar has its own executed sub-agreement |
| Commission ceiling | All pricing within the regulatory cap |
| Representations | Every rep is backed by existing executed evidence |
| Conditions precedent | Each open blocker is captured as a CP to effectiveness |

## Step 14: Close with conditions precedent

Where a blocker cannot be fully resolved before signature, do not delay the whole transaction and do not paper over the gap. Convert the blocker into a condition precedent to the effectiveness of the affected pillar. For example, the QR pillar does not go live until the regulator's non-objection or a qualifying legal opinion is obtained. This lets the client sign the framework and launch the unaffected pillars immediately, while the gated pillar activates only once its condition is satisfied, so no party assumes unmanaged regulatory risk.

|  |
| --- |
| **PRACTICE NOTE**  Conditions precedent are the drafter's mechanism for honest sequencing. They let a deal close on what is ready while ring-fencing what is not, and they make the consequence of an unmet condition explicit rather than disputed. A well-drafted CP names the condition, the party responsible for satisfying it, the deadline, and what happens to the pillar if the deadline passes. |

**One-Page Workflow Summary**

| **Phase** | **Steps** | **Output** |
| --- | --- | --- |
| 1 Intake & mapping | 1–3 | Activity-to-licence matrix; resolved classifications; role map |
| 2 Architecture | 4–5 | Framework + sub-agreement structure; ring-fenced marketplace |
| Cross-cutting: balance | — | Negotiable/non-negotiable line; proportionate, sequenced controls |
| 3 Core drafting | 6–10 | Authority, money, caps, compliance, liability clauses |
| 4 Execution blockers | 11 | Decision packages with path + fallback per blocker |
| 5 Finalisation | 12–14 | Versioned draft; verification pass; conditions precedent |