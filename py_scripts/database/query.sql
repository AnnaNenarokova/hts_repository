select count (*)
from blasthit
inner join sequence as query on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Saccharomyces cerevisiae' and subject.organism = 'Euglena gracilis'
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
    and query.loc = 'Mito';

select count (*)
from blasthit
inner join sequence as query on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Homo sapiens' and subject.organism = 'Tripanosoma brucei';

select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Tripanosoma brucei'
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id) as count_table;

select query.function, subject.organism, subject.function, subject.mitoscore from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis'
    and (subject.organism = 'Tripanosoma brucei' or subject.organism = 'Homo sapiens' or (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100))
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
group by query.id;

Tripanosoma brucei
Saccharomyces cerevisiae
Homo sapiens
Euglena gracilis