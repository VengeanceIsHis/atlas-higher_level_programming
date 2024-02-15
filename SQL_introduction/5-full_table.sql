-- Onliny showing the description of a table.
USE hbtn_0c_0;
SELECT COLOUMN_NAME, DATAT_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM first_table.COLUMNS
WHERE TABLE_NAME = first_table;