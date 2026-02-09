/*UPDATE gym_members_raw SET gender = LOWER(TRIM(gender));
ALTER TABLE gym_members_raw ADD COLUMN hours_in_gym_per_week REAL;
UPDATE gym_members_raw SET hours_in_gym_per_week = visit_per_week * avg_time_in_gym / 60;
CREATE TABLE gym_members_cleaned AS SELECT * FROM gym_members_raw;*/
ALTER TABLE gym_members_cleaned ADD COLUMN activity_level TEXT;

UPDATE gym_members_cleaned
SET activity_level = CASE
    WHEN visit_per_week <= 2 THEN 'Low'
    WHEN visit_per_week <= 4 THEN 'Medium'
    ELSE 'High'
END;