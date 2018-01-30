# Generated by Django 2.0 on 2017-12-11 02:23

from django.db import migrations


def add_initial_data(apps, schema_editor):
    medication_klass = apps.get_model('api', 'Medication')
    dosage_klass = apps.get_model('api', 'Dosage')
    doctor_klass = apps.get_model('api', 'Doctor')
    article_klass = apps.get_model('api', 'Article')
    article_category_klass = apps.get_model('api', 'ArticleCategory')
    ordered_categorized_article_klass = apps.get_model('api', 'OrderedCategorizedArticle')

    api_medication_1 = medication_klass()
    api_medication_1.name = 'Coumadin'
    api_medication_1.generic_name = 'warfarin'
    api_medication_1.friendly_description = 'Warfarin, sold under the brand name Coumadin among others, ' \
                                            'is a medication that is used as an anticoagulant.'
    api_medication_1.function = 'Anticoagulant / Blood Thinner'
    api_medication_1.video_url = 'https://github.com/mediaelement/mediaelement-files/blob/master/big_buck_bunny.mp4' \
                                 '?raw=true'
    api_medication_1.save()

    api_medication_2 = medication_klass()
    api_medication_2.name = 'Chicken Soup'
    api_medication_2.generic_name = 'boulion'
    api_medication_2.friendly_description = 'Not just for eating, this powerful medicine is good for the body… and ' \
                                            'soul!'
    api_medication_2.function = 'Food / Sustenance'
    api_medication_2.video_url = 'https://github.com/mediaelement/mediaelement-files/blob/master/big_buck_bunny.mp4' \
                                 '?raw=true'
    api_medication_2.save()

    api_medication_3 = medication_klass()
    api_medication_3.name = 'Percocet'
    api_medication_3.generic_name = 'acetaminophen'
    api_medication_3.friendly_description = 'High risk for addiction and dependence. Can cause respiratory distress ' \
                                            'and death when taken in high doses or when combined with other ' \
                                            'substances, especially alcohol.'
    api_medication_3.function = 'Pain killer'
    api_medication_3.video_url = 'https://github.com/mediaelement/mediaelement-files/blob/master/big_buck_bunny.mp4' \
                                 '?raw=true'
    api_medication_3.save()

    # Processing model: doctorbox_web.api.models.Dosage


    api_dosage_1 = dosage_klass()
    api_dosage_1.name = '1 mg'
    api_dosage_1.medication = api_medication_1
    api_dosage_1.order = 0
    api_dosage_1.save()

    api_dosage_2 = dosage_klass()
    api_dosage_2.name = '3 mg'
    api_dosage_2.medication = api_medication_1
    api_dosage_2.order = 10
    api_dosage_2.save()

    api_dosage_3 = dosage_klass()
    api_dosage_3.name = '5 mg'
    api_dosage_3.medication = api_medication_1
    api_dosage_3.order = 20
    api_dosage_3.save()

    api_dosage_4 = dosage_klass()
    api_dosage_4.name = '7 mg'
    api_dosage_4.medication = api_medication_1
    api_dosage_4.order = 30
    api_dosage_4.save()

    api_dosage_5 = dosage_klass()
    api_dosage_5.name = '10 mg'
    api_dosage_5.medication = api_medication_1
    api_dosage_5.order = 40
    api_dosage_5.save()

    api_dosage_6 = dosage_klass()
    api_dosage_6.name = 'Teaspoon'
    api_dosage_6.medication = api_medication_2
    api_dosage_6.order = 0
    api_dosage_6.save()

    api_dosage_7 = dosage_klass()
    api_dosage_7.name = 'Cup'
    api_dosage_7.medication = api_medication_2
    api_dosage_7.order = 10
    api_dosage_7.save()

    api_dosage_8 = dosage_klass()
    api_dosage_8.name = 'Bowl'
    api_dosage_8.medication = api_medication_2
    api_dosage_8.order = 20
    api_dosage_8.save()

    api_dosage_9 = dosage_klass()
    api_dosage_9.name = 'Kettle'
    api_dosage_9.medication = api_medication_2
    api_dosage_9.order = 30
    api_dosage_9.save()

    api_dosage_10 = dosage_klass()
    api_dosage_10.name = 'Cauldron'
    api_dosage_10.medication = api_medication_2
    api_dosage_10.order = 40
    api_dosage_10.save()

    api_dosage_11 = dosage_klass()
    api_dosage_11.name = '1 mg'
    api_dosage_11.medication = api_medication_3
    api_dosage_11.order = 0
    api_dosage_11.save()

    api_dosage_12 = dosage_klass()
    api_dosage_12.name = '5 mg'
    api_dosage_12.medication = api_medication_3
    api_dosage_12.order = 10
    api_dosage_12.save()

    api_dosage_13 = dosage_klass()
    api_dosage_13.name = '10 mg'
    api_dosage_13.medication = api_medication_3
    api_dosage_13.order = 20
    api_dosage_13.save()

    # Processing model: doctorbox_web.api.models.Doctor


    api_doctor_1 = doctor_klass()
    api_doctor_1.name = 'James R. Adams, M.D., FACC, ASFD'
    api_doctor_1.save()

    api_doctor_2 = doctor_klass()
    api_doctor_2.name = 'Margaret L. Baer, M.D., FACC'
    api_doctor_2.save()

    api_doctor_3 = doctor_klass()
    api_doctor_3.name = 'Adam Baumgarten, M.D., FACC'
    api_doctor_3.save()

    api_doctor_4 = doctor_klass()
    api_doctor_4.name = 'Sujoya Dey, M.D., FACC'
    api_doctor_4.save()

    api_doctor_5 = doctor_klass()
    api_doctor_5.name = 'Kent N. Gershengorn, MD, FACC'
    api_doctor_5.save()

    api_doctor_6 = doctor_klass()
    api_doctor_6.name = 'Ann K. Kao, MD, FACC'
    api_doctor_6.save()

    api_doctor_7 = doctor_klass()
    api_doctor_7.name = 'Brian G. Keeffe, MD, FACC'
    api_doctor_7.save()

    api_doctor_8 = doctor_klass()
    api_doctor_8.name = 'Laura K. Pak, MD, FACS'
    api_doctor_8.save()

    api_doctor_9 = doctor_klass()
    api_doctor_9.name = 'Arun K. Raghupathy, MD, FACC'
    api_doctor_9.save()

    api_doctor_10 = doctor_klass()
    api_doctor_10.name = 'Joel Sklar, M.D., FACC'
    api_doctor_10.save()

    # Processing model: doctorbox_web.api.models.Article

    api_article_1 = article_klass()
    api_article_1.title = 'What is a heart attack?'
    api_article_1.body = "Is my heart really a muscle?\r\n\r\n        The heart is the human body's hardest working " \
                         "organ- a muscle pump. Throughout life it continuously pumps blood enriched with oxygen and " \
                         "vital nutrients through a network of arteries to all tissues of the body - to all of your " \
                         "cells. The heart is a powerful pump as you can imagine, but it’s also a muscle " \
                         "itself.\r\n\r\n        Since it’s a muscle, it needs its own supply of oxygen and nutrients " \
                         "– so it can keep working. It gets its supply from what are called “coronary arteries” that " \
                         "lie on the surface of the heart and branch into smaller vessels to get to the rest of the " \
                         "heart.\r\n\r\n        How did your Coronary Arteries get damaged?\r\n\r\n        Over the " \
                         "years, often starting early in life, plaque - which is the accumulation of fat, " \
                         "cholesterol, and other substances - builds up on the inner walls of arteries. This causes " \
                         "the arteries to become thick and stiff (instead of being flexible and elastic). This slow " \
                         "process is called atherosclerosis.\r\n\r\n        As plaque builds up in the coronary " \
                         "arteries which supply blood to the heart, it narrows them, reducing the oxygen-rich blood " \
                         "flow to the heart. This is called coronary heart disease or coronary artery disease. The " \
                         "plaque can severely reduce or stop the flow of blood to the heart, without which the heart " \
                         "can’t function, causing it to start to die -  this is a heart attack. Plaque can also break " \
                         "open, causing blood to clump together (as a clot), which can also block blood flow to the " \
                         "heart, resulting in a heart attack.\r\n\r\n        PS: You may hear people call a “heart " \
                         "attack” by other names - Myocardial Infarction (MI) or Acute MI. They may also say it is an " \
                         "Acute Coronary Syndrome (ACS), or Coronary Thrombosis – they are just different terms to " \
                         "describe the same event.\r\n\r\n        Why is Heart Disease Not Fair?\r\n\r\n        -    " \
                         "It has a Gender Bias. Men are more at risk for a heart attack, but a woman’s risk increases " \
                         "after menopause\r\n\r\n        -    It Cares About our Race. People of African, Mexican, " \
                         "Native Americans, Polynesian, and Asian (including south Asian) descent have a higher risk " \
                         "of heart disease.\r\n\r\n        -    It Runs in the Family. Heart disease is hereditary " \
                         "and you’re at a higher risk if your parents had it.\r\n\r\n        -    Whatever you do, " \
                         "don’t Stress about it. Stress can add to your risk of heart disease. Studies have found a " \
                         "link between stress and heart disease.\r\n\r\n        Interested in Reading More?\r\n\r\n   " \
                         "     To understand a heart attack, you may be asking yourself -”How did I get to this”, " \
                         "or “Was I that sick without knowing it”?"
    api_article_1.author = 'Dr. Evan Therber M.D., P.T.'
    api_article_1.time_to_read = 5
    api_article_1.save()

    api_article_2 = article_klass()
    api_article_2.title = 'What are the typical symptoms?'
    api_article_2.body = 'What are the typical symptoms?'
    api_article_2.author = 'Dr. Foo Bar M.D.'
    api_article_2.time_to_read = 3
    api_article_2.save()

    api_article_3 = article_klass()
    api_article_3.title = 'What happens when the paramedics or EMTs arrive?'
    api_article_3.body = 'What happens when the paramedics or EMTs arrive?'
    api_article_3.author = 'Dr. Dana Doctorson M.D.'
    api_article_3.time_to_read = 2
    api_article_3.save()

    api_article_4 = article_klass()
    api_article_4.title = 'What happens when you first get to the hospital?'
    api_article_4.body = 'What happens when you first get to the hospital?'
    api_article_4.author = 'Dr. Evan Therber M.D., P.T.'
    api_article_4.time_to_read = 10
    api_article_4.save()

    api_article_5 = article_klass()
    api_article_5.title = 'How is a heart attack diagnosed?'
    api_article_5.body = 'How is a heart attack diagnosed?'
    api_article_5.author = 'Dr. Evan Therber M.D., P.T.'
    api_article_5.time_to_read = 5
    api_article_5.save()

    api_article_6 = article_klass()
    api_article_6.title = 'What procedures are used to treat a heart attack?'
    api_article_6.body = 'What procedures are used to treat a heart attack?'
    api_article_6.author = 'Dr. Evan Therber M.D., P.T.'
    api_article_6.time_to_read = 50
    api_article_6.save()

    # Processing model: doctorbox_web.api.models.ArticleCategory

    api_articlecategory_1 = article_category_klass()
    api_articlecategory_1.title = 'Activities'
    api_articlecategory_1.image_url = 'https://www.example.com/activity_category_image.png'
    api_articlecategory_1.order = 0
    api_articlecategory_1.save()

    # Processing model: doctorbox_web.api.models.OrderedCategorizedArticle

    api_orderedcategorizedarticle_1 = ordered_categorized_article_klass()
    api_orderedcategorizedarticle_1.article = api_article_1
    api_orderedcategorizedarticle_1.category = api_articlecategory_1
    api_orderedcategorizedarticle_1.order = 0
    api_orderedcategorizedarticle_1.save()

    api_orderedcategorizedarticle_2 = ordered_categorized_article_klass()
    api_orderedcategorizedarticle_2.article = api_article_2
    api_orderedcategorizedarticle_2.category = api_articlecategory_1
    api_orderedcategorizedarticle_2.order = 10
    api_orderedcategorizedarticle_2.save()

    api_orderedcategorizedarticle_3 = ordered_categorized_article_klass()
    api_orderedcategorizedarticle_3.article = api_article_3
    api_orderedcategorizedarticle_3.category = api_articlecategory_1
    api_orderedcategorizedarticle_3.order = 20
    api_orderedcategorizedarticle_3.save()

    api_orderedcategorizedarticle_4 = ordered_categorized_article_klass()
    api_orderedcategorizedarticle_4.article = api_article_4
    api_orderedcategorizedarticle_4.category = api_articlecategory_1
    api_orderedcategorizedarticle_4.order = 30
    api_orderedcategorizedarticle_4.save()

    api_orderedcategorizedarticle_5 = ordered_categorized_article_klass()
    api_orderedcategorizedarticle_5.article = api_article_5
    api_orderedcategorizedarticle_5.category = api_articlecategory_1
    api_orderedcategorizedarticle_5.order = 40
    api_orderedcategorizedarticle_5.save()

    api_orderedcategorizedarticle_6 = ordered_categorized_article_klass()
    api_orderedcategorizedarticle_6.article = api_article_6
    api_orderedcategorizedarticle_6.category = api_articlecategory_1
    api_orderedcategorizedarticle_6.order = 50
    api_orderedcategorizedarticle_6.save()


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20171211_0133'),
    ]

    operations = [
        migrations.RunPython(add_initial_data)
    ]
