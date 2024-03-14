import sqlite3 

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

cur.execute('select * from property where name ="" ')#or owner like "POWER BROKER%";')
l= [(12, 'https://www.loopnet.com/Listing/Cavalier-Henrosa-Hotels/17411823/', 'Cavalier & Henrosa Hotels', '', 'Susan Gale', '', 'Miami Beach, FL', 0, 0), (56, 'https://www.loopnet.com/Listing/Hotel-Extended-Stay-Housing-2-Bldgs/24497524/', 'Hotel & Extended Stay/Housing 2 Bldgs', 'Dr. Mehdi Turabi', 'Mehdi Turabi', '', 'Beckley, WV', 0, 0), (99, 'https://www.loopnet.com/Listing/440-US-Highway-101-N-Crescent-City-CA/25273756/', '440 US Highway 101 N', '', 'Steve Song', '', 'Crescent City, CA', 0, 0), (108, 'https://www.loopnet.com/Listing/Quality-Inn-Super-8-Motel/25371264/', 'Quality Inn & Super 8 Motel', '', 'Dave Thompson', '', 'Harrisburg, IL', 0, 0), (209, 'https://www.loopnet.com/Listing/Miami-Miami-Beach-Triple-Net-leased-Ho/26254303/', 'Miami & Miami Beach Triple-Net leased Ho', '', 'Susan Gale', '', 'Miami Beach, FL', 0, 0), (231, 'https://www.loopnet.com/Listing/Boutique-Hotel-Portfolio-Palm-Springs/26419422/', 'Boutique Hotel Portfolio - Palm Springs', '', 'Harry Pflueger', '', 'Palm Springs, CA', 0, 0), (334, 'https://www.loopnet.com/Listing/Beach-Street-Rockport-Captains-Bounty/26874809/', "Beach Street Rockport - Captain's Bounty", '', 'Kevin Olson', '', 'Rockport, MA', 0, 0), (357, 'https://www.loopnet.com/Listing/Two-Property-Upscale-Marriott-Portfolio/26942045/', 'Two-Property Upscale Marriott Portfolio', '', 'Chris Gomes', '', 'Woodlands, TX', 0, 0), (372, 'https://www.loopnet.com/Listing/North-Dakota-3-Hotel-Portfolio/27031484/', 'North Dakota 3 Hotel Portfolio', 'Ray Starner', 'Gregg Marzano', '', 'Minot, ND', 0, 0), (392, 'https://www.loopnet.com/Listing/Motel-6-Studio-6-Hybrid/27113124/', 'Motel 6/Studio 6 Hybrid', '', 'Faiz Rajwani', '', 'Temple, TX', 0, 0), (399, 'https://www.loopnet.com/Listing/358-Relax-Dr-Smithville-TN/27141471/', '358 Relax Dr', '', 'Matt Messier', '', 'Smithville, TN', 0, 0), (435, 'https://www.loopnet.com/Listing/Two-Property-Portfolio-Wichita-KS/27283754/', '', '', 'Chris Gomes', '', '', 0, 0), (437, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-MI/27283512/', 'Two-Property Marriott Portfolio - MI', 'Ebrahim Valliani', 'Michael Klar', '', 'Lansing, MI', 0, 0), (438, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-IL/27283330/', 'Two-Property Marriott Portfolio - IL', 'Ebrahim Valliani', 'Michael Klar', '', 'Champaign, IL', 0, 0)] 
# t = list()
# for c in l:
#     t.append(c[0]-(c[0]//435))
#     # print(c[1])
#     # name = input("name:")
#     # city = input("city:")
#     cur.execute(f'update property set name="{c[2]}"  where id={c[0]}')
#     cur.execute(f"update property set city='{c[6]}' where id={c[0]}")
# cur.execute("delete from property where id=435")
# cur.execute("update property set id = id-1 where id>435")

# con.commit()
# cur.execute(f'select * from property where id in {str(tuple(t))} ')#or owner like "POWER BROKER%";')
# print(cur.fetchall())

"""
[(12, 'https://www.loopnet.com/Listing/Cavalier-Henrosa-Hotels/17411823/', 
'Cavalier & Henrosa Hotels', '', 'Susan Gale', '', 'Miami Beach, FL',
 0, 0), (56, 'https://www.loopnet.com/Listing/Hotel-Extended-Stay-Housing-2-Bldgs/24497524/', 
 'Hotel & Extended Stay/Housing 2 Bldgs', 'Dr. Mehdi Turabi', 'Mehdi Turabi', '', 'Beckley, WV', 0, 0), (99, 'https://www.loopnet.com/Listing/440-US-Highway-101-N-Crescent-City-CA/25273756/', '440 US Highway 101 N', '', 'Steve Song', '', 'Crescent City, CA', 0, 0), (108, 'https://www.loopnet.com/Listing/Quality-Inn-Super-8-Motel/25371264/', 'Quality Inn & Super 8 Motel', '', 'Dave Thompson', '', 'Harrisburg, IL', 0, 0), (209, 'https://www.loopnet.com/Listing/Miami-Miami-Beach-Triple-Net-leased-Ho/26254303/', 'Miami & Miami Beach Triple-Net leased Ho', '', 'Susan Gale', '', 'Miami Beach, FL', 0, 0), (231, 'https://www.loopnet.com/Listing/Boutique-Hotel-Portfolio-Palm-Springs/26419422/', 'Boutique Hotel Portfolio - Palm Springs', '', 'Harry Pflueger', '', 'Palm Springs, CA', 0, 0), (334, 'https://www.loopnet.com/Listing/Beach-Street-Rockport-Captains-Bounty/26874809/', "Beach Street Rockport - Captain's Bounty", '', 'Kevin Olson', '', 'Rockport, MA', 0, 0), (357, 'https://www.loopnet.com/Listing/Two-Property-Upscale-Marriott-Portfolio/26942045/', 'Two-Property Upscale Marriott Portfolio', '', 'Chris Gomes', '', 'Woodlands, TX', 0, 0), (372, 'https://www.loopnet.com/Listing/North-Dakota-3-Hotel-Portfolio/27031484/', 'North Dakota 3 Hotel Portfolio', 'Ray Starner', 'Gregg Marzano', '', 'Minot, ND', 0, 0), (392, 'https://www.loopnet.com/Listing/Motel-6-Studio-6-Hybrid/27113124/', 'Motel 6/Studio 6 Hybrid', '', 'Faiz Rajwani', '', 'Temple, TX', 0, 0), (399, 'https://www.loopnet.com/Listing/358-Relax-Dr-Smithville-TN/27141471/', '358 Relax Dr', '', 'Matt Messier', '', 'Smithville, TN', 0, 0), (435, 'https://www.loopnet.com/Listing/Two-Property-Portfolio-Wichita-KS/27283754/', '', '', 'Chris Gomes', '', '', 0, 0), (437, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-MI/27283512/', 'Two-Property Marriott Portfolio - MI', 'Ebrahim Valliani', 'Michael Klar', '', 'Lansing, MI', 0, 0), (438, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-IL/27283330/', 'Two-Property Marriott Portfolio - IL', 'Ebrahim Valliani', 'Michael Klar', '', 'Champaign, IL', 0, 0)]  




import sqlite3 

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

cur.execute('select * from property where name ="" ')#or owner like "POWER BROKER%";')
l= [(12, 'https://www.loopnet.com/Listing/Cavalier-Henrosa-Hotels/17411823/', 'Cavalier & Henrosa Hotels', '', 'Susan Gale', '', 'Miami Beach, FL', 0, 0), (56, 'https://www.loopnet.com/Listing/Hotel-Extended-Stay-Housing-2-Bldgs/24497524/', 'Hotel & Extended Stay/Housing 2 Bldgs', 'Dr. Mehdi Turabi', 'Mehdi Turabi', '', 'Beckley, WV', 0, 0), (99, 'https://www.loopnet.com/Listing/440-US-Highway-101-N-Crescent-City-CA/25273756/', '440 US Highway 101 N', '', 'Steve Song', '', 'Crescent City, CA', 0, 0), (108, 'https://www.loopnet.com/Listing/Quality-Inn-Super-8-Motel/25371264/', 'Quality Inn & Super 8 Motel', '', 'Dave Thompson', '', 'Harrisburg, IL', 0, 0), (209, 'https://www.loopnet.com/Listing/Miami-Miami-Beach-Triple-Net-leased-Ho/26254303/', 'Miami & Miami Beach Triple-Net leased Ho', '', 'Susan Gale', '', 'Miami Beach, FL', 0, 0), (231, 'https://www.loopnet.com/Listing/Boutique-Hotel-Portfolio-Palm-Springs/26419422/', 'Boutique Hotel Portfolio - Palm Springs', '', 'Harry Pflueger', '', 'Palm Springs, CA', 0, 0), (334, 'https://www.loopnet.com/Listing/Beach-Street-Rockport-Captains-Bounty/26874809/', "Beach Street Rockport - Captain's Bounty", '', 'Kevin Olson', '', 'Rockport, MA', 0, 0), (357, 'https://www.loopnet.com/Listing/Two-Property-Upscale-Marriott-Portfolio/26942045/', 'Two-Property Upscale Marriott Portfolio', '', 'Chris Gomes', '', 'Woodlands, TX', 0, 0), (372, 'https://www.loopnet.com/Listing/North-Dakota-3-Hotel-Portfolio/27031484/', 'North Dakota 3 Hotel Portfolio', 'Ray Starner', 'Gregg Marzano', '', 'Minot, ND', 0, 0), (392, 'https://www.loopnet.com/Listing/Motel-6-Studio-6-Hybrid/27113124/', 'Motel 6/Studio 6 Hybrid', '', 'Faiz Rajwani', '', 'Temple, TX', 0, 0), (399, 'https://www.loopnet.com/Listing/358-Relax-Dr-Smithville-TN/27141471/', '358 Relax Dr', '', 'Matt Messier', '', 'Smithville, TN', 0, 0), (435, 'https://www.loopnet.com/Listing/Two-Property-Portfolio-Wichita-KS/27283754/', '', '', 'Chris Gomes', '', '', 0, 0), (437, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-MI/27283512/', 'Two-Property Marriott Portfolio - MI', 'Ebrahim Valliani', 'Michael Klar', '', 'Lansing, MI', 0, 0), (438, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-IL/27283330/', 'Two-Property Marriott Portfolio - IL', 'Ebrahim Valliani', 'Michael Klar', '', 'Champaign, IL', 0, 0)] 
t = list()
for c in l:
    t.append(c[0])
    # print(c[1])
    # name = input("name:")
    # city = input("city:")
    cur.execute(f'update property set name="{c[2]}"  where id={c[0]}')
    cur.execute(f"update property set city='{c[6]}' where id={c[0]}")
# cur.execute("delete from property where id=435")
# con.commit()
cur.execute(f'select * from property where id in {str(tuple(t))} ')#or owner like "POWER BROKER%";')
print(cur.fetchall())


[(12, 'https://www.loopnet.com/Listing/Cavalier-Henrosa-Hotels/17411823/', 
'Cavalier & Henrosa Hotels', '', 'Susan Gale', '', 'Miami Beach, FL',
 0, 0), (56, 'https://www.loopnet.com/Listing/Hotel-Extended-Stay-Housing-2-Bldgs/24497524/', 
 'Hotel & Extended Stay/Housing 2 Bldgs', 'Dr. Mehdi Turabi', 'Mehdi Turabi', '', 'Beckley, WV', 0, 0), (99, 'https://www.loopnet.com/Listing/440-US-Highway-101-N-Crescent-City-CA/25273756/', '440 US Highway 101 N', '', 'Steve Song', '', 'Crescent City, CA', 0, 0), (108, 'https://www.loopnet.com/Listing/Quality-Inn-Super-8-Motel/25371264/', 'Quality Inn & Super 8 Motel', '', 'Dave Thompson', '', 'Harrisburg, IL', 0, 0), (209, 'https://www.loopnet.com/Listing/Miami-Miami-Beach-Triple-Net-leased-Ho/26254303/', 'Miami & Miami Beach Triple-Net leased Ho', '', 'Susan Gale', '', 'Miami Beach, FL', 0, 0), (231, 'https://www.loopnet.com/Listing/Boutique-Hotel-Portfolio-Palm-Springs/26419422/', 'Boutique Hotel Portfolio - Palm Springs', '', 'Harry Pflueger', '', 'Palm Springs, CA', 0, 0), (334, 'https://www.loopnet.com/Listing/Beach-Street-Rockport-Captains-Bounty/26874809/', "Beach Street Rockport - Captain's Bounty", '', 'Kevin Olson', '', 'Rockport, MA', 0, 0), (357, 'https://www.loopnet.com/Listing/Two-Property-Upscale-Marriott-Portfolio/26942045/', 'Two-Property Upscale Marriott Portfolio', '', 'Chris Gomes', '', 'Woodlands, TX', 0, 0), (372, 'https://www.loopnet.com/Listing/North-Dakota-3-Hotel-Portfolio/27031484/', 'North Dakota 3 Hotel Portfolio', 'Ray Starner', 'Gregg Marzano', '', 'Minot, ND', 0, 0), (392, 'https://www.loopnet.com/Listing/Motel-6-Studio-6-Hybrid/27113124/', 'Motel 6/Studio 6 Hybrid', '', 'Faiz Rajwani', '', 'Temple, TX', 0, 0), (399, 'https://www.loopnet.com/Listing/358-Relax-Dr-Smithville-TN/27141471/', '358 Relax Dr', '', 'Matt Messier', '', 'Smithville, TN', 0, 0), (435, 'https://www.loopnet.com/Listing/Two-Property-Portfolio-Wichita-KS/27283754/', '', '', 'Chris Gomes', '', '', 0, 0), (437, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-MI/27283512/', 'Two-Property Marriott Portfolio - MI', 'Ebrahim Valliani', 'Michael Klar', '', 'Lansing, MI', 0, 0), (438, 'https://www.loopnet.com/Listing/Two-Property-Marriott-Portfolio-IL/27283330/', 'Two-Property Marriott Portfolio - IL', 'Ebrahim Valliani', 'Michael Klar', '', 'Champaign, IL', 0, 0)]  

"""