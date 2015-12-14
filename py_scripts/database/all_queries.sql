select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

579

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

463

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Homo sapiens'
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

404

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens')
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

830

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

858

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

703

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

1050

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3 and query.loc = 'M'
group by query.id) as count_table;

227

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3 and query.mitoscore = 100
group by query.id) as count_table;

27

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3 and query.mitoscore = 100 and query.loc = 'M'
group by query.id) as count_table;

4

select count(*) from sequence where organism = 'Euglena gracilis' and loc='M' and mitoscore=100;

96

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3 and query.mitoscore = 100 and query.loc = 'M' and query.locrate <=2
group by query.id) as count_table;

2

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3 and query.mitoscore = 100 and query.locrate <=2
group by query.id) as count_table;

8

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3 and query.loc = 'M' and query.locrate <=2
group by query.id) as count_table;

59

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
    and query.mitoscore = 100
group by query.id) as count_table;

19

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
    and query.mitoscore = 100
group by query.id) as count_table;

13

select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Homo sapiens'
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
    and query.mitoscore = 100
group by query.id) as count_table;

19


select count(*) from sequence where organism = 'Euglena gracilis' and loc='M' and locrate <= 2;
1616




Tripanosoma brucei
Saccharomyces cerevisiae
Homo sapiens
Euglena gracilis