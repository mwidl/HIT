select
D.Date,
D.Insomnia,
FI.Amount,
F.SIGHI_Classification,
sum(FI.Amount * SIGHI_Classification) as Amount,
if M.Name='Aerius' then 1 else 0 end if

from inputs_diary D
left join inputs_food_inst FI on FI.Date_id = D.id
left join inputs_food F on FI.Food_id = F.id
left join inputs_medication_inst MI on MI.Date_id = D.id
left join inputs_medication M on MI.Medication_id = M.id

group by D.Date
order by D.Date








