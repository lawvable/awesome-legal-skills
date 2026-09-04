# Scope Assessment

Use this file to determine roles, territorial reach, covered data, and the applicable chapter. Record facts for each product, service, contract, and request separately.

## Contents

1. Role matrix
2. Covered objects and data
3. Territorial scope
4. Chapter routing
5. Enterprise-size rules
6. Exclusions and boundaries
7. Evidence table

## 1. Role Matrix

| Role | Legal anchor | Questions to prove or disprove the role |
|---|---|---|
| User | Article 2(12) | Does the person own the connected product, hold temporary contractual use rights, or receive a related service? |
| Data holder | Article 2(13) | What legal right or obligation permits or requires the person to use and make data available? Is product or related-service data contractually covered? |
| Data recipient | Article 2(14) | Does a professional recipient receive data from the holder, including at the user's request? Is it distinct from the user? |
| Related-service provider | Article 2(6) | Is the digital service, other than an electronic communications service, linked to product functions at purchase or later added to affect those functions? |
| Data-processing-service provider | Article 2(8) | Does the service provide ubiquitous, on-demand network access to a shared pool of configurable, scalable, elastic computing resources? |
| Public sector body | Article 2(28) | Is the requester a Member State authority, public-law body, or qualifying association? |
| Customer | Article 2(30) | Is there a contract to use one or more data processing services? |
| Smart-contract vendor/deployer | Articles 1(3)(g), 36 | Does the entity supply an application using smart contracts or professionally deploy smart contracts for others to execute a data-sharing agreement? |

The Data Act does not define “manufacturer” in Article 2. For Article 3, document the entity that designs or manufactures the product, the seller/rentor/lessor, and the related-service provider. Do not invent an Article 2 definition.

## 2. Covered Objects and Data

### Connected product, Article 2(5)

Confirm all elements:

- item obtains, generates, or collects data concerning its use or environment;
- communicates product data through an electronic service, physical connection, or on-device access;
- primary function is not storing, processing, or transmitting data on behalf of another party.

### Related service, Article 2(6)

Confirm that absence of the digital service would prevent one or more product functions, or that the service was later connected to add, update, or adapt product functions.

### Chapter II data

Article 1(2)(a) covers data, excluding content, concerning the performance, use, and environment of connected products and related services.

Classify:

- product data, Article 2(15);
- related service data, Article 2(16);
- readily available data, Article 2(17);
- relevant metadata needed to interpret and use the data;
- personal, non-personal, or mixed data;
- trade secrets and trade-secret holder;
- inferred or derived information not automatically within the access duty.

## 3. Territorial Scope

Apply Article 1(3) by role:

- connected-product manufacturers and related-service providers: products placed on the Union market, regardless of establishment;
- users: users in the Union;
- data holders: regardless of establishment, when making data available to recipients in the Union;
- data recipients: recipients in the Union;
- Chapter V requesters and responding data holders;
- data-processing-service providers: regardless of establishment, when providing services to customers in the Union;
- smart-contract participants described in Article 1(3)(g).

If an in-scope entity makes connected products available or offers services in the Union but is not established there, assess the legal-representative duty in Article 37(11) to (13).

## 4. Chapter Routing

| Facts | Chapter and provisions |
|---|---|
| Connected-product or related-service data and user rights | Chapter II, Articles 3 to 7 |
| Statutory B2B making available | Chapter III, Articles 8 to 12 |
| Unilaterally imposed B2B data terms | Chapter IV, Article 13 |
| Exceptional-need public-sector request | Chapter V, Articles 14 to 22 |
| Switching between data-processing services | Chapter VI, Articles 23 to 31 |
| Third-country governmental access to non-personal data held in the Union | Chapter VII, Article 32 |
| Interoperability and smart contracts | Chapter VIII, Articles 33 to 36 |
| Authority, remedy, penalty, and representative questions | Chapter IX, Articles 37 to 42 |

## 5. Enterprise-Size Rules

Use Recommendation 2003/361/EC and account for partner and linked enterprises. Do not use headcount alone.

- microenterprise: fewer than 10 persons and annual turnover or annual balance-sheet total no more than EUR 2 million;
- small enterprise: fewer than 50 persons and annual turnover or annual balance-sheet total no more than EUR 10 million;
- SME for Article 9(4): apply the Recommendation's full SME framework and linked/partner-enterprise rule.

Article 7(1) is narrow. Chapter II duties do not apply to data generated through connected products manufactured or designed, or related services provided, by a qualifying micro or small enterprise if the linked/partner and subcontracting conditions are met. The provision also creates a limited one-year treatment for certain newly medium-sized enterprises and their products.

Do not state that every micro or small data holder is exempt.

Chapter V has different size effects:

- Article 15(2): Article 15(1)(b) does not apply to micro and small enterprises.
- Article 20: micro and small enterprises may claim compensation even for public-emergency provision.

## 6. Exclusions and Boundaries

Check and document:

- personal-data and ePrivacy priority, Article 1(5);
- criminal, customs, taxation, public-security, defence, and national-security boundaries, Article 1(6);
- intellectual-property law, Article 1(8);
- consumer law, Article 1(9);
- sector-specific data-access acts and Article 43;
- Chapter II gatekeeper exclusion, Article 5(3);
- testing of not-yet-marketed products, Article 5(2);
- custom-built or non-production data-processing services, Article 31.

## 7. Evidence Table

For each conclusion, record:

| Field | Required evidence |
|---|---|
| Entity and establishment | corporate record, contracting entity, establishment map |
| Product/service | architecture, product specification, service description |
| Role | contract, technical control, legal right or duty, data-flow evidence |
| Data | inventory, schema, metadata, generation and retrieval path |
| Enterprise size | headcount, turnover, balance-sheet total, ownership links |
| Geography | user/customer location, market placement, service territory |
| Exceptions | technical evidence and exact legal condition |

Assign High, Medium, or Low confidence. A missing contract, ownership record, or architecture fact normally prevents a High-confidence result.
