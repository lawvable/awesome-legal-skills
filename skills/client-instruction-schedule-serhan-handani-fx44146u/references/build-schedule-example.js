// Complete working build script for the client instruction schedule (.docx).
// Pair with ./schedule-data-example.js (fictional demonstration data).
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, PageOrientation, AlignmentType, LevelFormat, ShadingType,
  Header, Footer, PageNumber, VerticalAlign, HeadingLevel, BorderStyle,
} = require("docx");
const fs = require("fs");
const rows = require("./schedule-data-example.js");

const FONT = "Times New Roman";
const SZ = 24; // 12pt in half-points

const run = (text, opts = {}) => new TextRun({ text, font: FONT, size: SZ, ...opts });
const para = (text, opts = {}, runOpts = {}) =>
  new Paragraph({ children: [run(text, runOpts)], spacing: { after: 60 }, ...opts });

// Column widths (DXA). Page: A4 landscape 16838 wide, margins 720 each side -> 15398 usable.
const COLS = [1450, 2200, 2500, 2100, 2750, 2000, 1378, 1020];
const TABLE_W = COLS.reduce((a, b) => a + b, 0);

const headCell = (text, w) =>
  new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: "D9D9D9" },
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({ children: [run(text, { bold: true })], spacing: { after: 0 } })],
  });

const bodyCell = (children, w) =>
  new TableCell({
    width: { size: w, type: WidthType.DXA },
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children,
  });

const headerRow = new TableRow({
  tableHeader: true,
  children: [
    headCell("Issue", COLS[0]),
    headCell("Our position", COLS[1]),
    headCell("The other side’s position", COLS[2]),
    headCell("Evidence we already hold", COLS[3]),
    headCell("What we need from you", COLS[4]),
    headCell("Your response", COLS[5]),
    headCell("Documents you are sending", COLS[6]),
    headCell("Priority", COLS[7]),
  ],
});

const bodyRows = rows.map((r) =>
  new TableRow({
    cantSplit: false,
    children: [
      bodyCell(
        [
          new Paragraph({
            numbering: { reference: "issue-numbers", level: 0 },
            children: [run(r.label, { bold: true })],
            spacing: { after: 0 },
          }),
        ],
        COLS[0]
      ),
      bodyCell([para(r.ours, { spacing: { after: 0 } })], COLS[1]),
      bodyCell([para(r.theirs, { spacing: { after: 0 } })], COLS[2]),
      bodyCell([para(r.held, { spacing: { after: 0 } })], COLS[3]),
      bodyCell([para(r.need, { spacing: { after: 0 } })], COLS[4]),
      bodyCell([new Paragraph({ children: [], spacing: { after: 0 } })], COLS[5]),
      bodyCell([new Paragraph({ children: [], spacing: { after: 0 } })], COLS[6]),
      bodyCell([para(r.priority, { spacing: { after: 0 } })], COLS[7]),
    ],
  })
);

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: FONT, size: SZ } },
    },
  },
  numbering: {
    config: [
      {
        reference: "issue-numbers",
        levels: [
          {
            level: 0,
            format: LevelFormat.DECIMAL,
            text: "%1.",
            alignment: AlignmentType.LEFT,
            style: {
              run: { font: FONT, size: SZ, bold: true },
              paragraph: { indent: { left: 340, hanging: 340 } },
            },
          },
        ],
      },
    ],
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
          margin: { top: 720, bottom: 720, left: 720, right: 720 },
        },
      },
      headers: {
        default: new Header({
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                run("AI-ASSISTED DRAFT — FOR SOLICITOR REVIEW — NOT YET APPROVED OR SENT", {
                  bold: true, color: "808080", size: 18,
                }),
              ],
              spacing: { after: 0 },
            }),
          ],
        }),
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({ font: FONT, size: 18, color: "808080", children: ["[CLIENT NAME] — Client Instruction Schedule (Draft [NN], [DATE]) — Page "] }),
                new TextRun({ font: FONT, size: 18, color: "808080", children: [PageNumber.CURRENT] }),
                new TextRun({ font: FONT, size: 18, color: "808080", children: [" of "] }),
                new TextRun({ font: FONT, size: 18, color: "808080", children: [PageNumber.TOTAL_PAGES] }),
              ],
              spacing: { after: 0 },
            }),
          ],
        }),
      },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [run("YOUR DISPUTE WITH [OPPONENT / MATTER NAME]", { bold: true, size: 28 })],
          spacing: { after: 60 },
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [run("Client Instruction Schedule — Draft [NN]", { bold: true })],
          spacing: { after: 60 },
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [run("Please work through the rows marked “High” first. Write your answers in the “Your response” column and list what you are sending in the “Documents you are sending” column, or use separate sheets numbered to match each row.", { italics: true })],
          spacing: { after: 120 },
        }),
        // NB: highlighted runs make the docx package emit an invalid <w:highlightCs>
        // element. Strip it after packing (see SKILL.md, "Verify before delivering",
        // step 1) or OOXML schema validation will fail. The file still opens fine in Word.
        new Paragraph({
          children: [run("[SOLICITOR TO VERIFY — DELETE BEFORE SENDING TO CLIENT: list here any inconsistencies found in the source papers.]", { bold: true, highlight: "yellow" })],
          spacing: { after: 160 },
        }),
        new Table({
          width: { size: TABLE_W, type: WidthType.DXA },
          columnWidths: COLS,
          rows: [headerRow, ...bodyRows],
        }),
      ],
    },
  ],
});

// Output path is a parameter (first CLI argument) so nothing is silently
// overwritten; the guard refuses to clobber an existing file.
const OUT = process.argv[2] || "client-instruction-schedule-draft-NN-YYYY-MM-DD.docx";
if (fs.existsSync(OUT)) {
  console.error(`refusing to overwrite existing file: ${OUT}`);
  process.exit(1);
}
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log(`schedule written: ${OUT}`);
});
