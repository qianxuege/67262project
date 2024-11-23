from common import *

us='''
* Simple US: Show the bug or feature associated with a comment

   As a:  Developer
 I want:  To see the details of a bug/feature associated with a comment
So That:  I can better understand the issue
'''

print(us)

def show_comment_bug_feature( cid ):

    cols = 'c.cid c.date c.comment i.iid i.initial_date i.product i.status i.priority tag'

    tmpl =  f'''
SELECT c.cid, c.date, c.comment, i.iid, i.initial_date, i.product, i.status, i.priority,
       case when f.fid is NULL then 'bug' else 'feature' end as tag
  FROM Comments as c
       LEFT JOIN Bugs as b ON c.iid = b.bid
       LEFT JOIN Features as f on c.iid = f.fid
       JOIN Issues as i on c.iid = i.iid
 WHERE c.cid = %s
'''
    cmd = cur.mogrify(tmpl, (cid,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    pp(rows)
    show_table( rows, cols) 

show_comment_bug_feature( 5 )
