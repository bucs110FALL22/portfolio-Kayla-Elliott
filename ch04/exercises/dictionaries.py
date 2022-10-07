article = "The Tampa Bay Buccaneers entered the 2022 N.F.L. season among the shortlist of contenders to win the N.F.C. The Jacksonville Jaguars, on the other hand, entered the year as perennial A.F.C. doormats still recovering from the brief coaching tenure of Urban Meyer, who managed the team in 2021 the way a bored child manages a pile of plastic soldiers.The Jaguars are currently outperforming the Buccaneers. Both teams are 2-1, but the Jaguars have outscored their opponents by 46 points, while the Buccaneers have outscored theirs by just 24. The Jaguars’ offense, led by the second-year quarterback Trevor Lawrence, has outscored the Tom Brady-led Buccaneer offense 84 to 51.The Buccaneers are not the only traditional N.F.C. favorites off to a sluggish start, nor are the Jaguars the A.F.C.’s only surprise. Those teams are just examples of the wide disparity in quality between the N.F.L.’s conferences right now. In college football terms, the A.F.C. looks like the Big Ten Conference or the Southeastern Conference, while the N.F.C. looks more like the Tumbleweed Valley Affiliation.Signs of the gap between the two N.F.L. conferences can be found everywhere. A.F.C. teams occupy six of the top eight spots in net point differential — the measure of points scored against points allowed — including first place (Buffalo Bills +53) and second (Jaguars +46)"



dictionary = {
  "Tampa Bay Buccaneers":"Old Pirates",
  "collage football":"Broke teen",
  "N.F.L.":"couch potato",
  "Jacksonville Jaguars":"Big Cats"
}

for key, value in dictionary.items():
  article = article.replace(key, value)

print(article)


# control c can get you out of a loop