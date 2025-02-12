-- PAY
-- Drop existing Pay views
DROP VIEW IF EXISTS new_schema.pay_to_view;
DROP VIEW IF EXISTS new_schema.pay_from_view;

-- Recreate pay_to_view
CREATE OR REPLACE VIEW new_schema.pay_to_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type = 'Payee';

-- Recreate pay_from_view
CREATE OR REPLACE VIEW new_schema.pay_from_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type = 'Payor';

-- REFUND
-- Drop existing REFUND views
DROP VIEW IF EXISTS new_schema.refund_from_view;
DROP VIEW IF EXISTS new_schema.refund_to_view;

-- Recreate refund_from_view
CREATE OR REPLACE VIEW new_schema.refund_from_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type = 'Payee';

-- Recreate refund_to_view
CREATE OR REPLACE VIEW new_schema.refund_to_view AS
SELECT *
FROM new_schema.top_level_view
WHERE category = 'Payment Method';

-- DEPOSIT
-- Drop existing DEPOSIT views
DROP VIEW IF EXISTS new_schema.deposit_to_view;
DROP VIEW IF EXISTS new_schema.deposit_from_view;

-- Recreate deposit_to_view
CREATE OR REPLACE VIEW new_schema.deposit_to_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type = 'Asset' AND subtype <> 'Cash';

-- Recreate deposit_from_view
CREATE OR REPLACE VIEW new_schema.deposit_from_view AS
SELECT *
FROM new_schema.top_level_view
WHERE category = 'payor';

-- TRANSFER
-- Drop existing TRANSFER views
DROP VIEW IF EXISTS new_schema.transfer_to_view;
DROP VIEW IF EXISTS new_schema.transfer_from_view;

-- Recreate transfer_to_view
CREATE OR REPLACE VIEW new_schema.transfer_to_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type IN ('Asset', 'Liability') AND subtype <> 'Cash';

-- Recreate transfer_from_view
CREATE OR REPLACE VIEW new_schema.transfer_from_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type = 'Asset' AND subtype <> 'Cash';

-- WITHDRAW
-- Drop existing WITHDRAW views
DROP VIEW IF EXISTS new_schema.withdraw_from_view;
DROP VIEW IF EXISTS new_schema.withdraw_to_view;

-- Recreate withdraw_to_view
CREATE OR REPLACE VIEW new_schema.withdraw_to_view AS
SELECT *
FROM new_schema.top_level_view
WHERE subtype = 'Cash';

-- Recreate withdraw_from_view
CREATE OR REPLACE VIEW new_schema.withdraw_from_view AS
SELECT *
FROM new_schema.top_level_view
WHERE type = 'Asset' AND subtype <> 'Cash';