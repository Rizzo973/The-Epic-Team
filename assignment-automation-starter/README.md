# Assignment Automation — Starter Prototype

**Professor check-in status: working proof of concept using fictional examples.**
This demonstrates a proposed workflow: questions → student text template →
submitted text files → extracted answers and provisional grades in CSV.
It is an introductory Python starter, not a finished grading system.

## Included files

- `assignment_questions.txt`: three example questions to replace.
- `student_answer_template.txt`: code directly under each question, followed by an explanation.
- `solution_key.json`: example answers and point values; instructor review required.
- `submissions/example_student.txt`: fictional completed submission with one deliberate error.
- `grade_submissions.py`: reads all submission text files, extracts answers, and grades against the key.
- `.gitignore`: excludes generated results and real student submissions from Git commits.

## Run the example

Use Python 3.8 or newer. No extra packages are required.
Extract the ZIP, open a terminal in this project folder, and run:

```sh
python grade_submissions.py
```

On Windows, `py grade_submissions.py` may work if `python` is unavailable.
Open `results/grades.csv` in Excel or another spreadsheet program.
The example should produce three rows: Q1 and Q3 match the key, Q2 needs review,
for a provisional total of 2 out of 3 points. The CSV contains one row per question,
including student ID, code, explanation, status, and points. Multiline code is quoted
automatically so it remains in one CSV cell. There is no separate totals sheet yet.

Optional folder and output settings:

```sh
python grade_submissions.py --submissions submissions --key solution_key.json --output results/grades.csv
```

## Try your own submission

1. Copy `student_answer_template.txt` into `submissions/` with a new `.txt` filename.
2. Replace the student ID and placeholders. Keep the QUESTION, CODE, END_CODE,
   EXPLANATION, and END_EXPLANATION marker lines exactly as written.
3. Enter Python code under CODE and an explanation under EXPLANATION.
4. Run the script again. All `.txt` files in the folder are processed together.
   Each run replaces the output CSV.

## What grading currently means

The script compares code text to the example key. It preserves indentation and
ignores only outer blank lines and trailing spaces. A matching answer receives the
listed points. A different answer receives zero provisional points and the status
`review_needed`; a valid alternative may still be correct. Missing answers receive
zero points. Explanations are extracted but are not graded. Student code is never run.

Malformed files receive a `parse_error` row; other files continue to process.
The program exits with status 1 if any files have parsing errors. Unknown or duplicate
question IDs are rejected. Use unique student IDs and one file per student; duplicate
student IDs across files are not checked yet. Reserved marker lines cannot be used
as standalone lines inside an answer.

## Current scope and next steps

Included: sample questions, a manually prepared answer template, local batch parsing,
CSV export, and simple key comparison. Placeholder questions and keys must be replaced
and reviewed before classroom use.

Next steps: generate templates automatically from questions, agree on the final
submission format, add instructor-approved grading rules for alternative solutions,
validate keys and duplicate students, and add totals/reporting. LMS collection, Word/PDF
parsing, program execution, and AI grading are not implemented.

## Upload to GitHub

Upload the extracted project folder's contents so this README is at the repository root.
Include `.gitignore` (it may be hidden in your file browser). Keep the fictional sample
submission for demonstrations. Keep real student files, solution keys for live assignments,
and generated grades private. `.gitignore` helps when using Git, but does not prevent
manual browser uploads or remove files that are already tracked. The included key is
public demonstration data only. No GitHub upload has been performed by this project.
