select

D.Date,

D.Insomnia,

FI.Amount,

sum(FI.Amount * SIGHI_Classification) as SIGHI,

case when M.Name = 'Aerius' or M.Name = 'Xyzall' then 1 else 0 end  as H1_Blocker,

	sum(CI.Strength) as Cond,

	min(B.Sys) as Sys,

	max(P.Pulse) as Pulse





	from inputs_diary D

	left join inputs_food_inst FI on FI.Date_id = D.id

	left join inputs_food F on FI.Food_id = F.id

	left join inputs_medication_inst MI on MI.Date_id = D.id

	left join inputs_medication M on MI.Medication_id = M.id

	left join inputs_condition_inst CI on CI.Date_id = D.id

	left join inputs_condition C on CI.Condition_id = C.id

	left join inputs_blood_pressure_inst B on B.Date_id = D.id

	left join inputs_pulse_inst P on P.Date_id = D.id



	group by D.Date

	order by D.Date


