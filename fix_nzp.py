#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

h = h.replace('Mark Evans-Smith</div>', 'Mark Molsbee</div>')
h = h.replace('Mark Evans-Smith, NZP Commercial Lead', 'Mark Molsbee, NZP Commercial Lead')
h = h.replace('alt="Mark Evans-Smith"', 'alt="Mark Molsbee"')
h = h.replace('Richard Malsby</div>', 'Richard Molsbee</div>')
h = h.replace('Richard Malsby</h4>', 'Richard Molsbee</h4>')
h = h.replace('alt="Richard Malsby"', 'alt="Richard Molsbee"')

old_intro = 'Our senior technical team are InEnTec veterans — the pioneers of commercial plasma gasification. CTO Richard Malsby: decades in gasification, ex-US government. This expertise is not on a hiring platform.'
new_intro = 'Our senior technical team brings deep experience across commercial and government sectors — with decades in plasma gasification and ex-US government programme roles. This expertise is not on a hiring platform.'
h = h.replace(old_intro, new_intro)

h = h.replace('InEnTec Heritage — CTO Richard Malsby', 'Technical Heritage — CTO Richard Molsbee')
h = h.replace('InEnTec Heritage — CTO Richard Molsbee', 'Technical Heritage — CTO Richard Molsbee')

old_card = 'Senior team includes InEnTec veterans. CTO Richard Malsby brings decades of gasification experience including ex-US government roles. Technology maturity: TRL 8–9. Not TRL 6 demos.'
new_card = 'Senior team brings broad commercial and government sector experience. CTO Richard Molsbee brings decades of gasification expertise including ex-US government programme roles. Technology maturity: TRL 8–9. Not TRL 6 demos.'
h = h.replace(old_card, new_card)

h = h.replace('Hitachi / Westinghouse', 'Hitachi / AlterNrg')
h = h.replace('Hitachi/Westinghouse', 'Hitachi/AlterNrg')
h = h.replace('Westinghouse Partnership', 'AlterNrg Partnership')
h = h.replace('Hitachi Energy and Westinghouse', 'Hitachi Energy and AlterNrg')

h = h.replace('rgba(255,255,255,.45)', 'rgba(255,255,255,.80)')

old_pills = '<span class="partner-pill">HITACHI ENERGY</span>\n       <span class="partner-pill">WESTINGHOUSE</span>\n       <span class="partner-pill">MAJOR ENERGY OFFTAKE PARTNER</span>\n       <span class="partner-pill">GLOBAL FMCG CONSORTIUM</span>\n       <span class="partner-pill">InEnTec VETERANS</span>'
new_pills = '<span class="partner-pill">HITACHI ENERGY</span>\n       <span class="partner-pill">ALTERNRG</span>\n       <span class="partner-pill">MAJOR ENERGY OFFTAKE PARTNER</span>\n       <span class="partner-pill">GLOBAL FMCG CONSORTIUM</span>\n       <span class="partner-pill">SMS &amp; TENOVA — gasification</span>\n       <span class="partner-pill">GE VERNOVA &amp; SIEMENS — power</span>\n       <span class="partner-pill">AIR PRODUCTS &amp; AIR LIQUIDE — gas handling</span>\n       <span class="partner-pill">AON — insurance</span>\n       <span class="partner-pill">BP · MARATHON · ECOENERGY · MANSFIELD · TENASKA — fuel buyers</span>'
h = h.replace(old_pills, new_pills)

old_partners = 'Equipment supply through Hitachi/Westinghouse. Synthesis partners for F-T and Haber-Bosch. Offtake agreements in place.'
new_partners = 'Equipment supply through Hitachi/AlterNrg and SMS/Tenova; power equipment through GE Vernova and Siemens; gas handling through Air Products and Air Liquide; synthesis partners for F-T and Haber-Bosch; insurance through AON; fuel buyers including BP, Marathon Petroleum, Ecoenergy, Mansfield Oil and Tenaska Biofuels. Offtake agreements in place.'
h = h.replace(old_partners, new_partners)

old_richard = 'InEnTec veteran — UHTMG gasification pioneer'
new_richard = 'Broad sector experience — plasma arc and gasification'
h = h.replace(old_richard, new_richard)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)

checks = {
    'Mark Molsbee': 'Evans-Smith' not in h and 'Mark Molsbee' in h,
    'Richard Molsbee': 'Richard Molsbee' in h and 'Richard Malsby' not in h,
    'Technical Heritage': 'Technical Heritage' in h,
    'AlterNrg (no Westinghouse)': 'Westinghouse' not in h and h.count('AlterNrg') >= 2,
    'SMS + Tenova': 'SMS' in h and 'Tenova' in h,
    'GE Vernova + Siemens': 'GE Vernova' in h and 'Siemens' in h,
    'Air Products + Air Liquide': 'Air Products' in h and 'Air Liquide' in h,
    'AON': 'AON' in h,
    'Marathon': 'Marathon' in h,
    'Brighter logos': 'rgba(255,255,255,.80)' in h,
}
all_ok = True
for k, v in checks.items():
    print(f"{'OK' if v else 'FAIL'}: {k}")
    if not v: all_ok = False
print(f"\n{'ALL OK' if all_ok else 'ISSUES FOUND'} — {len(h)//1024}KB")
