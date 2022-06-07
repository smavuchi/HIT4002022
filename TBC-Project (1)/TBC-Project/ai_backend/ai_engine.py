#!/usr/bin/python

from firebase_init import *
from threading import Thread
from ml import *
from time import sleep
from os import remove as rm

JOB_DATABASE_REF = "OrderQueue/QueuedTasks"
JOB_STORAGE_REF = "ProcessedOrders/{}"
JOB_THREAD_POOL = {}
GRADES = {0:"XL", 1:"XF", 2:"CL", 3:"CF", 4:"BL", 5:"BF", 6:"BR"}

def process_job(thread_id):
	try:
		keys = thread_id.split(":")

		print("* JOB:{} :: JOB DEPLOYED".format(thread_id))
		storage_ref = storage.child(JOB_STORAGE_REF.format(keys[0])).child(keys[1]).download("/tmp/{}".format(thread_id))

		print("+ JOB:{} :: PROCESSING".format(thread_id))
		predictions = infer_img("/tmp/{}".format(thread_id))

		print("+ JOB:{} :: CLEAN UP".format(thread_id))
		rm("/tmp/{}".format(thread_id))

		not_graded = True
		for i in range(7):
			if predictions[i] >= 0.90:
				not_graded = False
				price_peg = database.child("settings").child(GRADES[i]).get().val()
				pending_order = database.child("PendingOrders").child(keys[0]).child(keys[1]).get().val()

				quantity = pending_order['quantity']
				pending_order.update({"status":"Processed"})
				pending_order.update({"grade":GRADES[i]})
				pending_order.update({"quantity":quantity * price_peg})

				database.child("ProcessedOrders").child(keys[0]).child(keys[1]).set(pending_order)
				database.child("PendingOrders").child(keys[0]).child(keys[1]).remove()
				database.child(JOB_DATABASE_REF).child(thread_id).remove()

				print("+ JOB:{} :: {}:GRADE MATCH".format(thread_id, GRADES[i]))
			else:
				print("+ JOB:{} :: {}:NO MATCH".format(thread_id, GRADES[i]))

		if not_graded:
				pending_order = database.child("PendingOrders").child(keys[0]).child(keys[1]).get().val()

				pending_order.update({"status":"Rejected"})
				pending_order.update({"grade":"REJECT"})
				pending_order.update({"quantity":0})

				database.child("RejectedOrders").child(keys[0]).child(keys[1]).set(pending_order)
				database.child("PendingOrders").child(keys[0]).child(keys[1]).remove()
				database.child(JOB_DATABASE_REF).child(thread_id).remove()

				print("+ JOB:{} :: REJECTED".format(thread_id))


	except Exception as e:
		print("! JOB:{} :: JOB CRASHED".format(thread_id))
		print(e)

def run_engine():

	try:
		job_clusters = database.child(JOB_DATABASE_REF).get().val()

		if job_clusters:
			print("[+] AI ENGINE ::: RUNNING")
			for id in job_clusters:
				if id not in JOB_THREAD_POOL:

					JOB_THREAD_POOL.update({id:None})
					JOB_THREAD_POOL[id] = Thread(target=process_job, args=(id,))
					JOB_THREAD_POOL[id].start()

	except Exception as e:
		print(e)


print("[+] AI ENGINE ::: STARTED")
while True:
	run_engine()
