# Annex III Area 3 — Education and vocational training

**Annex III citation:** Nr. 3
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 3 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

## Scope of the area

Annex III Nr. 3 captures AI systems intended to be used in the area of education and vocational training. The Commission recognises that such systems can promote high-quality education but may also negatively affect health, safety, or fundamental rights of students and apprentices because they can shape the educational and professional course of a person's life, and therefore that person's ability to secure a livelihood. Poorly designed systems risk violating the right to education and the right not to be discriminated against, and may perpetuate historical patterns of discrimination against women, certain age groups, persons with disabilities, or persons of particular racial, ethnic, or sexual-orientation backgrounds (¶207). Although Member States retain prerogatives over education under Art. 165 TFEU, the AI Act — based on Art. 114 TFEU — establishes a harmonised framework that applies regardless of national education competences (¶208).

The Commission reads the term "educational and vocational training institution" **broadly** (¶210–¶214). It covers all levels of formal and non-formal education: early childhood, primary, secondary, tertiary, vocational, and adult/continuing education. It includes public and private institutions, online, in-person, and blended modes, with no limitation on the age of pupils or students. Institutions are typically accredited or sanctioned by national education authorities and may issue certificates upon completion. Crucially, an AI system only falls within Nr. 3 if it is intended to be used **in the context of or within** such an institution and primarily impacts **learners** (students or apprentices). Systems directed mainly at training educators and academic staff fall outside Nr. 3 but may be in scope under Nr. 4 (employment).

A central distinction runs through Area 3: systems that **evaluate or steer learners** (in scope) versus systems that **assist teaching or support voluntary, non-formal learning without affecting credentials** (out of scope). The rights at stake are the right to education and training, the right to non-discrimination, and — given the heavy use of personal data and profiling — data-protection rights. The Commission emphasises that Area 3 systems will frequently involve automated processing of personal data to evaluate aspects of a person's academic or vocational trajectory, will often perform **profiling**, and may lead to automated decision-making under Art. 22 GDPR — so the profiling re-exception in Art. 6(3) AI Act will frequently bite, blocking the filter mechanism (¶215). Note also the interplay with prohibited practices: Art. 5(1)(f) prohibits emotion-inference systems in the area of education (except medical/safety use); if a system avoids that prohibition it may still be high-risk under Annex III Nr. 3 or Nr. 1(c) (¶216).

## Sub-categories
- **Nr. 3(a)** Access or admission decisions; assignment to institutions/programmes.
- **Nr. 3(b)** Evaluating learning outcomes (including outcomes used to steer learning).
- **Nr. 3(c)** Assessing appropriate level of education for an individual.
- **Nr. 3(d)** Monitoring/detecting prohibited behaviour during tests.

## Practical examples — HIGH-RISK

### Nr. 3(a) — Access, admission, assignment
- **Automated admissions systems** intended to review and evaluate student applications, transcripts, and test scores to determine eligibility for admission to an educational institution, where the system's evaluation and recommendation have the potential to influence the admissions decision (¶219 list).
- **School assignment systems** used by municipalities or regional authorities to allocate students (often in primary or secondary education) to public schools based on home address, catchment boundaries, available capacity, sibling attendance, and parental status. Because this involves profiling, the Art. 6(3) filter cannot apply.
- **Vocational training assignment tools** used by a regional employment agency to match applicants' prior education, certifications, and aptitude-test results to apprenticeship programmes against predefined eligibility criteria and capacity limits. Profiling triggers high-risk classification with no Art. 6(3) escape.
- **Automated scholarship eligibility assessment** systems that determine an individual's eligibility for a scholarship programme based on financial data (income, expenses, family size), thereby determining access to an educational institution.

### Nr. 3(b) — Evaluating learning outcomes
- **AI-enabled grading and feedback systems** used to evaluate students' assignments — tests, quizzes, exams — which count towards a **summative** final evaluation (¶223; only summative evaluations fall under 3(b)).
- **AI-enabled personalised learning assistants** that generate end-of-unit reports including grades, strengths/weaknesses, and improvement recommendations, where teachers also use the output to inform decisions about final grades — bringing them into the summative-evaluation envelope.

### Nr. 3(c) — Appropriate level of education
- **AI-powered adaptive placement tools** used by an educational or vocational training institution to determine the optimal course level for incoming students (beginner/intermediate/advanced) or whether a student should move to higher education or vocational training.
- **Vocational training level assessment systems** combining placement tests and skill assessments to evaluate a learner's knowledge in subjects such as mathematics, physics, or engineering principles and determine eligibility for a particular level or course.
- **AI classifiers for special education** that recommend educational placement and required support level for students with special educational needs, using assessment data (standardised, IQ, achievement, behavioural tests), teacher feedback, psychological evaluations, and medical history.

### Nr. 3(d) — Monitoring prohibited behaviour during tests
- **AI-enabled proctoring systems for certification exams** that monitor test-takers for prohibited behaviour (unauthorised materials, communication) using facial recognition, keystroke analysis, and screen monitoring.
- **Real-time behaviour analysis systems** using machine learning to detect cheating patterns during online exams.
- **AI-enabled exam monitoring systems** for in-person exams using facial recognition and object detection to detect use of unauthorised materials or devices.

## Practical examples — NOT HIGH-RISK

- **Educational programme matching platforms** that recommend tertiary programmes to secondary students based on their stated preferences and topics of interest — they inform the student's own decision-making, not an admission decision (Nr. 3(a) out of scope).
- **University admission chatbots** that answer prospective students' questions and provide information about admission requirements, application process, and programmes — limited to general information, no personalised recommendation that materially influences admission (Nr. 3(a) out of scope).
- **AI-enabled language-learning applications** used by students on their own volition for non-formal/informal learning, providing instant feedback and corrections but not leading to a credential, certification, or accredited validation (¶225).
- **AI-enabled neurodiverse learning companions** that adapt materials, pace, and format for students with autism, dyslexia, or ADHD (text-to-speech, font adjustments, multisensory materials, extra time, breaks). The output supports teaching, but is not used to determine grades or assess learning (formative, not summative).
- **AI-enabled pronunciation or reading feedback tools** that analyse a learner's speech and suggest improvements (intonation, rhythm, accent) — used by learners themselves, not by educators to determine grades.
- **Personalised education recommendation systems** providing students with recommendations on the appropriate level of education (courses, programmes, certifications) based on their interests and career goals, where the system is not intended to be used **by** an educational institution (Nr. 3(c) out of scope).
- **Trend analysis of educational attainment** systems used by institutions, policymakers, or researchers to analyse patterns in post-secondary educational pathways — aggregate analytics, no decisions about individual students (Nr. 3(c) out of scope).
- **Plagiarism checkers for homework** that analyse submitted assignments against a database of existing content — work produced unsupervised, no live monitoring, so outside Nr. 3(d) (¶235).
- **Non-academic student behaviour monitoring** in cafeterias, hallways, or other non-testing environments to flag bullying or harassment — outside Nr. 3(d) because it is not during a test (but may be in scope under Annex III Nr. 1 if it qualifies as remote biometric identification).

## Common Art. 6(3) exception scenarios

The Commission provides worked examples by limb. Always apply the **profiling re-exception** check first: for any system that processes personal data to evaluate aspects of an individual learner, Art. 6(3) is typically blocked. The exceptions below illustrate cases where the Commission accepted that the filter mechanism applies.

- **(a) Narrow procedural task**
  - *Nr. 3(a):* AI-enabled admissions data organisers that extract information from unstructured application documents, classify applications into predefined categories (undergraduate, graduate, international), and flag duplicates — provided the system takes no admission decision.
  - *Nr. 3(b):* AI-enabled grade calculator computing weighted averages of assessment scores; output is a numerical value used by the teacher.
  - *Nr. 3(d):* AI identity-verification system during a test that processes IDs or facial-recognition scans to confirm the registered candidate is the test-taker — the human proctor decides on consequences.

- **(b) Improvement of a completed human activity**
  - *Nr. 3(b):* AI-enabled exam quality checker that reviews a teacher-drafted exam for grammatical issues, ambiguous wording, or rubric inconsistencies and suggests revisions — without altering core content or difficulty.
  - *Nr. 3(c):* System analysing tutors' prior recommendations on advanced-course placement to suggest methodology improvements — does not decide on the apprentice's placement.
  - *Nr. 3(d):* AI confirmation of suspicious behaviour where a human proctor's existing suspicion (e.g., looking away from screen) is checked against a model of known cheating patterns; the proctor decides whether to escalate.

- **(c) Detection of decision-making patterns or deviations**
  - *Nr. 3(a):* AI-enabled admissions decision review tools that analyse ex-post admissions decisions for quality control — not meant to replace or influence the prior human assessment.
  - *Nr. 3(b):* AI-enabled assessment review tools that flag deviations in instructors' grading patterns over time for human review.

- **(d) Preparatory task**
  - *Nr. 3(a):* AI systems supporting application file handling — indexing, searching, text/speech processing, document translation, extracting and organising data — provided they do not influence the admission decision.
  - *Nr. 3(c):* AI-enabled pre-assessment tools that help educators prepare to assess a student's readiness by generating questions and topics based on prior education and work experience — the system makes no level-of-education decision itself.

## Common profiling considerations

Annex III Nr. 3 systems will very frequently involve automated processing of personal data to evaluate aspects of a natural person — in particular to analyse or predict aspects of that person's academic or vocational pathway. The Commission states explicitly in ¶215 that such systems will often perform profiling within the meaning of GDPR and may lead to automated decision-making under Art. 22 GDPR, and that **they should always be classified as high-risk, even if they otherwise fulfil the conditions of the Art. 6(3) filter mechanism**.

Practical consequences:

- **Profiling typically present** in: school assignment systems (collecting and combining home address, capacity, family status), vocational training assignment tools (prior education + certifications + aptitude scores), adaptive placement and special-education classifiers (combining assessment data, behavioural observations, medical history), AI-enabled grading systems that evaluate individual learners' work, AI-enabled personalised learning assistants used in summative evaluation, and most proctoring systems (biometric and behavioural monitoring of an identified test-taker).
- **Profiling typically NOT present** in: aggregate trend analysis on cohort or system-wide level (no individual evaluation), grade calculators performing a fixed mathematical computation, exam quality checkers that operate on the exam document rather than on learners, and admissions decision-review tools that analyse decision patterns at population level rather than re-evaluating individual applicants.
- Where profiling is present, the Art. 6(3) filter is blocked and the system is high-risk regardless of how "narrow" any individual sub-task may appear. When in doubt, assume profiling applies in Area 3 and document the reasoning carefully if claiming otherwise.

## Cross-references
- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — apply this decision tree for every Art. 6(3) claim, including the mandatory profiling check.
- [art-6-2-annex-iii-guidelines.md](art-6-2-annex-iii-guidelines.md) — general guidance on Annex III classification.
- [ai-omnibus-timeline-postponements.md](ai-omnibus-timeline-postponements.md) — confirms 2 December 2027 effective date for Annex III high-risk obligations.
- Related follow-on activities: **role determination** (provider vs. deployer distinctions in education contexts — e.g., a university deploying a third-party proctoring tool); **obligation mapping** (high-risk provider/deployer duties triggered once Area 3 classification stands).
- Art. 50 transparency: education AI that generates content (e.g., AI tutors, automated feedback, AI-generated study materials) may also be subject to Art. 50 transparency obligations independently of high-risk classification.
- Art. 5(1)(f) prohibition: emotion-inference systems in the area of education are prohibited (except medical/safety use); confirm the system is not prohibited before classifying it as high-risk (¶216).
