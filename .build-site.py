# Generates the three support pages. Shared head/style lives here so the
# palette and typography cannot drift between pages.
import datetime

UPDATED = "September 9, 2026"

STYLE = """  :root{
    color-scheme: light dark;
    --bg:#F2F4F8;
    --surface:#FFFFFF;
    --ink:#171A21;
    --ink-soft:#5A6070;
    --accent:#2B4A8B;
    --rule:#DDE2EA;
    --amber:#8A6412;
    --callout-bg:#E7ECF5;
    --mono-bg:#E7ECF5;
  }
  @media (prefers-color-scheme: dark){
    :root{
      --bg:#101319;
      --surface:#191D25;
      --ink:#E8EBF1;
      --ink-soft:#99A0B0;
      --accent:#93A7D6;
      --rule:#272C36;
      --amber:#D6AC55;
      --callout-bg:#1D222C;
      --mono-bg:#1D222C;
    }
  }
  *{ box-sizing:border-box; }
  html{ scroll-behavior:smooth; }
  body{
    margin:0;
    background:var(--bg);
    color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    line-height:1.65;
    -webkit-font-smoothing:antialiased;
  }
  main{ max-width:40em; margin:0 auto; padding:2.75rem 1.5rem 6rem; }
  h1{
    font-family:Georgia,"Iowan Old Style","Palatino Linotype",Palatino,serif;
    font-size:1.9rem; line-height:1.25; margin:0 0 .35rem; color:var(--ink);
  }
  h2{
    font-family:Georgia,"Iowan Old Style","Palatino Linotype",Palatino,serif;
    font-size:1.3rem; margin:2.4rem 0 .9rem; padding-top:1.5rem;
    border-top:1px solid var(--rule); color:var(--ink); scroll-margin-top:1rem;
  }
  h3{ font-size:1.05rem; margin:1.6rem 0 .6rem; color:var(--ink); }
  p, li{ font-size:1rem; color:var(--ink); }
  p{ margin:0 0 1rem; }
  .meta{ color:var(--ink-soft); font-size:.95rem; margin:0 0 2.25rem; }
  .lede{ color:var(--ink-soft); font-size:1.08rem; }
  a{ color:var(--accent); }
  ul, ol{ padding-left:1.3rem; margin:0 0 1rem; }
  li{ margin-bottom:.5rem; }
  .callout{
    background:var(--callout-bg); border-left:4px solid var(--amber);
    border-radius:10px; padding:1.2rem 1.4rem .2rem; margin:1.75rem 0;
  }
  .callout h2, .callout h3{ margin-top:0; border-top:none; padding-top:0; }
  .toc{
    background:var(--surface); border:1px solid var(--rule);
    border-radius:12px; padding:1.1rem 1.4rem; margin:2.25rem 0;
  }
  .toc p{
    margin:0 0 .6rem; font-weight:600; font-size:.8rem;
    text-transform:uppercase; letter-spacing:.06em; color:var(--ink-soft);
  }
  .toc ol{ margin:0; padding-left:1.2rem; columns:1; }
  .toc li{ margin-bottom:.4rem; font-size:.95rem; }
  .toc a{ text-decoration:none; }
  .toc a:hover{ text-decoration:underline; }
  footer{
    margin-top:3.5rem; padding-top:1.5rem; border-top:1px solid var(--rule);
    color:var(--ink-soft); font-size:.9rem;
  }
  strong{ color:var(--ink); }"""

FOOTER = """<footer>
  <p>Charter is made by an independent developer. Questions:
  <a href="mailto:williamscott701@gmail.com?subject=Charter">williamscott701@gmail.com</a></p>
  <p><a href="./">Support</a> · <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></p>
  <p>CFA&reg; and Chartered Financial Analyst&reg; are registered trademarks owned by CFA Institute.
  Charter is not affiliated with, endorsed by, or associated with CFA Institute.</p>
</footer>"""

def page(filename, title, description, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<style>
{STYLE}
</style>
</head>
<body>
<main>
{body}
{FOOTER}
</main>
</body>
</html>
"""
    open(filename, "w").write(html)
    print(f"  wrote {filename} ({len(html):,} bytes)")

def toc(items):
    entries = "\n".join(f'    <li><a href="#{anchor}">{label}</a></li>' for anchor, label in items)
    return f'<nav class="toc">\n  <p>Contents</p>\n  <ol>\n{entries}\n  </ol>\n</nav>'

# ─────────────────────────────────────────────────────── privacy
PRIVACY_SECTIONS = [
    ("short", "1. The short version"),
    ("accounts", "2. No accounts, no sign-in"),
    ("stores", "3. What Charter stores, and where"),
    ("widgets", "4. Widgets"),
    ("notifications", "5. Notifications"),
    ("subscriptions", "6. Subscriptions and payment"),
    ("export", "7. Exporting and sharing your data"),
    ("backups", "8. Device backups"),
    ("tracking", "9. No tracking, analytics, or advertising"),
    ("deleting", "10. Deleting your data"),
    ("rights", "11. Your rights, wherever you are"),
    ("transfers", "12. International users and data transfers"),
    ("children", "13. Children's privacy"),
    ("changes", "14. Changes to this policy"),
    ("contact", "15. Contact"),
]

page("privacy.html", "Charter Privacy Policy",
     "How Charter handles your data: everything stays on your device. No account, no server, no analytics.",
     f"""<h1>Charter Privacy Policy</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p class="lede">Charter is a study planner for the CFA&reg; exams. It keeps your exam date, your
study hours and your self-ratings on your device, and sends them nowhere.</p>

{toc(PRIVACY_SECTIONS)}

<div class="callout">
<h3>In one paragraph</h3>
<p>Charter has no account system, no server and no analytics. Everything you enter stays in the
app's own storage on your iPhone or iPad. The developer cannot see your study log, your readiness
score or your exam date, because none of it is ever transmitted. The only network requests Charter
makes are to Apple, to check whether your subscription is active.</p>
</div>

<h2 id="short">1. The short version</h2>
<ul>
  <li>Everything you enter stays on your device.</li>
  <li>There is no account, no login and no user profile.</li>
  <li>There is no analytics SDK, no advertising SDK and no crash reporter.</li>
  <li>Nothing you enter is transmitted to the developer or to any third party.</li>
  <li>Deleting the app deletes the data with it.</li>
</ul>

<h2 id="accounts">2. No accounts, no sign-in</h2>
<p>Charter does not ask for your name, email address, phone number or date of birth. There is
nothing to sign in to. Your Apple Account is used only by Apple, to process a subscription if you
buy one — Charter never sees your Apple Account details.</p>

<h2 id="stores">3. What Charter stores, and where</h2>
<p>Charter stores the following on your device, and only on your device:</p>
<ul>
  <li>The exam and level you selected, and your exam date.</li>
  <li>Your target hours and the hours you have said you can study each day of the week.</li>
  <li>Your self-rated confidence for each topic.</li>
  <li>Each study session you log: topic, date, length, type and any note you write.</li>
  <li>Any mock exam scores you record.</li>
  <li>The generated schedule, and app preferences such as reminder times.</li>
</ul>
<p>This lives in the app's private container, which iOS protects from other apps, plus a shared
container used so the widgets can read a small summary. None of it leaves the device.</p>

<h2 id="widgets">4. Widgets</h2>
<p>Charter's widgets run in a separate process from the app, so the app writes a small summary
file — days remaining, today's sessions, your readiness score and recent hours — into a shared
container that both can read. That file stays on your device. Anyone who can see your Home Screen
or Lock Screen can see whatever the widget displays, which is worth knowing before adding one.</p>

<h2 id="notifications">5. Notifications</h2>
<p>Reminders are scheduled locally by iOS. Nothing is sent through a push server, and the developer
has no way to send you a notification. Notification text is composed on your device and may
include today's topic and your countdown, so it can appear on your Lock Screen. Turn reminders off
in Settings, or revoke the permission in iOS Settings, at any time.</p>

<h2 id="subscriptions">6. Subscriptions and payment</h2>
<p>Charter Pro is sold through Apple's In-App Purchase system. Apple handles the entire
transaction; Charter never sees or stores your payment details. The app asks Apple whether an
active subscription exists for this Apple Account and receives back an entitlement — nothing that
identifies you personally. Apple's own privacy policy governs that transaction.</p>

<h2 id="export">7. Exporting and sharing your data</h2>
<p>Charter Pro can export your sessions and mock scores as CSV files. The file is created on your
device and handed to the iOS share sheet, where you choose what happens to it. If you send it
somewhere — email, a messaging app, a cloud drive — that destination's own privacy policy applies
from then on. Charter has no involvement once you have chosen.</p>

<h2 id="backups">8. Device backups</h2>
<p>Because Charter's data lives in your app container, it is included in iCloud backups and
encrypted local backups if you have those turned on. Those backups are managed by Apple under
Apple's terms, not by Charter.</p>

<h2 id="tracking">9. No tracking, analytics, or advertising</h2>
<p>Charter contains no analytics, no advertising, no attribution SDK, no fingerprinting and no
third-party trackers of any kind. It does not use the Advertising Identifier and never presents
an App Tracking Transparency prompt, because there is nothing to track. No data is shared with
data brokers.</p>

<h2 id="deleting">10. Deleting your data</h2>
<p>Settings has a <strong>Delete all data</strong> option that removes every session, rating,
mock score and plan immediately. Deleting the app from your device also removes everything.
Because the developer never receives your data, there is nothing to request deletion of from
anyone else.</p>

<h2 id="rights">11. Your rights, wherever you are</h2>
<p>Privacy laws including the EU and UK GDPR, the California Consumer Privacy Act, Brazil's LGPD,
Canada's PIPEDA and Australia's Privacy Act give you rights to access, correct, export and delete
your personal information, and to object to its processing.</p>
<p>Charter is built so those rights are exercised directly in the app rather than by request:
you can view everything you have entered, edit or delete any of it, and export it as CSV. The
developer acts as data controller only in the narrow sense of publishing the app; because no
personal data is collected or transmitted, there is no stored copy to disclose, rectify, port or
erase. Charter does not sell or share personal information, and has never done so.</p>
<p>If you believe your rights have not been respected, you can contact the developer at the
address below, and you have the right to complain to your local data protection authority.</p>

<h2 id="transfers">12. International users and data transfers</h2>
<p>Charter performs no international transfer of your data, because it performs no transfer of
your data at all. Everything stays on the device you entered it on. Purchases are processed by
Apple in your own storefront under Apple's terms.</p>

<h2 id="children">13. Children's privacy</h2>
<p>Charter is a study planner for professional certification exams and is not directed at
children. It is rated 4+ because it contains no objectionable content, but it collects no personal
information from anyone, children included. No data is knowingly collected from children under 13
(or the equivalent age in your country) because no data is collected from any user.</p>

<h2 id="changes">14. Changes to this policy</h2>
<p>If this policy changes, the updated version will be posted on this page with a new
"last updated" date. Material changes will also be noted in the app's release notes. Charter's
design goal is that this policy stays this short.</p>

<h2 id="contact">15. Contact</h2>
<p>Questions about privacy, or anything else:
<a href="mailto:williamscott701@gmail.com?subject=Charter%20privacy">williamscott701@gmail.com</a>.
Charter is made by an independent developer, William Scott.</p>""")

# ─────────────────────────────────────────────────────── terms
TERMS_SECTIONS = [
    ("who", "1. Who this agreement is with"),
    ("what", "2. What Charter is, and what it is not"),
    ("licence", "3. Your licence to use Charter"),
    ("yours", "4. Your data is yours"),
    ("free", "5. What's free, and what Pro adds"),
    ("subscription", "6. Subscription terms"),
    ("trials", "7. Free trials"),
    ("cancelling", "8. Cancelling"),
    ("refunds", "9. Refunds"),
    ("consumer", "10. Consumer rights by country"),
    ("acceptable", "11. Acceptable use"),
    ("availability", "12. Availability and changes"),
    ("warranty", "13. No warranty, and no guarantee of results"),
    ("liability", "14. Limitation of liability"),
    ("apple", "15. Apple's role"),
    ("trademarks", "16. Trademarks"),
    ("law", "17. Governing law"),
    ("changes", "18. Changes to these terms"),
    ("entire", "19. Entire agreement and severability"),
    ("contact", "20. Contact"),
]

page("terms.html", "Charter Terms of Use",
     "The terms covering your use of Charter, including subscription, trial, cancellation and refund terms.",
     f"""<h1>Charter Terms of Use</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p class="lede">These terms cover your use of Charter, the study planner app for the CFA&reg;
exams. Installing or using Charter means you accept them.</p>

{toc(TERMS_SECTIONS)}

<div class="callout">
<h3>The parts people actually need</h3>
<p>Charter plans your study time. It contains no exam content and cannot tell you whether you
will pass. Pro is an auto-renewing subscription billed by Apple; it renews until you cancel, and
you cancel through your Apple Account settings rather than through the app. Refunds are handled
by Apple, not by the developer.</p>
</div>

<h2 id="who">1. Who this agreement is with</h2>
<p>Charter is published by William Scott, an independent developer ("the developer", "we").
"You" means the person using the app. This agreement is between you and the developer. Apple is
not a party to it, other than as described in section 15.</p>

<h2 id="what">2. What Charter is, and what it is not</h2>
<p>Charter takes an exam date, the hours you can study each week and how confident you feel about
each topic, and turns them into a dated schedule. It tracks the hours you log against that
schedule, scores how ready you appear to be, and re-cuts the plan when you fall behind.</p>
<p>Charter is <strong>not</strong> a course, a question bank, a tutor or a source of exam content.
It contains no curriculum material, no practice questions and no study notes. It is a calendar and
a tracker. The topic names and published weight bands it uses to divide your hours are factual
references to publicly available exam outlines, and you should confirm them against the official
outline for your own sitting — the app says so where they are shown.</p>
<p>Charter is an independent tool. It is not affiliated with, endorsed by, sponsored by or
associated with CFA Institute or any other examining body, and none of them has reviewed,
approved or contributed to it.</p>

<h2 id="licence">3. Your licence to use Charter</h2>
<p>You get a personal, non-transferable, non-exclusive licence to use Charter on Apple devices you
own or control, as permitted by the App Store Terms of Service. You may not sell, rent,
sublicense, redistribute, reverse-engineer, decompile or attempt to derive the source code of the
app, except to the extent that restriction is prohibited by law in your country.</p>

<h2 id="yours">4. Your data is yours</h2>
<p>Everything you enter belongs to you. It stays on your device — see the
<a href="privacy.html">privacy policy</a> — and Charter Pro can export it as CSV at any time. The
developer claims no ownership of and no rights over anything you enter.</p>

<h2 id="free">5. What's free, and what Pro adds</h2>
<p>Without a subscription, Charter gives you the exam countdown, your next scheduled session,
unlimited manual session logging and the first days of your schedule, for as long as you want.
Nothing you have logged is ever taken away or locked if a subscription lapses; you keep access to
your own data.</p>
<p>Charter Pro adds the complete schedule through to exam day, automatic re-planning when you fall
behind, readiness scoring and projection, the burndown and weekly charts, mock exam tracking,
per-topic tracking and CSV export.</p>

<h2 id="subscription">6. Subscription terms</h2>
<p>Charter Pro is offered as an auto-renewing subscription, billed through your Apple Account:</p>
<ul>
  <li><strong>Annual</strong> — billed once a year.</li>
  <li><strong>Monthly</strong> — billed once a month.</li>
</ul>
<p>Prices are shown in your local currency inside the app before you buy, and may differ between
countries. Payment is charged to your Apple Account at confirmation of purchase. The subscription
renews automatically at the same interval unless auto-renew is turned off at least 24 hours before
the end of the current period. Your account is charged for renewal within 24 hours before the
period ends. Prices may change; Apple will notify you and ask for consent where required before
any increase takes effect.</p>

<h2 id="trials">7. Free trials</h2>
<p>Where a free trial is offered, it is available once per Apple Account and only to accounts that
have not previously had a trial or subscription in this group. If you do not cancel at least 24
hours before the trial ends, it converts automatically into a paid subscription at the price
shown. Any unused portion of a trial is forfeited if you buy a subscription during it.</p>

<h2 id="cancelling">8. Cancelling</h2>
<p>Cancel at any time in <strong>Settings &rarr; your name &rarr; Subscriptions</strong> on your
device, or through the App Store app. Charter cannot cancel a subscription for you — Apple does
not give apps that ability. Settings inside Charter has a "Manage subscription" link that opens
Apple's own sheet. Cancelling stops the next renewal; you keep Pro until the end of the period
you have already paid for.</p>

<h2 id="refunds">9. Refunds</h2>
<p>All purchases are processed by Apple, so all refunds are handled by Apple. Request one at
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. The developer cannot
issue, approve or expedite a refund, and has no visibility of your purchase history. If something
in the app is broken, please email — that is a bug worth fixing regardless of the refund.</p>

<h2 id="consumer">10. Consumer rights by country</h2>
<p>Nothing in these terms removes rights you have as a consumer under the law of the country you
live in, and where those laws conflict with these terms, those laws win.</p>
<ul>
  <li><strong>European Union and United Kingdom.</strong> You normally have a 14-day right of
  withdrawal on digital purchases. Because Apple is the merchant of record, exercise it through
  Apple.</li>
  <li><strong>Australia.</strong> Our goods and services come with guarantees that cannot be
  excluded under the Australian Consumer Law, including remedies for major failures.</li>
  <li><strong>Elsewhere.</strong> Local mandatory consumer protection law applies in full.</li>
</ul>

<h2 id="acceptable">11. Acceptable use</h2>
<p>Use Charter lawfully and for your own study. Do not use it to break the rules of any
examination body, and do not use it in any way that interferes with Apple's services or with other
people's use of their devices.</p>

<h2 id="availability">12. Availability and changes</h2>
<p>Charter is offered as it is, and features may be added, changed or removed over time. The
developer may stop distributing or supporting the app; if that happens, the version already
installed on your device keeps working with the data already on it, because it needs no server.
Existing subscriptions would be discontinued through Apple in the ordinary way.</p>

<h2 id="warranty">13. No warranty, and no guarantee of results</h2>
<p>Charter is provided "as is" and "as available", without warranties of any kind, whether
express, implied or statutory, including any implied warranty of merchantability, fitness for a
particular purpose, accuracy or non-infringement, to the fullest extent the law allows.</p>
<p>In particular, and to be completely clear: <strong>Charter cannot and does not guarantee that
you will pass any examination.</strong> Its schedule, readiness score and projection are estimates
derived from figures you supply about yourself. They are a planning aid, not a prediction and not
a measure of competence. Exam outcomes depend on many things this app knows nothing about. Do not
substitute Charter's readiness score for your own judgement, your tutor's, or your official
provider's.</p>

<h2 id="liability">14. Limitation of liability</h2>
<p>To the fullest extent permitted by law, the developer is not liable for indirect, incidental,
special, consequential or exemplary damages, or for lost time, lost opportunity, exam results,
professional consequences or lost data, arising from your use of or inability to use Charter.
Where liability cannot be excluded, it is limited to the amount you paid for the app in the twelve
months before the claim. Some jurisdictions do not allow these exclusions, in which case they
apply only to the extent permitted.</p>

<h2 id="apple">15. Apple's role</h2>
<p>This agreement is between you and the developer, not Apple. Apple is not responsible for the
app or its content and has no obligation to provide support for it. Apple is not responsible for
addressing any claim you have relating to the app, including product liability claims, claims that
the app fails to conform to a legal or regulatory requirement, and claims arising under consumer
protection or similar legislation. If a third party claims the app infringes their intellectual
property, the developer is solely responsible for investigating and resolving that claim. Apple
and its subsidiaries are third-party beneficiaries of this agreement and may enforce it against
you. You confirm you are not located in a country subject to a US Government embargo or designated
as a "terrorist supporting" country, and that you are not on any US Government list of prohibited
or restricted parties.</p>

<h2 id="trademarks">16. Trademarks</h2>
<p>CFA&reg; and Chartered Financial Analyst&reg; are registered trademarks owned by CFA Institute.
Any reference to them in Charter or on this site is nominative — it identifies the exam the
planner is designed around, and implies no affiliation, endorsement or sponsorship. All other
trademarks belong to their respective owners.</p>

<h2 id="law">17. Governing law</h2>
<p>These terms are governed by the laws of India, without regard to conflict-of-law rules, and the
courts of India have non-exclusive jurisdiction. This does not deprive you of the protection of
mandatory consumer law in your country of residence, or of the right to bring proceedings there
where local law gives you that right.</p>

<h2 id="changes">18. Changes to these terms</h2>
<p>If these terms change, the updated version will be posted on this page with a new "last
updated" date. Continuing to use Charter after a change means you accept the updated terms. If you
do not accept them, stop using the app and cancel any subscription.</p>

<h2 id="entire">19. Entire agreement and severability</h2>
<p>These terms and the <a href="privacy.html">privacy policy</a> are the entire agreement between
you and the developer about Charter. If any provision is found unenforceable, the rest stays in
force and the unenforceable part is applied as closely as the law allows to its original intent.
Not enforcing a provision at one time is not a waiver of it.</p>

<h2 id="contact">20. Contact</h2>
<p><a href="mailto:williamscott701@gmail.com?subject=Charter%20terms">williamscott701@gmail.com</a></p>""")

# ─────────────────────────────────────────────────────── support / FAQ
page("index.html", "Charter Support",
     "Support and FAQ for Charter, the CFA exam study planner: how the schedule works, re-planning, widgets, subscriptions.",
     f"""<h1>Charter Support</h1>
<p class="meta">Last updated: {UPDATED}</p>
<p class="lede">Charter turns an exam date and the hours you actually have into a schedule, then
keeps it honest when the weeks don't go to plan. Here's how it works, and what to do when it
doesn't.</p>

<div class="callout">
<h3>Contact</h3>
<p>Email <a href="mailto:williamscott701@gmail.com?subject=Charter">williamscott701@gmail.com</a>.
It's one developer, so replies take a day or two — but every email is read. Mentioning your device
and iOS version helps.</p>
</div>

<h2 id="how">How does Charter decide what to study today?</h2>
<p>Three inputs. The exam's own published weight for each topic sets the baseline, so a topic
worth 15% of the paper gets roughly triple the hours of one worth 5%. Your self-rated confidence
then bends that: the topic you rated 0 pulls up to about 1.8 times what its weight alone would
give it, and the one you rated 5 gets exactly its weighted share and no less — nobody should walk
in having spent zero hours on anything.</p>
<p>Those hours are then spread across the days you said you're free, interleaved so no topic is
finished in one block and forgotten, with the last stretch before the exam reserved for review and
mock papers rather than new material.</p>

<h2 id="behind">What happens when I fall behind?</h2>
<p>Nothing accumulates. Charter does not show you a growing pile of missed days — that is the
thing that makes people delete study apps. Instead it re-cuts the days you have left around the
work that is genuinely still outstanding, re-weighted by how you feel about each topic now.</p>
<p>This happens automatically once you have drifted more than six hours from the plan, or on
demand from the rebuild button on the Plan tab. Hours you have already logged are always kept.
You can turn the automatic version off in Settings.</p>

<h2 id="wontfit">It says my plan "won't fit" — what does that mean?</h2>
<p>It means the honest thing: the hours still to do are more than the days before your exam can
hold at the availability you entered. Charter tells you this as early as it can see it, rather
than quietly overfilling days you were never going to work.</p>
<p>You have three real options, and the app will show you the numbers for each: add hours to your
weekly availability, reduce your target hours, or accept it and let the schedule prioritise by
exam weight so the shortfall comes off the topics worth least. Any of those is better than finding
out in the last fortnight.</p>

<h2 id="weights">Are the topic weights official?</h2>
<p>They follow the published outline for the curriculum year shown in the app, but exam boards
revise them, and Charter ships with them marked unverified for exactly that reason — you will see
a notice on the Topics tab saying so.</p>
<p><strong>Check them against the official study session outline for your own sitting.</strong>
Charter is a planner, not an authority on the syllabus. If the weights have moved, the split of
your hours will be slightly off, and that is worth knowing before you rely on it.</p>

<h2 id="content">Does Charter include practice questions or study notes?</h2>
<p>No, and it never will. Charter contains no exam content of any kind. It plans and tracks your
time; your curriculum, question bank and notes come from wherever you already get them. That's a
deliberate scope, not a missing feature.</p>

<h2 id="readiness">What is the readiness score, and should I trust it?</h2>
<p>It combines three things per topic: how much of the allocated time you have actually done
(55%), how confident you have rated yourself (30%), and how recently you touched it (15%, halving
roughly every three weeks). Those are weighted by what each topic is worth to the exam.</p>
<p>Treat it as a planning aid, not a prediction. It is built from numbers you gave it about
yourself, so it is exactly as honest as your own ratings. It cannot tell you whether you will
pass — nothing can. The projection next to it shows where the score lands on exam day if your
recent pace holds, which is usually the more useful of the two.</p>

<h2 id="data">Where is my data, and how do I get it out?</h2>
<p>On your device, and nowhere else — no account, no server. Charter Pro exports every session and
mock score as CSV from Settings &rarr; Data. Settings also has a Delete all data option that
removes everything immediately. Full detail in the <a href="privacy.html">privacy policy</a>.</p>

<h2 id="widgets">My widget isn't updating</h2>
<p>Widgets refresh when the app writes a new summary — which happens whenever you log a session or
change the plan — and again after midnight so the countdown stays right. If one looks stale:</p>
<ul>
  <li>Open Charter once; that forces a refresh.</li>
  <li>Remove the widget and add it again.</li>
  <li>Check <strong>Settings &rarr; General &rarr; Background App Refresh</strong> is on.</li>
</ul>
<p>The readiness widget shows a lock without a subscription; that is expected, not a fault.</p>

<h2 id="reminders">Reminders aren't arriving</h2>
<p>Charter uses local notifications only, so there is no server to blame. Check
<strong>Settings &rarr; Notifications &rarr; Charter</strong> is allowed, that Focus or Scheduled
Summary is not holding them back, and that the daily reminder is switched on inside Charter's own
Settings. Changing the reminder time reschedules everything.</p>

<h2 id="pro">Pro, trials, and cancelling</h2>
<p>Pro is an auto-renewing subscription, annual or monthly, billed by Apple. The countdown, your
next session and manual logging stay free forever, and nothing you have logged is ever locked away
if a subscription ends.</p>
<p>Cancel in <strong>Settings &rarr; your name &rarr; Subscriptions</strong>, or via the Manage
subscription link in Charter's Settings. Cancelling stops the next renewal and you keep Pro until
the period you paid for runs out. Refunds are Apple's to give — request one at
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>. Restored a device or
changed phone? Tap <strong>Restore purchases</strong> in Settings.</p>

<h2 id="affiliation">Charter is not affiliated with CFA Institute</h2>
<p>Charter is an independent app by an independent developer. CFA Institute has not reviewed,
approved, endorsed or contributed to it, and has no association with it. Charter references the
exam by name only to say which exam it helps you plan for.</p>

<h2 id="legal">Privacy and terms</h2>
<p><a href="privacy.html">Privacy policy</a> &middot; <a href="terms.html">Terms of use</a></p>""")
