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

Tripanosoma brucei
Saccharomyces cerevisiae
Homo sapiens
Euglena gracilis