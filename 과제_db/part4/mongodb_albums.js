use json_test;

db.getCollection("csvjson(mongodb)").renameCollection("albums")

db.albums.find({}, {앨범: 1, 연도: 1})

db.albums.find({연도: '2000'})

// 최고 순위가 문자열로 되있어서 $lte 사용이 안됨
db.albums.find({최고순위: {$lte: 10}})

// 최고순위에 "-" 이 있어야 해서 숫자열로 변경할수가 없
db.albums.find({최고순위: '-'})

db.albums.aggregate([{$group: {_id: "$연도", count: {$sum: 1}}}])

db.albums.find().sort({연도: -1}).limit(1)

db.albums.find().sort({연도: 1}).limit(1)

// 최고 순위가 문자열로 되있어서 $gte 사용이 안됨
db.albums.find({최고순위: {$gte: 10}})

db.albums.find({앨범: /White/})

db.albums.find({연도: {$gte: '2000', $lte: '2005'}})

//CRUD 연습 문제
db.albums.insert({앨범: 'New Album', 연도: '2024', 최고순위: '1'})

db.albums.update({앨범: 'New Album'}, {$set: {최고순위: '2'}})

db.albums.remove({앨범: 'New Album'})