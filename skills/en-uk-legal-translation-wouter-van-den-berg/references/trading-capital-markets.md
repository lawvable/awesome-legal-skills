# Trading / Capital Markets Lexicon

Standard English terminology for trading and capital markets agreements: ISDA master
agreements, derivatives, repo agreements, prime brokerage, clearing, margin, securities
lending, and related instruments. Includes EMIR, MiFID, and market infrastructure terminology.

> **Per-language sub-lexicon note.** This English reference file is the cross-language canon for trading & capital markets only; finance & banking terminology lives in `references/finance-banking.md`. In the per-language sub-lexicons the two domains are consolidated into a single file: `sub-lexicons/<language>-finance-banking.md` covers both. When working on a capital-markets document, read both English reference files but only the single per-language sub-lexicon.

## Core Trading/Derivatives Terms

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| ISDA Master Agreement | Standard framework for derivatives trading between two counterparties | generic "master agreement"; confuse with individual transaction confirmations |
| confirmation | Individual transaction details under ISDA Master Agreement | "attestation"; mixing with formal legal assignment |
| schedule | Standard terms and amendments to ISDA Master Agreement | "appendix" (too vague); "annex" (prefer for CSA) |
| ISDA Definitions | Published specifications for derivative calculations and payment flows | paraphrasing with "definitions section" |
| transaction | Individual trade executed under ISDA Master Agreement | "operation"; "deal" (imprecise) |
| derivative / derivative instrument | Financial contract deriving value from underlying asset/rate/index | "derived product"; "financial product" (too broad) |
| OTC derivative | Over-the-counter derivative (uncleared, bilateral) | "private derivative"; "non-exchange" (imprecise) |
| exchange-traded derivative | Derivative cleared through CCP on regulated market | "exchange product"; "cleared derivative" (not all exchange-traded are cleared) |
| interest rate swap (IRS) | Exchange of fixed vs floating interest payments on same currency | "rate exchange"; "swap contract" (too generic) |
| cross-currency swap | Exchange of principal and interest in two different currencies | "currency swap" (less precise); "FX swap" (different product) |
| forward | Bilateral contract to buy/sell at agreed future price | "forward contract" (acceptable but "forward" is standard); "futures" (exchange-traded, different) |
| option | Right (not obligation) to buy/sell at agreed price on/before specified date | "optional contract"; "conditional derivative" |
| cap | Floating rate derivative that limits maximum interest rate | "ceiling"; "rate cap" (acceptable but less standard) |
| floor | Floating rate derivative that establishes minimum interest rate | "base rate"; "rate floor" (acceptable but less standard) |
| collar | Combination of cap and floor, often zero-cost | "rate collar" (acceptable but less standard) |
| credit default swap (CDS) | Insurance-like protection against default by reference entity | "credit protection"; "default insurance" (incorrect—not insurance product) |
| credit event | Event triggering payment under credit default swap (bankruptcy, failure to pay, restructuring); as defined in ISDA Credit Derivatives Definitions | Default event (too broad); Trigger event (too vague) |
| total return swap | Counterparty receives all economic returns (price + coupons) on reference asset | "return swap"; "TRS" (abbreviation acceptable after full first use) |
| notional amount | Face value amount used to calculate payments (not exchanged in most derivatives) | "principal" (typically refers to amounts actually paid); "contract value" (imprecise) |
| effective date | Trade date or date when contract terms commence | "start date"; "commencement date" (less technical) |
| termination date / maturity date | Date when contract ends and final payment is made | "end date"; "expiry date" (less precise) |
| payment date | Scheduled date for interim or final cash flow | "settlement date" (different—refers to T+n); "due date" (less technical) |
| calculation date | Date used to determine payment amount (e.g., end of interest period) | "fixing date" (different—when benchmark is observed); "determination date" (less standard) |
| calculation agent | Party responsible for computing payment amounts per ISDA Definitions | "agent" (too vague); "paying agent" (different role) |
| fixed rate | Interest rate set at outset, fixed for contract term | "fixed interest"; "coupon" (used for bonds, not derivatives) |
| floating rate | Interest rate linked to benchmark (EURIBOR, SOFR, €STR) plus spread | "variable rate" (acceptable); "benchmark rate" (imprecise) |
| reference rate / benchmark rate | Published index (EURIBOR, SOFR, €STR, SONIA) used to determine payments | "base rate"; "index" (too generic) |
| EURIBOR | Euro Interbank Offered Rate (published daily, primary EUR benchmark) | "Euribor" (capitalization); other generic "interbank rate" terms |
| SOFR | Secured Overnight Financing Rate (primary USD benchmark, post-LIBOR) | "LIBOR replacement" (SOFR is primary now, not replacement); other benchmark names if not verified current |
| €STR | Euro Short-Term Rate (primary EUR overnight benchmark, post-EONIA) | "EONIA replacement" (€STR is primary now); older benchmark names |
| spread | Fixed adjustment (in basis points) added to floating rate | "margin" (acceptable in some contexts); "increment" |
| mark-to-market | Current market valuation of outstanding contract position | "mark-to-market valuation" (acceptable); "MTM" (use only after full first use) |
| prime brokerage agreement | Comprehensive facility providing clearing, financing, and settlement services | "prime broker contract"; "prime broker agreement" (less formal) |
| give-up agreement | Agreement allowing introducing broker to give up trade to clearing broker | "clearing arrangement"; "trade assignment" (imprecise) |
| ISDA Credit Support Annex (CSA) | Standardised collateral framework under ISDA Master Agreement, specifying initial/variation margin requirements, eligible collateral, thresholds, haircuts | "margin agreement"; "collateral agreement" (less precise); "security annex" (incorrect terminology) |
| novation | Replacement of existing contract with new contract, often to change counterparty | "contract replacement" (less technical); "substitution" (not standard legal term in derivatives context) |
| portfolio reconciliation | Regular matching of trade positions and exposures between counterparties | "position reconciliation" (acceptable); "portfolio matching" (less standard) |
| portfolio compression | Termination of multiple offsetting trades to reduce systemic risk (EMIR requirement) | "trade compression" (acceptable); "position netting" (different process) |

## ISDA-Specific Terms

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| termination event | Event (usually non-default) that allows contract termination at then-current market value | "termination right"; "exit event" |
| event of default | Breach or failure by counterparty triggering early termination and close-out | "default"; "failure to pay" (too narrow) |
| early termination | Termination before scheduled maturity date, typically following event of default | "early exit"; "premature termination" (less formal) |
| close-out amount | Amount calculated post-termination reflecting market value of terminated transactions | "settlement amount"; "exit value" |
| netting | Offsetting amounts owed by each party to determine net payment | "offsetting"; "compensation" (ambiguous) |
| close-out netting | Netting of all outstanding transactions following termination event | "termination netting"; "final netting" |
| payment netting | Periodic netting of scheduled payments under same contract | "settlement netting"; "interim netting" |
| netting agreement | Standalone agreement allowing netting across multiple contracts | "master netting agreement" (acceptable); "clearing agreement" (different) |
| representations | Statements by counterparty regarding authority, solvency, regulatory status | "warranties" (overlapping but different emphasis); "statements" (too vague) |
| covenants | Ongoing obligations and restrictions on counterparty behaviour | "undertakings" (acceptable in UK English); "commitments" (less technical) |
| cross-default | Clause triggering default if counterparty defaults under other material contracts | "cross-acceleration" (related but different); "linked default" |
| flawed asset | Security/collateral with legal defect preventing full transfer (ISDA-specific concept) | "defective security"; "problematic collateral" |
| set-off | Right to offset amounts owed by one party against amounts it owes | "offset"; "mutual offset" (acceptable) |
| ISDA Protocol | Market-wide mechanism enabling parties to amend existing ISDA agreements by mutual adherence (e.g., IBOR Fallbacks Protocol, ISDA 2020 Protocol) | ISDA amendment (less precise) |
| master confirmation agreement | Pre-agreed terms for specific derivative product types, supplementing ISDA Master Agreement; reduces documentation for repeated trades | Standard confirmation (less precise); Template confirmation (non-standard) |
| transfer / assignment | Transfer of rights and obligations to third party (subject to restrictions) | "cession" (civil law term; use "assignment" in English); "novation" (legal replacement, different) |

## Margin and Collateral Terms

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| margin / collateral | Assets pledged to secure exposure or posted under CSA | "security" (broader); "guarantee" (implies guarantor) |
| initial margin | Margin required upfront to cover potential future exposure (EMIR requirement) | "IM"; "opening margin" |
| variation margin | Daily/periodic margin adjustment reflecting mark-to-market changes | "VM"; "mark-to-market margin"; "daily margin" |
| margin call | Demand for additional margin following threshold breach or mark-to-market loss | "collateral call" (acceptable); "funding call" (imprecise) |
| financial collateral arrangement | Formalised security over financial assets under CSA | "collateral agreement"; "security arrangement" |
| financial pledge | Charge/lien on financial assets, typically under title transfer or pledge | "security interest"; "lien" (less technical in this context) |
| title transfer | Transfer of legal ownership of collateral (as security, not absolute sale) | "ownership transfer"; "security transfer" |
| credit support annex (CSA) | See ISDA Credit Support Annex above | "margin agreement"; "collateral annex" |
| haircut | Discount applied to collateral value (e.g., 98% of market value for highly liquid securities) | "markdown" (acceptable); "discount" (too vague) |
| eligible securities / eligible collateral | Securities meeting CSA requirements (e.g., government bonds, investment-grade corporates) | "approved collateral"; "acceptable securities" (less standard) |
| threshold | CSA limit: if net exposure exceeds threshold, security transfer required | "limit"; "tolerance level" (imprecise) |
| minimum transfer amount (MTA) | CSA limit: amounts below threshold not transferred (administrative de minimis). Abbreviate to "MTA" after first spelled-out use, consistent with the ISDA/CSA acronym convention noted elsewhere in this lexicon. | transfer floor (informal); minimum call amount (imprecise) |
| return of excess collateral | CSA provision requiring return of collateral if security exceeds required amount | "excess return"; "overcollateral release" |

## Repo and Securities Lending

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| repurchase agreement (repo) | Sale of security with simultaneous obligation to repurchase at agreed price/date | "repo contract" (acceptable); "reverse repo" (opposite party perspective) |
| repo transaction | Individual repo deal structured under GMRA | "repo deal" (acceptable); "repo operation" |
| term repo | Repo with fixed term (e.g., 30 days, 3 months) | "time repo"; "forward repo" |
| overnight repo | Repo with one-day term, rolled daily | "O/N repo"; "next-day repo" |
| repo rate | Interest rate on repo transaction (expressed as percentage discount on sale price) | "financing rate" (broader); "money market rate" (too generic) |
| securities lending | Transfer of securities for temporary possession in exchange for fee/return | "loan of securities"; "stock lending" (overlapping) |
| securities lender | Party transferring securities in lending arrangement | "owner"; "original holder" |
| securities borrower | Party receiving securities under lending arrangement | "temporary owner"; "user" |
| fee | Compensation paid by borrower to lender for use of securities | "commission"; "rebate" (negative fee) |
| substitution of securities | Lender's right to substitute different securities meeting same criteria | "replacement of securities"; "security swap" |
| recall of securities | Lender's right to demand return of loaned securities | "return demand"; "recall right" |
| Global Master Repurchase Agreement (GMRA) | Standard framework for repo transactions, maintained by ICMA/SIFMA | "GMRA agreement" (redundant); "repurchase master agreement" |
| Global Master Securities Lending Agreement (GMSLA) | Standard framework for securities lending transactions, maintained by ICMA/LSTA | "GMSLA agreement" (redundant); "securities loan master agreement" |

## Market Infrastructure and Regulatory

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| central counterparty (CCP) | Entity interposing itself as counterparty to all transactions for clearing/settlement | "clearing counterparty"; "CCP entity" (redundant) |
| clearing house | Entity operating clearing system (may or may not be a CCP) | "clearing centre"; "settlement house" (less precise) |
| clearing | Process of matching, confirmation, and settlement of trades via CCP | "settlement" (different—final transfer of funds/securities); "registration" |
| settlement | Final transfer of securities and funds to complete trade | "clearing" (often overlapping but clearing occurs first); "execution" |
| central securities depository (CSD) | Entity responsible for immobilisation, safekeeping, and settlement of securities | "securities depository" (acceptable); "central vault" (imprecise) |
| trading venue | Regulated market or multilateral facility where securities are traded | "exchange" (legal term for regulated market); "trading platform" (too generic) |
| regulated market | Formally recognised, supervised venue meeting legal/transparency requirements | "stock exchange" (specific type); "official market" (less standard) |
| multilateral trading facility (MTF) | Alternative venue for trading securities, subject to lighter regulation than regulated market | "alternative venue"; "trading facility" (too broad) |
| systematic internaliser (SI) | Investment firm that regularly buys/sells financial instruments for own account | "internaliser"; "proprietary trader" (different role) |
| EMIR (Regulation (EU) No. 648/2012) | EU Regulation on derivatives markets infrastructure (clearing, reporting, risk mitigation) | "EMIR regulation" (redundant); "derivatives regulation" (imprecise) |
| MiFID II (Directive 2014/65/EU) | EU Markets in Financial Instruments Directive II (investment services/products regulation) | "MiFID" (older version—specify II); "MiFID2" (non-standard abbreviation) |
| MiFIR (Regulation (EU) No. 600/2014) | EU Markets in Financial Instruments Regulation (traded reporting/transparency) | "MiFIR regulation" (redundant); "trading transparency regulation" |
| clearing obligation | EMIR requirement for certain derivatives to be cleared through CCP | "mandatory clearing"; "clearing requirement" (less formal) |
| reporting obligation | Requirement under EMIR/MiFID II to report trades to trade repository | "trade reporting"; "disclosure requirement" (broader) |
| trade repository | Approved system for storing and reporting derivative trade information (EMIR requirement) | "data repository"; "central repository" (imprecise) |
| Legal Entity Identifier (LEI) | 20-character code assigned to legal entities to enable unambiguous identification | "LEI code" (redundant); "entity identifier" (too broad) |
| financial counterparty (FC) | Counterparty classified as financial entity under EMIR (banks, investment firms, insurance, etc.) | "financial party"; "financial institution" (less precise in EMIR context) |
| non-financial counterparty (NFC) | Non-financial entity (corporate customer) subject to clearing obligation if exceeds threshold | "non-financial party"; "corporate counterparty" |
| clearing member | Entity admitted as member of CCP to clear trades on own account and/or for clients | CCP member (acceptable); Direct participant (less precise) |
| client clearing | Clearing of trades by CCP on behalf of clients via clearing member | Indirect clearing (less precise) |
| clearing threshold | EMIR requirement: NFC must clear OTC derivatives once aggregate notional exceeds limit | "clearing exemption threshold"; "clearing exemption level" (inverse concept) |
| risk mitigation techniques | EMIR-required measures for uncleared derivatives: daily mark-to-market, collateral, compression | "risk mitigation"; "alternative risk controls" (less specific) |

## Section Headings

| Correct English heading | Avoid |
|---|---|
| DEFINITIONS | "DEFINED TERMS"; "INTERPRETATION"; mixing definition section with general interpretation |
| SCOPE / SUBJECT MATTER | "APPLICATION"; "OBJECT"; "PURPOSE" (less formal) |
| MARGIN OBLIGATIONS | "COLLATERAL REQUIREMENTS"; "SECURITY"; avoid generic "GUARANTEES" |
| EVENTS OF DEFAULT | "DEFAULT"; "TERMINATION EVENTS" (different concept—includes non-default events) |
| EARLY TERMINATION | "TERMINATION"; "CLOSEOUT" (closeout is result of termination) |
| CALCULATIONS AND PAYMENTS | "PAYMENT MECHANICS"; "FLOATING RATE CALCULATIONS"; "COMPUTATIONS" (less formal) |
| NETTING | "CLOSE-OUT NETTING"; "COMPENSATION" (ambiguous); "OFFSETTING" (less formal) |
| COLLATERAL | "MARGIN"; "SECURITY" (narrower); "GUARANTEES" (incorrect—collateral is not guarantee) |
| REPRESENTATIONS AND WARRANTIES | "REPRESENTATIONS"; "WARRANTIES" (splitting weakens legal effect); "ASSURANCES" (too informal) |
| GOVERNING LAW | "LAW APPLICABLE"; "JURISDICTION"; "APPLICABLE LAW" (acceptable alternative) |

## Notes

- **ISDA terminology**: When translating documents that reference or implement ISDA agreements,
  use the exact English terms from the ISDA Master Agreement. These are highly standardised
  and any deviation creates legal uncertainty. ISDA Definitions are published in multiple
  versions (1991, 2000, 2006); confirm which version applies.

- **ISDA Credit Support Annex (CSA)**: This is the foundational document for margin
  management under ISDA Master Agreements. There are two standard versions: the 1994 CSA
  (older, rarely used) and the 2016 CSA (current standard). Some contracts use schedule
  amendments instead of full CSA. Always identify which mechanism applies.

- **Netting/set-off/clearing ambiguity**: Many source languages use a single term that can mean "netting" (ISDA/financial context), "set-off" (general law), "clearing" (CCP context), or "compensation/damages" (broad legal). Always determine from context and contract structure. Sub-lexicon provides source-language mappings.

- **Regulation/settlement/rules ambiguity**: Many source languages use a single term that can mean "regulation" (EU legislative act), "settlement" (of a trade), "rules" (of an exchange/CCP), or "by-laws" (internal rules). Context-dependent; confirm exact meaning. Sub-lexicon provides source-language mappings.

- **Benchmark reform**: Post-LIBOR transition, references to interbank offered rates or other
  benchmarks must be verified against current rates. €STR and SOFR are now primary benchmarks.
  Confirm the document hasn't frozen outdated benchmark references.

- **Novation and give-up agreements**: Novation is common in secondary market trading (counterparty
  replacement). Give-up agreements are used with introducing brokers. Ensure correct term is used
  based on transactional context.

- **Portfolio compression and EMIR**: Portfolio compression is an EMIR-mandated technique
  for reducing systemic risk. It's distinct from portfolio reconciliation (routine matching).

- **Keep acronyms unexpanded**: ISDA, CSA, GMRA, GMSLA, CCP, CSD, MTF, LEI, EMIR, MiFID, MiFIR —
  these are universally used in English and should not be translated or expanded after first use
  in a document.

- **UK vs US English**: This lexicon uses UK English conventions (e.g., "recognised", "licence" as
  noun). US alternatives noted where material (e.g., "authorization" vs "authorisation").
