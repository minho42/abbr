import multiprocessing

# this is added to prevent django-rq error:
"""
06:52:42 default: abbr.views.save_wiki_summary('CPAP', 'Continuous positive airway pressure') (b062d972-d417-4977-98c4-62aa3eca9f30)
objc[98787]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called.
objc[98787]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
06:52:42 Moving job to FailedJobRegistry (Work-horse terminated unexpectedly; waitpid returned 6 (signal 6); )
"""
multiprocessing.set_start_method("spawn")
