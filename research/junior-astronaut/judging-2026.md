# 2026 judging and submission rules vs our plan

Checked 13 Nov 2026 in the browser (curl fails on spaceappschallenge.org: the server sends an incomplete certificate chain, curl error 60, and the site is a JavaScript app). Pages are saved as hand-copied, trimmed text in `pages/spaceapps-2026-*.txt`.

The 2026 Judging & Awards Guide and Project Submission Guide are both live (dated 12 Nov 2026), so the "re-check on 13 Nov" item in `CLAUDE.md` is done.

## TL;DR

- The five criteria, the demo limits (30 s video or 7 slides), the English-subtitles rule, the public no-login link and the 23:59 local deadline are all unchanged from our plan.
- Four things are new or stricter than we planned for:
  1. **SI must not be used to come up with the idea** for how to solve the challenge.
  2. **SI audio and code must be acknowledged in metadata as well as in text** (images and video need a visible watermark, as before).
  3. **Every resource, even open source or CC0, must be listed in the References field**, with licence documentation. Ticking a box says all work is original.
  4. **At least one NASA data source or resource is needed to be eligible for a Global Award.**
- Nothing in 2026 says that prepared assets are allowed. The only written rule is the old one, so the verbal permission from the Colombo Local Lead still needs to be in writing.
- Colombo's page gives no local deadline. Local judging may end earlier than the global 23:59, so ask the Local Lead.

## The "work before the event" rule, exact words

Participant FAQs (page dated 5 Nov 2026), answer to "What are the challenges?":

> "Resources for each challenge will be published on November 13. Teams are not allowed to begin working on the challenges prior to the hackathon."

The Terms and Conditions (updated 7 Aug 2026) say the event runs "starting on November 14, 2026". The Submission Guide says the team Project tab "will appear only when the hackathon begins on November 14, 2026 at 9:00 a.m. local time". No 2026 page mentions prepared assets, models, art or maps, and none sets any exception. Any permission for them comes only from the Local Lead.

## What changed from our plan

| Item | Our plan | 2026 says | Source |
|---|---|---|---|
| Criteria | Impact, Creativity, Validity, Relevance, Presentation | Same five, each scored 1 to 5 at every level of judging. Relevance wants NASA data as "a core component ... rather than a superficial addition". Presentation is judged from the demo and the full project | Judging guide |
| Demo | 30 s video with English subtitles, or up to 7 slides | Same. The video may be spoken in another language but MUST have English subtitles; slides must be in English. Over the limit means "not eligible for Global Judging". The demo is part of the evaluation, but the majority of the evaluation is the project submission | Submission guide |
| Game link | Public, no login | Same: no password, permission or registration. New advice: test it in a private window; a new website should request a FortiGuard web filter classification (optional) so judges can open it | Submission guide |
| Deadline | 23:59 local on day 2 | Sun 15 Nov 23:59 in the time zone of the team's Local Event. Submission opens Sat 14 Nov 09:00. Later saves or submits are not judged. Only the last saved submission is read. Local judging and awards times "may differ", ask the Local Lead | Submission guide |
| Starting early | Verbal OK for assets only | Unchanged rule, no exception written anywhere. See the exact words above | FAQ |
| SI, how it may be used | Describe it in the submission | Permitted "to accelerate innovation and creativity", but "SI should not be used to (come up with your idea of how to solve the challenge)". Judges do not see the SI answer, they see watermarks, text and metadata | Submission guide |
| SI, labels | Images/videos watermarked; audio and code "acknowledged in text" | Images and videos: visible watermark. Audio, code and data: acknowledged in descriptive text **and metadata** | Submission guide |
| SI and NASA marks | No NASA logos | Same, and it now covers generated content: it may not "use, contain, or modify any NASA branding or design elements (such as the NASA logos, flags, or mission identifiers)" | Submission guide |
| NASA data | "Data: NASA" credit | To be eligible for a Global Award you "must use at least one NASA data or resource". Using Space Agency Partner data is encouraged | Submission guide |
| Sources and assets | Keep CREDITS.md | Every source, "even if it is open source or freely available", goes in the References field. Licence documentation is required for non-NASA materials, or the solution is not accepted or posted. Missing citations can cost nominations or awards. The original-work box says no copyrighted music, images or text without permission | Terms, Judging guide |
| Our own work | Apache-2.0 | Original content must be free of restriction or OSI open source. If we name no licence, NASA uses Apache 2.0. Third-party materials must be free and public or OSI licensed | Terms |
| Under-18s | No photos, video or voices | Same, plus no "recognizable names". Under-18 team members must be registered by a guardian and accompanied at the event. Adult likenesses need the person's consent | FAQ, Terms |
| Video ownership | Not covered | The video must be our own work, with no third-party rights issues. The US government gets a royalty-free licence to it | Terms |
| Slide deck contents | Not covered | If slides: team name, member names, challenge chosen, project image, user experience, how NASA data made it possible (watch the under-18 rule on names) | Submission guide |
| Page uploads | Not covered | The project page takes JPG, PNG and GIF up to 10 MB only. Videos and documents must be hosted elsewhere and linked | Submission guide |
| Team | Four people | 1 to 6 members, all registered at the same Local Event and not waitlisted, one challenge per team, no new members after submission closes | Judging guide, FAQ |
| Path after submit | Not covered | Local judges (organised by the Local Lead) pick Global Nominees, announced 3 Dec 2026. Global judges pick Finalists and Honorable Mentions, 17 Dec 2026. An executive committee picks winners in ten categories, announced 26 Jan 2027. Local awards are separate and do not decide Global judging | Judging guide |

## Global Nominee / local winner path

1. Submit on the team page before the deadline (every submitter gets a certificate).
2. The Colombo panel scores projects with the five criteria and picks the Global Nominees. Colombo had a Global Finalist in 2025 (its page).
3. Local awards, such as the US Embassy ceremony the Colombo page mentions, are separate. Only officially submitted Global Nominees go to Global Judging.
4. Ten Global Awards: Best Use of Science, Best Use of Data, Best Use of Technology, Galactic Impact, Best Mission Concept, Most Inspirational, Best Storytelling, Global Connection, Art & Technology, Local Impact.

## What to do

- Fix the SI paragraph: we must be able to say the idea and design came from the team (the challenge text and our own research), with SI used for building. Check the Docmost "How we build it with AI" page against this. Decide who owns that statement before 14 Nov.
- Add SI notes to metadata: a header or README line for code, ID3/Vorbis comment tags on the Piper audio files, and the game's credits screen. Watermark any AI image or video.
- List every asset (Kenney, NASA models, Piper voices, fonts, NOAA data) in the References field with its licence. `assets-cache/CREDITS.md` is the source.
- Name a NASA dataset in the NASA Data field (Curiosity REMS weather, NOAA flares, NASA 3D models) so we stay eligible for Global Awards.
- Ask the Colombo Local Lead (listed on the event page) in writing: (a) may prepared assets be used, (b) the local submission and judging deadline, (c) which time zone and cut-off counts for our team. Save the reply in this folder.
- Host the game where a phone can open it with no login, and test it in a private window.

## Not found

- No 2026 page on prepared assets or pre-event work other than the FAQ sentence above.
- No separate "rules" page: the rules are the FAQ, the Terms and the two guides.
- The Colombo Local Event Schedule tab returned no text, so we have no local times.
