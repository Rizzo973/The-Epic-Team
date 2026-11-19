HOW TO GRADE SUBMISSIONS WITH THE ASSIGNMENT GRADER

WHAT THE PRPOGRAM DOES
This program reads student answer files and compares each answer key, and creates
spreadsheet of results. It doesnt run student code. It just compares text.

SETUP

1. Install python 3 from https://www.python.org/downloads/
2. Download our project from Github, Download it as zip and then extract it

EVERY TIME YOU GRADE
1. Put the students in a .txt files in this folder: assignment-automation-starter\assignment-automation-starter\submissions
2. Open the main project folder (The one that contains grade_submissions.py) in File Explorer
3. Click the address bar at the top and type powershell and press enter
4. Copy this command, paste it in the pSowershell window:
python grade_submissions.py --submissions assignment-automation-starter/assignment-automation-starter/submissions --key assignment-automation-starter/solution_key.json --output results/grades.csv
5. Something its going to appear like "Wrote X rows to results\grades.csv"
6. Open the results. Choose ONE of these:

   Option A (recommended) - open in Excel. Type this and press Enter:
   start results/grades.csv

   Option B - show a quick table in PowerShell. Paste this and press Enter:
   Import-Csv results/grades.csv Format-Table submission_file, question_id, status, points_earned, note -AutoSize
BOTH OPTIONS SHOWS THE SAME RESULT

HOW TO GRADE SUBMISSIONS WITH THE ASSIGNMENT GRADER

WHAT THE PROGRAM DOES
This program reads student answer files, compares each answer to
the answer key, and creates a spreadsheet of results.
It does NOT run student code. It only compares text.

ONE-TIME SETUP
1. Install Python 3 from https://www.python.org/downloads/
   IMPORTANT: on the first install screen, tick the box
   "Add python.exe to PATH" before clicking Install.
2. Download our project from GitHub (Code > Download ZIP),
   then right-click the ZIP and choose Extract All.

HOW STUDENTS SUBMIT
- Students copy assignment-automation-starter\student_answer_template.txt
  and rename it (for example, with their name or ID).
- They replace REPLACE_WITH_YOUR_ID with their student ID and type
  their code between CODE: and END_CODE for each question.
- They must NOT delete or change the marker lines
  (QUESTION:, CODE:, END_CODE, EXPLANATION:, END_EXPLANATION).

EVERY TIME YOU GRADE
1. Put all the students' .txt files in this folder:
   assignment-automation-starter\assignment-automation-starter\submissions
2. Open the main project folder (the one that contains
   grade_submissions.py) in File Explorer.
3. Click the address bar at the top, type powershell, and press Enter.
4. Copy this command, paste it into the PowerShell window
   (right-click to paste), and press Enter:

   python grade_submissions.py --submissions assignment-automation-starter/assignment-automation-starter/submissions --key assignment-automation-starter/solution_key.json --output results/grades.csv

5. You should see a message like "Wrote X rows to results\grades.csv".
   This grades every student at once.
6. Open the results. Choose ONE of these:

   Option A (recommended) - open in Excel. Type this and press Enter:
   start results/grades.csv

   Option B - show a quick table in PowerShell. Paste this and press Enter:
   Import-Csv results/grades.csv | Format-Table submission_file, question_id, status, points_earned, note -AutoSize

   Both options show the same results.
7. Check the results (see "WHAT TO DO AFTER GRADING" below),
   then close Excel when you are done.

WHAT EACH COLUMN MEANS
  submission_file  The name of the student's .txt file.
  student_id       The ID the student typed in their file.
  question_id      Which question the row is about (Q1, Q2, Q3...).
  code             The code the student wrote for that question.
  explanation      The student's explanation of their code.
  status           The result for that question (see below).
  points_earned    Points the program gave for that question.
  points_possible  The most points that question is worth.
  note             Extra information, such as why a file failed.

WHAT THE RESULTS MEAN (the "status" column)
  matches_key    The answer is exactly the same as the key. Full points.
  review_needed  The answer is different from the key. 0 points for now.
                 Please check it, because it may still be correct
                 (for example, 4 + 3 instead of 3 + 4).
  missing        The student left the answer blank. 0 points.
  parse_error    The file could not be read, usually because a marker
                 line was deleted. The "note" column explains why.


WHAT TO DO AFTER GRADING
- matches_key rows: nothing to do. Points are already given.
- review_needed rows: read the student's code. If it is correct,
  give the points yourself.
- missing rows: the student did not answer. Nothing to do.
- parse_error rows: the file could not be read, so NONE of that
  student's questions were graded. A file with an error shows as
  only ONE row, not one row per question. The note column says
  where the problem is. Ask the student to fix their file and
  resubmit, then run the program again.


THINGS YOU SHOULD KNOW
- You have to close the Spreadsheet in Excel before you run the program again,
or its not going to be able to save the new results.
- Each run replaces the previous results file.
- To change the question or answers, edit assignment-automation-starter\solution_key.json in the notepad
