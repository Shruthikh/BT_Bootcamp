-- =========================================
-- HeartiHealth PostgreSQL Schema
-- =========================================

BEGIN;

-- Drop tables safely (for re-runs)
DROP TABLE IF EXISTS xray CASCADE;
DROP TABLE IF EXISTS wearabledevicedata CASCADE;
DROP TABLE IF EXISTS symptom CASCADE;
DROP TABLE IF EXISTS ecgreport CASCADE;
DROP TABLE IF EXISTS diseasedetail CASCADE;
DROP TABLE IF EXISTS bloodtest CASCADE;
DROP TABLE IF EXISTS cardiodiagnosis CASCADE;
DROP TABLE IF EXISTS addressinfo CASCADE;
DROP TABLE IF EXISTS memberinfo CASCADE;

DROP TABLE IF EXISTS
    bloodtest,
    ecgreport,
    symptom,
    wearabledevicedata,
    xray,
    diseasedetail,
    cardiodiagnosis
CASCADE;


-- -----------------------------------------
-- MEMBER INFO
-- -----------------------------------------
CREATE TABLE memberinfo (
    member_id VARCHAR(45) PRIMARY KEY,
    username VARCHAR(45),
    firstname VARCHAR(45),
    lastname VARCHAR(45),
    age INTEGER,
    gender VARCHAR(5),          -- '1' = Male, '0' = Female
    email VARCHAR(100),
    phonenumber BIGINT
);

-- -----------------------------------------
-- ADDRESS INFO
-- -----------------------------------------
CREATE TABLE addressinfo (
    address_id VARCHAR(45),
    city VARCHAR(45),
    state VARCHAR(45),
    country VARCHAR(45),
    pincode VARCHAR(20),
    memberinfo_member_id VARCHAR(45),
    PRIMARY KEY (address_id, memberinfo_member_id),
    FOREIGN KEY (memberinfo_member_id)
        REFERENCES memberinfo(member_id)
);

-- -----------------------------------------
-- CARDIO DIAGNOSIS
-- -----------------------------------------
CREATE TABLE cardiodiagnosis (
    cardio_id VARCHAR(45),
    cardioarrestdetected INTEGER,
    date TIMESTAMP,
    memberinfo_member_id VARCHAR(45),
    PRIMARY KEY (cardio_id, memberinfo_member_id),
    UNIQUE (cardio_id),     -- ✅ FIX ADDED
    FOREIGN KEY (memberinfo_member_id)
        REFERENCES memberinfo(member_id)
);


-- -----------------------------------------
-- BLOOD TEST
-- -----------------------------------------
CREATE TABLE bloodtest (
    blood_id VARCHAR(45),
    date TIMESTAMP,
    bloodpressure INTEGER,
    fbs INTEGER,
    thal INTEGER,
    serumcholesterol INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (blood_id, cardiodiagnosis_cardio_id),
    FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);




-- -----------------------------------------
-- ECG REPORT
-- -----------------------------------------
CREATE TABLE ecgreport (
    ecg_id VARCHAR(45),
    date TIMESTAMP,
    restecg INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (ecg_id, cardiodiagnosis_cardio_id),
    FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

-- -----------------------------------------
-- SYMPTOM
-- -----------------------------------------
CREATE TABLE symptom (
    symptom_id VARCHAR(45),
    date TIMESTAMP,
    exang INTEGER,
    oldpeak FLOAT,
    cp INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (symptom_id, cardiodiagnosis_cardio_id),
    FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

-- -----------------------------------------
-- WEARABLE DEVICE DATA
-- -----------------------------------------
CREATE TABLE wearabledevicedata (
    wearable_device_id VARCHAR(45),
    thalach INTEGER,
    slope INTEGER,
    date TIMESTAMP,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (wearable_device_id, cardiodiagnosis_cardio_id),
    FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

-- -----------------------------------------
-- XRAY
-- -----------------------------------------
CREATE TABLE xray (
    xray_id VARCHAR(45),
    date TIMESTAMP,
    ca INTEGER,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (xray_id, cardiodiagnosis_cardio_id),
    FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

-- -----------------------------------------
-- DISEASE DETAIL
-- -----------------------------------------
CREATE TABLE diseasedetail (
    disease_id VARCHAR(45),
    diagnoseddate TIMESTAMP,
    recovereddate TIMESTAMP,
    isrecovered BOOLEAN,
    cardiodiagnosis_cardio_id VARCHAR(45),
    PRIMARY KEY (disease_id, cardiodiagnosis_cardio_id),
    FOREIGN KEY (cardiodiagnosis_cardio_id)
        REFERENCES cardiodiagnosis(cardio_id)
);

ALTER TABLE diseasedetail
ADD COLUMN disease_name VARCHAR(100);

COMMIT;
