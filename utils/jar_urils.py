# utils/java_utils.py
import jpype
import jpype.imports
from jpype.types import *

def start_jvm(jar_path, jvm_path=None):
    """Start the JVM with the specified JAR file."""
    if not jpype.isJVMStarted():
        jpype.startJVM(jvm_path, "-ea", f"-Djava.class.path={jar_path}")

def stop_jvm():
    """Shutdown the JVM."""
    if jpype.isJVMStarted():
        jpype.shutdownJVM()

def call_java_method(class_name, method_name, *args):
    """Call a method from a Java class."""
    JavaClass = jpype.JClass(class_name)
    result = getattr(JavaClass, method_name)(*args)
    return result