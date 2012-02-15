ATSDown = int

ATSNone = int

ATSUNSPECIFIED = int

ATSUp = int

class AdaptiveLru:
  def __init__(self):
    pass
  def assign(self):
    pass
  def beginEpoch(self):
    pass
  def clearName(self):
    pass
  def considerEvict(self):
    pass
  def countActiveSize(self):
    pass
  def evictTo(self):
    pass
  def getClassType():
    pass
  def getMaxSize(self):
    pass
  def getMaxUpdatesPerFrame(self):
    pass
  def getName(self):
    pass
  def getTotalSize(self):
    pass
  def getWeight(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def setMaxSize(self):
    pass
  def setMaxUpdatesPerFrame(self):
    pass
  def setName(self):
    pass
  def setWeight(self):
    pass
  def validate(self):
    pass
  def write(self):
    pass
class AdaptiveLruPage:
  def __init__(self):
    pass
  def assign(self):
    pass
  def dequeueLru(self):
    pass
  def downcastToIndexBufferContext(self):
    pass
  def downcastToTextureContext(self):
    pass
  def downcastToVertexBufferContext(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def getNumFrames(self):
    pass
  def getNumInactiveFrames(self):
    pass
  def markUsedLru(self):
    pass
  def output(self):
    pass
  def setLruSize(self):
    pass
  def write(self):
    pass
class AlphaTestAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getReferenceAlpha(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class AmbientLight:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def asNode(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setColor(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToLight(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPandaNode(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class AnalogNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearOutput(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getControlState(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumControls(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOutput(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isControlKnown(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOutputFlipped(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOutput(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class AnimBundle:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def copyBundle(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBaseFrameRate(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getNumFrames(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimBundleNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findAnimBundle():
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getBundle(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class AnimChannelACMatrixSwitchType:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getHpr(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getPos(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getShear(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def getValueNoScaleShear(self):
    pass
  def getValueType(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimChannelACScalarSwitchType:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getHpr(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getPos(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getShear(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValueType(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimChannelBase:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimChannelMatrixDynamic:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getHpr(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getPos(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getShear(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def getValueNoScaleShear(self):
    pass
  def getValueNode(self):
    pass
  def getValueTransform(self):
    pass
  def getValueType(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def setValue(self):
    pass
  def setValueNode(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimChannelMatrixXfmTable:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearAllTables(self):
    pass
  def clearName(self):
    pass
  def clearTable(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getHpr(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getPos(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getShear(self):
    pass
  def getTable(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def getValueNoScaleShear(self):
    pass
  def getValueType(self):
    pass
  def hasName(self):
    pass
  def hasTable(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isValidId():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def setTable(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimChannelScalarDynamic:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getHpr(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getPos(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getShear(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValueType(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def setValue(self):
    pass
  def setValueNode(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimChannelScalarTable:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def clearTable(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getHpr(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getPos(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getShear(self):
    pass
  def getTable(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValueType(self):
    pass
  def hasName(self):
    pass
  def hasTable(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def setTable(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimControl:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAnim(self):
    pass
  def getAnimModel(self):
    pass
  def getBoundJoints(self):
    pass
  def getChannelIndex(self):
    pass
  def getClassType():
    pass
  def getFrac(self):
    pass
  def getFrame(self):
    pass
  def getFrameRate(self):
    pass
  def getFullFframe(self):
    pass
  def getFullFrame(self):
    pass
  def getName(self):
    pass
  def getNextFrame(self):
    pass
  def getNumFrames(self):
    pass
  def getPart(self):
    pass
  def getPendingDoneEvent(self):
    pass
  def getPlayRate(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasAnim(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isPending(self):
    pass
  def isPlaying(self):
    pass
  def loop(self):
    pass
  def output(self):
    pass
  def pingpong(self):
    pass
  def play(self):
    pass
  def pose(self):
    pass
  def ref(self):
    pass
  def setAnimModel(self):
    pass
  def setName(self):
    pass
  def setPendingDoneEvent(self):
    pass
  def setPlayRate(self):
    pass
  def stop(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToAnimInterface(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def waitPending(self):
    pass
class AnimControlCollection:
  def __init__(self):
    pass
  def clearAnims(self):
    pass
  def findAnim(self):
    pass
  def getAnim(self):
    pass
  def getAnimName(self):
    pass
  def getAnimNames(self):
    pass
  def getAnims(self):
    pass
  def getFrame(self):
    pass
  def getNumAnims(self):
    pass
  def getNumFrames(self):
    pass
  def isPlaying(self):
    pass
  def loop(self):
    pass
  def loopAll(self):
    pass
  def output(self):
    pass
  def play(self):
    pass
  def playAll(self):
    pass
  def pose(self):
    pass
  def poseAll(self):
    pass
  def stop(self):
    pass
  def stopAll(self):
    pass
  def storeAnim(self):
    pass
  def unbindAnim(self):
    pass
  def whichAnimPlaying(self):
    pass
  def write(self):
    pass
class AnimGroup:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class AnimInterface:
  def __init__(self):
    pass
  def getClassType():
    pass
  def getFrac(self):
    pass
  def getFrame(self):
    pass
  def getFrameRate(self):
    pass
  def getFullFframe(self):
    pass
  def getFullFrame(self):
    pass
  def getNextFrame(self):
    pass
  def getNumFrames(self):
    pass
  def getPlayRate(self):
    pass
  def isPlaying(self):
    pass
  def loop(self):
    pass
  def output(self):
    pass
  def pingpong(self):
    pass
  def play(self):
    pass
  def pose(self):
    pass
  def setPlayRate(self):
    pass
  def stop(self):
    pass
class AnimPreloadTable:
  def __init__(self):
    pass
  def addAnim(self):
    pass
  def addAnimsFrom(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearAnims(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findAnim(self):
    pass
  def getBamModified(self):
    pass
  def getBaseFrameRate(self):
    pass
  def getBasename(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getNumAnims(self):
    pass
  def getNumFrames(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeAnim(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class AnimateVerticesRequest:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isReady(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class AntialiasAttrib:
  def __init__(self):
    pass
  MAlways = int

  MAuto = int

  MBetter = int

  MConstant = int

  MDontCare = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MFaster = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MLine = int

  MMultisample = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPoint = int

  MPointSprite = int

  MPolygon = int

  MTypeMask = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getModeQuality(self):
    pass
  def getModeType(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class AsyncTask:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class AsyncTaskChain:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getActiveTasks(self):
    pass
  def getClassType():
    pass
  def getFrameBudget(self):
    pass
  def getFrameSync(self):
    pass
  def getName(self):
    pass
  def getNextWakeTime(self):
    pass
  def getNumRunningThreads(self):
    pass
  def getNumTasks(self):
    pass
  def getNumThreads(self):
    pass
  def getRefCount(self):
    pass
  def getSleepingTasks(self):
    pass
  def getTasks(self):
    pass
  def getThreadPriority(self):
    pass
  def getTickClock(self):
    pass
  def getTimeslicePriority(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def hasTask(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isStarted(self):
    pass
  def output(self):
    pass
  def poll(self):
    pass
  def ref(self):
    pass
  def setFrameBudget(self):
    pass
  def setFrameSync(self):
    pass
  def setName(self):
    pass
  def setNumThreads(self):
    pass
  def setThreadPriority(self):
    pass
  def setTickClock(self):
    pass
  def setTimeslicePriority(self):
    pass
  def startThreads(self):
    pass
  def stopThreads(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def waitForTasks(self):
    pass
  def write(self):
    pass
class AsyncTaskCollection:
  def __init__(self):
    pass
  def addTask(self):
    pass
  def addTasksFrom(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def findTask(self):
    pass
  def getNumTasks(self):
    pass
  def getTask(self):
    pass
  def getTasks(self):
    pass
  def hasTask(self):
    pass
  def output(self):
    pass
  def removeDuplicateTasks(self):
    pass
  def removeTask(self):
    pass
  def removeTasksFrom(self):
    pass
  def size(self):
    pass
  def write(self):
    pass
class AsyncTaskManager:
  def __init__(self):
    pass
  def add(self):
    pass
  def assign(self):
    pass
  def cleanup(self):
    pass
  def clearName(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def findTask(self):
    pass
  def findTaskChain(self):
    pass
  def findTasks(self):
    pass
  def findTasksMatching(self):
    pass
  def getActiveTasks(self):
    pass
  def getClassType():
    pass
  def getClock(self):
    pass
  def getGlobalPtr():
    pass
  def getName(self):
    pass
  def getNextWakeTime(self):
    pass
  def getNumTaskChains(self):
    pass
  def getNumTasks(self):
    pass
  def getRefCount(self):
    pass
  def getSleepingTasks(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskChains(self):
    pass
  def getTasks(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def hasTask(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeTaskChain(self):
    pass
  def output(self):
    pass
  def poll(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def removeTaskChain(self):
    pass
  def setClock(self):
    pass
  def setName(self):
    pass
  def startThreads(self):
    pass
  def stopThreads(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def waitForTasks(self):
    pass
  def write(self):
    pass
class AsyncTaskPause:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class AsyncTaskSequence:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def addTask(self):
    pass
  def addTasksFrom(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def findTask(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getCurrentTaskIndex(self):
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getNumTasks(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getRepeatCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTask(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getTasks(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def hasTask(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def removeDuplicateTasks(self):
    pass
  def removeTask(self):
    pass
  def removeTasksFrom(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setRepeatCount(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def size(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToAsyncTask(self):
    pass
  def upcastToAsyncTaskCollection(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def write(self):
    pass
class AttribNodeRegistry:
  def __init__(self):
    pass
  def addNode(self):
    pass
  def clear(self):
    pass
  def findNode(self):
    pass
  def getGlobalPtr():
    pass
  def getNode(self):
    pass
  def getNodeName(self):
    pass
  def getNodeType(self):
    pass
  def getNodes(self):
    pass
  def getNumNodes(self):
    pass
  def lookupNode(self):
    pass
  def output(self):
    pass
  def removeNode(self):
    pass
  def write(self):
    pass
class AudioManager:
  def __init__(self):
    pass
  SMHeuristic = int

  SMSample = int

  SMStream = int

  SPEAKERMODE5point1 = int

  SPEAKERMODE7point1 = int

  SPEAKERMODECOUNT = int

  SPEAKERMODEMax = int

  SPEAKERMODEMono = int

  SPEAKERMODEPrologic = int

  SPEAKERMODEQuad = int

  SPEAKERMODERaw = int

  SPEAKERMODEStereo = int

  SPEAKERMODESurround = int

  SPKBackleft = int

  SPKBackright = int

  SPKCOUNT = int

  SPKCenter = int

  SPKFrontleft = int

  SPKFrontright = int

  SPKNone = int

  SPKSideleft = int

  SPKSideright = int

  SPKSub = int

  def audio3dGetDistanceFactor(self):
    pass
  def audio3dGetDopplerFactor(self):
    pass
  def audio3dGetDropOffFactor(self):
    pass
  def audio3dSetDistanceFactor(self):
    pass
  def audio3dSetDopplerFactor(self):
    pass
  def audio3dSetDropOffFactor(self):
    pass
  def audio3dSetListenerAttributes(self):
    pass
  def clearCache(self):
    pass
  def configureFilters(self):
    pass
  def createAudioManager():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getActive(self):
    pass
  def getCacheLimit(self):
    pass
  def getClassType():
    pass
  def getConcurrentSoundLimit(self):
    pass
  def getDlsPathname():
    pass
  def getNullSound(self):
    pass
  def getRefCount(self):
    pass
  def getSound(self):
    pass
  def getSpeakerSetup(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVolume(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def reduceSoundsPlayingTo(self):
    pass
  def ref(self):
    pass
  def setActive(self):
    pass
  def setCacheLimit(self):
    pass
  def setConcurrentSoundLimit(self):
    pass
  def setSpeakerConfiguration(self):
    pass
  def setSpeakerSetup(self):
    pass
  def setVolume(self):
    pass
  def shutdown(self):
    pass
  def stopAllSounds(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncacheSound(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def update(self):
    pass
  def write(self):
    pass
class AudioSound:
  def __init__(self):
    pass
  BAD = int

  PLAYING = int

  READY = int

  def configureFilters(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def get3dMaxDistance(self):
    pass
  def get3dMinDistance(self):
    pass
  def getActive(self):
    pass
  def getBalance(self):
    pass
  def getClassType():
    pass
  def getFinishedEvent(self):
    pass
  def getLoop(self):
    pass
  def getLoopCount(self):
    pass
  def getName(self):
    pass
  def getPlayRate(self):
    pass
  def getPriority(self):
    pass
  def getRefCount(self):
    pass
  def getSpeakerLevel(self):
    pass
  def getSpeakerMix(self):
    pass
  def getTime(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVolume(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def length(self):
    pass
  def output(self):
    pass
  def play(self):
    pass
  def ref(self):
    pass
  def set3dAttributes(self):
    pass
  def set3dMaxDistance(self):
    pass
  def set3dMinDistance(self):
    pass
  def setActive(self):
    pass
  def setBalance(self):
    pass
  def setFinishedEvent(self):
    pass
  def setLoop(self):
    pass
  def setLoopCount(self):
    pass
  def setPlayRate(self):
    pass
  def setPriority(self):
    pass
  def setSpeakerLevels(self):
    pass
  def setSpeakerMix(self):
    pass
  def setTime(self):
    pass
  def setVolume(self):
    pass
  def status(self):
    pass
  def stop(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
class AudioVolumeAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def getVolume(self):
    pass
  def hasVolume(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isOff(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeIdentity():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setVolume(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class AutonomousLerp:
  def __init__(self):
    pass
  def assign(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEndEvent(self):
    pass
  def getFunctor(self):
    pass
  def getRefCount(self):
    pass
  def getT(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isDone(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def resume(self):
    pass
  def setEndEvent(self):
    pass
  def setT(self):
    pass
  def start(self):
    pass
  def stop(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class AuxBitplaneAttrib:
  def __init__(self):
    pass
  ABOAuxGlow = int

  ABOAuxNormal = int

  ABOGlow = int

  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getOutputs(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class AuxSceneData:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getDuration(self):
    pass
  def getExpirationTime(self):
    pass
  def getLastRenderTime(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setDuration(self):
    pass
  def setLastRenderTime(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
class BamCache:
  def __init__(self):
    pass
  def considerFlushIndex(self):
    pass
  def flushIndex(self):
    pass
  def getActive(self):
    pass
  def getCacheCompressedTextures(self):
    pass
  def getCacheMaxKbytes(self):
    pass
  def getCacheModels(self):
    pass
  def getCacheTextures(self):
    pass
  def getFlushTime(self):
    pass
  def getGlobalPtr():
    pass
  def getReadOnly(self):
    pass
  def getRoot(self):
    pass
  def lookup(self):
    pass
  def setActive(self):
    pass
  def setCacheCompressedTextures(self):
    pass
  def setCacheMaxKbytes(self):
    pass
  def setCacheModels(self):
    pass
  def setCacheTextures(self):
    pass
  def setFlushTime(self):
    pass
  def setReadOnly(self):
    pass
  def setRoot(self):
    pass
  def store(self):
    pass
class BamCacheRecord:
  def __init__(self):
    pass
  def addDependentFile(self):
    pass
  def clearData(self):
    pass
  def clearDependentFiles(self):
    pass
  def decodeFromBamStream():
    pass
  def dependentsUnchanged(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def eq(self):
    pass
  def getBamModified(self):
    pass
  def getCacheFilename(self):
    pass
  def getClassType():
    pass
  def getData(self):
    pass
  def getDependentPathname(self):
    pass
  def getNumDependentFiles(self):
    pass
  def getRecordedTime(self):
    pass
  def getRefCount(self):
    pass
  def getSourcePathname(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasData(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setData(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class BamEnums:
  def __init__(self):
    pass
  BEBigendian = int

  BELittleendian = int

  BENative = int

  BOCAdjunct = int

  BOCPop = int

  BOCPush = int

  BOCRemove = int

  BTMBasename = int

  BTMFullpath = int

  BTMRawdata = int

  BTMRelative = int

  BTMUnchanged = int

class BamFile:
  def __init__(self):
    pass
  BEBigendian = int

  BELittleendian = int

  BENative = int

  BOCAdjunct = int

  BOCPop = int

  BOCPush = int

  BOCRemove = int

  BTMBasename = int

  BTMFullpath = int

  BTMRawdata = int

  BTMRelative = int

  BTMUnchanged = int

  def close(self):
    pass
  def getCurrentMajorVer(self):
    pass
  def getCurrentMinorVer(self):
    pass
  def getFileEndian(self):
    pass
  def getFileMajorVer(self):
    pass
  def getFileMinorVer(self):
    pass
  def getReader(self):
    pass
  def getWriter(self):
    pass
  def isEof(self):
    pass
  def isValidRead(self):
    pass
  def isValidWrite(self):
    pass
  def openRead(self):
    pass
  def openWrite(self):
    pass
  def readNode(self):
    pass
  def readObject(self):
    pass
  def resolve(self):
    pass
  def writeObject(self):
    pass
class BamReader:
  def __init__(self):
    pass
  BEBigendian = int

  BELittleendian = int

  BENative = int

  BOCAdjunct = int

  BOCPop = int

  BOCPush = int

  BOCRemove = int

  BTMBasename = int

  BTMFullpath = int

  BTMRawdata = int

  BTMRelative = int

  BTMUnchanged = int

  def changePointer(self):
    pass
  def getCurrentMajorVer(self):
    pass
  def getCurrentMinorVer(self):
    pass
  def getFileEndian(self):
    pass
  def getFileMajorVer(self):
    pass
  def getFileMinorVer(self):
    pass
  def getFilename(self):
    pass
  def getLoaderOptions(self):
    pass
  def init(self):
    pass
  def isEof(self):
    pass
  def readObject(self):
    pass
  def resolve(self):
    pass
  def setLoaderOptions(self):
    pass
class BamWriter:
  def __init__(self):
    pass
  BEBigendian = int

  BELittleendian = int

  BENative = int

  BOCAdjunct = int

  BOCPop = int

  BOCPush = int

  BOCRemove = int

  BTMBasename = int

  BTMFullpath = int

  BTMRawdata = int

  BTMRelative = int

  BTMUnchanged = int

  def flush(self):
    pass
  def getFileEndian(self):
    pass
  def getFileTextureMode(self):
    pass
  def getFilename(self):
    pass
  def hasObject(self):
    pass
  def init(self):
    pass
  def setFileTextureMode(self):
    pass
  def writeObject(self):
    pass
class BillboardEffect:
  def __init__(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getAxialRotate(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getEyeRelative(self):
    pass
  def getLookAt(self):
    pass
  def getLookAtPoint(self):
    pass
  def getNumEffects():
    pass
  def getOffset(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUpVector(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isOff(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def makeAxis():
    pass
  def makePointEye():
    pass
  def makePointWorld():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class BindAnimRequest:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getFilename(self):
    pass
  def getLoader(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getModel(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getOptions(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isReady(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class BitArray:
  def __init__(self):
    pass
  def allOff():
    pass
  def allOn():
    pass
  def assign(self):
    pass
  def bit():
    pass
  def clear(self):
    pass
  def clearBit(self):
    pass
  def clearRange(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def extract(self):
    pass
  def getBit(self):
    pass
  def getClassType():
    pass
  def getHighestBits(self):
    pass
  def getHighestOffBit(self):
    pass
  def getHighestOnBit(self):
    pass
  def getLowestOffBit(self):
    pass
  def getLowestOnBit(self):
    pass
  def getMaxNumBits():
    pass
  def getNextHigherDifferentBit(self):
    pass
  def getNumBits(self):
    pass
  def getNumBitsPerWord():
    pass
  def getNumOffBits(self):
    pass
  def getNumOnBits(self):
    pass
  def getNumWords(self):
    pass
  def getWord(self):
    pass
  def hasAllOf(self):
    pass
  def hasAnyOf(self):
    pass
  def hasBitsInCommon(self):
    pass
  def hasMaxNumBits():
    pass
  def invertInPlace(self):
    pass
  def isAllOn(self):
    pass
  def isZero(self):
    pass
  def lessThan(self):
    pass
  def lowerOn():
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def outputBinary(self):
    pass
  def outputHex(self):
    pass
  def range():
    pass
  def setBit(self):
    pass
  def setBitTo(self):
    pass
  def setRange(self):
    pass
  def setRangeTo(self):
    pass
  def setWord(self):
    pass
  def store(self):
    pass
  def write(self):
    pass
class BitMaskUnsignedInt32:
  def __init__(self):
    pass
  def allOff():
    pass
  def allOn():
    pass
  def assign(self):
    pass
  def bit():
    pass
  def clear(self):
    pass
  def clearBit(self):
    pass
  def clearRange(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def extract(self):
    pass
  def floodBitsDown(self):
    pass
  def floodBitsUp(self):
    pass
  def floodDownInPlace(self):
    pass
  def floodUpInPlace(self):
    pass
  def getBit(self):
    pass
  def getClassType():
    pass
  def getHighestOffBit(self):
    pass
  def getHighestOnBit(self):
    pass
  def getKey(self):
    pass
  def getLowestOffBit(self):
    pass
  def getLowestOnBit(self):
    pass
  def getMaxNumBits():
    pass
  def getNextHigherDifferentBit(self):
    pass
  def getNumBits():
    pass
  def getNumOffBits(self):
    pass
  def getNumOnBits(self):
    pass
  def getWord(self):
    pass
  def hasAllOf(self):
    pass
  def hasAnyOf(self):
    pass
  def hasBitsInCommon(self):
    pass
  def hasMaxNumBits():
    pass
  def invertInPlace(self):
    pass
  def isAllOn(self):
    pass
  def isZero(self):
    pass
  def keepNextHighestBit(self):
    pass
  def keepNextLowestBit(self):
    pass
  def lessThan(self):
    pass
  def lowerOn():
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def outputBinary(self):
    pass
  def outputHex(self):
    pass
  def range():
    pass
  def setBit(self):
    pass
  def setBitTo(self):
    pass
  def setRange(self):
    pass
  def setRangeTo(self):
    pass
  def setWord(self):
    pass
  def store(self):
    pass
  def write(self):
    pass
class BitMaskUnsignedInt6464:
  def __init__(self):
    pass
  def allOff():
    pass
  def allOn():
    pass
  def assign(self):
    pass
  def bit():
    pass
  def clear(self):
    pass
  def clearBit(self):
    pass
  def clearRange(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def extract(self):
    pass
  def floodBitsDown(self):
    pass
  def floodBitsUp(self):
    pass
  def floodDownInPlace(self):
    pass
  def floodUpInPlace(self):
    pass
  def getBit(self):
    pass
  def getClassType():
    pass
  def getHighestOffBit(self):
    pass
  def getHighestOnBit(self):
    pass
  def getKey(self):
    pass
  def getLowestOffBit(self):
    pass
  def getLowestOnBit(self):
    pass
  def getMaxNumBits():
    pass
  def getNextHigherDifferentBit(self):
    pass
  def getNumBits():
    pass
  def getNumOffBits(self):
    pass
  def getNumOnBits(self):
    pass
  def getWord(self):
    pass
  def hasAllOf(self):
    pass
  def hasAnyOf(self):
    pass
  def hasBitsInCommon(self):
    pass
  def hasMaxNumBits():
    pass
  def invertInPlace(self):
    pass
  def isAllOn(self):
    pass
  def isZero(self):
    pass
  def keepNextHighestBit(self):
    pass
  def keepNextLowestBit(self):
    pass
  def lessThan(self):
    pass
  def lowerOn():
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def outputBinary(self):
    pass
  def outputHex(self):
    pass
  def range():
    pass
  def setBit(self):
    pass
  def setBitTo(self):
    pass
  def setRange(self):
    pass
  def setRangeTo(self):
    pass
  def setWord(self):
    pass
  def store(self):
    pass
  def write(self):
    pass
class BoundingBox:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getMax(self):
    pass
  def getMin(self):
    pass
  def getNumPlanes(self):
    pass
  def getNumPoints(self):
    pass
  def getPlane(self):
    pass
  def getPlanes(self):
    pass
  def getPoint(self):
    pass
  def getPoints(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVolume(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class BoundingHexahedron:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getMax(self):
    pass
  def getMin(self):
    pass
  def getNumPlanes(self):
    pass
  def getNumPoints(self):
    pass
  def getPlane(self):
    pass
  def getPlanes(self):
    pass
  def getPoint(self):
    pass
  def getPoints(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVolume(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class BoundingLine:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getPointA(self):
    pass
  def getPointB(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class BoundingPlane:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getPlane(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class BoundingSphere:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getMax(self):
    pass
  def getMin(self):
    pass
  def getRadius(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVolume(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class BoundingVolume:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
class BufferContext:
  def __init__(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToIndexBufferContext(self):
    pass
  def downcastToTextureContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToVertexBufferContext(self):
    pass
  def getActive(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getModified(self):
    pass
  def getResident(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def upcastToSavedContext(self):
    pass
class BufferedDatagramConnection:
  def __init__(self):
    pass
  def Active(self):
    pass
  def ActiveOpen(self):
    pass
  def ActiveOpenNonBlocking(self):
    pass
  def AddAddress(self):
    pass
  def AddressQueueSize(self):
    pass
  def ClearAddresses(self):
    pass
  def Close(self):
    pass
  def DoConnect(self):
    pass
  def DontLinger(self):
    pass
  def ErrorIsWouldBlocking(self):
    pass
  def Flush(self):
    pass
  def GetLastError():
    pass
  def GetMessage(self):
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def IsConnected(self):
    pass
  def RecvData(self):
    pass
  def Reset(self):
    pass
  def SendData(self):
    pass
  def SendMessage(self):
    pass
  def SetBlocking(self):
    pass
  def SetLinger(self):
    pass
  def SetNoDelay(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSendBufferSize(self):
    pass
  def SetSocket(self):
    pass
  def ShutdownSend(self):
    pass
  def WaitForNetworkReadEvent(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class ButtonHandle:
  def __init__(self):
    pass
  def getAlias(self):
    pass
  def getAsciiEquivalent(self):
    pass
  def getClassType():
    pass
  def getIndex(self):
    pass
  def getName(self):
    pass
  def hasAsciiEquivalent(self):
    pass
  def matches(self):
    pass
  def none():
    pass
  def output(self):
    pass
class ButtonNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getButtonMap(self):
    pass
  def getButtonState(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumButtons(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isButtonKnown(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setButtonMap(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class ButtonRegistry:
  def __init__(self):
    pass
  def findAsciiButton(self):
    pass
  def getButton(self):
    pass
  def ptr():
    pass
  def write(self):
    pass
class ButtonThrower:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addParameter(self):
    pass
  def addStashed(self):
    pass
  def addThrowButton(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearThrowButtons(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getButtonDownEvent(self):
    pass
  def getButtonRepeatEvent(self):
    pass
  def getButtonUpEvent(self):
    pass
  def getCandidateEvent(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getModifierButtons(self):
    pass
  def getMoveEvent(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParameters(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParameter(self):
    pass
  def getParameters(self):
    pass
  def getParent(self):
    pass
  def getPrefix(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getSpecificFlag(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getThrowButtonsActive(self):
    pass
  def getTimeFlag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hasThrowButton(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def removeThrowButton(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setButtonDownEvent(self):
    pass
  def setButtonRepeatEvent(self):
    pass
  def setButtonUpEvent(self):
    pass
  def setCandidateEvent(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setKeystrokeEvent(self):
    pass
  def setModifierButtons(self):
    pass
  def setMoveEvent(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrefix(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSpecificFlag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setThrowButtonsActive(self):
    pass
  def setTimeFlag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
CSDefault = int

CSInvalid = int

CSYupLeft = int

CSYupRight = int

CSZupLeft = int

CSZupRight = int

class BasicStringChar:
  def __init__(self):
    pass
class CachedTypedWritableReferenceCount:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class CallbackData:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def upcall(self):
    pass
class CallbackNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearCullCallback(self):
    pass
  def clearDrawCallback(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCullCallback(self):
    pass
  def getDrawCallback(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCullCallback(self):
    pass
  def setDrawCallback(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CallbackObject:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class Camera:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def activateLens(self):
    pass
  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def cleanupAuxSceneData(self):
    pass
  def clearAttrib(self):
    pass
  def clearAuxSceneData(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTagState(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copyLens(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def deactivateLens(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getAuxSceneData(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCameraMask(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCullCenter(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInitialState(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLens(self):
    pass
  def getLensActive(self):
    pass
  def getLodCenter(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTagState(self):
    pass
  def getTagStateKey(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTagState(self):
    pass
  def hasTags(self):
    pass
  def hideFrustum(self):
    pass
  def isActive(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isInView(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listAuxSceneData(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setAuxSceneData(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCameraMask(self):
    pass
  def setCullCenter(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setInitialState(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLens(self):
    pass
  def setLensActive(self):
    pass
  def setLodCenter(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setScene(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTagState(self):
    pass
  def setTagStateKey(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showFrustum(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CardMaker:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def clearSourceGeometry(self):
    pass
  def generate(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def reset(self):
    pass
  def setColor(self):
    pass
  def setFrame(self):
    pass
  def setFrameFullscreenQuad(self):
    pass
  def setHas3dUvs(self):
    pass
  def setHasNormals(self):
    pass
  def setHasUvs(self):
    pass
  def setName(self):
    pass
  def setSourceGeometry(self):
    pass
  def setUvRange(self):
    pass
  def setUvRangeCube(self):
    pass
class Character:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearLodAnimation(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findJoint(self):
    pass
  def findParent(self):
    pass
  def findSlider(self):
    pass
  def findStashed(self):
    pass
  def forceUpdate(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getBundle(self):
    pass
  def getBundleHandle(self):
    pass
  def getBundleHandles(self):
    pass
  def getBundles(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumBundles(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def mergeBundles(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLodAnimation(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def update(self):
    pass
  def updateToNow(self):
    pass
  def write(self):
    pass
  def writePartValues(self):
    pass
  def writeParts(self):
    pass
class CharacterJoint:
  def __init__(self):
    pass
  def addLocalTransform(self):
    pass
  def addNetTransform(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearLocalTransforms(self):
    pass
  def clearName(self):
    pass
  def clearNetTransforms(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getCharacter(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getDefaultValue(self):
    pass
  def getForcedChannel(self):
    pass
  def getLocalTransforms(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNetTransform(self):
    pass
  def getNetTransforms(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def hasLocalTransform(self):
    pass
  def hasName(self):
    pass
  def hasNetTransform(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def removeLocalTransform(self):
    pass
  def removeNetTransform(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class CharacterJointBundle:
  def __init__(self):
    pass
  BTComponentwise = int

  BTComponentwiseQuat = int

  BTLinear = int

  BTNormalizedLinear = int

  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def applyTransform(self):
    pass
  def assign(self):
    pass
  def bindAnim(self):
    pass
  def clearAnimPreload(self):
    pass
  def clearControlEffects(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def controlJoint(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def forceUpdate(self):
    pass
  def freezeJoint(self):
    pass
  def getAnimBlendFlag(self):
    pass
  def getAnimPreload(self):
    pass
  def getBamModified(self):
    pass
  def getBlendType(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getControlEffect(self):
    pass
  def getForcedChannel(self):
    pass
  def getFrameBlendFlag(self):
    pass
  def getName(self):
    pass
  def getNode(self):
    pass
  def getNodes(self):
    pass
  def getNumChildren(self):
    pass
  def getNumNodes(self):
    pass
  def getRefCount(self):
    pass
  def getRootXform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def loadBindAnim(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def mergeAnimPreloads(self):
    pass
  def modifyAnimPreload(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def releaseJoint(self):
    pass
  def setAnimBlendFlag(self):
    pass
  def setAnimPreload(self):
    pass
  def setBlendType(self):
    pass
  def setControlEffect(self):
    pass
  def setFrameBlendFlag(self):
    pass
  def setName(self):
    pass
  def setRootXform(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def update(self):
    pass
  def waitPending(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
  def xform(self):
    pass
class CharacterJointEffect:
  def __init__(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCharacter(self):
    pass
  def getClassType():
    pass
  def getNumEffects():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class CharacterSlider:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getDefaultValue(self):
    pass
  def getForcedChannel(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def updateInternals(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class CharacterVertexSlider:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCharSlider(self):
    pass
  def getClassType():
    pass
  def getModified(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSlider(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class ClientBase:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def forkAsynchronousThread(self):
    pass
  def getClassType():
    pass
  def getCoordinateSystem(self):
    pass
  def getLastPollTime(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isForked(self):
    pass
  def isOfType(self):
    pass
  def poll(self):
    pass
  def ref(self):
    pass
  def setCoordinateSystem(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class ClipPlaneAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  OAdd = int

  ORemove = int

  OSet = int

  def addOffPlane(self):
    pass
  def addOnPlane(self):
    pass
  def addPlane(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def filterToMax(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getNumOffPlanes(self):
    pass
  def getNumOnPlanes(self):
    pass
  def getNumPlanes(self):
    pass
  def getOffPlane(self):
    pass
  def getOffPlanes(self):
    pass
  def getOnPlane(self):
    pass
  def getOnPlanes(self):
    pass
  def getOperation(self):
    pass
  def getPlane(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasAllOff(self):
    pass
  def hasOffPlane(self):
    pass
  def hasOnPlane(self):
    pass
  def hasPlane(self):
    pass
  def isExactType(self):
    pass
  def isIdentity(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeAllOff():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeOffPlane(self):
    pass
  def removeOnPlane(self):
    pass
  def removePlane(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class ClockObject:
  def __init__(self):
    pass
  MDegrade = int

  MForced = int

  MInteger = int

  MIntegerLimited = int

  MLimited = int

  MNonRealTime = int

  MNormal = int

  MSlave = int

  def calcFrameRateDeviation(self):
    pass
  def checkErrors(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageFrameRate(self):
    pass
  def getAverageFrameRateInterval(self):
    pass
  def getClassType():
    pass
  def getDegradeFactor(self):
    pass
  def getDt(self):
    pass
  def getFrameCount(self):
    pass
  def getFrameTime(self):
    pass
  def getGlobalClock():
    pass
  def getLongTime(self):
    pass
  def getMaxDt(self):
    pass
  def getMaxFrameDuration(self):
    pass
  def getMode(self):
    pass
  def getNetFrameRate(self):
    pass
  def getRealTime(self):
    pass
  def getRefCount(self):
    pass
  def ref(self):
    pass
  def reset(self):
    pass
  def setAverageFrameRateInterval(self):
    pass
  def setDegradeFactor(self):
    pass
  def setDt(self):
    pass
  def setFrameCount(self):
    pass
  def setFrameRate(self):
    pass
  def setFrameTime(self):
    pass
  def setMaxDt(self):
    pass
  def setMode(self):
    pass
  def setRealTime(self):
    pass
  def syncFrameTime(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def tick(self):
    pass
  def unref(self):
    pass
class CollisionBox:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getNumPlanes(self):
    pass
  def getNumPoints(self):
    pass
  def getPlane(self):
    pass
  def getPoint(self):
    pass
  def getPointAabb(self):
    pass
  def getRadius(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setCenter(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setPlane(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionDSSolid:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def distToPlaneA(self):
    pass
  def distToPlaneB(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getCenterA(self):
    pass
  def getCenterB(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getNormalA(self):
    pass
  def getNormalB(self):
    pass
  def getPlaneA(self):
    pass
  def getPlaneB(self):
    pass
  def getRadiusA(self):
    pass
  def getRadiusB(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setCenterA(self):
    pass
  def setCenterB(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setPlaneA(self):
    pass
  def setPlaneB(self):
    pass
  def setRadiusA(self):
    pass
  def setRadiusB(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionEntry:
  def __init__(self):
    pass
  def collided(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getAll(self):
    pass
  def getAllContactInfo(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getContactNormal(self):
    pass
  def getContactPos(self):
    pass
  def getFrom(self):
    pass
  def getFromNode(self):
    pass
  def getFromNodePath(self):
    pass
  def getInteriorPoint(self):
    pass
  def getInto(self):
    pass
  def getIntoNode(self):
    pass
  def getIntoNodePath(self):
    pass
  def getRefCount(self):
    pass
  def getRespectPrevTransform(self):
    pass
  def getSurfaceNormal(self):
    pass
  def getSurfacePoint(self):
    pass
  def getT(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasContactNormal(self):
    pass
  def hasContactPos(self):
    pass
  def hasInteriorPoint(self):
    pass
  def hasInto(self):
    pass
  def hasSurfaceNormal(self):
    pass
  def hasSurfacePoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def resetCollided(self):
    pass
  def setContactNormal(self):
    pass
  def setContactPos(self):
    pass
  def setInteriorPoint(self):
    pass
  def setSurfaceNormal(self):
    pass
  def setSurfacePoint(self):
    pass
  def setT(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionFloorMesh:
  def __init__(self):
    pass
  def addTriangle(self):
    pass
  def addVertex(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getNumTriangles(self):
    pass
  def getNumVertices(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getTriangle(self):
    pass
  def getTriangles(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionHandler:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerEvent:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getClassType():
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def setAgainPattern(self):
    pass
  def setInPattern(self):
    pass
  def setOutPattern(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerFloor:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addCollider(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearCenter(self):
    pass
  def clearColliders(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getMaxVelocity(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOffset(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getReach(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasCenter(self):
    pass
  def hasCollider(self):
    pass
  def hasContact(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def removeCollider(self):
    pass
  def setAgainPattern(self):
    pass
  def setCenter(self):
    pass
  def setInPattern(self):
    pass
  def setMaxVelocity(self):
    pass
  def setOffset(self):
    pass
  def setOutPattern(self):
    pass
  def setReach(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerFluidPusher:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addCollider(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearCenter(self):
    pass
  def clearColliders(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getHorizontal(self):
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasCenter(self):
    pass
  def hasCollider(self):
    pass
  def hasContact(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def removeCollider(self):
    pass
  def setAgainPattern(self):
    pass
  def setCenter(self):
    pass
  def setHorizontal(self):
    pass
  def setInPattern(self):
    pass
  def setOutPattern(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerGravity:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addCollider(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def addVelocity(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearCenter(self):
    pass
  def clearColliders(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getAirborneHeight(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getContactNormal(self):
    pass
  def getGravity(self):
    pass
  def getImpactVelocity(self):
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getLegacyMode(self):
    pass
  def getMaxVelocity(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOffset(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getReach(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVelocity(self):
    pass
  def hasCenter(self):
    pass
  def hasCollider(self):
    pass
  def hasContact(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isOnGround(self):
    pass
  def ref(self):
    pass
  def removeCollider(self):
    pass
  def setAgainPattern(self):
    pass
  def setCenter(self):
    pass
  def setGravity(self):
    pass
  def setInPattern(self):
    pass
  def setLegacyMode(self):
    pass
  def setMaxVelocity(self):
    pass
  def setOffset(self):
    pass
  def setOutPattern(self):
    pass
  def setReach(self):
    pass
  def setVelocity(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerHighestEvent:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getClassType():
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def setAgainPattern(self):
    pass
  def setInPattern(self):
    pass
  def setOutPattern(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerPhysical:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addCollider(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearCenter(self):
    pass
  def clearColliders(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasCenter(self):
    pass
  def hasCollider(self):
    pass
  def hasContact(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def removeCollider(self):
    pass
  def setAgainPattern(self):
    pass
  def setCenter(self):
    pass
  def setInPattern(self):
    pass
  def setOutPattern(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerPusher:
  def __init__(self):
    pass
  def addAgainPattern(self):
    pass
  def addCollider(self):
    pass
  def addInPattern(self):
    pass
  def addOutPattern(self):
    pass
  def clear(self):
    pass
  def clearAgainPatterns(self):
    pass
  def clearCenter(self):
    pass
  def clearColliders(self):
    pass
  def clearInPatterns(self):
    pass
  def clearOutPatterns(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAgainPattern(self):
    pass
  def getAgainPatterns(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getHorizontal(self):
    pass
  def getInPattern(self):
    pass
  def getInPatterns(self):
    pass
  def getNumAgainPatterns(self):
    pass
  def getNumInPatterns(self):
    pass
  def getNumOutPatterns(self):
    pass
  def getOutPattern(self):
    pass
  def getOutPatterns(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasCenter(self):
    pass
  def hasCollider(self):
    pass
  def hasContact(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def removeCollider(self):
    pass
  def setAgainPattern(self):
    pass
  def setCenter(self):
    pass
  def setHorizontal(self):
    pass
  def setInPattern(self):
    pass
  def setOutPattern(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CollisionHandlerQueue:
  def __init__(self):
    pass
  def clearEntries(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEntries(self):
    pass
  def getEntry(self):
    pass
  def getNumEntries(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def sortEntries(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
class CollisionInvSphere:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getRadius(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setCenter(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setRadius(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionLine:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getDirection(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getOrigin(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setDirection(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setFromLens(self):
    pass
  def setOrigin(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addSolid(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSolids(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getColliderSort(self):
    pass
  def getDefaultCollideMask():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getFromCollideMask(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumSolids(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getSolid(self):
    pass
  def getSolids(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def modifySolid(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeSolid(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCollideMask(self):
    pass
  def setColliderSort(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFromCollideMask(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSolid(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionParabola:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getParabola(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getT1(self):
    pass
  def getT2(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setParabola(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setT1(self):
    pass
  def setT2(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionPlane:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def distToPlane(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getNormal(self):
    pass
  def getPlane(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setPlane(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionPolygon:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def distToPlane(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getNormal(self):
    pass
  def getNumPoints(self):
    pass
  def getPlane(self):
    pass
  def getPoint(self):
    pass
  def getPoints(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isConcave(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def isValid(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setPlane(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def verifyPoints():
    pass
  def write(self):
    pass
class CollisionRay:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getDirection(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getOrigin(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setDirection(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setFromLens(self):
    pass
  def setOrigin(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionRecorder:
  def __init__(self):
    pass
  def downcastToCollisionVisualizer(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
class CollisionSegment:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getPointA(self):
    pass
  def getPointB(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setFromLens(self):
    pass
  def setPointA(self):
    pass
  def setPointB(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionSolid:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionSphere:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getCenter(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getRadius(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setCenter(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setRadius(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionTraverser:
  def __init__(self):
    pass
  def addCollider(self):
    pass
  def assign(self):
    pass
  def clearColliders(self):
    pass
  def clearName(self):
    pass
  def clearRecorder(self):
    pass
  def getClassType():
    pass
  def getCollider(self):
    pass
  def getColliders(self):
    pass
  def getHandler(self):
    pass
  def getName(self):
    pass
  def getNumColliders(self):
    pass
  def getRecorder(self):
    pass
  def getRespectPrevTransform(self):
    pass
  def hasCollider(self):
    pass
  def hasName(self):
    pass
  def hasRecorder(self):
    pass
  def hideCollisions(self):
    pass
  def output(self):
    pass
  def removeCollider(self):
    pass
  def setName(self):
    pass
  def setRecorder(self):
    pass
  def setRespectPrevTransform(self):
    pass
  def showCollisions(self):
    pass
  def traverse(self):
    pass
  def write(self):
    pass
class CollisionTube:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearEffectiveNormal(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCollisionOrigin(self):
    pass
  def getEffectiveNormal(self):
    pass
  def getPointA(self):
    pass
  def getPointB(self):
    pass
  def getRadius(self):
    pass
  def getRefCount(self):
    pass
  def getRespectEffectiveNormal(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasEffectiveNormal(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isTangible(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setBounds(self):
    pass
  def setEffectiveNormal(self):
    pass
  def setPointA(self):
    pass
  def setPointB(self):
    pass
  def setRadius(self):
    pass
  def setRespectEffectiveNormal(self):
    pass
  def setTangible(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class CollisionVisualizer:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToCollisionVisualizer(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNormalScale(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPointScale(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNormalScale(self):
    pass
  def setOverallHidden(self):
    pass
  def setPointScale(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToCollisionRecorder(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPandaNode(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class ColorAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  TFlat = int

  TOff = int

  TVertex = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getColorType(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def makeDefault():
    pass
  def makeFlat():
    pass
  def makeOff():
    pass
  def makeVertex():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class ColorBlendAttrib:
  def __init__(self):
    pass
  MAdd = int

  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MInvSubtract = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MMax = int

  MMin = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MSubtract = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  OAlphaScale = int

  OColorScale = int

  OConstantAlpha = int

  OConstantColor = int

  OFbufferAlpha = int

  OFbufferColor = int

  OIncomingAlpha = int

  OIncomingColor = int

  OIncomingColorSaturate = int

  OOne = int

  OOneMinusAlphaScale = int

  OOneMinusColorScale = int

  OOneMinusConstantAlpha = int

  OOneMinusConstantColor = int

  OOneMinusFbufferAlpha = int

  OOneMinusFbufferColor = int

  OOneMinusIncomingAlpha = int

  OOneMinusIncomingColor = int

  OZero = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getOperandA(self):
    pass
  def getOperandB(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def involvesColorScale(self):
    pass
  def involvesConstantColor(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class ColorLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class ColorScaleAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasAlphaScale(self):
    pass
  def hasRgbScale(self):
    pass
  def hasScale(self):
    pass
  def isExactType(self):
    pass
  def isIdentity(self):
    pass
  def isOfType(self):
    pass
  def isOff(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeIdentity():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setScale(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class ColorScaleLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class ColorWriteAttrib:
  def __init__(self):
    pass
  CAll = int

  CAlpha = int

  CBlue = int

  CGreen = int

  COff = int

  CRed = int

  CRgb = int

  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getChannels(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class CompassEffect:
  def __init__(self):
    pass
  PAll = int

  PPos = int

  PRot = int

  PScale = int

  PSx = int

  PSy = int

  PSz = int

  PX = int

  PY = int

  PZ = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumEffects():
    pass
  def getProperties(self):
    pass
  def getRefCount(self):
    pass
  def getReference(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class ConditionVar:
  def __init__(self):
    pass
  def getMutex(self):
    pass
  def notify(self):
    pass
  def output(self):
    pass
  def wait(self):
    pass
class ConditionVarDirect:
  def __init__(self):
    pass
  def getMutex(self):
    pass
  def notify(self):
    pass
  def output(self):
    pass
  def wait(self):
    pass
class ConditionVarFull:
  def __init__(self):
    pass
  def getMutex(self):
    pass
  def notify(self):
    pass
  def notifyAll(self):
    pass
  def output(self):
    pass
  def wait(self):
    pass
class ConditionVarFullDirect:
  def __init__(self):
    pass
  def getMutex(self):
    pass
  def notify(self):
    pass
  def notifyAll(self):
    pass
  def output(self):
    pass
  def wait(self):
    pass
class Connection:
  def __init__(self):
    pass
  def considerFlush(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getAddress(self):
    pass
  def getClassType():
    pass
  def getCollectTcp(self):
    pass
  def getCollectTcpInterval(self):
    pass
  def getManager(self):
    pass
  def getRefCount(self):
    pass
  def getSocket(self):
    pass
  def ref(self):
    pass
  def setCollectTcp(self):
    pass
  def setCollectTcpInterval(self):
    pass
  def setIpTimeToLive(self):
    pass
  def setIpTypeOfService(self):
    pass
  def setKeepAlive(self):
    pass
  def setLinger(self):
    pass
  def setMaxSegment(self):
    pass
  def setNoDelay(self):
    pass
  def setRecvBufferSize(self):
    pass
  def setReuseAddr(self):
    pass
  def setSendBufferSize(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class ConnectionListener:
  def __init__(self):
    pass
  def addConnection(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def downcastToQueuedConnectionListener(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getManager(self):
    pass
  def getNumThreads(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isConnectionOk(self):
    pass
  def isPolling(self):
    pass
  def poll(self):
    pass
  def removeConnection(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
class ConnectionManager:
  def __init__(self):
    pass
  def closeConnection(self):
    pass
  def downcastToQueuedConnectionManager(self):
    pass
  def getHostName():
    pass
  def openTCPClientConnection(self):
    pass
  def openTCPServerRendezvous(self):
    pass
  def openUDPConnection(self):
    pass
class ConnectionReader:
  def __init__(self):
    pass
  def addConnection(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getManager(self):
    pass
  def getNumThreads(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isConnectionOk(self):
    pass
  def isPolling(self):
    pass
  def poll(self):
    pass
  def removeConnection(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
class ConnectionWriter:
  def __init__(self):
    pass
  def downcastToDatagramSinkNet(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getManager(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getNumThreads(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isImmediate(self):
    pass
  def isValidForUdp(self):
    pass
  def send(self):
    pass
  def setMaxQueueSize(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
class CopyOnWriteObject:
  def __init__(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class CubicCurveseg:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def adjustPoint(self):
    pass
  def adjustPt(self):
    pass
  def adjustTangent(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcLength(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findLength(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def get2ndtangent(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCurveType(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMaxT(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDimensions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPt(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTangent(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCurveType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNumDimensions(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def stitch(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeEgg(self):
    pass
class CullBinAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBinName(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getDrawOrder(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class CullBinEnums:
  def __init__(self):
    pass
  BTBackToFront = int

  BTFixed = int

  BTFrontToBack = int

  BTInvalid = int

  BTStateSorted = int

  BTUnsorted = int

class CullBinManager:
  def __init__(self):
    pass
  BTBackToFront = int

  BTFixed = int

  BTFrontToBack = int

  BTInvalid = int

  BTStateSorted = int

  BTUnsorted = int

  def addBin(self):
    pass
  def findBin(self):
    pass
  def getBin(self):
    pass
  def getBinActive(self):
    pass
  def getBinName(self):
    pass
  def getBinSort(self):
    pass
  def getBinType(self):
    pass
  def getBins(self):
    pass
  def getGlobalPtr():
    pass
  def getNumBins(self):
    pass
  def removeBin(self):
    pass
  def setBinActive(self):
    pass
  def setBinSort(self):
    pass
  def setBinType(self):
    pass
  def write(self):
    pass
class CullFaceAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MCullClockwise = int

  MCullCounterClockwise = int

  MCullNone = int

  MCullUnchanged = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActualMode(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getEffectiveMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getReverse(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeReverse():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class CullResult:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def draw(self):
    pass
  def finishCull(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def makeNext(self):
    pass
  def makeResultGraph(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class CullTraverser:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def drawBoundingVolume(self):
    pass
  def endTraverse(self):
    pass
  def flushLevel():
    pass
  def getCameraMask(self):
    pass
  def getCameraTransform(self):
    pass
  def getClassType():
    pass
  def getCurrentThread(self):
    pass
  def getDepthOffsetDecals(self):
    pass
  def getEffectiveIncompleteRender(self):
    pass
  def getGsg(self):
    pass
  def getInitialState(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getTagStateKey(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getViewFrustum(self):
    pass
  def getWorldTransform(self):
    pass
  def hasTagStateKey(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def setCameraMask(self):
    pass
  def setScene(self):
    pass
  def setViewFrustum(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def traverse(self):
    pass
  def traverseBelow(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class CullTraverserData:
  def __init__(self):
    pass
  def applyTransformAndState(self):
    pass
  def getModelviewTransform(self):
    pass
  def getNetTransform(self):
    pass
  def isInView(self):
    pass
  def isThisNodeHidden(self):
    pass
  def node(self):
    pass
class CurveFitter:
  def __init__(self):
    pass
  def addHpr(self):
    pass
  def addXyz(self):
    pass
  def addXyzHpr(self):
    pass
  def computeTangents(self):
    pass
  def desample(self):
    pass
  def getClassType():
    pass
  def getNumSamples(self):
    pass
  def getSampleHpr(self):
    pass
  def getSampleT(self):
    pass
  def getSampleTangent(self):
    pass
  def getSampleXyz(self):
    pass
  def makeHermite(self):
    pass
  def makeNurbs(self):
    pass
  def output(self):
    pass
  def removeSamples(self):
    pass
  def reset(self):
    pass
  def sample(self):
    pass
  def sortPoints(self):
    pass
  def wrapHpr(self):
    pass
  def write(self):
    pass
class DataGraphTraverser:
  def __init__(self):
    pass
  def collectLeftovers(self):
    pass
  def getCurrentThread(self):
    pass
  def traverse(self):
    pass
class DataNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class DatagramGeneratorNet:
  def __init__(self):
    pass
  def addConnection(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getDatagram(self):
    pass
  def getFile(self):
    pass
  def getFilePos(self):
    pass
  def getManager(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getNumThreads(self):
    pass
  def getOverflowFlag(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isConnectionOk(self):
    pass
  def isEof(self):
    pass
  def isError(self):
    pass
  def isPolling(self):
    pass
  def poll(self):
    pass
  def removeConnection(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
  def upcastToConnectionReader(self):
    pass
  def upcastToDatagramGenerator(self):
    pass
  def upcastToQueuedReturnDatagram(self):
    pass
class DatagramSinkNet:
  def __init__(self):
    pass
  def downcastToDatagramSinkNet(self):
    pass
  def flush(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getManager(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getNumThreads(self):
    pass
  def getRawMode(self):
    pass
  def getTarget(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isError(self):
    pass
  def isImmediate(self):
    pass
  def isValidForUdp(self):
    pass
  def putDatagram(self):
    pass
  def send(self):
    pass
  def setMaxQueueSize(self):
    pass
  def setRawMode(self):
    pass
  def setTarget(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
  def upcastToConnectionWriter(self):
    pass
  def upcastToDatagramSink(self):
    pass
class DecalEffect:
  def __init__(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumEffects():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class DepthOffsetAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getOffset(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class DepthTestAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class DepthWriteAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MOn = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class DialNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDials(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isDialKnown(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def readDial(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class DirectionalLight:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def activateLens(self):
    pass
  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def asNode(self):
    pass
  def assign(self):
    pass
  def cleanupAuxSceneData(self):
    pass
  def clearAttrib(self):
    pass
  def clearAuxSceneData(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTagState(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copyLens(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def deactivateLens(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getAuxSceneData(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCameraMask(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getCullCenter(self):
    pass
  def getDirection(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInitialState(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLens(self):
    pass
  def getLensActive(self):
    pass
  def getLodCenter(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getSpecularColor(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTagState(self):
    pass
  def getTagStateKey(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTagState(self):
    pass
  def hasTags(self):
    pass
  def hideFrustum(self):
    pass
  def isActive(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isInView(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isShadowCaster(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listAuxSceneData(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setAuxSceneData(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCameraMask(self):
    pass
  def setColor(self):
    pass
  def setCullCenter(self):
    pass
  def setDirection(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setInitialState(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLens(self):
    pass
  def setLensActive(self):
    pass
  def setLodCenter(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPoint(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setScene(self):
    pass
  def setShadowCaster(self):
    pass
  def setSpecularColor(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTagState(self):
    pass
  def setTagStateKey(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showFrustum(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToCamera(self):
    pass
  def upcastToLight(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class DisplayInformation:
  def __init__(self):
    pass
  DSCreateDeviceError = int

  DSCreateWindowError = int

  DSDirect3dCreateError = int

  DSSuccess = int

  DSUnknown = int

  def getAvailablePageFileSize(self):
    pass
  def getAvailablePhysicalMemory(self):
    pass
  def getAvailableProcessVirtualMemory(self):
    pass
  def getCpuBrandIndex(self):
    pass
  def getCpuBrandString(self):
    pass
  def getCpuFrequency(self):
    pass
  def getCpuIdData(self):
    pass
  def getCpuIdSize(self):
    pass
  def getCpuIdVersion(self):
    pass
  def getCpuTime(self):
    pass
  def getCpuVendorString(self):
    pass
  def getCpuVersionInformation(self):
    pass
  def getCurrentCpuFrequency(self):
    pass
  def getDeviceId(self):
    pass
  def getDisplayModeBitsPerPixel(self):
    pass
  def getDisplayModeFullscreenOnly(self):
    pass
  def getDisplayModeHeight(self):
    pass
  def getDisplayModeRefreshRate(self):
    pass
  def getDisplayModeWidth(self):
    pass
  def getDisplayState(self):
    pass
  def getDriverBuild(self):
    pass
  def getDriverDateDay(self):
    pass
  def getDriverDateMonth(self):
    pass
  def getDriverDateYear(self):
    pass
  def getDriverProduct(self):
    pass
  def getDriverSubVersion(self):
    pass
  def getDriverVersion(self):
    pass
  def getMaximumCpuFrequency(self):
    pass
  def getMaximumWindowHeight(self):
    pass
  def getMaximumWindowWidth(self):
    pass
  def getMemoryLoad(self):
    pass
  def getNumCpuCores(self):
    pass
  def getNumLogicalCpus(self):
    pass
  def getOsPlatformId(self):
    pass
  def getOsVersionBuild(self):
    pass
  def getOsVersionMajor(self):
    pass
  def getOsVersionMinor(self):
    pass
  def getPageFaultCount(self):
    pass
  def getPageFileSize(self):
    pass
  def getPageFileUsage(self):
    pass
  def getPeakPageFileUsage(self):
    pass
  def getPeakProcessMemory(self):
    pass
  def getPhysicalMemory(self):
    pass
  def getProcessMemory(self):
    pass
  def getProcessVirtualMemory(self):
    pass
  def getShaderModel(self):
    pass
  def getTextureMemory(self):
    pass
  def getTotalDisplayModes(self):
    pass
  def getVendorId(self):
    pass
  def getVideoMemory(self):
    pass
  def getWindowBitsPerPixel(self):
    pass
  def updateCpuFrequency(self):
    pass
  def updateMemoryInformation(self):
    pass
class DisplayRegion:
  def __init__(self):
    pass
  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def clearCullCallback(self):
    pass
  def clearDrawCallback(self):
    pass
  def disableClears(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getBottom(self):
    pass
  def getCamera(self):
    pass
  def getClassType():
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getCubeMapIndex(self):
    pass
  def getCullCallback(self):
    pass
  def getCullTraverser(self):
    pass
  def getDrawCallback(self):
    pass
  def getIncompleteRender(self):
    pass
  def getLeft(self):
    pass
  def getLensIndex(self):
    pass
  def getPipe(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelHeight(self):
    pass
  def getPixelWidth(self):
    pass
  def getPixelZoom(self):
    pass
  def getRefCount(self):
    pass
  def getRenderbufferType():
    pass
  def getRight(self):
    pass
  def getScreenshot(self):
    pass
  def getSort(self):
    pass
  def getStereoChannel(self):
    pass
  def getTextureReloadPriority(self):
    pass
  def getTop(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWindow(self):
    pass
  def isActive(self):
    pass
  def isAnyClearActive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isStereo(self):
    pass
  def makeCullResultGraph(self):
    pass
  def makeScreenshotFilename():
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def saveScreenshot(self):
    pass
  def saveScreenshotDefault(self):
    pass
  def setActive(self):
    pass
  def setCamera(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setCubeMapIndex(self):
    pass
  def setCullCallback(self):
    pass
  def setCullTraverser(self):
    pass
  def setDimensions(self):
    pass
  def setDrawCallback(self):
    pass
  def setIncompleteRender(self):
    pass
  def setLensIndex(self):
    pass
  def setPixelZoom(self):
    pass
  def setSort(self):
    pass
  def setStereoChannel(self):
    pass
  def setTextureReloadPriority(self):
    pass
  def supportsPixelZoom(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToDisplayRegionBase(self):
    pass
  def upcastToDrawableRegion(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class DisplayRegionBase:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class DisplayRegionCullCallbackData:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getSceneSetup(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def upcall(self):
    pass
class DisplayRegionDrawCallbackData:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getCullResult(self):
    pass
  def getSceneSetup(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def upcall(self):
    pass
class DisplaySearchParameters:
  def __init__(self):
    pass
  def setMaximumBitsPerPixel(self):
    pass
  def setMaximumHeight(self):
    pass
  def setMaximumWidth(self):
    pass
  def setMinimumBitsPerPixel(self):
    pass
  def setMinimumHeight(self):
    pass
  def setMinimumWidth(self):
    pass
class DoubleBitMaskBitMaskUnsignedInt32:
  def __init__(self):
    pass
  def allOff():
    pass
  def allOn():
    pass
  def assign(self):
    pass
  def bit():
    pass
  def clear(self):
    pass
  def clearBit(self):
    pass
  def clearRange(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def extract(self):
    pass
  def getBit(self):
    pass
  def getClassType():
    pass
  def getHighestOffBit(self):
    pass
  def getHighestOnBit(self):
    pass
  def getLowestOffBit(self):
    pass
  def getLowestOnBit(self):
    pass
  def getMaxNumBits():
    pass
  def getNextHigherDifferentBit(self):
    pass
  def getNumBits():
    pass
  def getNumOffBits(self):
    pass
  def getNumOnBits(self):
    pass
  def hasAllOf(self):
    pass
  def hasAnyOf(self):
    pass
  def hasBitsInCommon(self):
    pass
  def hasMaxNumBits():
    pass
  def invertInPlace(self):
    pass
  def isAllOn(self):
    pass
  def isZero(self):
    pass
  def lessThan(self):
    pass
  def lowerOn():
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def outputBinary(self):
    pass
  def outputHex(self):
    pass
  def range():
    pass
  def setBit(self):
    pass
  def setBitTo(self):
    pass
  def setRange(self):
    pass
  def setRangeTo(self):
    pass
  def store(self):
    pass
  def write(self):
    pass
class DrawableRegion:
  def __init__(self):
    pass
  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def disableClears(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelZoom(self):
    pass
  def getRenderbufferType():
    pass
  def isAnyClearActive(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setPixelZoom(self):
    pass
  def supportsPixelZoom(self):
    pass
class DriveInterface:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAllButtons(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearButton(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def forceDgraph(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getForceMouse(self):
    pass
  def getForwardSpeed(self):
    pass
  def getH(self):
    pass
  def getHorizontalDeadZone(self):
    pass
  def getHorizontalRampDownTime(self):
    pass
  def getHorizontalRampUpTime(self):
    pass
  def getHpr(self):
    pass
  def getIgnoreMouse(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMat(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getP(self):
    pass
  def getParent(self):
    pass
  def getPos(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getR(self):
    pass
  def getRefCount(self):
    pass
  def getReverseSpeed(self):
    pass
  def getRotSpeed(self):
    pass
  def getRotateSpeed(self):
    pass
  def getSpeed(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStopThisFrame(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getVerticalDeadZone(self):
    pass
  def getVerticalRampDownTime(self):
    pass
  def getVerticalRampUpTime(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def requireButton(self):
    pass
  def reset(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setForceMouse(self):
    pass
  def setForceRoll(self):
    pass
  def setForwardSpeed(self):
    pass
  def setH(self):
    pass
  def setHorizontalDeadZone(self):
    pass
  def setHorizontalRampDownTime(self):
    pass
  def setHorizontalRampUpTime(self):
    pass
  def setHpr(self):
    pass
  def setIgnoreMouse(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMat(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setP(self):
    pass
  def setPos(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setR(self):
    pass
  def setReverseSpeed(self):
    pass
  def setRotateSpeed(self):
    pass
  def setState(self):
    pass
  def setStopThisFrame(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setVerticalDeadZone(self):
    pass
  def setVerticalRampDownTime(self):
    pass
  def setVerticalRampUpTime(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
def Dtool_AddToDictionary():
  pass
def Dtool_BorrowThisReference():
  pass
Dtool_PyNativeInterface = int

class DynamicTextFont:
  def __init__(self):
    pass
  RMExtruded = int

  RMInvalid = int

  RMPolygon = int

  RMSolid = int

  RMTexture = int

  RMWireframe = int

  WODefault = int

  WOInvalid = int

  WOLeft = int

  WORight = int

  def assign(self):
    pass
  def clear(self):
    pass
  def clearName(self):
    pass
  def downcastToDynamicTextFont(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def garbageCollect(self):
    pass
  def getAnisotropicDegree(self):
    pass
  def getBg(self):
    pass
  def getClassType():
    pass
  def getFg(self):
    pass
  def getFontPixelSize(self):
    pass
  def getLineHeight(self):
    pass
  def getMagfilter(self):
    pass
  def getMinfilter(self):
    pass
  def getName(self):
    pass
  def getNativeAntialias(self):
    pass
  def getNumPages(self):
    pass
  def getOutlineColor(self):
    pass
  def getOutlineFeather(self):
    pass
  def getOutlineWidth(self):
    pass
  def getPage(self):
    pass
  def getPageXSize(self):
    pass
  def getPageYSize(self):
    pass
  def getPages(self):
    pass
  def getPixelSize(self):
    pass
  def getPixelsPerUnit(self):
    pass
  def getPointSize(self):
    pass
  def getPointsPerInch():
    pass
  def getPointsPerUnit():
    pass
  def getPolyMargin(self):
    pass
  def getRefCount(self):
    pass
  def getRenderMode(self):
    pass
  def getScaleFactor(self):
    pass
  def getSpaceAdvance(self):
    pass
  def getTexFormat(self):
    pass
  def getTextureMargin(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWindingOrder(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setAnisotropicDegree(self):
    pass
  def setBg(self):
    pass
  def setFg(self):
    pass
  def setLineHeight(self):
    pass
  def setMagfilter(self):
    pass
  def setMinfilter(self):
    pass
  def setName(self):
    pass
  def setNativeAntialias(self):
    pass
  def setOutline(self):
    pass
  def setPageSize(self):
    pass
  def setPixelSize(self):
    pass
  def setPixelsPerUnit(self):
    pass
  def setPointSize(self):
    pass
  def setPolyMargin(self):
    pass
  def setRenderMode(self):
    pass
  def setScaleFactor(self):
    pass
  def setSpaceAdvance(self):
    pass
  def setTextureMargin(self):
    pass
  def setWindingOrder(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToFreetypeFont(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTextFont(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def write(self):
    pass
class DynamicTextPage:
  def __init__(self):
    pass
  CMDefault = int

  CMDxt1 = int

  CMDxt2 = int

  CMDxt3 = int

  CMDxt4 = int

  CMDxt5 = int

  CMFxt1 = int

  CMOff = int

  CMOn = int

  FAlpha = int

  FBlue = int

  FColorIndex = int

  FDepthComponent = int

  FDepthComponent16 = int

  FDepthComponent24 = int

  FDepthComponent32 = int

  FDepthStencil = int

  FGreen = int

  FLuminance = int

  FLuminanceAlpha = int

  FLuminanceAlphamask = int

  FRed = int

  FRgb = int

  FRgb12 = int

  FRgb332 = int

  FRgb5 = int

  FRgb8 = int

  FRgba = int

  FRgba12 = int

  FRgba16 = int

  FRgba32 = int

  FRgba4 = int

  FRgba5 = int

  FRgba8 = int

  FRgbm = int

  FTDefault = int

  FTInvalid = int

  FTLinear = int

  FTLinearMipmapLinear = int

  FTLinearMipmapNearest = int

  FTNearest = int

  FTNearestMipmapLinear = int

  FTNearestMipmapNearest = int

  FTShadow = int

  QLBest = int

  QLDefault = int

  QLFastest = int

  QLNormal = int

  TFloat = int

  TT1dTexture = int

  TT2dTexture = int

  TT3dTexture = int

  TTCubeMap = int

  TUnsignedByte = int

  TUnsignedInt248 = int

  TUnsignedShort = int

  WMBorderColor = int

  WMClamp = int

  WMInvalid = int

  WMMirror = int

  WMMirrorOnce = int

  WMRepeat = int

  def assign(self):
    pass
  def clear(self):
    pass
  def clearAlphaFilename(self):
    pass
  def clearAlphaFullpath(self):
    pass
  def clearAuxData(self):
    pass
  def clearFilename(self):
    pass
  def clearFullpath(self):
    pass
  def clearName(self):
    pass
  def clearRamImage(self):
    pass
  def clearRamMipmapImage(self):
    pass
  def clearRamMipmapImages(self):
    pass
  def clearSimpleRamImage(self):
    pass
  def compressRamImage(self):
    pass
  def considerRescale(self):
    pass
  def decodeFromBamStream():
    pass
  def downToPower2():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def downcastToVideoTexture(self):
    pass
  def encodeToBamStream(self):
    pass
  def estimateTextureMemory(self):
    pass
  def generateAlphaScaleMap(self):
    pass
  def generateNormalizationCubeMap(self):
    pass
  def generateRamMipmapImages(self):
    pass
  def generateSimpleRamImage(self):
    pass
  def getActive(self):
    pass
  def getAlphaFilename(self):
    pass
  def getAlphaFullpath(self):
    pass
  def getAnisotropicDegree(self):
    pass
  def getAuxData(self):
    pass
  def getBamModified(self):
    pass
  def getBorderColor(self):
    pass
  def getClassType():
    pass
  def getComponentType(self):
    pass
  def getComponentWidth(self):
    pass
  def getCompression(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getEffectiveAnisotropicDegree(self):
    pass
  def getEffectiveMagfilter(self):
    pass
  def getEffectiveMinfilter(self):
    pass
  def getEffectiveQualityLevel(self):
    pass
  def getExpectedMipmapXSize(self):
    pass
  def getExpectedMipmapYSize(self):
    pass
  def getExpectedMipmapZSize(self):
    pass
  def getExpectedNumMipmapLevels(self):
    pass
  def getExpectedRamImageSize(self):
    pass
  def getExpectedRamMipmapImageSize(self):
    pass
  def getExpectedRamMipmapPageSize(self):
    pass
  def getExpectedRamPageSize(self):
    pass
  def getFilename(self):
    pass
  def getFormat(self):
    pass
  def getFullpath(self):
    pass
  def getImageModified(self):
    pass
  def getKeepRamImage(self):
    pass
  def getLoadedFromImage(self):
    pass
  def getLoadedFromTxo(self):
    pass
  def getMagfilter(self):
    pass
  def getMatchFramebufferFormat(self):
    pass
  def getMinfilter(self):
    pass
  def getName(self):
    pass
  def getNumComponents(self):
    pass
  def getNumLoadableRamMipmapImages(self):
    pass
  def getNumRamMipmapImages(self):
    pass
  def getOrigFileXSize(self):
    pass
  def getOrigFileYSize(self):
    pass
  def getOrigFileZSize(self):
    pass
  def getPadXSize(self):
    pass
  def getPadYSize(self):
    pass
  def getPadZSize(self):
    pass
  def getPostLoadStoreCache(self):
    pass
  def getPropertiesModified(self):
    pass
  def getQualityLevel(self):
    pass
  def getRamImage(self):
    pass
  def getRamImageAs(self):
    pass
  def getRamImageCompression(self):
    pass
  def getRamImageSize(self):
    pass
  def getRamMipmapImage(self):
    pass
  def getRamMipmapImageSize(self):
    pass
  def getRamMipmapPageSize(self):
    pass
  def getRamPageSize(self):
    pass
  def getRefCount(self):
    pass
  def getRenderToTexture(self):
    pass
  def getResident(self):
    pass
  def getSimpleImageModified(self):
    pass
  def getSimpleRamImage(self):
    pass
  def getSimpleRamImageSize(self):
    pass
  def getSimpleXSize(self):
    pass
  def getSimpleYSize(self):
    pass
  def getTextureType(self):
    pass
  def getTexturesPower2():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUncompressedRamImage(self):
    pass
  def getWrapU(self):
    pass
  def getWrapV(self):
    pass
  def getWrapW(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def getZSize(self):
    pass
  def hasAllRamMipmapImages(self):
    pass
  def hasAlphaFilename(self):
    pass
  def hasAlphaFullpath(self):
    pass
  def hasCompression(self):
    pass
  def hasFilename(self):
    pass
  def hasFullpath(self):
    pass
  def hasName(self):
    pass
  def hasRamImage(self):
    pass
  def hasRamMipmapImage(self):
    pass
  def hasSimpleRamImage(self):
    pass
  def hasUncompressedRamImage(self):
    pass
  def haveTexturesPower2():
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isMipmap():
    pass
  def isOfType(self):
    pass
  def isPrepared(self):
    pass
  def load(self):
    pass
  def loadRelated(self):
    pass
  def makeCopy(self):
    pass
  def makeRamImage(self):
    pass
  def makeRamMipmapImage(self):
    pass
  def markBamModified(self):
    pass
  def mightHaveRamImage(self):
    pass
  def modifyRamImage(self):
    pass
  def modifyRamMipmapImage(self):
    pass
  def modifySimpleRamImage(self):
    pass
  def newSimpleRamImage(self):
    pass
  def output(self):
    pass
  def peek(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def read(self):
    pass
  def readDds(self):
    pass
  def readTxo(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def reload(self):
    pass
  def setAlphaFilename(self):
    pass
  def setAlphaFullpath(self):
    pass
  def setAnisotropicDegree(self):
    pass
  def setAuxData(self):
    pass
  def setBorderColor(self):
    pass
  def setComponentType(self):
    pass
  def setCompression(self):
    pass
  def setFilename(self):
    pass
  def setFormat(self):
    pass
  def setFullpath(self):
    pass
  def setKeepRamImage(self):
    pass
  def setLoadedFromImage(self):
    pass
  def setLoadedFromTxo(self):
    pass
  def setMagfilter(self):
    pass
  def setMatchFramebufferFormat(self):
    pass
  def setMinfilter(self):
    pass
  def setName(self):
    pass
  def setOrigFileSize(self):
    pass
  def setPadSize(self):
    pass
  def setPostLoadStoreCache(self):
    pass
  def setQualityLevel(self):
    pass
  def setRamImage(self):
    pass
  def setRamMipmapImage(self):
    pass
  def setRamMipmapPointerFromInt(self):
    pass
  def setRenderToTexture(self):
    pass
  def setSimpleRamImage(self):
    pass
  def setSizePadded(self):
    pass
  def setTexturesPower2():
    pass
  def setWrapU(self):
    pass
  def setWrapV(self):
    pass
  def setWrapW(self):
    pass
  def setXSize(self):
    pass
  def setYSize(self):
    pass
  def setZSize(self):
    pass
  def setup1dTexture(self):
    pass
  def setup2dTexture(self):
    pass
  def setup3dTexture(self):
    pass
  def setupCubeMap(self):
    pass
  def setupTexture(self):
    pass
  def store(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncompressRamImage(self):
    pass
  def unref(self):
    pass
  def upToPower2():
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def usesMipmaps(self):
    pass
  def wasImageModified(self):
    pass
  def write(self):
    pass
  def writeTxo(self):
    pass
class EaseInBlendType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class EaseInOutBlendType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class EaseOutBlendType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class Event:
  def __init__(self):
    pass
  def addParameter(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def clearReceiver(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def getNumParameters(self):
    pass
  def getParameter(self):
    pass
  def getParameters(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def hasReceiver(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class EventHandler:
  def __init__(self):
    pass
  def dispatchEvent(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getGlobalEventHandler():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def processEvents(self):
    pass
  def write(self):
    pass
class EventParameter:
  def __init__(self):
    pass
  def assign(self):
    pass
  def getDoubleValue(self):
    pass
  def getIntValue(self):
    pass
  def getPtr(self):
    pass
  def getStringValue(self):
    pass
  def getTypedRefCountValue(self):
    pass
  def getWstringValue(self):
    pass
  def isDouble(self):
    pass
  def isEmpty(self):
    pass
  def isInt(self):
    pass
  def isString(self):
    pass
  def isTypedRefCount(self):
    pass
  def isWstring(self):
    pass
  def output(self):
    pass
class EventQueue:
  def __init__(self):
    pass
  def clear(self):
    pass
  def dequeueEvent(self):
    pass
  def getGlobalEventQueue():
    pass
  def isQueueEmpty(self):
    pass
  def isQueueFull(self):
    pass
  def queueEvent(self):
    pass
class EventStorePandaNode:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setValue(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class EventStoreTypedRefCount:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setValue(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class EventStoreValueBase:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class ExternalThread:
  def __init__(self):
    pass
  def assign(self):
    pass
  def bindThread():
    pass
  def clearName(self):
    pass
  def considerYield():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def forceYield():
    pass
  def getClassType():
    pass
  def getCurrentPipelineStage():
    pass
  def getCurrentThread():
    pass
  def getExternalThread():
    pass
  def getMainThread():
    pass
  def getName(self):
    pass
  def getPipelineStage(self):
    pass
  def getPstatsIndex(self):
    pass
  def getPythonData(self):
    pass
  def getRefCount(self):
    pass
  def getSyncName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUniqueId(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isJoinable(self):
    pass
  def isOfType(self):
    pass
  def isStarted(self):
    pass
  def isThreadingSupported():
    pass
  def isTrueThreads():
    pass
  def join(self):
    pass
  def output(self):
    pass
  def outputBlocker(self):
    pass
  def preempt(self):
    pass
  def prepareForExit():
    pass
  def ref(self):
    pass
  def setMinPipelineStage(self):
    pass
  def setName(self):
    pass
  def setPipelineStage(self):
    pass
  def setPythonData(self):
    pass
  def sleep():
    pass
  def start(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def writeStatus():
    pass
class FFMpegTexture:
  def __init__(self):
    pass
  CMDefault = int

  CMDxt1 = int

  CMDxt2 = int

  CMDxt3 = int

  CMDxt4 = int

  CMDxt5 = int

  CMFxt1 = int

  CMOff = int

  CMOn = int

  FAlpha = int

  FBlue = int

  FColorIndex = int

  FDepthComponent = int

  FDepthComponent16 = int

  FDepthComponent24 = int

  FDepthComponent32 = int

  FDepthStencil = int

  FGreen = int

  FLuminance = int

  FLuminanceAlpha = int

  FLuminanceAlphamask = int

  FRed = int

  FRgb = int

  FRgb12 = int

  FRgb332 = int

  FRgb5 = int

  FRgb8 = int

  FRgba = int

  FRgba12 = int

  FRgba16 = int

  FRgba32 = int

  FRgba4 = int

  FRgba5 = int

  FRgba8 = int

  FRgbm = int

  FTDefault = int

  FTInvalid = int

  FTLinear = int

  FTLinearMipmapLinear = int

  FTLinearMipmapNearest = int

  FTNearest = int

  FTNearestMipmapLinear = int

  FTNearestMipmapNearest = int

  FTShadow = int

  QLBest = int

  QLDefault = int

  QLFastest = int

  QLNormal = int

  TFloat = int

  TT1dTexture = int

  TT2dTexture = int

  TT3dTexture = int

  TTCubeMap = int

  TUnsignedByte = int

  TUnsignedInt248 = int

  TUnsignedShort = int

  WMBorderColor = int

  WMClamp = int

  WMInvalid = int

  WMMirror = int

  WMMirrorOnce = int

  WMRepeat = int

  def assign(self):
    pass
  def clear(self):
    pass
  def clearAlphaFilename(self):
    pass
  def clearAlphaFullpath(self):
    pass
  def clearAuxData(self):
    pass
  def clearFilename(self):
    pass
  def clearFullpath(self):
    pass
  def clearName(self):
    pass
  def clearRamImage(self):
    pass
  def clearRamMipmapImage(self):
    pass
  def clearRamMipmapImages(self):
    pass
  def clearSimpleRamImage(self):
    pass
  def compressRamImage(self):
    pass
  def considerRescale(self):
    pass
  def decodeFromBamStream():
    pass
  def downToPower2():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def downcastToVideoTexture(self):
    pass
  def encodeToBamStream(self):
    pass
  def estimateTextureMemory(self):
    pass
  def generateAlphaScaleMap(self):
    pass
  def generateNormalizationCubeMap(self):
    pass
  def generateRamMipmapImages(self):
    pass
  def generateSimpleRamImage(self):
    pass
  def getActive(self):
    pass
  def getAlphaFilename(self):
    pass
  def getAlphaFullpath(self):
    pass
  def getAnisotropicDegree(self):
    pass
  def getAuxData(self):
    pass
  def getBamModified(self):
    pass
  def getBorderColor(self):
    pass
  def getClassType():
    pass
  def getComponentType(self):
    pass
  def getComponentWidth(self):
    pass
  def getCompression(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getEffectiveAnisotropicDegree(self):
    pass
  def getEffectiveMagfilter(self):
    pass
  def getEffectiveMinfilter(self):
    pass
  def getEffectiveQualityLevel(self):
    pass
  def getExpectedMipmapXSize(self):
    pass
  def getExpectedMipmapYSize(self):
    pass
  def getExpectedMipmapZSize(self):
    pass
  def getExpectedNumMipmapLevels(self):
    pass
  def getExpectedRamImageSize(self):
    pass
  def getExpectedRamMipmapImageSize(self):
    pass
  def getExpectedRamMipmapPageSize(self):
    pass
  def getExpectedRamPageSize(self):
    pass
  def getFilename(self):
    pass
  def getFormat(self):
    pass
  def getFrac(self):
    pass
  def getFrame(self):
    pass
  def getFrameRate(self):
    pass
  def getFullFframe(self):
    pass
  def getFullFrame(self):
    pass
  def getFullpath(self):
    pass
  def getImageModified(self):
    pass
  def getKeepRamImage(self):
    pass
  def getLoadedFromImage(self):
    pass
  def getLoadedFromTxo(self):
    pass
  def getMagfilter(self):
    pass
  def getMatchFramebufferFormat(self):
    pass
  def getMinfilter(self):
    pass
  def getName(self):
    pass
  def getNextFrame(self):
    pass
  def getNumComponents(self):
    pass
  def getNumFrames(self):
    pass
  def getNumLoadableRamMipmapImages(self):
    pass
  def getNumRamMipmapImages(self):
    pass
  def getOrigFileXSize(self):
    pass
  def getOrigFileYSize(self):
    pass
  def getOrigFileZSize(self):
    pass
  def getPadXSize(self):
    pass
  def getPadYSize(self):
    pass
  def getPadZSize(self):
    pass
  def getPlayRate(self):
    pass
  def getPostLoadStoreCache(self):
    pass
  def getPropertiesModified(self):
    pass
  def getQualityLevel(self):
    pass
  def getRamImage(self):
    pass
  def getRamImageAs(self):
    pass
  def getRamImageCompression(self):
    pass
  def getRamImageSize(self):
    pass
  def getRamMipmapImage(self):
    pass
  def getRamMipmapImageSize(self):
    pass
  def getRamMipmapPageSize(self):
    pass
  def getRamPageSize(self):
    pass
  def getRefCount(self):
    pass
  def getRenderToTexture(self):
    pass
  def getResident(self):
    pass
  def getSimpleImageModified(self):
    pass
  def getSimpleRamImage(self):
    pass
  def getSimpleRamImageSize(self):
    pass
  def getSimpleXSize(self):
    pass
  def getSimpleYSize(self):
    pass
  def getTexScale(self):
    pass
  def getTextureType(self):
    pass
  def getTexturesPower2():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUncompressedRamImage(self):
    pass
  def getVideoHeight(self):
    pass
  def getVideoWidth(self):
    pass
  def getWrapU(self):
    pass
  def getWrapV(self):
    pass
  def getWrapW(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def getZSize(self):
    pass
  def hasAllRamMipmapImages(self):
    pass
  def hasAlphaFilename(self):
    pass
  def hasAlphaFullpath(self):
    pass
  def hasCompression(self):
    pass
  def hasFilename(self):
    pass
  def hasFullpath(self):
    pass
  def hasName(self):
    pass
  def hasRamImage(self):
    pass
  def hasRamMipmapImage(self):
    pass
  def hasSimpleRamImage(self):
    pass
  def hasUncompressedRamImage(self):
    pass
  def haveTexturesPower2():
    pass
  def isExactType(self):
    pass
  def isMipmap():
    pass
  def isOfType(self):
    pass
  def isPlaying(self):
    pass
  def isPrepared(self):
    pass
  def load(self):
    pass
  def loadRelated(self):
    pass
  def loop(self):
    pass
  def makeCopy(self):
    pass
  def makeRamImage(self):
    pass
  def makeRamMipmapImage(self):
    pass
  def markBamModified(self):
    pass
  def mightHaveRamImage(self):
    pass
  def modifyRamImage(self):
    pass
  def modifyRamMipmapImage(self):
    pass
  def modifySimpleRamImage(self):
    pass
  def newSimpleRamImage(self):
    pass
  def output(self):
    pass
  def peek(self):
    pass
  def pingpong(self):
    pass
  def play(self):
    pass
  def pose(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def read(self):
    pass
  def readDds(self):
    pass
  def readTxo(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def reload(self):
    pass
  def setAlphaFilename(self):
    pass
  def setAlphaFullpath(self):
    pass
  def setAnisotropicDegree(self):
    pass
  def setAuxData(self):
    pass
  def setBorderColor(self):
    pass
  def setComponentType(self):
    pass
  def setCompression(self):
    pass
  def setFilename(self):
    pass
  def setFormat(self):
    pass
  def setFullpath(self):
    pass
  def setKeepRamImage(self):
    pass
  def setLoadedFromImage(self):
    pass
  def setLoadedFromTxo(self):
    pass
  def setMagfilter(self):
    pass
  def setMatchFramebufferFormat(self):
    pass
  def setMinfilter(self):
    pass
  def setName(self):
    pass
  def setOrigFileSize(self):
    pass
  def setPadSize(self):
    pass
  def setPlayRate(self):
    pass
  def setPostLoadStoreCache(self):
    pass
  def setQualityLevel(self):
    pass
  def setRamImage(self):
    pass
  def setRamMipmapImage(self):
    pass
  def setRamMipmapPointerFromInt(self):
    pass
  def setRenderToTexture(self):
    pass
  def setSimpleRamImage(self):
    pass
  def setSizePadded(self):
    pass
  def setTexturesPower2():
    pass
  def setWrapU(self):
    pass
  def setWrapV(self):
    pass
  def setWrapW(self):
    pass
  def setXSize(self):
    pass
  def setYSize(self):
    pass
  def setZSize(self):
    pass
  def setup1dTexture(self):
    pass
  def setup2dTexture(self):
    pass
  def setup3dTexture(self):
    pass
  def setupCubeMap(self):
    pass
  def setupTexture(self):
    pass
  def stop(self):
    pass
  def store(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncompressRamImage(self):
    pass
  def unref(self):
    pass
  def upToPower2():
    pass
  def upcastToAnimInterface(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTexture(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def usesMipmaps(self):
    pass
  def wasImageModified(self):
    pass
  def write(self):
    pass
  def writeTxo(self):
    pass
class FadeLODNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def addSwitch(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearForceSwitch(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearSwitches(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def forceSwitch(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCenter(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFadeBinDrawOrder(self):
    pass
  def getFadeBinName(self):
    pass
  def getFadeStateOverride(self):
    pass
  def getFadeTime(self):
    pass
  def getFancyBits(self):
    pass
  def getHighestSwitch(self):
    pass
  def getIn(self):
    pass
  def getIns(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLowestSwitch(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumSwitches(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOut(self):
    pass
  def getOuts(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hideAllSwitches(self):
    pass
  def hideSwitch(self):
    pass
  def isAmbientLight(self):
    pass
  def isAnyShown(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def makeDefaultLod():
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCenter(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFadeBin(self):
    pass
  def setFadeStateOverride(self):
    pass
  def setFadeTime(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setSwitch(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showAllSwitches(self):
    pass
  def showSwitch(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def verifyChildBounds(self):
    pass
  def write(self):
    pass
class FfmpegAudio:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class FfmpegAudioCursor:
  def __init__(self):
    pass
  def aborted(self):
    pass
  def audioChannels(self):
    pass
  def audioRate(self):
    pass
  def canSeek(self):
    pass
  def canSeekFast(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getSource(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def length(self):
    pass
  def markBamModified(self):
    pass
  def readSamples(self):
    pass
  def ready(self):
    pass
  def ref(self):
    pass
  def seek(self):
    pass
  def skipSamples(self):
    pass
  def tell(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class FfmpegVideo:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class FfmpegVideoCursor:
  def __init__(self):
    pass
  def aborted(self):
    pass
  def canSeek(self):
    pass
  def canSeekFast(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def fetchIntoBitbucket(self):
    pass
  def fetchIntoTexture(self):
    pass
  def fetchIntoTextureAlpha(self):
    pass
  def fetchIntoTextureRgb(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumComponents(self):
    pass
  def getRefCount(self):
    pass
  def getSource(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lastStart(self):
    pass
  def length(self):
    pass
  def markBamModified(self):
    pass
  def nextStart(self):
    pass
  def ready(self):
    pass
  def ref(self):
    pass
  def setupTexture(self):
    pass
  def sizeX(self):
    pass
  def sizeY(self):
    pass
  def streaming(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class FilterProperties:
  def __init__(self):
    pass
  def addChorus(self):
    pass
  def addCompress(self):
    pass
  def addDistort(self):
    pass
  def addEcho(self):
    pass
  def addFlange(self):
    pass
  def addHighpass(self):
    pass
  def addLowpass(self):
    pass
  def addNormalize(self):
    pass
  def addParameq(self):
    pass
  def addPitchshift(self):
    pass
  def addReverb(self):
    pass
  def clear(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class FiniteBoundingVolume:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getMax(self):
    pass
  def getMin(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVolume(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class FisheyeMaker:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def generate(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def reset(self):
    pass
  def setFov(self):
    pass
  def setName(self):
    pass
  def setNumVertices(self):
    pass
  def setReflection(self):
    pass
  def setSquareInscribed(self):
    pass
class SimpleLerpFunctorFloat:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorFloat:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class Fog:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  MExponential = int

  MExponentialSquared = int

  MLinear = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getExpDensity(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLinearOnsetPoint(self):
    pass
  def getLinearOpaquePoint(self):
    pass
  def getMode(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setColor(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setExpDensity(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLinearFallback(self):
    pass
  def setLinearOnsetPoint(self):
    pass
  def setLinearOpaquePoint(self):
    pass
  def setLinearRange(self):
    pass
  def setMode(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class FogAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getFog(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isOff(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class FontPool:
  def __init__(self):
    pass
  def addFont():
    pass
  def garbageCollect():
    pass
  def hasFont():
    pass
  def listContents():
    pass
  def loadFont():
    pass
  def releaseAllFonts():
    pass
  def releaseFont():
    pass
  def verifyFont():
    pass
  def write():
    pass
class FrameBufferProperties:
  def __init__(self):
    pass
  def addProperties(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def eq(self):
    pass
  def getAccumBits(self):
    pass
  def getAlphaBits(self):
    pass
  def getAuxFloat(self):
    pass
  def getAuxHrgba(self):
    pass
  def getAuxMask(self):
    pass
  def getAuxRgba(self):
    pass
  def getBackBuffers(self):
    pass
  def getBufferMask(self):
    pass
  def getColorBits(self):
    pass
  def getCoverageSamples(self):
    pass
  def getDefault():
    pass
  def getDepthBits(self):
    pass
  def getForceHardware(self):
    pass
  def getForceSoftware(self):
    pass
  def getIndexedColor(self):
    pass
  def getMultisamples(self):
    pass
  def getQuality(self):
    pass
  def getRgbColor(self):
    pass
  def getStencilBits(self):
    pass
  def getStereo(self):
    pass
  def isAnySpecified(self):
    pass
  def isBasic(self):
    pass
  def isSingleBuffered(self):
    pass
  def isStereo(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def setAccumBits(self):
    pass
  def setAllSpecified(self):
    pass
  def setAlphaBits(self):
    pass
  def setAuxFloat(self):
    pass
  def setAuxHrgba(self):
    pass
  def setAuxRgba(self):
    pass
  def setBackBuffers(self):
    pass
  def setColorBits(self):
    pass
  def setCoverageSamples(self):
    pass
  def setDepthBits(self):
    pass
  def setForceHardware(self):
    pass
  def setForceSoftware(self):
    pass
  def setIndexedColor(self):
    pass
  def setMultisamples(self):
    pass
  def setOneBitPerChannel(self):
    pass
  def setRgbColor(self):
    pass
  def setStencilBits(self):
    pass
  def setStereo(self):
    pass
  def subsumes(self):
    pass
  def verifyHardwareSoftware(self):
    pass
class FrameRateMeter:
  def __init__(self):
    pass
  ABoxedCenter = int

  ABoxedLeft = int

  ABoxedRight = int

  ACenter = int

  ALeft = int

  ARight = int

  EIso8859 = int

  EUnicode = int

  EUtf8 = int

  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  FFDynamicMerge = int

  FFLight = int

  FFMedium = int

  FFNone = int

  FFStrong = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addProperties(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def appendText(self):
    pass
  def appendUnicodeChar(self):
    pass
  def appendWtext(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcWidth(self):
    pass
  def clear(self):
    pass
  def clearAlign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBin(self):
    pass
  def clearBounds(self):
    pass
  def clearCard(self):
    pass
  def clearCardBorder(self):
    pass
  def clearCardTexture(self):
    pass
  def clearDrawOrder(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFont(self):
    pass
  def clearFrame(self):
    pass
  def clearGlyphScale(self):
    pass
  def clearGlyphShift(self):
    pass
  def clearIndent(self):
    pass
  def clearMaxRows(self):
    pass
  def clearName(self):
    pass
  def clearPreserveTrailingWhitespace(self):
    pass
  def clearPythonTag(self):
    pass
  def clearShadow(self):
    pass
  def clearShadowColor(self):
    pass
  def clearSlant(self):
    pass
  def clearSmallCaps(self):
    pass
  def clearSmallCapsScale(self):
    pass
  def clearState(self):
    pass
  def clearTabWidth(self):
    pass
  def clearTag(self):
    pass
  def clearText(self):
    pass
  def clearTextColor(self):
    pass
  def clearTextScale(self):
    pass
  def clearTransform(self):
    pass
  def clearUnderscore(self):
    pass
  def clearUnderscoreHeight(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def clearWindow(self):
    pass
  def clearWordwrap(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def decodeText(self):
    pass
  def downcastToTextNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def encodeWchar():
    pass
  def encodeWtext(self):
    pass
  def eq(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def forceUpdate(self):
    pass
  def generate(self):
    pass
  def getAlign(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBin(self):
    pass
  def getBottom(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCardActual(self):
    pass
  def getCardAsSet(self):
    pass
  def getCardBorderSize(self):
    pass
  def getCardBorderUvPortion(self):
    pass
  def getCardColor(self):
    pass
  def getCardDecal(self):
    pass
  def getCardTexture(self):
    pass
  def getCardTransformed(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClockObject(self):
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultEncoding():
    pass
  def getDefaultFont():
    pass
  def getDisplayRegion(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawOrder(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEncodedChar(self):
    pass
  def getEncoding(self):
    pass
  def getFancyBits(self):
    pass
  def getFlattenFlags(self):
    pass
  def getFont(self):
    pass
  def getFrameActual(self):
    pass
  def getFrameAsSet(self):
    pass
  def getFrameColor(self):
    pass
  def getFrameCorners(self):
    pass
  def getFrameLineWidth(self):
    pass
  def getGlyphScale(self):
    pass
  def getGlyphShift(self):
    pass
  def getHeight(self):
    pass
  def getIndent(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalGeom(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLeft(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLineHeight(self):
    pass
  def getLowerRight3d(self):
    pass
  def getMaxRows(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChars(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumRows(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPreserveTrailingWhitespace(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getRight(self):
    pass
  def getShadow(self):
    pass
  def getShadowColor(self):
    pass
  def getSlant(self):
    pass
  def getSmallCaps(self):
    pass
  def getSmallCapsScale(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTabWidth(self):
    pass
  def getTag(self):
    pass
  def getText(self):
    pass
  def getTextAsAscii(self):
    pass
  def getTextColor(self):
    pass
  def getTextPattern(self):
    pass
  def getTextScale(self):
    pass
  def getTop(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnderscore(self):
    pass
  def getUnderscoreHeight(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getUnicodeChar(self):
    pass
  def getUpdateInterval(self):
    pass
  def getUpperLeft3d(self):
    pass
  def getUsageHint(self):
    pass
  def getWidth(self):
    pass
  def getWindow(self):
    pass
  def getWordwrap(self):
    pass
  def getWordwrappedText(self):
    pass
  def getWordwrappedWtext(self):
    pass
  def getWtext(self):
    pass
  def getWtextAsAscii(self):
    pass
  def hasAlign(self):
    pass
  def hasAttrib(self):
    pass
  def hasBin(self):
    pass
  def hasCard(self):
    pass
  def hasCardBorder(self):
    pass
  def hasCardTexture(self):
    pass
  def hasCharacter(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasDrawOrder(self):
    pass
  def hasEffect(self):
    pass
  def hasExactCharacter(self):
    pass
  def hasFont(self):
    pass
  def hasFrame(self):
    pass
  def hasGlyphScale(self):
    pass
  def hasGlyphShift(self):
    pass
  def hasIndent(self):
    pass
  def hasMaxRows(self):
    pass
  def hasName(self):
    pass
  def hasOverflow(self):
    pass
  def hasPreserveTrailingWhitespace(self):
    pass
  def hasPythonTag(self):
    pass
  def hasShadow(self):
    pass
  def hasShadowColor(self):
    pass
  def hasSlant(self):
    pass
  def hasSmallCaps(self):
    pass
  def hasSmallCapsScale(self):
    pass
  def hasTabWidth(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hasText(self):
    pass
  def hasTextColor(self):
    pass
  def hasTextScale(self):
    pass
  def hasUnderscore(self):
    pass
  def hasUnderscoreHeight(self):
    pass
  def hasWordwrap(self):
    pass
  def isAmbientLight(self):
    pass
  def isAnySpecified(self):
    pass
  def isBoundsStale(self):
    pass
  def isCardAsMargin(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isFrameAsMargin(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isWhitespace(self):
    pass
  def isWtext(self):
    pass
  def listTags(self):
    pass
  def lower():
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def makeLower(self):
    pass
  def makeUpper(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def reencodeText():
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAlign(self):
    pass
  def setAttrib(self):
    pass
  def setBin(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCardActual(self):
    pass
  def setCardAsMargin(self):
    pass
  def setCardBorder(self):
    pass
  def setCardColor(self):
    pass
  def setCardDecal(self):
    pass
  def setCardTexture(self):
    pass
  def setClockObject(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setDefaultEncoding():
    pass
  def setDefaultFont():
    pass
  def setDrawOrder(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setEncoding(self):
    pass
  def setFinal(self):
    pass
  def setFlattenFlags(self):
    pass
  def setFont(self):
    pass
  def setFrameActual(self):
    pass
  def setFrameAsMargin(self):
    pass
  def setFrameColor(self):
    pass
  def setFrameCorners(self):
    pass
  def setFrameLineWidth(self):
    pass
  def setGlyphScale(self):
    pass
  def setGlyphShift(self):
    pass
  def setIndent(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMaxRows(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPreserveTrailingWhitespace(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setShadow(self):
    pass
  def setShadowColor(self):
    pass
  def setSlant(self):
    pass
  def setSmallCaps(self):
    pass
  def setSmallCapsScale(self):
    pass
  def setState(self):
    pass
  def setTabWidth(self):
    pass
  def setTag(self):
    pass
  def setText(self):
    pass
  def setTextColor(self):
    pass
  def setTextPattern(self):
    pass
  def setTextScale(self):
    pass
  def setTransform(self):
    pass
  def setUnderscore(self):
    pass
  def setUnderscoreHeight(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setUnicodeChar(self):
    pass
  def setUpdateInterval(self):
    pass
  def setUsageHint(self):
    pass
  def setWordwrap(self):
    pass
  def setWtext(self):
    pass
  def setupWindow(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unicodeIsalpha():
    pass
  def unicodeIsdigit():
    pass
  def unicodeIslower():
    pass
  def unicodeIspunct():
    pass
  def unicodeIsspace():
    pass
  def unicodeIsupper():
    pass
  def unicodeTolower():
    pass
  def unicodeToupper():
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPandaNode(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTextEncoder(self):
    pass
  def upcastToTextProperties(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def update(self):
    pass
  def upper():
    pass
  def write(self):
    pass
class FreetypeFace:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class FreetypeFont:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def getClassType():
    pass
  def getFontPixelSize(self):
    pass
  def getLineHeight(self):
    pass
  def getName(self):
    pass
  def getNativeAntialias(self):
    pass
  def getPixelSize(self):
    pass
  def getPixelsPerUnit(self):
    pass
  def getPointSize(self):
    pass
  def getPointsPerInch():
    pass
  def getPointsPerUnit():
    pass
  def getScaleFactor(self):
    pass
  def getSpaceAdvance(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def setName(self):
    pass
  def setNativeAntialias(self):
    pass
  def setPixelSize(self):
    pass
  def setPixelsPerUnit(self):
    pass
  def setPointSize(self):
    pass
  def setScaleFactor(self):
    pass
class Frustum:
  def __init__(self):
    pass
  def makeOrtho(self):
    pass
  def makeOrtho2D(self):
    pass
  def makePerspective(self):
    pass
  def makePerspectiveHfov(self):
    pass
  def makePerspectiveVfov(self):
    pass
class FrustumD:
  def __init__(self):
    pass
  def makeOrtho(self):
    pass
  def makeOrtho2D(self):
    pass
  def makePerspective(self):
    pass
  def makePerspectiveHfov(self):
    pass
  def makePerspectiveVfov(self):
    pass
class GeoMipTerrain:
  def __init__(self):
    pass
  AFMLight = int

  AFMMedium = int

  AFMOff = int

  AFMStrong = int

  def clearColorMap(self):
    pass
  def colorMap(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def generate(self):
    pass
  def getBlockFromPos(self):
    pass
  def getBlockNodePath(self):
    pass
  def getBlockSize(self):
    pass
  def getBorderStitching(self):
    pass
  def getBruteforce(self):
    pass
  def getClassType():
    pass
  def getElevation(self):
    pass
  def getFocalPoint(self):
    pass
  def getMaxLevel(self):
    pass
  def getMinLevel(self):
    pass
  def getNormal(self):
    pass
  def getRoot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasColorMap(self):
    pass
  def heightfield(self):
    pass
  def isDirty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeSlopeImage(self):
    pass
  def setAutoFlatten(self):
    pass
  def setBlockSize(self):
    pass
  def setBorderStitching(self):
    pass
  def setBruteforce(self):
    pass
  def setColorMap(self):
    pass
  def setFactor(self):
    pass
  def setFar(self):
    pass
  def setFocalPoint(self):
    pass
  def setHeightfield(self):
    pass
  def setMinLevel(self):
    pass
  def setNear(self):
    pass
  def setNearFar(self):
    pass
  def update(self):
    pass
class Geom:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addPrimitive(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearBounds(self):
    pass
  def clearCache(self):
    pass
  def clearCacheStage(self):
    pass
  def clearPrimitives(self):
    pass
  def copyPrimitivesFrom(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def decomposeInPlace(self):
    pass
  def doubleside(self):
    pass
  def doublesideInPlace(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getGeomRendering(self):
    pass
  def getModified(self):
    pass
  def getNestedVertices(self):
    pass
  def getNumBytes(self):
    pass
  def getNumPrimitives(self):
    pass
  def getPrimitive(self):
    pass
  def getPrimitiveType(self):
    pass
  def getPrimitives(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertexData(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isPrepared(self):
    pass
  def makeCopy(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def makePointsInPlace(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def modifyPrimitive(self):
    pass
  def modifyVertexData(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def removePrimitive(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def reverseInPlace(self):
    pass
  def rotate(self):
    pass
  def rotateInPlace(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setPrimitive(self):
    pass
  def setUsageHint(self):
    pass
  def setVertexData(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def transformVertices(self):
    pass
  def unify(self):
    pass
  def unifyInPlace(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomCacheManager:
  def __init__(self):
    pass
  def flush(self):
    pass
  def getGlobalPtr():
    pass
  def getMaxSize(self):
    pass
  def getTotalSize(self):
    pass
  def setMaxSize(self):
    pass
class GeomContext:
  def __init__(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getGeom(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class GeomDrawCallbackData:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getForce(self):
    pass
  def getGsg(self):
    pass
  def getLostState(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def setLostState(self):
    pass
  def upcall(self):
    pass
class GeomEnums:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
class GeomLines:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomLinestrips:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addGeom(self):
    pass
  def addGeomsFrom(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def checkValid(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDefaultCollideMask():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getGeom(self):
    pass
  def getGeomState(self):
    pass
  def getGeomStates(self):
    pass
  def getGeoms(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumGeoms(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPreserved(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def modifyGeom(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeAllGeoms(self):
    pass
  def removeChild(self):
    pass
  def removeGeom(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setGeom(self):
    pass
  def setGeomState(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPreserved(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unify(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeGeoms(self):
    pass
  def writeVerbose(self):
    pass
class GeomPoints:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomPrimitive:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomTextGlyph:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addPrimitive(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearBounds(self):
    pass
  def clearCache(self):
    pass
  def clearCacheStage(self):
    pass
  def clearPrimitives(self):
    pass
  def copyPrimitivesFrom(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def decomposeInPlace(self):
    pass
  def doubleside(self):
    pass
  def doublesideInPlace(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getGeomRendering(self):
    pass
  def getModified(self):
    pass
  def getNestedVertices(self):
    pass
  def getNumBytes(self):
    pass
  def getNumPrimitives(self):
    pass
  def getPrimitive(self):
    pass
  def getPrimitiveType(self):
    pass
  def getPrimitives(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertexData(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isPrepared(self):
    pass
  def makeCopy(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def makePointsInPlace(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def modifyPrimitive(self):
    pass
  def modifyVertexData(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def removePrimitive(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def reverseInPlace(self):
    pass
  def rotate(self):
    pass
  def rotateInPlace(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setPrimitive(self):
    pass
  def setUsageHint(self):
    pass
  def setVertexData(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def transformVertices(self):
    pass
  def unify(self):
    pass
  def unifyInPlace(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomTriangles:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomTrifans:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomTristrips:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addConsecutiveVertices(self):
    pass
  def addNextVertices(self):
    pass
  def addVertex(self):
    pass
  def addVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def checkValid(self):
    pass
  def clearMinmax(self):
    pass
  def clearVertices(self):
    pass
  def closePrimitive(self):
    pass
  def decodeFromBamStream():
    pass
  def decompose(self):
    pass
  def doubleside(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getEnds(self):
    pass
  def getFirstVertex(self):
    pass
  def getGeomRendering(self):
    pass
  def getIndexStride(self):
    pass
  def getIndexType(self):
    pass
  def getMaxVertex(self):
    pass
  def getMaxs(self):
    pass
  def getMinNumVerticesPerPrimitive(self):
    pass
  def getMinVertex(self):
    pass
  def getMins(self):
    pass
  def getModified(self):
    pass
  def getNumBytes(self):
    pass
  def getNumFaces(self):
    pass
  def getNumPrimitives(self):
    pass
  def getNumUnusedVerticesPerPrimitive(self):
    pass
  def getNumVertices(self):
    pass
  def getNumVerticesPerPrimitive(self):
    pass
  def getPrimitiveEnd(self):
    pass
  def getPrimitiveMaxVertex(self):
    pass
  def getPrimitiveMinVertex(self):
    pass
  def getPrimitiveNumFaces(self):
    pass
  def getPrimitiveNumVertices(self):
    pass
  def getPrimitiveStart(self):
    pass
  def getPrimitiveType(self):
    pass
  def getRefCount(self):
    pass
  def getShadeModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isComposite(self):
    pass
  def isExactType(self):
    pass
  def isIndexed(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def makeIndexed(self):
    pass
  def makeNonindexed(self):
    pass
  def makePoints(self):
    pass
  def markBamModified(self):
    pass
  def matchShadeModel(self):
    pass
  def modifyEnds(self):
    pass
  def modifyVertices(self):
    pass
  def offsetVertices(self):
    pass
  def output(self):
    pass
  def packVertices(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def reverse(self):
    pass
  def rotate(self):
    pass
  def setEnds(self):
    pass
  def setIndexType(self):
    pass
  def setMinmax(self):
    pass
  def setNonindexedVertices(self):
    pass
  def setShadeModel(self):
    pass
  def setUsageHint(self):
    pass
  def setVertices(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomVertexAnimationSpec:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def assign(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def getAnimationType(self):
    pass
  def getIndexedTransforms(self):
    pass
  def getNumTransforms(self):
    pass
  def output(self):
    pass
  def setHardware(self):
    pass
  def setNone(self):
    pass
  def setPanda(self):
    pass
class GeomVertexArrayData:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearRows(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def dequeueLru(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def downcastToVertexDataPage(self):
    pass
  def encodeToBamStream(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def getArrayFormat(self):
    pass
  def getBamModified(self):
    pass
  def getBook():
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getHandle(self):
    pass
  def getIndependentLru():
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def getModified(self):
    pass
  def getNumRows(self):
    pass
  def getRefCount(self):
    pass
  def getSmallLru():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def hasColumn(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isPrepared(self):
    pass
  def lruEpoch():
    pass
  def markBamModified(self):
    pass
  def markUsedLru(self):
    pass
  def modifyHandle(self):
    pass
  def output(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def requestResident(self):
    pass
  def setLruSize(self):
    pass
  def setNumRows(self):
    pass
  def setUsageHint(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncleanSetNumRows(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToSimpleLruPage(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomVertexArrayDataHandle:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def clearRows(self):
    pass
  def copyDataFrom(self):
    pass
  def copySubdataFrom(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getArrayFormat(self):
    pass
  def getClassType():
    pass
  def getData(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getModified(self):
    pass
  def getNumRows(self):
    pass
  def getObject(self):
    pass
  def getRefCount(self):
    pass
  def getSubdata(self):
    pass
  def getUsageHint(self):
    pass
  def markUsed(self):
    pass
  def ref(self):
    pass
  def requestResident(self):
    pass
  def setData(self):
    pass
  def setNumRows(self):
    pass
  def setSubdata(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncleanSetNumRows(self):
    pass
  def unref(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
class GeomVertexArrayFormat:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addColumn(self):
    pass
  def assign(self):
    pass
  def clearColumns(self):
    pass
  def countUnusedSpace(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getColumn(self):
    pass
  def getColumns(self):
    pass
  def getNumColumns(self):
    pass
  def getPadTo(self):
    pass
  def getRefCount(self):
    pass
  def getStride(self):
    pass
  def getTotalBytes(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasColumn(self):
    pass
  def isDataSubsetOf(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isRegistered(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def packColumns(self):
    pass
  def ref(self):
    pass
  def registerFormat():
    pass
  def removeColumn(self):
    pass
  def setStride(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithData(self):
    pass
class GeomVertexColumn:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def assign(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def getComponentBytes(self):
    pass
  def getContents(self):
    pass
  def getName(self):
    pass
  def getNumComponents(self):
    pass
  def getNumValues(self):
    pass
  def getNumericType(self):
    pass
  def getStart(self):
    pass
  def getTotalBytes(self):
    pass
  def hasHomogeneousCoord(self):
    pass
  def isBytewiseEquivalent(self):
    pass
  def output(self):
    pass
  def overlapsWith(self):
    pass
class GeomVertexData:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def animateVertices(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearAnimatedVertices(self):
    pass
  def clearCache(self):
    pass
  def clearCacheStage(self):
    pass
  def clearRows(self):
    pass
  def clearSliderTable(self):
    pass
  def clearTransformBlendTable(self):
    pass
  def clearTransformTable(self):
    pass
  def compareTo(self):
    pass
  def convertTo(self):
    pass
  def copyFrom(self):
    pass
  def copyRowFrom(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getArray(self):
    pass
  def getArrays(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getFormat(self):
    pass
  def getModified(self):
    pass
  def getName(self):
    pass
  def getNumArrays(self):
    pass
  def getNumBytes(self):
    pass
  def getNumRows(self):
    pass
  def getRefCount(self):
    pass
  def getSliderTable(self):
    pass
  def getTransformBlendTable(self):
    pass
  def getTransformTable(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUsageHint(self):
    pass
  def hasColumn(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def modifyArray(self):
    pass
  def modifyTransformBlendTable(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def replaceColumn(self):
    pass
  def requestResident(self):
    pass
  def reverseNormals(self):
    pass
  def scaleColor(self):
    pass
  def setArray(self):
    pass
  def setColor(self):
    pass
  def setFormat(self):
    pass
  def setName(self):
    pass
  def setNumRows(self):
    pass
  def setSliderTable(self):
    pass
  def setTransformBlendTable(self):
    pass
  def setTransformTable(self):
    pass
  def setUsageHint(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncleanSetNumRows(self):
    pass
  def unref(self):
    pass
  def upcastToCopyOnWriteObject(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class GeomVertexFormat:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addArray(self):
    pass
  def assign(self):
    pass
  def clearArrays(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getAnimation(self):
    pass
  def getArray(self):
    pass
  def getArrayWith(self):
    pass
  def getArrays(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getColumn(self):
    pass
  def getMorphBase(self):
    pass
  def getMorphBases(self):
    pass
  def getMorphDelta(self):
    pass
  def getMorphDeltas(self):
    pass
  def getMorphSlider(self):
    pass
  def getMorphSliders(self):
    pass
  def getNumArrays(self):
    pass
  def getNumColumns(self):
    pass
  def getNumMorphs(self):
    pass
  def getNumPoints(self):
    pass
  def getNumTexcoords(self):
    pass
  def getNumVectors(self):
    pass
  def getPoint(self):
    pass
  def getPoints(self):
    pass
  def getPostAnimatedFormat(self):
    pass
  def getRefCount(self):
    pass
  def getTexcoord(self):
    pass
  def getTexcoords(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnionFormat(self):
    pass
  def getV3():
    pass
  def getV3c4():
    pass
  def getV3c4t2():
    pass
  def getV3cp():
    pass
  def getV3cpt2():
    pass
  def getV3n3():
    pass
  def getV3n3c4():
    pass
  def getV3n3c4t2():
    pass
  def getV3n3cp():
    pass
  def getV3n3cpt2():
    pass
  def getV3n3t2():
    pass
  def getV3t2():
    pass
  def getVector(self):
    pass
  def getVectors(self):
    pass
  def hasColumn(self):
    pass
  def insertArray(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isRegistered(self):
    pass
  def markBamModified(self):
    pass
  def modifyArray(self):
    pass
  def output(self):
    pass
  def packColumns(self):
    pass
  def ref(self):
    pass
  def registerFormat():
    pass
  def removeArray(self):
    pass
  def removeColumn(self):
    pass
  def setAnimation(self):
    pass
  def setArray(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToGeomEnums(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithData(self):
    pass
class GeomVertexReader:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def assign(self):
    pass
  def clear(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToGeomVertexRewriter(self):
    pass
  def getArray(self):
    pass
  def getArrayData(self):
    pass
  def getColumn(self):
    pass
  def getCurrentThread(self):
    pass
  def getData1f(self):
    pass
  def getData1i(self):
    pass
  def getData2f(self):
    pass
  def getData3f(self):
    pass
  def getData4f(self):
    pass
  def getForce(self):
    pass
  def getReadRow(self):
    pass
  def getStartRow(self):
    pass
  def getVertexData(self):
    pass
  def hasColumn(self):
    pass
  def isAtEnd(self):
    pass
  def output(self):
    pass
  def setColumn(self):
    pass
  def setForce(self):
    pass
  def setRow(self):
    pass
class GeomVertexRewriter:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addData1f(self):
    pass
  def addData1i(self):
    pass
  def addData2f(self):
    pass
  def addData2i(self):
    pass
  def addData3f(self):
    pass
  def addData3i(self):
    pass
  def addData4f(self):
    pass
  def addData4i(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToGeomVertexRewriter(self):
    pass
  def getArray(self):
    pass
  def getArrayData(self):
    pass
  def getColumn(self):
    pass
  def getCurrentThread(self):
    pass
  def getData1f(self):
    pass
  def getData1i(self):
    pass
  def getData2f(self):
    pass
  def getData3f(self):
    pass
  def getData4f(self):
    pass
  def getForce(self):
    pass
  def getReadRow(self):
    pass
  def getStartRow(self):
    pass
  def getVertexData(self):
    pass
  def getWriteRow(self):
    pass
  def hasColumn(self):
    pass
  def isAtEnd(self):
    pass
  def output(self):
    pass
  def setColumn(self):
    pass
  def setData1f(self):
    pass
  def setData1i(self):
    pass
  def setData2f(self):
    pass
  def setData2i(self):
    pass
  def setData3f(self):
    pass
  def setData3i(self):
    pass
  def setData4f(self):
    pass
  def setData4i(self):
    pass
  def setForce(self):
    pass
  def setRow(self):
    pass
  def upcastToGeomVertexReader(self):
    pass
  def upcastToGeomVertexWriter(self):
    pass
class GeomVertexWriter:
  def __init__(self):
    pass
  ATHardware = int

  ATNone = int

  ATPanda = int

  CClipPoint = int

  CColor = int

  CIndex = int

  CMorphDelta = int

  COther = int

  CPoint = int

  CTexcoord = int

  CVector = int

  GRCompositeBits = int

  GRFlatFirstVertex = int

  GRFlatLastVertex = int

  GRIndexedBits = int

  GRIndexedOther = int

  GRIndexedPoint = int

  GRLineStrip = int

  GRPerPointSize = int

  GRPoint = int

  GRPointAspectRatio = int

  GRPointBits = int

  GRPointPerspective = int

  GRPointRotate = int

  GRPointScale = int

  GRPointSprite = int

  GRPointSpriteTexMatrix = int

  GRPointUniformSize = int

  GRShadeModelBits = int

  GRTexcoordLightVector = int

  GRTriangleFan = int

  GRTriangleStrip = int

  NTFloat32 = int

  NTPackedDabc = int

  NTPackedDcba = int

  NTUint16 = int

  NTUint32 = int

  NTUint8 = int

  PTLines = int

  PTNone = int

  PTPoints = int

  PTPolygons = int

  SMFlatFirstVertex = int

  SMFlatLastVertex = int

  SMSmooth = int

  SMUniform = int

  UHClient = int

  UHDynamic = int

  UHStatic = int

  UHStream = int

  UHUnspecified = int

  def addData1f(self):
    pass
  def addData1i(self):
    pass
  def addData2f(self):
    pass
  def addData2i(self):
    pass
  def addData3f(self):
    pass
  def addData3i(self):
    pass
  def addData4f(self):
    pass
  def addData4i(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def downcastToGeom(self):
    pass
  def downcastToGeomPrimitive(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToGeomVertexArrayDataHandle(self):
    pass
  def downcastToGeomVertexArrayFormat(self):
    pass
  def downcastToGeomVertexData(self):
    pass
  def downcastToGeomVertexFormat(self):
    pass
  def downcastToGeomVertexRewriter(self):
    pass
  def getArray(self):
    pass
  def getArrayData(self):
    pass
  def getColumn(self):
    pass
  def getCurrentThread(self):
    pass
  def getStartRow(self):
    pass
  def getVertexData(self):
    pass
  def getWriteRow(self):
    pass
  def hasColumn(self):
    pass
  def isAtEnd(self):
    pass
  def output(self):
    pass
  def setColumn(self):
    pass
  def setData1f(self):
    pass
  def setData1i(self):
    pass
  def setData2f(self):
    pass
  def setData2i(self):
    pass
  def setData3f(self):
    pass
  def setData3i(self):
    pass
  def setData4f(self):
    pass
  def setData4i(self):
    pass
  def setRow(self):
    pass
class GeometricBoundingVolume:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class GraphicsBuffer:
  def __init__(self):
    pass
  FMParasite = int

  FMRefresh = int

  FMRender = int

  RTMBindOrCopy = int

  RTMCopyRam = int

  RTMCopyTexture = int

  RTMNone = int

  RTMTriggeredCopyRam = int

  RTMTriggeredCopyTexture = int

  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def addRenderTexture(self):
    pass
  def clearChildSort(self):
    pass
  def clearDeleteFlag(self):
    pass
  def clearRenderTextures(self):
    pass
  def countTextures(self):
    pass
  def decodeFromBamStream():
    pass
  def disableClears(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActiveDisplayRegion(self):
    pass
  def getActiveDisplayRegions(self):
    pass
  def getBamModified(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getDeleteFlag(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getEngine(self):
    pass
  def getFbProperties(self):
    pass
  def getFbXSize(self):
    pass
  def getFbYSize(self):
    pass
  def getGsg(self):
    pass
  def getInverted(self):
    pass
  def getLeftEyeColorMask(self):
    pass
  def getName(self):
    pass
  def getNumActiveDisplayRegions(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getOneShot(self):
    pass
  def getPipe(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelZoom(self):
    pass
  def getRedBlueStereo(self):
    pass
  def getRefCount(self):
    pass
  def getRenderbufferType():
    pass
  def getRightEyeColorMask(self):
    pass
  def getRtmMode(self):
    pass
  def getScreenshot(self):
    pass
  def getSort(self):
    pass
  def getTexture(self):
    pass
  def getTextureCard(self):
    pass
  def getTexturePlane(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def hasSize(self):
    pass
  def hasTexture(self):
    pass
  def isActive(self):
    pass
  def isAnyClearActive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isStereo(self):
    pass
  def isValid(self):
    pass
  def makeCubeMap(self):
    pass
  def makeDisplayRegion(self):
    pass
  def makeMonoDisplayRegion(self):
    pass
  def makeScreenshotFilename():
    pass
  def makeStereoDisplayRegion(self):
    pass
  def makeTextureBuffer(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def removeAllDisplayRegions(self):
    pass
  def removeDisplayRegion(self):
    pass
  def saveScreenshot(self):
    pass
  def saveScreenshotDefault(self):
    pass
  def setActive(self):
    pass
  def setChildSort(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setInverted(self):
    pass
  def setOneShot(self):
    pass
  def setPixelZoom(self):
    pass
  def setRedBlueStereo(self):
    pass
  def setSize(self):
    pass
  def setSort(self):
    pass
  def setupRenderTexture(self):
    pass
  def shareDepthBuffer(self):
    pass
  def supportsPixelZoom(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def triggerCopy(self):
    pass
  def unref(self):
    pass
  def unshareDepthBuffer(self):
    pass
  def upcastToDrawableRegion(self):
    pass
  def upcastToGraphicsOutputBase(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class GraphicsDevice:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getPipe(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class GraphicsEngine:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extractTextureData(self):
    pass
  def flipFrame(self):
    pass
  def getAutoFlip(self):
    pass
  def getClassType():
    pass
  def getDefaultLoader(self):
    pass
  def getGlobalPtr():
    pass
  def getNumWindows(self):
    pass
  def getPortalCull(self):
    pass
  def getRefCount(self):
    pass
  def getThreadingModel(self):
    pass
  def getWindow(self):
    pass
  def getWindows(self):
    pass
  def isEmpty(self):
    pass
  def makeBuffer(self):
    pass
  def makeOutput(self):
    pass
  def makeParasite(self):
    pass
  def openWindows(self):
    pass
  def ref(self):
    pass
  def removeAllWindows(self):
    pass
  def removeWindow(self):
    pass
  def renderFrame(self):
    pass
  def resetAllWindows(self):
    pass
  def setAutoFlip(self):
    pass
  def setDefaultLoader(self):
    pass
  def setPortalCull(self):
    pass
  def setThreadingModel(self):
    pass
  def syncFrame(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class GraphicsOutput:
  def __init__(self):
    pass
  FMParasite = int

  FMRefresh = int

  FMRender = int

  RTMBindOrCopy = int

  RTMCopyRam = int

  RTMCopyTexture = int

  RTMNone = int

  RTMTriggeredCopyRam = int

  RTMTriggeredCopyTexture = int

  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def addRenderTexture(self):
    pass
  def clearChildSort(self):
    pass
  def clearDeleteFlag(self):
    pass
  def clearRenderTextures(self):
    pass
  def countTextures(self):
    pass
  def decodeFromBamStream():
    pass
  def disableClears(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActiveDisplayRegion(self):
    pass
  def getActiveDisplayRegions(self):
    pass
  def getBamModified(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getDeleteFlag(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getEngine(self):
    pass
  def getFbProperties(self):
    pass
  def getFbXSize(self):
    pass
  def getFbYSize(self):
    pass
  def getGsg(self):
    pass
  def getInverted(self):
    pass
  def getLeftEyeColorMask(self):
    pass
  def getName(self):
    pass
  def getNumActiveDisplayRegions(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getOneShot(self):
    pass
  def getPipe(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelZoom(self):
    pass
  def getRedBlueStereo(self):
    pass
  def getRefCount(self):
    pass
  def getRenderbufferType():
    pass
  def getRightEyeColorMask(self):
    pass
  def getRtmMode(self):
    pass
  def getScreenshot(self):
    pass
  def getSort(self):
    pass
  def getTexture(self):
    pass
  def getTextureCard(self):
    pass
  def getTexturePlane(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def hasSize(self):
    pass
  def hasTexture(self):
    pass
  def isActive(self):
    pass
  def isAnyClearActive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isStereo(self):
    pass
  def isValid(self):
    pass
  def makeCubeMap(self):
    pass
  def makeDisplayRegion(self):
    pass
  def makeMonoDisplayRegion(self):
    pass
  def makeScreenshotFilename():
    pass
  def makeStereoDisplayRegion(self):
    pass
  def makeTextureBuffer(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def removeAllDisplayRegions(self):
    pass
  def removeDisplayRegion(self):
    pass
  def saveScreenshot(self):
    pass
  def saveScreenshotDefault(self):
    pass
  def setActive(self):
    pass
  def setChildSort(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setInverted(self):
    pass
  def setOneShot(self):
    pass
  def setPixelZoom(self):
    pass
  def setRedBlueStereo(self):
    pass
  def setSort(self):
    pass
  def setupRenderTexture(self):
    pass
  def shareDepthBuffer(self):
    pass
  def supportsPixelZoom(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def triggerCopy(self):
    pass
  def unref(self):
    pass
  def unshareDepthBuffer(self):
    pass
  def upcastToDrawableRegion(self):
    pass
  def upcastToGraphicsOutputBase(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class GraphicsOutputBase:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def setSort(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class GraphicsPipe:
  def __init__(self):
    pass
  BFCanBindColor = int

  BFCanBindEvery = int

  BFFbPropsOptional = int

  BFRefuseParasite = int

  BFRefuseWindow = int

  BFRequireParasite = int

  BFRequireWindow = int

  BFResizeable = int

  BFRttCumulative = int

  BFSizePower2 = int

  BFSizeSquare = int

  BFSizeTrackHost = int

  OTBuffer = int

  OTFullscreenWindow = int

  OTTextureBuffer = int

  OTWindow = int

  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getDisplayHeight(self):
    pass
  def getDisplayInformation(self):
    pass
  def getDisplayWidth(self):
    pass
  def getInterfaceName(self):
    pass
  def getRefCount(self):
    pass
  def getSupportedTypes(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def lookupCpuData(self):
    pass
  def ref(self):
    pass
  def supportsType(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class GraphicsPipeSelection:
  def __init__(self):
    pass
  def getGlobalPtr():
    pass
  def getNumAuxModules(self):
    pass
  def getNumPipeTypes(self):
    pass
  def getPipeType(self):
    pass
  def getPipeTypes(self):
    pass
  def loadAuxModules(self):
    pass
  def makeDefaultPipe(self):
    pass
  def makeModulePipe(self):
    pass
  def makePipe(self):
    pass
  def printPipeTypes(self):
    pass
class GraphicsStateGuardian:
  def __init__(self):
    pass
  SM00 = int

  SM11 = int

  SM20 = int

  SM2X = int

  SM30 = int

  SM40 = int

  def beginScene(self):
    pass
  def clearFlashTexture(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def endScene(self):
    pass
  def getAlphaScaleTextureStage():
    pass
  def getAlphaScaleViaTexture(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getColorScaleViaLighting(self):
    pass
  def getCoordinateSystem(self):
    pass
  def getCopyTextureInverted(self):
    pass
  def getDefaultGsg():
    pass
  def getEffectiveIncompleteRender(self):
    pass
  def getEngine(self):
    pass
  def getFlashTexture(self):
    pass
  def getGamma(self):
    pass
  def getGsg():
    pass
  def getGsgs(self):
    pass
  def getIncompleteRender(self):
    pass
  def getInternalCoordinateSystem(self):
    pass
  def getLoader(self):
    pass
  def getMax3dTextureDimension(self):
    pass
  def getMaxClipPlanes(self):
    pass
  def getMaxCubeMapDimension(self):
    pass
  def getMaxLights(self):
    pass
  def getMaxTextureDimension(self):
    pass
  def getMaxTextureStages(self):
    pass
  def getMaxVertexTransformIndices(self):
    pass
  def getMaxVertexTransforms(self):
    pass
  def getMaxVerticesPerArray(self):
    pass
  def getMaxVerticesPerPrimitive(self):
    pass
  def getMaximumSimultaneousRenderTargets(self):
    pass
  def getNumGsgs():
    pass
  def getPipe(self):
    pass
  def getPreparedObjects(self):
    pass
  def getPreparedTextures(self):
    pass
  def getRefCount(self):
    pass
  def getRuntimeColorScale(self):
    pass
  def getScene(self):
    pass
  def getShaderModel(self):
    pass
  def getSupportedGeomRendering(self):
    pass
  def getSupports3dTexture(self):
    pass
  def getSupportsBasicShaders(self):
    pass
  def getSupportsCompressedTexture(self):
    pass
  def getSupportsCompressedTextureFormat(self):
    pass
  def getSupportsCubeMap(self):
    pass
  def getSupportsDepthStencil(self):
    pass
  def getSupportsDepthTexture(self):
    pass
  def getSupportsGenerateMipmap(self):
    pass
  def getSupportsGeometryInstancing(self):
    pass
  def getSupportsGlsl(self):
    pass
  def getSupportsMultisample(self):
    pass
  def getSupportsOcclusionQuery(self):
    pass
  def getSupportsRenderTexture(self):
    pass
  def getSupportsShadowFilter(self):
    pass
  def getSupportsStencil(self):
    pass
  def getSupportsTexNonPow2(self):
    pass
  def getSupportsTextureCombine(self):
    pass
  def getSupportsTextureDot3(self):
    pass
  def getSupportsTextureSavedResult(self):
    pass
  def getSupportsTwoSidedStencil(self):
    pass
  def getTextureQualityOverride(self):
    pass
  def getThreadingModel(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isActive(self):
    pass
  def isExactType(self):
    pass
  def isHardware(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def markBamModified(self):
    pass
  def needsReset(self):
    pass
  def prefersTriangleStrips(self):
    pass
  def ref(self):
    pass
  def releaseAll(self):
    pass
  def releaseAllGeoms(self):
    pass
  def releaseAllIndexBuffers(self):
    pass
  def releaseAllTextures(self):
    pass
  def releaseAllVertexBuffers(self):
    pass
  def restoreGamma(self):
    pass
  def setActive(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setDefaultGsg():
    pass
  def setFlashTexture(self):
    pass
  def setGamma(self):
    pass
  def setIncompleteRender(self):
    pass
  def setLoader(self):
    pass
  def setScene(self):
    pass
  def setShaderModel(self):
    pass
  def setTextureQualityOverride(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class GraphicsStateGuardianBase:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getDefaultGsg():
    pass
  def getEffectiveIncompleteRender(self):
    pass
  def getGsg():
    pass
  def getGsgs(self):
    pass
  def getIncompleteRender(self):
    pass
  def getMaxTextureDimension(self):
    pass
  def getMaxVerticesPerArray(self):
    pass
  def getMaxVerticesPerPrimitive(self):
    pass
  def getNumGsgs():
    pass
  def getRefCount(self):
    pass
  def getSupportedGeomRendering(self):
    pass
  def getSupportsCompressedTextureFormat(self):
    pass
  def getSupportsMultisample(self):
    pass
  def getSupportsOcclusionQuery(self):
    pass
  def getSupportsShadowFilter(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def prefersTriangleStrips(self):
    pass
  def ref(self):
    pass
  def setDefaultGsg():
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class GraphicsThreadingModel:
  def __init__(self):
    pass
  def assign(self):
    pass
  def getCullName(self):
    pass
  def getCullSorting(self):
    pass
  def getCullStage(self):
    pass
  def getDrawName(self):
    pass
  def getDrawStage(self):
    pass
  def getModel(self):
    pass
  def isDefault(self):
    pass
  def isSingleThreaded(self):
    pass
  def output(self):
    pass
  def setCullName(self):
    pass
  def setCullSorting(self):
    pass
  def setDrawName(self):
    pass
class GraphicsWindow:
  def __init__(self):
    pass
  FMParasite = int

  FMRefresh = int

  FMRender = int

  RTMBindOrCopy = int

  RTMCopyRam = int

  RTMCopyTexture = int

  RTMNone = int

  RTMTriggeredCopyRam = int

  RTMTriggeredCopyTexture = int

  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def addRenderTexture(self):
    pass
  def clearChildSort(self):
    pass
  def clearDeleteFlag(self):
    pass
  def clearRejectedProperties(self):
    pass
  def clearRenderTextures(self):
    pass
  def closeIme(self):
    pass
  def countTextures(self):
    pass
  def decodeFromBamStream():
    pass
  def disableClears(self):
    pass
  def disablePointerEvents(self):
    pass
  def disablePointerMode(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def enablePointerEvents(self):
    pass
  def enablePointerMode(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActiveDisplayRegion(self):
    pass
  def getActiveDisplayRegions(self):
    pass
  def getBamModified(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getCloseRequestEvent(self):
    pass
  def getDeleteFlag(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getEngine(self):
    pass
  def getFbProperties(self):
    pass
  def getFbXSize(self):
    pass
  def getFbYSize(self):
    pass
  def getGsg(self):
    pass
  def getInputDeviceName(self):
    pass
  def getInputDeviceNames(self):
    pass
  def getInverted(self):
    pass
  def getLeftEyeColorMask(self):
    pass
  def getName(self):
    pass
  def getNumActiveDisplayRegions(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getNumInputDevices(self):
    pass
  def getOneShot(self):
    pass
  def getPipe(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelZoom(self):
    pass
  def getPointer(self):
    pass
  def getProperties(self):
    pass
  def getRedBlueStereo(self):
    pass
  def getRefCount(self):
    pass
  def getRejectedProperties(self):
    pass
  def getRenderbufferType():
    pass
  def getRequestedProperties(self):
    pass
  def getRightEyeColorMask(self):
    pass
  def getRtmMode(self):
    pass
  def getScreenshot(self):
    pass
  def getSort(self):
    pass
  def getTexture(self):
    pass
  def getTextureCard(self):
    pass
  def getTexturePlane(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWindowEvent(self):
    pass
  def getWindowHandle(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def hasKeyboard(self):
    pass
  def hasPointer(self):
    pass
  def hasSize(self):
    pass
  def hasTexture(self):
    pass
  def isActive(self):
    pass
  def isAnyClearActive(self):
    pass
  def isClosed(self):
    pass
  def isExactType(self):
    pass
  def isFullscreen(self):
    pass
  def isOfType(self):
    pass
  def isStereo(self):
    pass
  def isValid(self):
    pass
  def makeCubeMap(self):
    pass
  def makeDisplayRegion(self):
    pass
  def makeMonoDisplayRegion(self):
    pass
  def makeScreenshotFilename():
    pass
  def makeStereoDisplayRegion(self):
    pass
  def makeTextureBuffer(self):
    pass
  def markBamModified(self):
    pass
  def movePointer(self):
    pass
  def ref(self):
    pass
  def removeAllDisplayRegions(self):
    pass
  def removeDisplayRegion(self):
    pass
  def requestProperties(self):
    pass
  def saveScreenshot(self):
    pass
  def saveScreenshotDefault(self):
    pass
  def setActive(self):
    pass
  def setChildSort(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setCloseRequestEvent(self):
    pass
  def setInverted(self):
    pass
  def setOneShot(self):
    pass
  def setPixelZoom(self):
    pass
  def setRedBlueStereo(self):
    pass
  def setSort(self):
    pass
  def setWindowEvent(self):
    pass
  def setupRenderTexture(self):
    pass
  def shareDepthBuffer(self):
    pass
  def supportsPixelZoom(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def triggerCopy(self):
    pass
  def unref(self):
    pass
  def unshareDepthBuffer(self):
    pass
  def upcastToDrawableRegion(self):
    pass
  def upcastToGraphicsOutputBase(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
HCCUT = int

HCFREE = int

HCG1 = int

HCSMOOTH = int

class HeightfieldTesselator:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def generate(self):
    pass
  def getClassType():
    pass
  def getElevation(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def heightfield(self):
    pass
  def output(self):
    pass
  def setFocalPoint(self):
    pass
  def setHeightfield(self):
    pass
  def setHorizontalScale(self):
    pass
  def setMaxTriangles(self):
    pass
  def setName(self):
    pass
  def setPolyCount(self):
    pass
  def setVerticalScale(self):
    pass
  def setVisibilityRadius(self):
    pass
class HermiteCurve:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def adjustPoint(self):
    pass
  def adjustPt(self):
    pass
  def adjustTangent(self):
    pass
  def appendCv(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcLength(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToNurbsCurve(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findLength(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def get2ndtangent(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCurveType(self):
    pass
  def getCvIn(self):
    pass
  def getCvName(self):
    pass
  def getCvOut(self):
    pass
  def getCvPoint(self):
    pass
  def getCvTstart(self):
    pass
  def getCvType(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMaxT(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumCvs(self):
    pass
  def getNumDimensions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPt(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTangent(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def insertCv(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeAllCvs(self):
    pass
  def removeChild(self):
    pass
  def removeCv(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCurveType(self):
    pass
  def setCvIn(self):
    pass
  def setCvName(self):
    pass
  def setCvOut(self):
    pass
  def setCvPoint(self):
    pass
  def setCvTstart(self):
    pass
  def setCvType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNumDimensions(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def stitch(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeCv(self):
    pass
  def writeEgg(self):
    pass
class HprLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def takeLongest(self):
    pass
  def takeShortest(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class HprScaleLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def takeLongest(self):
    pass
  def takeShortest(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class IndexBufferContext:
  def __init__(self):
    pass
  def assign(self):
    pass
  def dequeueLru(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToIndexBufferContext(self):
    pass
  def downcastToTextureContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToVertexBufferContext(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def getActive(self):
    pass
  def getClassType():
    pass
  def getData(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def getModified(self):
    pass
  def getNumFrames(self):
    pass
  def getNumInactiveFrames(self):
    pass
  def getResident(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markUsedLru(self):
    pass
  def output(self):
    pass
  def setLruSize(self):
    pass
  def upcastToAdaptiveLruPage(self):
    pass
  def upcastToBufferContext(self):
    pass
  def upcastToSavedContext(self):
    pass
  def write(self):
    pass
class InkblotVideo:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class InkblotVideoCursor:
  def __init__(self):
    pass
  def aborted(self):
    pass
  def canSeek(self):
    pass
  def canSeekFast(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def fetchIntoBitbucket(self):
    pass
  def fetchIntoTexture(self):
    pass
  def fetchIntoTextureAlpha(self):
    pass
  def fetchIntoTextureRgb(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumComponents(self):
    pass
  def getRefCount(self):
    pass
  def getSource(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lastStart(self):
    pass
  def length(self):
    pass
  def markBamModified(self):
    pass
  def nextStart(self):
    pass
  def ready(self):
    pass
  def ref(self):
    pass
  def setupTexture(self):
    pass
  def sizeX(self):
    pass
  def sizeY(self):
    pass
  def streaming(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class SimpleLerpFunctorInt:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorInt:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class InternalName:
  def __init__(self):
    pass
  def append(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findAncestor(self):
    pass
  def getAncestor(self):
    pass
  def getAspectRatio():
    pass
  def getBamModified(self):
    pass
  def getBasename(self):
    pass
  def getBinormal():
    pass
  def getBinormalName():
    pass
  def getCamera():
    pass
  def getClassType():
    pass
  def getColor():
    pass
  def getError():
    pass
  def getIndex():
    pass
  def getModel():
    pass
  def getMorph():
    pass
  def getName(self):
    pass
  def getNetBasename(self):
    pass
  def getNormal():
    pass
  def getParent(self):
    pass
  def getRefCount(self):
    pass
  def getRoot():
    pass
  def getRotate():
    pass
  def getSize():
    pass
  def getTangent():
    pass
  def getTangentName():
    pass
  def getTexcoord():
    pass
  def getTexcoordName():
    pass
  def getTop(self):
    pass
  def getTransformBlend():
    pass
  def getTransformIndex():
    pass
  def getTransformWeight():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getVertex():
    pass
  def getView():
    pass
  def getWorld():
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class InternalNameCollection:
  def __init__(self):
    pass
  def addName(self):
    pass
  def addNamesFrom(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def getName(self):
    pass
  def getNames(self):
    pass
  def getNumNames(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def removeDuplicateNames(self):
    pass
  def removeName(self):
    pass
  def removeNamesFrom(self):
    pass
  def size(self):
    pass
  def write(self):
    pass
class JointVertexTransform:
  def __init__(self):
    pass
  def accumulateMatrix(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getGlobalModified():
    pass
  def getJoint(self):
    pass
  def getMatrix(self):
    pass
  def getModified(self):
    pass
  def getNextModified():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def multMatrix(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class KeyboardButton:
  def __init__(self):
    pass
  def _del():
    pass
  def alt():
    pass
  def asciiKey():
    pass
  def backspace():
    pass
  def capsLock():
    pass
  def control():
    pass
  def down():
    pass
  def end():
    pass
  def enter():
    pass
  def escape():
    pass
  def f1():
    pass
  def f10():
    pass
  def f11():
    pass
  def f12():
    pass
  def f13():
    pass
  def f14():
    pass
  def f15():
    pass
  def f16():
    pass
  def f2():
    pass
  def f3():
    pass
  def f4():
    pass
  def f5():
    pass
  def f6():
    pass
  def f7():
    pass
  def f8():
    pass
  def f9():
    pass
  def help():
    pass
  def home():
    pass
  def insert():
    pass
  def lalt():
    pass
  def lcontrol():
    pass
  def left():
    pass
  def lshift():
    pass
  def meta():
    pass
  def numLock():
    pass
  def pageDown():
    pass
  def pageUp():
    pass
  def pause():
    pass
  def printScreen():
    pass
  def ralt():
    pass
  def rcontrol():
    pass
  def right():
    pass
  def rshift():
    pass
  def scrollLock():
    pass
  def shift():
    pass
  def shiftLock():
    pass
  def space():
    pass
  def tab():
    pass
  def up():
    pass
LNTFade = int

LNTPop = int

class LODNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def addSwitch(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearForceSwitch(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearSwitches(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def forceSwitch(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCenter(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getHighestSwitch(self):
    pass
  def getIn(self):
    pass
  def getIns(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLowestSwitch(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumSwitches(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOut(self):
    pass
  def getOuts(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hideAllSwitches(self):
    pass
  def hideSwitch(self):
    pass
  def isAmbientLight(self):
    pass
  def isAnyShown(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def makeDefaultLod():
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCenter(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setSwitch(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showAllSwitches(self):
    pass
  def showSwitch(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def verifyChildBounds(self):
    pass
  def write(self):
    pass
class LOrientationd:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def almostSameDirection(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def conjugate(self):
    pass
  def conjugateFrom(self):
    pass
  def conjugateInPlace(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def extractToMatrix(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getAngle(self):
    pass
  def getAngleRad(self):
    pass
  def getAxis(self):
    pass
  def getAxisNormalized(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getForward(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getI(self):
    pass
  def getJ(self):
    pass
  def getK(self):
    pass
  def getNumComponents(self):
    pass
  def getR(self):
    pass
  def getRight(self):
    pass
  def getUp(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def identQuat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isAlmostIdentity(self):
    pass
  def isIdentity(self):
    pass
  def isNan(self):
    pass
  def isSameDirection(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pureImaginary():
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setFromAxisAngle(self):
    pass
  def setFromAxisAngleRad(self):
    pass
  def setFromMatrix(self):
    pass
  def setHpr(self):
    pass
  def setI(self):
    pass
  def setJ(self):
    pass
  def setK(self):
    pass
  def setR(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def xform(self):
    pass
  def zero():
    pass
class LOrientationf:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def almostSameDirection(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def conjugate(self):
    pass
  def conjugateFrom(self):
    pass
  def conjugateInPlace(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def extractToMatrix(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getAngle(self):
    pass
  def getAngleRad(self):
    pass
  def getAxis(self):
    pass
  def getAxisNormalized(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getForward(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getI(self):
    pass
  def getJ(self):
    pass
  def getK(self):
    pass
  def getNumComponents(self):
    pass
  def getR(self):
    pass
  def getRight(self):
    pass
  def getUp(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def identQuat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isAlmostIdentity(self):
    pass
  def isIdentity(self):
    pass
  def isNan(self):
    pass
  def isSameDirection(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pureImaginary():
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setFromAxisAngle(self):
    pass
  def setFromAxisAngleRad(self):
    pass
  def setFromMatrix(self):
    pass
  def setHpr(self):
    pass
  def setI(self):
    pass
  def setJ(self):
    pass
  def setK(self):
    pass
  def setR(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def xform(self):
    pass
  def zero():
    pass
class LRotationd:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def almostSameDirection(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def conjugate(self):
    pass
  def conjugateFrom(self):
    pass
  def conjugateInPlace(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def extractToMatrix(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getAngle(self):
    pass
  def getAngleRad(self):
    pass
  def getAxis(self):
    pass
  def getAxisNormalized(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getForward(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getI(self):
    pass
  def getJ(self):
    pass
  def getK(self):
    pass
  def getNumComponents(self):
    pass
  def getR(self):
    pass
  def getRight(self):
    pass
  def getUp(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def identQuat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isAlmostIdentity(self):
    pass
  def isIdentity(self):
    pass
  def isNan(self):
    pass
  def isSameDirection(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pureImaginary():
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setFromAxisAngle(self):
    pass
  def setFromAxisAngleRad(self):
    pass
  def setFromMatrix(self):
    pass
  def setHpr(self):
    pass
  def setI(self):
    pass
  def setJ(self):
    pass
  def setK(self):
    pass
  def setR(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def xform(self):
    pass
  def zero():
    pass
class LRotationf:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def almostSameDirection(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def conjugate(self):
    pass
  def conjugateFrom(self):
    pass
  def conjugateInPlace(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def extractToMatrix(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getAngle(self):
    pass
  def getAngleRad(self):
    pass
  def getAxis(self):
    pass
  def getAxisNormalized(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getForward(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getI(self):
    pass
  def getJ(self):
    pass
  def getK(self):
    pass
  def getNumComponents(self):
    pass
  def getR(self):
    pass
  def getRight(self):
    pass
  def getUp(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def identQuat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isAlmostIdentity(self):
    pass
  def isIdentity(self):
    pass
  def isNan(self):
    pass
  def isSameDirection(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pureImaginary():
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setFromAxisAngle(self):
    pass
  def setFromAxisAngleRad(self):
    pass
  def setFromMatrix(self):
    pass
  def setHpr(self):
    pass
  def setI(self):
    pass
  def setJ(self):
    pass
  def setK(self):
    pass
  def setR(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def xform(self):
    pass
  def zero():
    pass
class Lens:
  def __init__(self):
    pass
  FCAspectRatio = int

  FCCameraPlane = int

  FCKeystone = int

  FCOffAxis = int

  FCRoll = int

  FCShear = int

  SCLeft = int

  SCMono = int

  SCRight = int

  SCStereo = int

  def clear(self):
    pass
  def clearKeystone(self):
    pass
  def clearViewMat(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def extrude(self):
    pass
  def extrudeVec(self):
    pass
  def getAspectRatio(self):
    pass
  def getBamModified(self):
    pass
  def getChangeEvent(self):
    pass
  def getClassType():
    pass
  def getConvergenceDistance(self):
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultFar():
    pass
  def getDefaultNear():
    pass
  def getFar(self):
    pass
  def getFilmMat(self):
    pass
  def getFilmMatInv(self):
    pass
  def getFilmOffset(self):
    pass
  def getFilmSize(self):
    pass
  def getFocalLength(self):
    pass
  def getFov(self):
    pass
  def getHfov(self):
    pass
  def getInterocularDistance(self):
    pass
  def getKeystone(self):
    pass
  def getLensMat(self):
    pass
  def getLensMatInv(self):
    pass
  def getMinFov(self):
    pass
  def getNear(self):
    pass
  def getNodalPoint(self):
    pass
  def getProjectionMat(self):
    pass
  def getProjectionMatInv(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUpVector(self):
    pass
  def getVfov(self):
    pass
  def getViewHpr(self):
    pass
  def getViewMat(self):
    pass
  def getViewVector(self):
    pass
  def isExactType(self):
    pass
  def isLinear(self):
    pass
  def isOfType(self):
    pass
  def isOrthographic(self):
    pass
  def isPerspective(self):
    pass
  def makeBounds(self):
    pass
  def makeCopy(self):
    pass
  def makeGeometry(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def recomputeAll(self):
    pass
  def ref(self):
    pass
  def setAspectRatio(self):
    pass
  def setChangeEvent(self):
    pass
  def setConvergenceDistance(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setFar(self):
    pass
  def setFilmOffset(self):
    pass
  def setFilmSize(self):
    pass
  def setFocalLength(self):
    pass
  def setFov(self):
    pass
  def setFrustumFromCorners(self):
    pass
  def setInterocularDistance(self):
    pass
  def setKeystone(self):
    pass
  def setMinFov(self):
    pass
  def setNear(self):
    pass
  def setNearFar(self):
    pass
  def setViewHpr(self):
    pass
  def setViewMat(self):
    pass
  def setViewVector(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class LensNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def activateLens(self):
    pass
  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copyLens(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def deactivateLens(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLens(self):
    pass
  def getLensActive(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hideFrustum(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isInView(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLens(self):
    pass
  def setLensActive(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showFrustum(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class Lerp:
  def __init__(self):
    pass
  def assign(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEndEvent(self):
    pass
  def getFunctor(self):
    pass
  def getRefCount(self):
    pass
  def getStepSize(self):
    pass
  def getT(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isDone(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def setEndEvent(self):
    pass
  def setStepSize(self):
    pass
  def setT(self):
    pass
  def step(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class LerpBlendType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class LerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class Light:
  def __init__(self):
    pass
  def asNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getPriority(self):
    pass
  def getRefCount(self):
    pass
  def isAmbientLight(self):
    pass
  def ref(self):
    pass
  def setColor(self):
    pass
  def setPriority(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
class LightAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  OAdd = int

  ORemove = int

  OSet = int

  def addLight(self):
    pass
  def addOffLight(self):
    pass
  def addOnLight(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def filterToMax(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getLight(self):
    pass
  def getMostImportantLight(self):
    pass
  def getNumAttribs():
    pass
  def getNumLights(self):
    pass
  def getNumOffLights(self):
    pass
  def getNumOnLights(self):
    pass
  def getOffLight(self):
    pass
  def getOffLights(self):
    pass
  def getOnLight(self):
    pass
  def getOnLights(self):
    pass
  def getOperation(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasAllOff(self):
    pass
  def hasLight(self):
    pass
  def hasOffLight(self):
    pass
  def hasOnLight(self):
    pass
  def isExactType(self):
    pass
  def isIdentity(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeAllOff():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeLight(self):
    pass
  def removeOffLight(self):
    pass
  def removeOnLight(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class LightLensNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def activateLens(self):
    pass
  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def asNode(self):
    pass
  def assign(self):
    pass
  def cleanupAuxSceneData(self):
    pass
  def clearAttrib(self):
    pass
  def clearAuxSceneData(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTagState(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copyLens(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def deactivateLens(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getAuxSceneData(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCameraMask(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getCullCenter(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInitialState(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLens(self):
    pass
  def getLensActive(self):
    pass
  def getLodCenter(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTagState(self):
    pass
  def getTagStateKey(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTagState(self):
    pass
  def hasTags(self):
    pass
  def hideFrustum(self):
    pass
  def isActive(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isInView(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isShadowCaster(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listAuxSceneData(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setAuxSceneData(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCameraMask(self):
    pass
  def setColor(self):
    pass
  def setCullCenter(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setInitialState(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLens(self):
    pass
  def setLensActive(self):
    pass
  def setLodCenter(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setScene(self):
    pass
  def setShadowCaster(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTagState(self):
    pass
  def setTagStateKey(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showFrustum(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToCamera(self):
    pass
  def upcastToLight(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class LightMutex:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
class LightMutexDirect:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
class LightNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def asNode(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setColor(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToLight(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPandaNode(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class LightRampAttrib:
  def __init__(self):
    pass
  LRTDefault = int

  LRTDoubleThreshold = int

  LRTHdr0 = int

  LRTHdr1 = int

  LRTHdr2 = int

  LRTIdentity = int

  LRTSingleThreshold = int

  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getLevel(self):
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getThreshold(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def makeDefault():
    pass
  def makeDoubleThreshold():
    pass
  def makeHdr0():
    pass
  def makeHdr1():
    pass
  def makeHdr2():
    pass
  def makeIdentity():
    pass
  def makeSingleThreshold():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class LightReMutex:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def elevateLock(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
class LightReMutexDirect:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def elevateLock(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
class LineSegs:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def create(self):
    pass
  def drawTo(self):
    pass
  def getClassType():
    pass
  def getCurrentPosition(self):
    pass
  def getName(self):
    pass
  def getNumVertices(self):
    pass
  def getVertex(self):
    pass
  def getVertexColor(self):
    pass
  def getVertexColors(self):
    pass
  def getVertices(self):
    pass
  def hasName(self):
    pass
  def isEmpty(self):
    pass
  def moveTo(self):
    pass
  def output(self):
    pass
  def reset(self):
    pass
  def setColor(self):
    pass
  def setName(self):
    pass
  def setThickness(self):
    pass
  def setVertex(self):
    pass
  def setVertexColor(self):
    pass
class LineStream:
  def __init__(self):
    pass
  Beg = int

  Cur = int

  End = int

  def bad(self):
    pass
  def clear(self):
    pass
  def downcastToIostream(self):
    pass
  def eof(self):
    pass
  def fail(self):
    pass
  def flush(self):
    pass
  def getLine(self):
    pass
  def good(self):
    pass
  def hasNewline(self):
    pass
  def isTextAvailable(self):
    pass
  def put(self):
    pass
  def seekp(self):
    pass
  def tellp(self):
    pass
  def upcastToIos(self):
    pass
class LoaderFileType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAdditionalExtensions(self):
    pass
  def getAllowDiskCache(self):
    pass
  def getAllowRamCache(self):
    pass
  def getClassType():
    pass
  def getExtension(self):
    pass
  def getName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def supportsCompressed(self):
    pass
class LoaderFileTypeRegistry:
  def __init__(self):
    pass
  def getGlobalPtr():
    pass
  def getNumTypes(self):
    pass
  def getType(self):
    pass
  def getTypeFromExtension(self):
    pass
  def getTypes(self):
    pass
  def write(self):
    pass
class LoaderOptions:
  def __init__(self):
    pass
  LFAllowInstance = int

  LFCacheOnly = int

  LFConvertAnim = int

  LFConvertChannels = int

  LFConvertSkeleton = int

  LFNoCache = int

  LFNoDiskCache = int

  LFNoRamCache = int

  LFReportErrors = int

  LFSearch = int

  TFAllow1d = int

  TFGenerateMipmaps = int

  TFPreload = int

  TFPreloadSimple = int

  def assign(self):
    pass
  def getFlags(self):
    pass
  def getTextureFlags(self):
    pass
  def output(self):
    pass
  def setFlags(self):
    pass
  def setTextureFlags(self):
    pass
class MainThread:
  def __init__(self):
    pass
  def assign(self):
    pass
  def bindThread():
    pass
  def clearName(self):
    pass
  def considerYield():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def forceYield():
    pass
  def getClassType():
    pass
  def getCurrentPipelineStage():
    pass
  def getCurrentThread():
    pass
  def getExternalThread():
    pass
  def getMainThread():
    pass
  def getName(self):
    pass
  def getPipelineStage(self):
    pass
  def getPstatsIndex(self):
    pass
  def getPythonData(self):
    pass
  def getRefCount(self):
    pass
  def getSyncName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUniqueId(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isJoinable(self):
    pass
  def isOfType(self):
    pass
  def isStarted(self):
    pass
  def isThreadingSupported():
    pass
  def isTrueThreads():
    pass
  def join(self):
    pass
  def output(self):
    pass
  def outputBlocker(self):
    pass
  def preempt(self):
    pass
  def prepareForExit():
    pass
  def ref(self):
    pass
  def setMinPipelineStage(self):
    pass
  def setName(self):
    pass
  def setPipelineStage(self):
    pass
  def setPythonData(self):
    pass
  def sleep():
    pass
  def start(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def writeStatus():
    pass
class Mat3:
  def __init__(self):
    pass
  def addHash(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def convertMat():
    pass
  def determinant(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getCol(self):
    pass
  def getCol2(self):
    pass
  def getCol2s(self):
    pass
  def getCols(self):
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getRow(self):
    pass
  def getRow2(self):
    pass
  def getRow2s(self):
    pass
  def getRows(self):
    pass
  def identMat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def invertTransposeFrom(self):
    pass
  def isNan(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def pythonRepr(self):
    pass
  def rotateMat():
    pass
  def rotateMatNormaxis():
    pass
  def scaleMat():
    pass
  def scaleShearMat():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setCol(self):
    pass
  def setRotateMat(self):
    pass
  def setRotateMatNormaxis(self):
    pass
  def setRow(self):
    pass
  def setScaleMat(self):
    pass
  def setScaleShearMat(self):
    pass
  def setShearMat(self):
    pass
  def setTranslateMat(self):
    pass
  def shearMat():
    pass
  def size():
    pass
  def translateMat():
    pass
  def transposeFrom(self):
    pass
  def transposeInPlace(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
  def xformPoint(self):
    pass
  def xformVec(self):
    pass
  def xformVecGeneral(self):
    pass
class Mat3D:
  def __init__(self):
    pass
  def addHash(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def convertMat():
    pass
  def determinant(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getCol(self):
    pass
  def getCol2(self):
    pass
  def getCol2s(self):
    pass
  def getCols(self):
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getRow(self):
    pass
  def getRow2(self):
    pass
  def getRow2s(self):
    pass
  def getRows(self):
    pass
  def identMat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def invertTransposeFrom(self):
    pass
  def isNan(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def pythonRepr(self):
    pass
  def rotateMat():
    pass
  def rotateMatNormaxis():
    pass
  def scaleMat():
    pass
  def scaleShearMat():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setCol(self):
    pass
  def setRotateMat(self):
    pass
  def setRotateMatNormaxis(self):
    pass
  def setRow(self):
    pass
  def setScaleMat(self):
    pass
  def setScaleShearMat(self):
    pass
  def setShearMat(self):
    pass
  def setTranslateMat(self):
    pass
  def shearMat():
    pass
  def size():
    pass
  def translateMat():
    pass
  def transposeFrom(self):
    pass
  def transposeInPlace(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
  def xformPoint(self):
    pass
  def xformVec(self):
    pass
  def xformVecGeneral(self):
    pass
class Mat4:
  def __init__(self):
    pass
  def addHash(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def convertMat():
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getCol(self):
    pass
  def getCol3(self):
    pass
  def getCols(self):
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getRow(self):
    pass
  def getRow3(self):
    pass
  def getRow3s(self):
    pass
  def getRows(self):
    pass
  def getUpper3(self):
    pass
  def identMat():
    pass
  def invertAffineFrom(self):
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isNan(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def onesMat():
    pass
  def output(self):
    pass
  def pythonRepr(self):
    pass
  def rotateMat():
    pass
  def rotateMatNormaxis():
    pass
  def scaleMat():
    pass
  def scaleShearMat():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setCol(self):
    pass
  def setRotateMat(self):
    pass
  def setRotateMatNormaxis(self):
    pass
  def setRow(self):
    pass
  def setScaleMat(self):
    pass
  def setScaleShearMat(self):
    pass
  def setShearMat(self):
    pass
  def setTranslateMat(self):
    pass
  def setUpper3(self):
    pass
  def shearMat():
    pass
  def size():
    pass
  def translateMat():
    pass
  def transposeFrom(self):
    pass
  def transposeInPlace(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
  def xformPoint(self):
    pass
  def xformVec(self):
    pass
  def xformVecGeneral(self):
    pass
  def yToZUpMat():
    pass
  def zToYUpMat():
    pass
  def zerosMat():
    pass
class Mat4D:
  def __init__(self):
    pass
  def addHash(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def convertMat():
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getCol(self):
    pass
  def getCol3(self):
    pass
  def getCols(self):
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getRow(self):
    pass
  def getRow3(self):
    pass
  def getRow3s(self):
    pass
  def getRows(self):
    pass
  def getUpper3(self):
    pass
  def identMat():
    pass
  def invertAffineFrom(self):
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isNan(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def onesMat():
    pass
  def output(self):
    pass
  def pythonRepr(self):
    pass
  def rotateMat():
    pass
  def rotateMatNormaxis():
    pass
  def scaleMat():
    pass
  def scaleShearMat():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setCol(self):
    pass
  def setRotateMat(self):
    pass
  def setRotateMatNormaxis(self):
    pass
  def setRow(self):
    pass
  def setScaleMat(self):
    pass
  def setScaleShearMat(self):
    pass
  def setShearMat(self):
    pass
  def setTranslateMat(self):
    pass
  def setUpper3(self):
    pass
  def shearMat():
    pass
  def size():
    pass
  def translateMat():
    pass
  def transposeFrom(self):
    pass
  def transposeInPlace(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
  def xformPoint(self):
    pass
  def xformVec(self):
    pass
  def xformVecGeneral(self):
    pass
  def yToZUpMat():
    pass
  def zToYUpMat():
    pass
  def zerosMat():
    pass
class Material:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearAmbient(self):
    pass
  def clearDiffuse(self):
    pass
  def clearEmission(self):
    pass
  def clearName(self):
    pass
  def clearSpecular(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def eq(self):
    pass
  def getAmbient(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getDefault():
    pass
  def getDiffuse(self):
    pass
  def getEmission(self):
    pass
  def getLocal(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getShininess(self):
    pass
  def getSpecular(self):
    pass
  def getTwoside(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasAmbient(self):
    pass
  def hasDiffuse(self):
    pass
  def hasEmission(self):
    pass
  def hasName(self):
    pass
  def hasSpecular(self):
    pass
  def isAttribLocked(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lessThan(self):
    pass
  def markBamModified(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setAmbient(self):
    pass
  def setAttribLock(self):
    pass
  def setDiffuse(self):
    pass
  def setEmission(self):
    pass
  def setLocal(self):
    pass
  def setName(self):
    pass
  def setShininess(self):
    pass
  def setSpecular(self):
    pass
  def setTwoside(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class MaterialAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMaterial(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isOff(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class MaterialCollection:
  def __init__(self):
    pass
  def addMaterial(self):
    pass
  def addMaterialsFrom(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def findMaterial(self):
    pass
  def getMaterial(self):
    pass
  def getNumMaterials(self):
    pass
  def hasMaterial(self):
    pass
  def output(self):
    pass
  def removeDuplicateMaterials(self):
    pass
  def removeMaterial(self):
    pass
  def removeMaterialsFrom(self):
    pass
  def size(self):
    pass
  def write(self):
    pass
class MaterialPool:
  def __init__(self):
    pass
  def garbageCollect():
    pass
  def getMaterial():
    pass
  def listContents():
    pass
  def write():
    pass
class MathNumbers:
  def __init__(self):
    pass
class MatrixLens:
  def __init__(self):
    pass
  FCAspectRatio = int

  FCCameraPlane = int

  FCKeystone = int

  FCOffAxis = int

  FCRoll = int

  FCShear = int

  SCLeft = int

  SCMono = int

  SCRight = int

  SCStereo = int

  def clear(self):
    pass
  def clearKeystone(self):
    pass
  def clearLeftEyeMat(self):
    pass
  def clearRightEyeMat(self):
    pass
  def clearViewMat(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def extrude(self):
    pass
  def extrudeVec(self):
    pass
  def getAspectRatio(self):
    pass
  def getBamModified(self):
    pass
  def getChangeEvent(self):
    pass
  def getClassType():
    pass
  def getConvergenceDistance(self):
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultFar():
    pass
  def getDefaultNear():
    pass
  def getFar(self):
    pass
  def getFilmMat(self):
    pass
  def getFilmMatInv(self):
    pass
  def getFilmOffset(self):
    pass
  def getFilmSize(self):
    pass
  def getFocalLength(self):
    pass
  def getFov(self):
    pass
  def getHfov(self):
    pass
  def getInterocularDistance(self):
    pass
  def getKeystone(self):
    pass
  def getLeftEyeMat(self):
    pass
  def getLensMat(self):
    pass
  def getLensMatInv(self):
    pass
  def getMinFov(self):
    pass
  def getNear(self):
    pass
  def getNodalPoint(self):
    pass
  def getProjectionMat(self):
    pass
  def getProjectionMatInv(self):
    pass
  def getRefCount(self):
    pass
  def getRightEyeMat(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUpVector(self):
    pass
  def getUserMat(self):
    pass
  def getVfov(self):
    pass
  def getViewHpr(self):
    pass
  def getViewMat(self):
    pass
  def getViewVector(self):
    pass
  def hasLeftEyeMat(self):
    pass
  def hasRightEyeMat(self):
    pass
  def isExactType(self):
    pass
  def isLinear(self):
    pass
  def isOfType(self):
    pass
  def isOrthographic(self):
    pass
  def isPerspective(self):
    pass
  def makeBounds(self):
    pass
  def makeCopy(self):
    pass
  def makeGeometry(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def recomputeAll(self):
    pass
  def ref(self):
    pass
  def setAspectRatio(self):
    pass
  def setChangeEvent(self):
    pass
  def setConvergenceDistance(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setFar(self):
    pass
  def setFilmOffset(self):
    pass
  def setFilmSize(self):
    pass
  def setFocalLength(self):
    pass
  def setFov(self):
    pass
  def setFrustumFromCorners(self):
    pass
  def setInterocularDistance(self):
    pass
  def setKeystone(self):
    pass
  def setLeftEyeMat(self):
    pass
  def setMinFov(self):
    pass
  def setNear(self):
    pass
  def setNearFar(self):
    pass
  def setRightEyeMat(self):
    pass
  def setUserMat(self):
    pass
  def setViewHpr(self):
    pass
  def setViewMat(self):
    pass
  def setViewVector(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class Mersenne:
  def __init__(self):
    pass
  def getUint31(self):
    pass
class MeshDrawer:
  def __init__(self):
    pass
  def begin(self):
    pass
  def billboard(self):
    pass
  def blendedParticle(self):
    pass
  def crossSegment(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def end(self):
    pass
  def explosion(self):
    pass
  def geometry(self):
    pass
  def getBudget(self):
    pass
  def getClassType():
    pass
  def getRoot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def linkSegment(self):
    pass
  def linkSegmentEnd(self):
    pass
  def particle(self):
    pass
  def segment(self):
    pass
  def setBudget(self):
    pass
  def stream(self):
    pass
  def tri(self):
    pass
  def unevenSegment(self):
    pass
class MeshDrawer2D:
  def __init__(self):
    pass
  def begin(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def end(self):
    pass
  def getBudget(self):
    pass
  def getClassType():
    pass
  def getRoot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def quadRaw(self):
    pass
  def rectangle(self):
    pass
  def rectangleBorder(self):
    pass
  def rectangleBorderTiled(self):
    pass
  def rectangleRaw(self):
    pass
  def rectangleTiled(self):
    pass
  def setBudget(self):
    pass
  def setClip(self):
    pass
class MicrophoneAudio:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getChannels(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getNumOptions():
    pass
  def getOption():
    pass
  def getOptions(self):
    pass
  def getRate(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class ModelFlattenRequest:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getModel(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getOrig(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isReady(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class ModelLoadRequest:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getFilename(self):
    pass
  def getLoader(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getModel(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getOptions(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isReady(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class ModelNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  PTDropNode = int

  PTLocal = int

  PTNet = int

  PTNoTouch = int

  PTNone = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPreserveAttributes(self):
    pass
  def getPreserveTransform(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPreserveAttributes(self):
    pass
  def setPreserveTransform(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setTransformLimit(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class ModelPool:
  def __init__(self):
    pass
  def addModel():
    pass
  def garbageCollect():
    pass
  def hasModel():
    pass
  def listContents():
    pass
  def loadModel():
    pass
  def releaseAllModels():
    pass
  def releaseModel():
    pass
  def verifyModel():
    pass
  def write():
    pass
class ModelRoot:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  PTDropNode = int

  PTLocal = int

  PTNet = int

  PTNoTouch = int

  PTNone = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getFullpath(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getModelRefCount(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPreserveAttributes(self):
    pass
  def getPreserveTransform(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getReference(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFullpath(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPreserveAttributes(self):
    pass
  def setPreserveTransform(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setReference(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setTransformLimit(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class ModifierButtons:
  def __init__(self):
    pass
  def addButton(self):
    pass
  def allButtonsUp(self):
    pass
  def assign(self):
    pass
  def buttonDown(self):
    pass
  def buttonUp(self):
    pass
  def eq(self):
    pass
  def getButton(self):
    pass
  def getButtons(self):
    pass
  def getNumButtons(self):
    pass
  def getPrefix(self):
    pass
  def hasButton(self):
    pass
  def isAnyDown(self):
    pass
  def isDown(self):
    pass
  def lessThan(self):
    pass
  def matches(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def removeButton(self):
    pass
  def setButtonList(self):
    pass
  def write(self):
    pass
class MouseAndKeyboard:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSource(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class MouseButton:
  def __init__(self):
    pass
  def button():
    pass
  def five():
    pass
  def four():
    pass
  def isMouseButton():
    pass
  def one():
    pass
  def three():
    pass
  def two():
    pass
  def wheelDown():
    pass
  def wheelLeft():
    pass
  def wheelRight():
    pass
  def wheelUp():
    pass
class MouseData:
  def __init__(self):
    pass
  def assign(self):
    pass
  def getInWindow(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def output(self):
    pass
class MouseInterfaceNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAllButtons(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearButton(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def requireButton(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class MouseRecorder:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToMouseRecorder(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isPlaying(self):
    pass
  def isRecording(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToDataNode(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToRecorderBase(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class MouseSubregion:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAllButtons(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearButton(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBottom(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLeft(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getRight(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTop(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def requireButton(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setDimensions(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class MouseWatcher:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addGroup(self):
    pass
  def addRegion(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearDisplayRegion(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearGeometry(self):
    pass
  def clearInactivityTimeout(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearRegions(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTrailLog(self):
    pass
  def clearTrailNode(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToMouseWatcher(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findRegion(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getButtonDownPattern(self):
    pass
  def getButtonRepeatPattern(self):
    pass
  def getButtonUpPattern(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDisplayRegion(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterPattern(self):
    pass
  def getExtraHandler(self):
    pass
  def getFancyBits(self):
    pass
  def getFrame(self):
    pass
  def getGeometry(self):
    pass
  def getGroup(self):
    pass
  def getGroups(self):
    pass
  def getInactivityTimeout(self):
    pass
  def getInactivityTimeoutEvent(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLeavePattern(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getModifierButtons(self):
    pass
  def getMouse(self):
    pass
  def getMouseX(self):
    pass
  def getMouseY(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumGroups(self):
    pass
  def getNumParents(self):
    pass
  def getNumRegions(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverRegion(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getRegion(self):
    pass
  def getRegions(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTrailLog(self):
    pass
  def getTrailNode(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getWithinPattern(self):
    pass
  def getWithoutPattern(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasDisplayRegion(self):
    pass
  def hasEffect(self):
    pass
  def hasGeometry(self):
    pass
  def hasInactivityTimeout(self):
    pass
  def hasMouse(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasRegion(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hideRegions(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isButtonDown(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isMouseOpen(self):
    pass
  def isOfType(self):
    pass
  def isOverRegion(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isSorted(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def noteActivity(self):
    pass
  def numTrailRecent(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeGroup(self):
    pass
  def removeRegion(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceGroup(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setButtonDownPattern(self):
    pass
  def setButtonRepeatPattern(self):
    pass
  def setButtonUpPattern(self):
    pass
  def setColor(self):
    pass
  def setDisplayRegion(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setEnterPattern(self):
    pass
  def setExtraHandler(self):
    pass
  def setFinal(self):
    pass
  def setFrame(self):
    pass
  def setGeometry(self):
    pass
  def setInactivityTimeout(self):
    pass
  def setInactivityTimeoutEvent(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLeavePattern(self):
    pass
  def setModifierButtons(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTrailLogDuration(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setWithinPattern(self):
    pass
  def setWithoutPattern(self):
    pass
  def showRegions(self):
    pass
  def sortRegions(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToDataNode(self):
    pass
  def upcastToMouseWatcherGroup(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def updateRegions(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class MouseWatcherGroup:
  def __init__(self):
    pass
  def addRegion(self):
    pass
  def clearRegions(self):
    pass
  def downcastToMouseWatcher(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def findRegion(self):
    pass
  def getClassType():
    pass
  def getNumRegions(self):
    pass
  def getRefCount(self):
    pass
  def getRegion(self):
    pass
  def getRegions(self):
    pass
  def hasRegion(self):
    pass
  def hideRegions(self):
    pass
  def isSorted(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeRegion(self):
    pass
  def setColor(self):
    pass
  def showRegions(self):
    pass
  def sortRegions(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def updateRegions(self):
    pass
  def write(self):
    pass
class MouseWatcherParameter:
  def __init__(self):
    pass
  def getButton(self):
    pass
  def getCandidateStringEncoded(self):
    pass
  def getCursorPos(self):
    pass
  def getHighlightEnd(self):
    pass
  def getHighlightStart(self):
    pass
  def getKeycode(self):
    pass
  def getModifierButtons(self):
    pass
  def getMouse(self):
    pass
  def hasButton(self):
    pass
  def hasCandidate(self):
    pass
  def hasKeycode(self):
    pass
  def hasMouse(self):
    pass
  def isKeyrepeat(self):
    pass
  def isOutside(self):
    pass
  def output(self):
    pass
class MouseWatcherRegion:
  def __init__(self):
    pass
  SFAnyButton = int

  SFMouseButton = int

  SFMousePosition = int

  SFOtherButton = int

  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActive(self):
    pass
  def getArea(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFrame(self):
    pass
  def getKeyboard(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getSuppressFlags(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setActive(self):
    pass
  def setFrame(self):
    pass
  def setKeyboard(self):
    pass
  def setName(self):
    pass
  def setSort(self):
    pass
  def setSuppressFlags(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class MovieAudio:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class MovieAudioCursor:
  def __init__(self):
    pass
  def aborted(self):
    pass
  def audioChannels(self):
    pass
  def audioRate(self):
    pass
  def canSeek(self):
    pass
  def canSeekFast(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getSource(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def length(self):
    pass
  def markBamModified(self):
    pass
  def readSamples(self):
    pass
  def ready(self):
    pass
  def ref(self):
    pass
  def seek(self):
    pass
  def skipSamples(self):
    pass
  def tell(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class MovieTexture:
  def __init__(self):
    pass
  CMDefault = int

  CMDxt1 = int

  CMDxt2 = int

  CMDxt3 = int

  CMDxt4 = int

  CMDxt5 = int

  CMFxt1 = int

  CMOff = int

  CMOn = int

  FAlpha = int

  FBlue = int

  FColorIndex = int

  FDepthComponent = int

  FDepthComponent16 = int

  FDepthComponent24 = int

  FDepthComponent32 = int

  FDepthStencil = int

  FGreen = int

  FLuminance = int

  FLuminanceAlpha = int

  FLuminanceAlphamask = int

  FRed = int

  FRgb = int

  FRgb12 = int

  FRgb332 = int

  FRgb5 = int

  FRgb8 = int

  FRgba = int

  FRgba12 = int

  FRgba16 = int

  FRgba32 = int

  FRgba4 = int

  FRgba5 = int

  FRgba8 = int

  FRgbm = int

  FTDefault = int

  FTInvalid = int

  FTLinear = int

  FTLinearMipmapLinear = int

  FTLinearMipmapNearest = int

  FTNearest = int

  FTNearestMipmapLinear = int

  FTNearestMipmapNearest = int

  FTShadow = int

  QLBest = int

  QLDefault = int

  QLFastest = int

  QLNormal = int

  TFloat = int

  TT1dTexture = int

  TT2dTexture = int

  TT3dTexture = int

  TTCubeMap = int

  TUnsignedByte = int

  TUnsignedInt248 = int

  TUnsignedShort = int

  WMBorderColor = int

  WMClamp = int

  WMInvalid = int

  WMMirror = int

  WMMirrorOnce = int

  WMRepeat = int

  def assign(self):
    pass
  def clear(self):
    pass
  def clearAlphaFilename(self):
    pass
  def clearAlphaFullpath(self):
    pass
  def clearAuxData(self):
    pass
  def clearFilename(self):
    pass
  def clearFullpath(self):
    pass
  def clearName(self):
    pass
  def clearRamImage(self):
    pass
  def clearRamMipmapImage(self):
    pass
  def clearRamMipmapImages(self):
    pass
  def clearSimpleRamImage(self):
    pass
  def compressRamImage(self):
    pass
  def considerRescale(self):
    pass
  def decodeFromBamStream():
    pass
  def downToPower2():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def downcastToVideoTexture(self):
    pass
  def encodeToBamStream(self):
    pass
  def estimateTextureMemory(self):
    pass
  def generateAlphaScaleMap(self):
    pass
  def generateNormalizationCubeMap(self):
    pass
  def generateRamMipmapImages(self):
    pass
  def generateSimpleRamImage(self):
    pass
  def getActive(self):
    pass
  def getAlphaFilename(self):
    pass
  def getAlphaFullpath(self):
    pass
  def getAnisotropicDegree(self):
    pass
  def getAuxData(self):
    pass
  def getBamModified(self):
    pass
  def getBorderColor(self):
    pass
  def getClassType():
    pass
  def getComponentType(self):
    pass
  def getComponentWidth(self):
    pass
  def getCompression(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getEffectiveAnisotropicDegree(self):
    pass
  def getEffectiveMagfilter(self):
    pass
  def getEffectiveMinfilter(self):
    pass
  def getEffectiveQualityLevel(self):
    pass
  def getExpectedMipmapXSize(self):
    pass
  def getExpectedMipmapYSize(self):
    pass
  def getExpectedMipmapZSize(self):
    pass
  def getExpectedNumMipmapLevels(self):
    pass
  def getExpectedRamImageSize(self):
    pass
  def getExpectedRamMipmapImageSize(self):
    pass
  def getExpectedRamMipmapPageSize(self):
    pass
  def getExpectedRamPageSize(self):
    pass
  def getFilename(self):
    pass
  def getFormat(self):
    pass
  def getFullpath(self):
    pass
  def getImageModified(self):
    pass
  def getKeepRamImage(self):
    pass
  def getLoadedFromImage(self):
    pass
  def getLoadedFromTxo(self):
    pass
  def getLoop(self):
    pass
  def getLoopCount(self):
    pass
  def getMagfilter(self):
    pass
  def getMatchFramebufferFormat(self):
    pass
  def getMinfilter(self):
    pass
  def getName(self):
    pass
  def getNumComponents(self):
    pass
  def getNumLoadableRamMipmapImages(self):
    pass
  def getNumRamMipmapImages(self):
    pass
  def getOrigFileXSize(self):
    pass
  def getOrigFileYSize(self):
    pass
  def getOrigFileZSize(self):
    pass
  def getPadXSize(self):
    pass
  def getPadYSize(self):
    pass
  def getPadZSize(self):
    pass
  def getPlayRate(self):
    pass
  def getPostLoadStoreCache(self):
    pass
  def getPropertiesModified(self):
    pass
  def getQualityLevel(self):
    pass
  def getRamImage(self):
    pass
  def getRamImageAs(self):
    pass
  def getRamImageCompression(self):
    pass
  def getRamImageSize(self):
    pass
  def getRamMipmapImage(self):
    pass
  def getRamMipmapImageSize(self):
    pass
  def getRamMipmapPageSize(self):
    pass
  def getRamPageSize(self):
    pass
  def getRefCount(self):
    pass
  def getRenderToTexture(self):
    pass
  def getResident(self):
    pass
  def getSimpleImageModified(self):
    pass
  def getSimpleRamImage(self):
    pass
  def getSimpleRamImageSize(self):
    pass
  def getSimpleXSize(self):
    pass
  def getSimpleYSize(self):
    pass
  def getTexScale(self):
    pass
  def getTextureType(self):
    pass
  def getTexturesPower2():
    pass
  def getTime(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUncompressedRamImage(self):
    pass
  def getVideoHeight(self):
    pass
  def getVideoLength(self):
    pass
  def getVideoWidth(self):
    pass
  def getWrapU(self):
    pass
  def getWrapV(self):
    pass
  def getWrapW(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def getZSize(self):
    pass
  def hasAllRamMipmapImages(self):
    pass
  def hasAlphaFilename(self):
    pass
  def hasAlphaFullpath(self):
    pass
  def hasCompression(self):
    pass
  def hasFilename(self):
    pass
  def hasFullpath(self):
    pass
  def hasName(self):
    pass
  def hasRamImage(self):
    pass
  def hasRamMipmapImage(self):
    pass
  def hasSimpleRamImage(self):
    pass
  def hasUncompressedRamImage(self):
    pass
  def haveTexturesPower2():
    pass
  def isExactType(self):
    pass
  def isMipmap():
    pass
  def isOfType(self):
    pass
  def isPlaying(self):
    pass
  def isPrepared(self):
    pass
  def load(self):
    pass
  def loadRelated(self):
    pass
  def makeCopy(self):
    pass
  def makeRamImage(self):
    pass
  def makeRamMipmapImage(self):
    pass
  def markBamModified(self):
    pass
  def mightHaveRamImage(self):
    pass
  def modifyRamImage(self):
    pass
  def modifyRamMipmapImage(self):
    pass
  def modifySimpleRamImage(self):
    pass
  def newSimpleRamImage(self):
    pass
  def output(self):
    pass
  def peek(self):
    pass
  def play(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def read(self):
    pass
  def readDds(self):
    pass
  def readTxo(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def reload(self):
    pass
  def restart(self):
    pass
  def setAlphaFilename(self):
    pass
  def setAlphaFullpath(self):
    pass
  def setAnisotropicDegree(self):
    pass
  def setAuxData(self):
    pass
  def setBorderColor(self):
    pass
  def setComponentType(self):
    pass
  def setCompression(self):
    pass
  def setFilename(self):
    pass
  def setFormat(self):
    pass
  def setFullpath(self):
    pass
  def setKeepRamImage(self):
    pass
  def setLoadedFromImage(self):
    pass
  def setLoadedFromTxo(self):
    pass
  def setLoop(self):
    pass
  def setLoopCount(self):
    pass
  def setMagfilter(self):
    pass
  def setMatchFramebufferFormat(self):
    pass
  def setMinfilter(self):
    pass
  def setName(self):
    pass
  def setOrigFileSize(self):
    pass
  def setPadSize(self):
    pass
  def setPlayRate(self):
    pass
  def setPostLoadStoreCache(self):
    pass
  def setQualityLevel(self):
    pass
  def setRamImage(self):
    pass
  def setRamMipmapImage(self):
    pass
  def setRamMipmapPointerFromInt(self):
    pass
  def setRenderToTexture(self):
    pass
  def setSimpleRamImage(self):
    pass
  def setSizePadded(self):
    pass
  def setTexturesPower2():
    pass
  def setTime(self):
    pass
  def setWrapU(self):
    pass
  def setWrapV(self):
    pass
  def setWrapW(self):
    pass
  def setXSize(self):
    pass
  def setYSize(self):
    pass
  def setZSize(self):
    pass
  def setup1dTexture(self):
    pass
  def setup2dTexture(self):
    pass
  def setup3dTexture(self):
    pass
  def setupCubeMap(self):
    pass
  def setupTexture(self):
    pass
  def stop(self):
    pass
  def store(self):
    pass
  def synchronizeTo(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncompressRamImage(self):
    pass
  def unref(self):
    pass
  def unsynchronize(self):
    pass
  def upToPower2():
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def usesMipmaps(self):
    pass
  def wasImageModified(self):
    pass
  def write(self):
    pass
  def writeTxo(self):
    pass
class MovieVideo:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class MovieVideoCursor:
  def __init__(self):
    pass
  def aborted(self):
    pass
  def canSeek(self):
    pass
  def canSeekFast(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def fetchIntoBitbucket(self):
    pass
  def fetchIntoTexture(self):
    pass
  def fetchIntoTextureAlpha(self):
    pass
  def fetchIntoTextureRgb(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumComponents(self):
    pass
  def getRefCount(self):
    pass
  def getSource(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lastStart(self):
    pass
  def length(self):
    pass
  def markBamModified(self):
    pass
  def nextStart(self):
    pass
  def ready(self):
    pass
  def ref(self):
    pass
  def setupTexture(self):
    pass
  def sizeX(self):
    pass
  def sizeY(self):
    pass
  def streaming(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class MovingPartACMatrixSwitchType:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getDefaultValue(self):
    pass
  def getForcedChannel(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class MovingPartACScalarSwitchType:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getDefaultValue(self):
    pass
  def getForcedChannel(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class MovingPartBase:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getForcedChannel(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class MovingPartMatrix:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getDefaultValue(self):
    pass
  def getForcedChannel(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class MovingPartScalar:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getBound(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getDefaultValue(self):
    pass
  def getForcedChannel(self):
    pass
  def getMaxBound(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def outputValue(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class MultiLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class MultitexReducer:
  def __init__(self):
    pass
  def clear(self):
    pass
  def flatten(self):
    pass
  def scan(self):
    pass
  def setAllowTexMat(self):
    pass
  def setTarget(self):
    pass
  def setUseGeom(self):
    pass
class Mutex:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
  def tryAcquire(self):
    pass
class MutexDirect:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
  def tryAcquire(self):
    pass
class NativeWindowHandle:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getIntHandle(self):
    pass
  def getOsHandle(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeInt():
    pass
  def makeSubprocess():
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def sendWindowsMessage(self):
    pass
  def setOsHandle(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class NetAddress:
  def __init__(self):
    pass
  def clear(self):
    pass
  def getAddr(self):
    pass
  def getIp(self):
    pass
  def getIpComponent(self):
    pass
  def getIpString(self):
    pass
  def getPort(self):
    pass
  def output(self):
    pass
  def setAny(self):
    pass
  def setHost(self):
    pass
  def setLocalhost(self):
    pass
  def setPort(self):
    pass
class NetDatagram:
  def __init__(self):
    pass
  def addBeFloat32(self):
    pass
  def addBeFloat64(self):
    pass
  def addBeInt16(self):
    pass
  def addBeInt32(self):
    pass
  def addBeInt64(self):
    pass
  def addBeUint16(self):
    pass
  def addBeUint32(self):
    pass
  def addBeUint64(self):
    pass
  def addBool(self):
    pass
  def addFixedString(self):
    pass
  def addFloat32(self):
    pass
  def addFloat64(self):
    pass
  def addInt16(self):
    pass
  def addInt32(self):
    pass
  def addInt64(self):
    pass
  def addInt8(self):
    pass
  def addString(self):
    pass
  def addString32(self):
    pass
  def addUint16(self):
    pass
  def addUint32(self):
    pass
  def addUint64(self):
    pass
  def addUint8(self):
    pass
  def addWstring(self):
    pass
  def addZString(self):
    pass
  def appendData(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def copyArray(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def dumpHex(self):
    pass
  def eq(self):
    pass
  def getAddress(self):
    pass
  def getArray(self):
    pass
  def getClassType():
    pass
  def getConnection(self):
    pass
  def getLength(self):
    pass
  def getMessage(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lessThan(self):
    pass
  def modifyArray(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def padBytes(self):
    pass
  def setAddress(self):
    pass
  def setArray(self):
    pass
  def setConnection(self):
    pass
  def write(self):
    pass
class NoBlendType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class NodeCachedReferenceCount:
  def __init__(self):
    pass
  RCache = int

  RNode = int

  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getNodeRefCount(self):
    pass
  def getRefCount(self):
    pass
  def getReferencedBits(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def nodeRef(self):
    pass
  def nodeUnref(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class NodeCullCallbackData:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getData(self):
    pass
  def getTrav(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def upcall(self):
    pass
class NodePath:
  def __init__(self):
    pass
  ETFail = int

  ETNotFound = int

  ETOk = int

  ETRemoved = int

  def adjustAllPriorities(self):
    pass
  def analyze():
    pass
  def anyPath():
    pass
  def applyTextureColors(self):
    pass
  def assign(self):
    pass
  def attachCollisionRay():
    pass
  def attachCollisionSegment():
    pass
  def attachCollisionSphere():
    pass
  def attachNewNode(self):
    pass
  def calcTightBounds(self):
    pass
  def clearAntialias(self):
    pass
  def clearAttrib(self):
    pass
  def clearAudioVolume(self):
    pass
  def clearBillboard(self):
    pass
  def clearBin(self):
    pass
  def clearClipPlane(self):
    pass
  def clearColor(self):
    pass
  def clearColorScale(self):
    pass
  def clearCompass(self):
    pass
  def clearDepthOffset(self):
    pass
  def clearDepthTest(self):
    pass
  def clearDepthWrite(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFog(self):
    pass
  def clearLight(self):
    pass
  def clearMat(self):
    pass
  def clearMaterial(self):
    pass
  def clearModelNodes(self):
    pass
  def clearNormalMap(self):
    pass
  def clearProjectTexture(self):
    pass
  def clearPythonTag(self):
    pass
  def clearRenderMode(self):
    pass
  def clearScissor(self):
    pass
  def clearShader(self):
    pass
  def clearShaderInput(self):
    pass
  def clearTag(self):
    pass
  def clearTexGen(self):
    pass
  def clearTexProjector(self):
    pass
  def clearTexTransform(self):
    pass
  def clearTexture(self):
    pass
  def clearTransform(self):
    pass
  def clearTransparency(self):
    pass
  def clearTwoSided(self):
    pass
  def colorInterval():
    pass
  def colorScaleInterval():
    pass
  def compareTo(self):
    pass
  def composeColorScale(self):
    pass
  def copyTo(self):
    pass
  def countNumDescendants(self):
    pass
  def deselect():
    pass
  def detachNode(self):
    pass
  def doBillboardAxis(self):
    pass
  def doBillboardPointEye(self):
    pass
  def doBillboardPointWorld(self):
    pass
  def eq(self):
    pass
  def explore():
    pass
  def fail():
    pass
  def find(self):
    pass
  def findAllMatches(self):
    pass
  def findAllMaterials(self):
    pass
  def findAllPathsTo(self):
    pass
  def findAllTexcoords(self):
    pass
  def findAllTextureStages(self):
    pass
  def findAllTextures(self):
    pass
  def findAllVertexColumns(self):
    pass
  def findMaterial(self):
    pass
  def findNetPythonTag(self):
    pass
  def findNetTag(self):
    pass
  def findPathTo(self):
    pass
  def findTexture(self):
    pass
  def findTextureStage(self):
    pass
  def flattenLight(self):
    pass
  def flattenMedium(self):
    pass
  def flattenMultitex():
    pass
  def flattenStrong(self):
    pass
  def forceRecomputeBounds(self):
    pass
  def getAncestor(self):
    pass
  def getAncestors(self):
    pass
  def getAncestry():
    pass
  def getAntialias(self):
    pass
  def getAttrib(self):
    pass
  def getAudioVolume(self):
    pass
  def getBinDrawOrder(self):
    pass
  def getBinName(self):
    pass
  def getBounds(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getChildrenAsList():
    pass
  def getClassType():
    pass
  def getCollideMask(self):
    pass
  def getColor(self):
    pass
  def getColorScale(self):
    pass
  def getCommonAncestor(self):
    pass
  def getDepthOffset(self):
    pass
  def getDepthTest(self):
    pass
  def getDepthWrite(self):
    pass
  def getDistance(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getErrorType(self):
    pass
  def getFog(self):
    pass
  def getH(self):
    pass
  def getHiddenAncestor(self):
    pass
  def getHpr(self):
    pass
  def getInstanceCount(self):
    pass
  def getKey(self):
    pass
  def getMat(self):
    pass
  def getMaterial(self):
    pass
  def getMaxSearchDepth():
    pass
  def getName(self):
    pass
  def getNetAudioVolume(self):
    pass
  def getNetPrevTransform(self):
    pass
  def getNetPythonTag(self):
    pass
  def getNetState(self):
    pass
  def getNetTag(self):
    pass
  def getNetTransform(self):
    pass
  def getNode(self):
    pass
  def getNodes(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDescendants():
    pass
  def getNumNodes(self):
    pass
  def getP(self):
    pass
  def getParent(self):
    pass
  def getPos(self):
    pass
  def getPosDelta(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getQuat(self):
    pass
  def getR(self):
    pass
  def getRelativePoint(self):
    pass
  def getRelativeVector(self):
    pass
  def getRenderMode(self):
    pass
  def getRenderModePerspective(self):
    pass
  def getRenderModeThickness(self):
    pass
  def getSa(self):
    pass
  def getSb(self):
    pass
  def getScale(self):
    pass
  def getSg(self):
    pass
  def getShader(self):
    pass
  def getShaderInput(self):
    pass
  def getShear(self):
    pass
  def getShxy(self):
    pass
  def getShxz(self):
    pass
  def getShyz(self):
    pass
  def getSort(self):
    pass
  def getSr(self):
    pass
  def getStashedAncestor(self):
    pass
  def getStashedChildren(self):
    pass
  def getState(self):
    pass
  def getSx(self):
    pass
  def getSy(self):
    pass
  def getSz(self):
    pass
  def getTag(self):
    pass
  def getTexGen(self):
    pass
  def getTexGenLight(self):
    pass
  def getTexHpr(self):
    pass
  def getTexOffset(self):
    pass
  def getTexPos(self):
    pass
  def getTexProjectorFrom(self):
    pass
  def getTexProjectorTo(self):
    pass
  def getTexRotate(self):
    pass
  def getTexScale(self):
    pass
  def getTexScale3d(self):
    pass
  def getTexTransform(self):
    pass
  def getTexture(self):
    pass
  def getTightBounds():
    pass
  def getTop(self):
    pass
  def getTopNode(self):
    pass
  def getTransform(self):
    pass
  def getTransparency(self):
    pass
  def getTwoSided(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def hasAntialias(self):
    pass
  def hasAttrib(self):
    pass
  def hasAudioVolume(self):
    pass
  def hasBillboard(self):
    pass
  def hasBin(self):
    pass
  def hasClipPlane(self):
    pass
  def hasClipPlaneOff(self):
    pass
  def hasColor(self):
    pass
  def hasColorScale(self):
    pass
  def hasCompass(self):
    pass
  def hasDepthOffset(self):
    pass
  def hasDepthTest(self):
    pass
  def hasDepthWrite(self):
    pass
  def hasEffect(self):
    pass
  def hasFog(self):
    pass
  def hasFogOff(self):
    pass
  def hasLight(self):
    pass
  def hasLightOff(self):
    pass
  def hasMat(self):
    pass
  def hasMaterial(self):
    pass
  def hasNetPythonTag(self):
    pass
  def hasNetTag(self):
    pass
  def hasParent(self):
    pass
  def hasPythonTag(self):
    pass
  def hasRenderMode(self):
    pass
  def hasScissor(self):
    pass
  def hasTag(self):
    pass
  def hasTexGen(self):
    pass
  def hasTexProjector(self):
    pass
  def hasTexTransform(self):
    pass
  def hasTexcoord(self):
    pass
  def hasTexture(self):
    pass
  def hasTextureOff(self):
    pass
  def hasTransparency(self):
    pass
  def hasTwoSided(self):
    pass
  def hasVertexColumn(self):
    pass
  def headsUp(self):
    pass
  def hide(self):
    pass
  def hideBounds(self):
    pass
  def hideCS():
    pass
  def hideSiblings():
    pass
  def hprInterval():
    pass
  def hprScaleInterval():
    pass
  def iHpr():
    pass
  def iPos():
    pass
  def iPosHpr():
    pass
  def iPosHprScale():
    pass
  def iScale():
    pass
  def id():
    pass
  def instanceTo(self):
    pass
  def instanceUnderNode(self):
    pass
  def isAncestorOf(self):
    pass
  def isEmpty(self):
    pass
  def isHidden(self):
    pass
  def isSameGraph(self):
    pass
  def isSingleton(self):
    pass
  def isStashed(self):
    pass
  def isolate():
    pass
  def lerpColor():
    pass
  def lerpColorRGBA():
    pass
  def lerpColorRGBARGBA():
    pass
  def lerpColorScale():
    pass
  def lerpColorScaleRGBA():
    pass
  def lerpColorScaleRGBARGBA():
    pass
  def lerpColorScaleVBase4():
    pass
  def lerpColorScaleVBase4VBase4():
    pass
  def lerpColorVBase4():
    pass
  def lerpColorVBase4VBase4():
    pass
  def lerpHpr():
    pass
  def lerpHprHPR():
    pass
  def lerpHprVBase3():
    pass
  def lerpPos():
    pass
  def lerpPosHpr():
    pass
  def lerpPosHprPoint3VBase3():
    pass
  def lerpPosHprScale():
    pass
  def lerpPosHprXYZHPR():
    pass
  def lerpPosPoint3():
    pass
  def lerpPosXYZ():
    pass
  def lerpScale():
    pass
  def lerpScaleVBase3():
    pass
  def lerpScaleXYZ():
    pass
  def lessThan(self):
    pass
  def listTags(self):
    pass
  def lookAt(self):
    pass
  def ls(self):
    pass
  def lsNames():
    pass
  def lsNamesRecurse():
    pass
  def ne(self):
    pass
  def node(self):
    pass
  def notFound():
    pass
  def output(self):
    pass
  def pPrintString():
    pass
  def place():
    pass
  def posHprInterval():
    pass
  def posHprScaleInterval():
    pass
  def posHprScaleShearInterval():
    pass
  def posInterval():
    pass
  def posQuatInterval():
    pass
  def posQuatScaleInterval():
    pass
  def posQuatScaleShearInterval():
    pass
  def premungeScene(self):
    pass
  def prepareScene(self):
    pass
  def printChildren():
    pass
  def printHpr():
    pass
  def printPos():
    pass
  def printPosHpr():
    pass
  def printPosHprScale():
    pass
  def printScale():
    pass
  def printTransform():
    pass
  def projectTexture(self):
    pass
  def quatInterval():
    pass
  def quatScaleInterval():
    pass
  def r_constructCollisionTree():
    pass
  def r_subdivideCollisions():
    pass
  def remove():
    pass
  def removeChildren():
    pass
  def removeNode(self):
    pass
  def removeNonCollisions():
    pass
  def removed():
    pass
  def reparentTo(self):
    pass
  def reverseLs(self):
    pass
  def reverseLsNames():
    pass
  def rgbPanel():
    pass
  def scaleInterval():
    pass
  def select():
    pass
  def setAllColorScale(self):
    pass
  def setAlphaScale(self):
    pass
  def setAntialias(self):
    pass
  def setAttrib(self):
    pass
  def setAudioVolume(self):
    pass
  def setAudioVolumeOff(self):
    pass
  def setBillboardAxis(self):
    pass
  def setBillboardPointEye(self):
    pass
  def setBillboardPointWorld(self):
    pass
  def setBin(self):
    pass
  def setClipPlane(self):
    pass
  def setClipPlaneOff(self):
    pass
  def setCollideMask(self):
    pass
  def setColor(self):
    pass
  def setColorOff(self):
    pass
  def setColorScale(self):
    pass
  def setColorScaleOff(self):
    pass
  def setCompass(self):
    pass
  def setDepthOffset(self):
    pass
  def setDepthTest(self):
    pass
  def setDepthWrite(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFluidPos(self):
    pass
  def setFluidX(self):
    pass
  def setFluidY(self):
    pass
  def setFluidZ(self):
    pass
  def setFog(self):
    pass
  def setFogOff(self):
    pass
  def setH(self):
    pass
  def setHpr(self):
    pass
  def setHprScale(self):
    pass
  def setInstanceCount(self):
    pass
  def setLight(self):
    pass
  def setLightOff(self):
    pass
  def setMat(self):
    pass
  def setMaterial(self):
    pass
  def setMaterialOff(self):
    pass
  def setMaxSearchDepth():
    pass
  def setName(self):
    pass
  def setNormalMap(self):
    pass
  def setP(self):
    pass
  def setPos(self):
    pass
  def setPosHpr(self):
    pass
  def setPosHprScale(self):
    pass
  def setPosHprScaleShear(self):
    pass
  def setPosQuat(self):
    pass
  def setPosQuatScale(self):
    pass
  def setPosQuatScaleShear(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setQuat(self):
    pass
  def setQuatScale(self):
    pass
  def setR(self):
    pass
  def setRenderMode(self):
    pass
  def setRenderModeFilled(self):
    pass
  def setRenderModePerspective(self):
    pass
  def setRenderModeThickness(self):
    pass
  def setRenderModeWireframe(self):
    pass
  def setSa(self):
    pass
  def setSb(self):
    pass
  def setScale(self):
    pass
  def setScissor(self):
    pass
  def setSg(self):
    pass
  def setShader(self):
    pass
  def setShaderAuto(self):
    pass
  def setShaderInput(self):
    pass
  def setShaderOff(self):
    pass
  def setShear(self):
    pass
  def setShxy(self):
    pass
  def setShxz(self):
    pass
  def setShyz(self):
    pass
  def setSr(self):
    pass
  def setState(self):
    pass
  def setSx(self):
    pass
  def setSy(self):
    pass
  def setSz(self):
    pass
  def setTag(self):
    pass
  def setTexGen(self):
    pass
  def setTexHpr(self):
    pass
  def setTexOffset(self):
    pass
  def setTexPos(self):
    pass
  def setTexProjector(self):
    pass
  def setTexRotate(self):
    pass
  def setTexScale(self):
    pass
  def setTexTransform(self):
    pass
  def setTexture(self):
    pass
  def setTextureOff(self):
    pass
  def setTransform(self):
    pass
  def setTransparency(self):
    pass
  def setTwoSided(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def shearInterval():
    pass
  def show(self):
    pass
  def showAllDescendants():
    pass
  def showBounds(self):
    pass
  def showCS():
    pass
  def showSiblings():
    pass
  def showThrough(self):
    pass
  def showTightBounds(self):
    pass
  def stash(self):
    pass
  def stashTo(self):
    pass
  def subdivideCollisions():
    pass
  def toggleVis():
    pass
  def unifyTextureStages(self):
    pass
  def unstash(self):
    pass
  def unstashAll(self):
    pass
  def verifyComplete(self):
    pass
  def writeBamFile(self):
    pass
  def writeBamStream(self):
    pass
  def writeBounds(self):
    pass
  def wrtReparentTo(self):
    pass
class NodePathCollection:
  def __init__(self):
    pass
  def addPath(self):
    pass
  def addPathsFrom(self):
    pass
  def asList():
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def composeColorScale(self):
    pass
  def detach(self):
    pass
  def findAllMatches(self):
    pass
  def getCollideMask(self):
    pass
  def getNumPaths(self):
    pass
  def getPath(self):
    pass
  def getPaths(self):
    pass
  def getTightBounds():
    pass
  def hasPath(self):
    pass
  def hide(self):
    pass
  def isEmpty(self):
    pass
  def ls(self):
    pass
  def output(self):
    pass
  def removeDuplicatePaths(self):
    pass
  def removePath(self):
    pass
  def removePathsFrom(self):
    pass
  def reparentTo(self):
    pass
  def setAttrib(self):
    pass
  def setCollideMask(self):
    pass
  def setColor(self):
    pass
  def setColorScale(self):
    pass
  def setTexture(self):
    pass
  def setTextureOff(self):
    pass
  def show(self):
    pass
  def size(self):
    pass
  def stash(self):
    pass
  def unstash(self):
    pass
  def write(self):
    pass
  def wrtReparentTo(self):
    pass
class NodeVertexTransform:
  def __init__(self):
    pass
  def accumulateMatrix(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getGlobalModified():
    pass
  def getMatrix(self):
    pass
  def getModified(self):
    pass
  def getNextModified():
    pass
  def getNode(self):
    pass
  def getPrev(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def multMatrix(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class NurbsCurve:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def adjustPoint(self):
    pass
  def adjustPt(self):
    pass
  def adjustTangent(self):
    pass
  def appendCv(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcLength(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToNurbsCurve(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findLength(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def get2ndtangent(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCurveType(self):
    pass
  def getCv(self):
    pass
  def getCvPoint(self):
    pass
  def getCvWeight(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKnot(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMaxT(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumCvs(self):
    pass
  def getNumDimensions(self):
    pass
  def getNumKnots(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOrder(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPt(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTangent(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def insertCv(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeAllCvs(self):
    pass
  def removeChild(self):
    pass
  def removeCv(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCurveType(self):
    pass
  def setCv(self):
    pass
  def setCvPoint(self):
    pass
  def setCvWeight(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setKnot(self):
    pass
  def setName(self):
    pass
  def setNumDimensions(self):
    pass
  def setOrder(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def stitch(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToNurbsCurveInterface(self):
    pass
  def upcastToPiecewiseCurve(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeCv(self):
    pass
  def writeEgg(self):
    pass
class NurbsCurveEvaluator:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def evaluate(self):
    pass
  def getClassType():
    pass
  def getExtendedVertex(self):
    pass
  def getKnot(self):
    pass
  def getKnots(self):
    pass
  def getNumKnots(self):
    pass
  def getNumSegments(self):
    pass
  def getNumVertices(self):
    pass
  def getOrder(self):
    pass
  def getRefCount(self):
    pass
  def getVertex(self):
    pass
  def getVertexSpace(self):
    pass
  def getVertices(self):
    pass
  def normalizeKnots(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def reset(self):
    pass
  def setExtendedVertex(self):
    pass
  def setKnot(self):
    pass
  def setOrder(self):
    pass
  def setVertex(self):
    pass
  def setVertexSpace(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class NurbsCurveInterface:
  def __init__(self):
    pass
  def appendCv(self):
    pass
  def downcastToNurbsCurve(self):
    pass
  def getClassType():
    pass
  def getCv(self):
    pass
  def getCvPoint(self):
    pass
  def getCvWeight(self):
    pass
  def getKnot(self):
    pass
  def getNumCvs(self):
    pass
  def getNumKnots(self):
    pass
  def getOrder(self):
    pass
  def insertCv(self):
    pass
  def removeAllCvs(self):
    pass
  def removeCv(self):
    pass
  def setCv(self):
    pass
  def setCvPoint(self):
    pass
  def setCvWeight(self):
    pass
  def setKnot(self):
    pass
  def setOrder(self):
    pass
  def writeCv(self):
    pass
class NurbsCurveResult:
  def __init__(self):
    pass
  def adaptiveSample(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def evalExtendedPoint(self):
    pass
  def evalPoint(self):
    pass
  def evalSegmentExtendedPoint(self):
    pass
  def evalSegmentPoint(self):
    pass
  def evalSegmentTangent(self):
    pass
  def evalTangent(self):
    pass
  def getClassType():
    pass
  def getEndT(self):
    pass
  def getNumSamples(self):
    pass
  def getNumSegments(self):
    pass
  def getRefCount(self):
    pass
  def getSamplePoint(self):
    pass
  def getSamplePoints(self):
    pass
  def getSampleT(self):
    pass
  def getSampleTs(self):
    pass
  def getSegmentT(self):
    pass
  def getStartT(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class NurbsSurfaceEvaluator:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def evaluate(self):
    pass
  def getClassType():
    pass
  def getExtendedVertex(self):
    pass
  def getNumUKnots(self):
    pass
  def getNumUSegments(self):
    pass
  def getNumUVertices(self):
    pass
  def getNumVKnots(self):
    pass
  def getNumVSegments(self):
    pass
  def getNumVVertices(self):
    pass
  def getRefCount(self):
    pass
  def getUKnot(self):
    pass
  def getUKnots(self):
    pass
  def getUOrder(self):
    pass
  def getVKnot(self):
    pass
  def getVKnots(self):
    pass
  def getVOrder(self):
    pass
  def getVertex(self):
    pass
  def getVertexSpace(self):
    pass
  def normalizeUKnots(self):
    pass
  def normalizeVKnots(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def reset(self):
    pass
  def setExtendedVertex(self):
    pass
  def setUKnot(self):
    pass
  def setUOrder(self):
    pass
  def setVKnot(self):
    pass
  def setVOrder(self):
    pass
  def setVertex(self):
    pass
  def setVertexSpace(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class NurbsSurfaceResult:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def evalExtendedPoint(self):
    pass
  def evalNormal(self):
    pass
  def evalPoint(self):
    pass
  def evalSegmentExtendedPoint(self):
    pass
  def evalSegmentNormal(self):
    pass
  def evalSegmentPoint(self):
    pass
  def getClassType():
    pass
  def getEndU(self):
    pass
  def getEndV(self):
    pass
  def getNumUSegments(self):
    pass
  def getNumVSegments(self):
    pass
  def getRefCount(self):
    pass
  def getSegmentU(self):
    pass
  def getSegmentV(self):
    pass
  def getStartU(self):
    pass
  def getStartV(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class OmniBoundingVolume:
  def __init__(self):
    pass
  BTBest = int

  BTBox = int

  BTDefault = int

  BTSphere = int

  IFAll = int

  IFDontUnderstand = int

  IFNoIntersection = int

  IFPossible = int

  IFSome = int

  def around(self):
    pass
  def contains(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def extendBy(self):
    pass
  def getApproxCenter(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isInfinite(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setInfinite(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class OrthographicLens:
  def __init__(self):
    pass
  FCAspectRatio = int

  FCCameraPlane = int

  FCKeystone = int

  FCOffAxis = int

  FCRoll = int

  FCShear = int

  SCLeft = int

  SCMono = int

  SCRight = int

  SCStereo = int

  def clear(self):
    pass
  def clearKeystone(self):
    pass
  def clearViewMat(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def extrude(self):
    pass
  def extrudeVec(self):
    pass
  def getAspectRatio(self):
    pass
  def getBamModified(self):
    pass
  def getChangeEvent(self):
    pass
  def getClassType():
    pass
  def getConvergenceDistance(self):
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultFar():
    pass
  def getDefaultNear():
    pass
  def getFar(self):
    pass
  def getFilmMat(self):
    pass
  def getFilmMatInv(self):
    pass
  def getFilmOffset(self):
    pass
  def getFilmSize(self):
    pass
  def getFocalLength(self):
    pass
  def getFov(self):
    pass
  def getHfov(self):
    pass
  def getInterocularDistance(self):
    pass
  def getKeystone(self):
    pass
  def getLensMat(self):
    pass
  def getLensMatInv(self):
    pass
  def getMinFov(self):
    pass
  def getNear(self):
    pass
  def getNodalPoint(self):
    pass
  def getProjectionMat(self):
    pass
  def getProjectionMatInv(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUpVector(self):
    pass
  def getVfov(self):
    pass
  def getViewHpr(self):
    pass
  def getViewMat(self):
    pass
  def getViewVector(self):
    pass
  def isExactType(self):
    pass
  def isLinear(self):
    pass
  def isOfType(self):
    pass
  def isOrthographic(self):
    pass
  def isPerspective(self):
    pass
  def makeBounds(self):
    pass
  def makeCopy(self):
    pass
  def makeGeometry(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def recomputeAll(self):
    pass
  def ref(self):
    pass
  def setAspectRatio(self):
    pass
  def setChangeEvent(self):
    pass
  def setConvergenceDistance(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setFar(self):
    pass
  def setFilmOffset(self):
    pass
  def setFilmSize(self):
    pass
  def setFocalLength(self):
    pass
  def setFov(self):
    pass
  def setFrustumFromCorners(self):
    pass
  def setInterocularDistance(self):
    pass
  def setKeystone(self):
    pass
  def setMinFov(self):
    pass
  def setNear(self):
    pass
  def setNearFar(self):
    pass
  def setViewHpr(self):
    pass
  def setViewMat(self):
    pass
  def setViewVector(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
PCTHPR = int

PCTNONE = int

PCTT = int

PCTXYZ = int

class PGButton:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  SDepressed = int

  SInactive = int

  SReady = int

  SRollover = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addClickButton(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getActive(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClickEvent(self):
    pass
  def getClickPrefix():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getTextNode():
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def hasAttrib(self):
    pass
  def hasClickButton(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isButtonDown(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeClickButton(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setTextNode():
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setup(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGEntry:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  SFocus = int

  SInactive = int

  SNoFocus = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearCursorDef(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAcceptEvent(self):
    pass
  def getAcceptFailedEvent(self):
    pass
  def getAcceptFailedPrefix():
    pass
  def getAcceptPrefix():
    pass
  def getActive(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBlinkRate(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCandidateActive(self):
    pass
  def getCandidateInactive(self):
    pass
  def getCharacter(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCursorDef(self):
    pass
  def getCursorKeysActive(self):
    pass
  def getCursorPosition(self):
    pass
  def getCursorX(self):
    pass
  def getCursorY(self):
    pass
  def getCursormoveEvent(self):
    pass
  def getCursormovePrefix():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getEraseEvent(self):
    pass
  def getErasePrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getGraphic(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLegalCollideMask(self):
    pass
  def getMaxChars(self):
    pass
  def getMaxWidth(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumCharacters(self):
    pass
  def getNumChildren(self):
    pass
  def getNumLines(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getObscureMode(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getOverflowEvent(self):
    pass
  def getOverflowMode(self):
    pass
  def getOverflowPrefix():
    pass
  def getParent(self):
    pass
  def getPlainText(self):
    pass
  def getPlainWtext(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getProperties(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getText(self):
    pass
  def getTextDef(self):
    pass
  def getTextNode():
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeEvent(self):
    pass
  def getTypeIndex(self):
    pass
  def getTypePrefix():
    pass
  def getUnexpectedChange(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def getWtext(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isWtext(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAcceptEnabled(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBlinkRate(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCandidateActive(self):
    pass
  def setCandidateInactive(self):
    pass
  def setCursorKeysActive(self):
    pass
  def setCursorPosition(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMaxChars(self):
    pass
  def setMaxWidth(self):
    pass
  def setName(self):
    pass
  def setNumLines(self):
    pass
  def setObscureMode(self):
    pass
  def setOverallHidden(self):
    pass
  def setOverflowMode(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setText(self):
    pass
  def setTextDef(self):
    pass
  def setTextNode():
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setWtext(self):
    pass
  def setup(self):
    pass
  def setupMinimal(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGFrameStyle:
  def __init__(self):
    pass
  TBevelIn = int

  TBevelOut = int

  TFlat = int

  TGroove = int

  TNone = int

  TRidge = int

  TTextureBorder = int

  def assign(self):
    pass
  def clearTexture(self):
    pass
  def getColor(self):
    pass
  def getInternalFrame(self):
    pass
  def getTexture(self):
    pass
  def getType(self):
    pass
  def getUvWidth(self):
    pass
  def getVisibleScale(self):
    pass
  def getWidth(self):
    pass
  def hasTexture(self):
    pass
  def output(self):
    pass
  def setColor(self):
    pass
  def setTexture(self):
    pass
  def setType(self):
    pass
  def setUvWidth(self):
    pass
  def setVisibleScale(self):
    pass
  def setWidth(self):
    pass
class PGItem:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getActive(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getTextNode():
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setTextNode():
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGMouseWatcherBackground:
  def __init__(self):
    pass
  SFAnyButton = int

  SFMouseButton = int

  SFMousePosition = int

  SFOtherButton = int

  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActive(self):
    pass
  def getArea(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFrame(self):
    pass
  def getKeyboard(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getSuppressFlags(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setActive(self):
    pass
  def setFrame(self):
    pass
  def setKeyboard(self):
    pass
  def setName(self):
    pass
  def setSort(self):
    pass
  def setSuppressFlags(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
class PGMouseWatcherParameter:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getButton(self):
    pass
  def getCandidateStringEncoded(self):
    pass
  def getClassType():
    pass
  def getCursorPos(self):
    pass
  def getHighlightEnd(self):
    pass
  def getHighlightStart(self):
    pass
  def getKeycode(self):
    pass
  def getModifierButtons(self):
    pass
  def getMouse(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasButton(self):
    pass
  def hasCandidate(self):
    pass
  def hasKeycode(self):
    pass
  def hasMouse(self):
    pass
  def isExactType(self):
    pass
  def isKeyrepeat(self):
    pass
  def isOfType(self):
    pass
  def isOutside(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToMouseWatcherParameter(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class PGScrollFrame:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearClipFrame(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearHorizontalSlider(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def clearVerticalSlider(self):
    pass
  def clearVirtualFrame(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGScrollFrame(self):
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getActive(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getAutoHide(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCanvasNode(self):
    pass
  def getCanvasParent(self):
    pass
  def getCanvasTransform(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClipFrame(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getHorizontalSlider(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLegalCollideMask(self):
    pass
  def getManagePieces(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getTextNode():
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getVerticalSlider(self):
    pass
  def getVirtualFrame(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def hasAttrib(self):
    pass
  def hasClipFrame(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hasVirtualFrame(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def remanage(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setAutoHide(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCanvasTransform(self):
    pass
  def setClipFrame(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setHorizontalSlider(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setManagePieces(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setTextNode():
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setVerticalSlider(self):
    pass
  def setVirtualFrame(self):
    pass
  def setup(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPGVirtualFrame(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGSliderBar:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearLeftButton(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearRightButton(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearThumbButton(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getActive(self):
    pass
  def getAdjustEvent(self):
    pass
  def getAdjustPrefix():
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getAxis(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLeftButton(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getManagePieces(self):
    pass
  def getMaxValue(self):
    pass
  def getMinValue(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getPageSize(self):
    pass
  def getParent(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRatio(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getResizeThumb(self):
    pass
  def getRightButton(self):
    pass
  def getScrollSize(self):
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getTextNode():
    pass
  def getThumbButton(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getValue(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isButtonDown(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def remanage(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setAxis(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLeftButton(self):
    pass
  def setManagePieces(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPageSize(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setRange(self):
    pass
  def setRatio(self):
    pass
  def setResizeThumb(self):
    pass
  def setRightButton(self):
    pass
  def setScrollSize(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setTextNode():
    pass
  def setThumbButton(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setValue(self):
    pass
  def setupScrollBar(self):
    pass
  def setupSlider(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPGItem(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGTop:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getGroup(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMouseWatcher(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStartSort(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMouseWatcher(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setStartSort(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGVirtualFrame:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearClipFrame(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGScrollFrame(self):
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getActive(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCanvasNode(self):
    pass
  def getCanvasParent(self):
    pass
  def getCanvasTransform(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClipFrame(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getTextNode():
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def hasAttrib(self):
    pass
  def hasClipFrame(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCanvasTransform(self):
    pass
  def setClipFrame(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setTextNode():
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setup(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PGWaitBar:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFrame(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearSound(self):
    pass
  def clearState(self):
    pass
  def clearStateDef(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToPGSliderBar(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getActive(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBackgroundFocus(self):
    pass
  def getBamModified(self):
    pass
  def getBarStyle(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEnterEvent(self):
    pass
  def getEnterPrefix():
    pass
  def getExitEvent(self):
    pass
  def getExitPrefix():
    pass
  def getFancyBits(self):
    pass
  def getFocus(self):
    pass
  def getFocusInEvent(self):
    pass
  def getFocusInPrefix():
    pass
  def getFocusItem():
    pass
  def getFocusOutEvent(self):
    pass
  def getFocusOutPrefix():
    pass
  def getFrame(self):
    pass
  def getFrameInvXform(self):
    pass
  def getFrameStyle(self):
    pass
  def getId(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getKeystrokeEvent(self):
    pass
  def getKeystrokePrefix():
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumStateDefs(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPercent(self):
    pass
  def getPressEvent(self):
    pass
  def getPressPrefix():
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRange(self):
    pass
  def getRefCount(self):
    pass
  def getReleaseEvent(self):
    pass
  def getReleasePrefix():
    pass
  def getRepeatEvent(self):
    pass
  def getRepeatPrefix():
    pass
  def getSound(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStateDef(self):
    pass
  def getStateDefs(self):
    pass
  def getSuppressFlags(self):
    pass
  def getTag(self):
    pass
  def getTextNode():
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getValue(self):
    pass
  def getWithinEvent(self):
    pass
  def getWithinPrefix():
    pass
  def getWithoutEvent(self):
    pass
  def getWithoutPrefix():
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasFrame(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasSound(self):
    pass
  def hasStateDef(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def instanceToStateDef(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttrib(self):
    pass
  def setBackgroundFocus(self):
    pass
  def setBarStyle(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFocus(self):
    pass
  def setFrame(self):
    pass
  def setFrameStyle(self):
    pass
  def setId(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setRange(self):
    pass
  def setSound(self):
    pass
  def setState(self):
    pass
  def setSuppressFlags(self):
    pass
  def setTag(self):
    pass
  def setTextNode():
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setValue(self):
    pass
  def setup(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PNMBrush:
  def __init__(self):
    pass
  BEBlend = int

  BEDarken = int

  BELighten = int

  BESet = int

  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def makeImage():
    pass
  def makePixel():
    pass
  def makeSpot():
    pass
  def makeTransparent():
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class PNMFileType:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getExtension(self):
    pass
  def getExtensions(self):
    pass
  def getName(self):
    pass
  def getNumExtensions(self):
    pass
  def getSuggestedExtension(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
class PNMFileTypeRegistry:
  def __init__(self):
    pass
  def getGlobalPtr():
    pass
  def getNumTypes(self):
    pass
  def getType(self):
    pass
  def getTypeByHandle(self):
    pass
  def getTypeFromExtension(self):
    pass
  def getTypeFromMagicNumber(self):
    pass
  def getTypes(self):
    pass
  def write(self):
    pass
class PNMImage:
  def __init__(self):
    pass
  CTColor = int

  CTFourChannel = int

  CTGrayscale = int

  CTInvalid = int

  CTTwoChannel = int

  def addAlpha(self):
    pass
  def alphaFill(self):
    pass
  def alphaFillVal(self):
    pass
  def assign(self):
    pass
  def blend(self):
    pass
  def blendSubImage(self):
    pass
  def boxFilter(self):
    pass
  def boxFilterFrom(self):
    pass
  def clampVal(self):
    pass
  def clear(self):
    pass
  def clearReadSize(self):
    pass
  def copyChannel(self):
    pass
  def copyFrom(self):
    pass
  def copyHeaderFrom(self):
    pass
  def copySubImage(self):
    pass
  def darkenSubImage(self):
    pass
  def expandBorder(self):
    pass
  def fill(self):
    pass
  def fillVal(self):
    pass
  def fromVal(self):
    pass
  def gaussianFilter(self):
    pass
  def gaussianFilterFrom(self):
    pass
  def getAlpha(self):
    pass
  def getAlphaVal(self):
    pass
  def getBlue(self):
    pass
  def getBlueVal(self):
    pass
  def getBright(self):
    pass
  def getChannel(self):
    pass
  def getChannelVal(self):
    pass
  def getColorType(self):
    pass
  def getComment(self):
    pass
  def getGray(self):
    pass
  def getGrayVal(self):
    pass
  def getGreen(self):
    pass
  def getGreenVal(self):
    pass
  def getMaxval(self):
    pass
  def getNumChannels(self):
    pass
  def getPixel(self):
    pass
  def getReadXSize(self):
    pass
  def getReadYSize(self):
    pass
  def getRed(self):
    pass
  def getRedVal(self):
    pass
  def getType(self):
    pass
  def getXSize(self):
    pass
  def getXel(self):
    pass
  def getXelA(self):
    pass
  def getXelVal(self):
    pass
  def getYSize(self):
    pass
  def hasAlpha(self):
    pass
  def hasReadSize(self):
    pass
  def hasType(self):
    pass
  def isGrayscale(self):
    pass
  def isValid(self):
    pass
  def lightenSubImage(self):
    pass
  def makeGrayscale(self):
    pass
  def makeHistogram(self):
    pass
  def makeRgb(self):
    pass
  def output(self):
    pass
  def quickFilterFrom(self):
    pass
  def read(self):
    pass
  def readHeader(self):
    pass
  def readMagicNumber():
    pass
  def remixChannels(self):
    pass
  def removeAlpha(self):
    pass
  def renderSpot(self):
    pass
  def setAlpha(self):
    pass
  def setAlphaVal(self):
    pass
  def setBlue(self):
    pass
  def setBlueVal(self):
    pass
  def setChannel(self):
    pass
  def setChannelVal(self):
    pass
  def setColorType(self):
    pass
  def setComment(self):
    pass
  def setGray(self):
    pass
  def setGrayVal(self):
    pass
  def setGreen(self):
    pass
  def setGreenVal(self):
    pass
  def setMaxval(self):
    pass
  def setNumChannels(self):
    pass
  def setPixel(self):
    pass
  def setReadSize(self):
    pass
  def setRed(self):
    pass
  def setRedVal(self):
    pass
  def setType(self):
    pass
  def setXel(self):
    pass
  def setXelA(self):
    pass
  def setXelVal(self):
    pass
  def takeFrom(self):
    pass
  def threshold(self):
    pass
  def toVal(self):
    pass
  def write(self):
    pass
class PNMImageHeader:
  def __init__(self):
    pass
  CTColor = int

  CTFourChannel = int

  CTGrayscale = int

  CTInvalid = int

  CTTwoChannel = int

  def assign(self):
    pass
  def getColorType(self):
    pass
  def getComment(self):
    pass
  def getMaxval(self):
    pass
  def getNumChannels(self):
    pass
  def getType(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def hasAlpha(self):
    pass
  def hasType(self):
    pass
  def isGrayscale(self):
    pass
  def output(self):
    pass
  def readHeader(self):
    pass
  def readMagicNumber():
    pass
  def setComment(self):
    pass
  def setType(self):
    pass
class PNMPainter:
  def __init__(self):
    pass
  def drawLine(self):
    pass
  def drawPoint(self):
    pass
  def drawRectangle(self):
    pass
  def getFill(self):
    pass
  def getPen(self):
    pass
  def setFill(self):
    pass
  def setPen(self):
    pass
class PNMTextGlyph:
  def __init__(self):
    pass
  def getAdvance(self):
    pass
  def getBottom(self):
    pass
  def getHeight(self):
    pass
  def getInteriorFlag(self):
    pass
  def getLeft(self):
    pass
  def getRight(self):
    pass
  def getTop(self):
    pass
  def getValue(self):
    pass
  def getWidth(self):
    pass
  def place(self):
    pass
class PNMTextMaker:
  def __init__(self):
    pass
  ACenter = int

  ALeft = int

  ARight = int

  def assign(self):
    pass
  def calcWidth(self):
    pass
  def clearName(self):
    pass
  def generateInto(self):
    pass
  def getAlign(self):
    pass
  def getClassType():
    pass
  def getFg(self):
    pass
  def getFontPixelSize(self):
    pass
  def getGlyph(self):
    pass
  def getInterior(self):
    pass
  def getInteriorFlag(self):
    pass
  def getLineHeight(self):
    pass
  def getName(self):
    pass
  def getNativeAntialias(self):
    pass
  def getPixelSize(self):
    pass
  def getPixelsPerUnit(self):
    pass
  def getPointSize(self):
    pass
  def getPointsPerInch():
    pass
  def getPointsPerUnit():
    pass
  def getScaleFactor(self):
    pass
  def getSpaceAdvance(self):
    pass
  def hasName(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def setAlign(self):
    pass
  def setFg(self):
    pass
  def setInterior(self):
    pass
  def setInteriorFlag(self):
    pass
  def setName(self):
    pass
  def setNativeAntialias(self):
    pass
  def setPixelSize(self):
    pass
  def setPixelsPerUnit(self):
    pass
  def setPointSize(self):
    pass
  def setScaleFactor(self):
    pass
class PStatClient:
  def __init__(self):
    pass
  def clientConnect(self):
    pass
  def clientDisconnect(self):
    pass
  def clientIsConnected(self):
    pass
  def clientMainTick(self):
    pass
  def clientResumeAfterPause(self):
    pass
  def clientThreadTick(self):
    pass
  def closeConnection(self):
    pass
  def connect():
    pass
  def disconnect():
    pass
  def downcastToQueuedConnectionManager(self):
    pass
  def getClientName(self):
    pass
  def getCollector(self):
    pass
  def getCollectorFullname(self):
    pass
  def getCollectorName(self):
    pass
  def getCollectors(self):
    pass
  def getCurrentThread(self):
    pass
  def getGlobalPstats():
    pass
  def getHostName():
    pass
  def getMainThread(self):
    pass
  def getMaxRate(self):
    pass
  def getNumCollectors(self):
    pass
  def getNumThreads(self):
    pass
  def getRealTime(self):
    pass
  def getThread(self):
    pass
  def getThreadName(self):
    pass
  def getThreadObject(self):
    pass
  def getThreadSyncName(self):
    pass
  def getThreads(self):
    pass
  def isConnected():
    pass
  def mainTick():
    pass
  def openTCPClientConnection(self):
    pass
  def openTCPServerRendezvous(self):
    pass
  def openUDPConnection(self):
    pass
  def resumeAfterPause():
    pass
  def setClientName(self):
    pass
  def setMaxRate(self):
    pass
  def threadTick():
    pass
  def upcastToConnectionManager(self):
    pass
class PStatCollector:
  def __init__(self):
    pass
  def addLevel(self):
    pass
  def addLevelNow(self):
    pass
  def addThreadLevel(self):
    pass
  def assign(self):
    pass
  def clearLevel(self):
    pass
  def clearThreadLevel(self):
    pass
  def flushLevel(self):
    pass
  def getFullname(self):
    pass
  def getIndex(self):
    pass
  def getLevel(self):
    pass
  def getName(self):
    pass
  def getThreadLevel(self):
    pass
  def isActive(self):
    pass
  def isStarted(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def setLevel(self):
    pass
  def setThreadLevel(self):
    pass
  def start(self):
    pass
  def stop(self):
    pass
  def subLevel(self):
    pass
  def subLevelNow(self):
    pass
  def subThreadLevel(self):
    pass
class PStatCollectorForward:
  def __init__(self):
    pass
  def addLevel(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class PStatThread:
  def __init__(self):
    pass
  def assign(self):
    pass
  def getIndex(self):
    pass
  def getThread(self):
    pass
  def newFrame(self):
    pass
class PandaLoader:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getGlobalPtr():
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskManager(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def loadAsync(self):
    pass
  def loadBamStream(self):
    pass
  def loadSync(self):
    pass
  def makeAsyncRequest(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setName(self):
    pass
  def setTaskChain(self):
    pass
  def setTaskManager(self):
    pass
  def stopThreads(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class PandaNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class Parabolad:
  def __init__(self):
    pass
  def assign(self):
    pass
  def calcPoint(self):
    pass
  def getA(self):
    pass
  def getB(self):
    pass
  def getC(self):
    pass
  def output(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class Parabolaf:
  def __init__(self):
    pass
  def assign(self):
    pass
  def calcPoint(self):
    pass
  def getA(self):
    pass
  def getB(self):
    pass
  def getC(self):
    pass
  def output(self):
    pass
  def write(self):
    pass
  def xform(self):
    pass
class ParametricCurve:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def adjustPoint(self):
    pass
  def adjustPt(self):
    pass
  def adjustTangent(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcLength(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findLength(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def get2ndtangent(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCurveType(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMaxT(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDimensions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPt(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTangent(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCurveType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNumDimensions(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def stitch(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeEgg(self):
    pass
class ParametricCurveCollection:
  def __init__(self):
    pass
  def addCurve(self):
    pass
  def addCurves(self):
    pass
  def adjustHpr(self):
    pass
  def adjustXyz(self):
    pass
  def clear(self):
    pass
  def clearTimewarps(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def evaluate(self):
    pass
  def evaluateHpr(self):
    pass
  def evaluateT(self):
    pass
  def evaluateXyz(self):
    pass
  def faceForward(self):
    pass
  def getClassType():
    pass
  def getCurve(self):
    pass
  def getCurves(self):
    pass
  def getDefaultCurve(self):
    pass
  def getHprCurve(self):
    pass
  def getMaxT(self):
    pass
  def getNumCurves(self):
    pass
  def getNumTimewarps(self):
    pass
  def getRefCount(self):
    pass
  def getTimewarpCurve(self):
    pass
  def getTimewarpCurves(self):
    pass
  def getXyzCurve(self):
    pass
  def hasCurve(self):
    pass
  def makeEven(self):
    pass
  def output(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def removeCurve(self):
    pass
  def resetMaxT(self):
    pass
  def stitch(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def write(self):
    pass
  def writeEgg(self):
    pass
class ParasiteBuffer:
  def __init__(self):
    pass
  FMParasite = int

  FMRefresh = int

  FMRender = int

  RTMBindOrCopy = int

  RTMCopyRam = int

  RTMCopyTexture = int

  RTMNone = int

  RTMTriggeredCopyRam = int

  RTMTriggeredCopyTexture = int

  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def addRenderTexture(self):
    pass
  def clearChildSort(self):
    pass
  def clearDeleteFlag(self):
    pass
  def clearRenderTextures(self):
    pass
  def countTextures(self):
    pass
  def decodeFromBamStream():
    pass
  def disableClears(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getActiveDisplayRegion(self):
    pass
  def getActiveDisplayRegions(self):
    pass
  def getBamModified(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getDeleteFlag(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getEngine(self):
    pass
  def getFbProperties(self):
    pass
  def getFbXSize(self):
    pass
  def getFbYSize(self):
    pass
  def getGsg(self):
    pass
  def getInverted(self):
    pass
  def getLeftEyeColorMask(self):
    pass
  def getName(self):
    pass
  def getNumActiveDisplayRegions(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getOneShot(self):
    pass
  def getPipe(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelZoom(self):
    pass
  def getRedBlueStereo(self):
    pass
  def getRefCount(self):
    pass
  def getRenderbufferType():
    pass
  def getRightEyeColorMask(self):
    pass
  def getRtmMode(self):
    pass
  def getScreenshot(self):
    pass
  def getSort(self):
    pass
  def getTexture(self):
    pass
  def getTextureCard(self):
    pass
  def getTexturePlane(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def hasSize(self):
    pass
  def hasTexture(self):
    pass
  def isActive(self):
    pass
  def isAnyClearActive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isStereo(self):
    pass
  def isValid(self):
    pass
  def makeCubeMap(self):
    pass
  def makeDisplayRegion(self):
    pass
  def makeMonoDisplayRegion(self):
    pass
  def makeScreenshotFilename():
    pass
  def makeStereoDisplayRegion(self):
    pass
  def makeTextureBuffer(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def removeAllDisplayRegions(self):
    pass
  def removeDisplayRegion(self):
    pass
  def saveScreenshot(self):
    pass
  def saveScreenshotDefault(self):
    pass
  def setActive(self):
    pass
  def setChildSort(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setInverted(self):
    pass
  def setOneShot(self):
    pass
  def setPixelZoom(self):
    pass
  def setRedBlueStereo(self):
    pass
  def setSize(self):
    pass
  def setSort(self):
    pass
  def setupRenderTexture(self):
    pass
  def shareDepthBuffer(self):
    pass
  def supportsPixelZoom(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def triggerCopy(self):
    pass
  def unref(self):
    pass
  def unshareDepthBuffer(self):
    pass
  def upcastToDrawableRegion(self):
    pass
  def upcastToGraphicsOutputBase(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class PartBundle:
  def __init__(self):
    pass
  BTComponentwise = int

  BTComponentwiseQuat = int

  BTLinear = int

  BTNormalizedLinear = int

  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def applyTransform(self):
    pass
  def assign(self):
    pass
  def bindAnim(self):
    pass
  def clearAnimPreload(self):
    pass
  def clearControlEffects(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def controlJoint(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def forceUpdate(self):
    pass
  def freezeJoint(self):
    pass
  def getAnimBlendFlag(self):
    pass
  def getAnimPreload(self):
    pass
  def getBamModified(self):
    pass
  def getBlendType(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getControlEffect(self):
    pass
  def getForcedChannel(self):
    pass
  def getFrameBlendFlag(self):
    pass
  def getName(self):
    pass
  def getNode(self):
    pass
  def getNodes(self):
    pass
  def getNumChildren(self):
    pass
  def getNumNodes(self):
    pass
  def getRefCount(self):
    pass
  def getRootXform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def loadBindAnim(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def mergeAnimPreloads(self):
    pass
  def modifyAnimPreload(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def releaseJoint(self):
    pass
  def setAnimBlendFlag(self):
    pass
  def setAnimPreload(self):
    pass
  def setBlendType(self):
    pass
  def setControlEffect(self):
    pass
  def setFrameBlendFlag(self):
    pass
  def setName(self):
    pass
  def setRootXform(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def update(self):
    pass
  def waitPending(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
  def xform(self):
    pass
class PartBundleHandle:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getBundle(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def ref(self):
    pass
  def setBundle(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class PartBundleNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getBundle(self):
    pass
  def getBundleHandle(self):
    pass
  def getBundleHandles(self):
    pass
  def getBundles(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumBundles(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PartGroup:
  def __init__(self):
    pass
  def applyControl(self):
    pass
  def applyFreeze(self):
    pass
  def applyFreezeMatrix(self):
    pass
  def applyFreezeScalar(self):
    pass
  def assign(self):
    pass
  def clearForcedChannel(self):
    pass
  def clearName(self):
    pass
  def copySubgraph(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def getBamModified(self):
    pass
  def getChild(self):
    pass
  def getChildren(self):
    pass
  def getClassType():
    pass
  def getForcedChannel(self):
    pass
  def getName(self):
    pass
  def getNumChildren(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isCharacterJoint(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def write(self):
    pass
  def writeWithValue(self):
    pass
class PartSubset:
  def __init__(self):
    pass
  def addExcludeJoint(self):
    pass
  def addIncludeJoint(self):
    pass
  def append(self):
    pass
  def assign(self):
    pass
  def isIncludeEmpty(self):
    pass
  def matchesExclude(self):
    pass
  def matchesInclude(self):
    pass
  def output(self):
    pass
class PerlinNoise:
  def __init__(self):
    pass
  def getSeed(self):
    pass
class PerlinNoise2:
  def __init__(self):
    pass
  def assign(self):
    pass
  def getSeed(self):
    pass
  def noise(self):
    pass
  def setScale(self):
    pass
class PerlinNoise3:
  def __init__(self):
    pass
  def assign(self):
    pass
  def getSeed(self):
    pass
  def noise(self):
    pass
  def setScale(self):
    pass
class PerspectiveLens:
  def __init__(self):
    pass
  FCAspectRatio = int

  FCCameraPlane = int

  FCKeystone = int

  FCOffAxis = int

  FCRoll = int

  FCShear = int

  SCLeft = int

  SCMono = int

  SCRight = int

  SCStereo = int

  def clear(self):
    pass
  def clearKeystone(self):
    pass
  def clearViewMat(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def extrude(self):
    pass
  def extrudeVec(self):
    pass
  def getAspectRatio(self):
    pass
  def getBamModified(self):
    pass
  def getChangeEvent(self):
    pass
  def getClassType():
    pass
  def getConvergenceDistance(self):
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultFar():
    pass
  def getDefaultNear():
    pass
  def getFar(self):
    pass
  def getFilmMat(self):
    pass
  def getFilmMatInv(self):
    pass
  def getFilmOffset(self):
    pass
  def getFilmSize(self):
    pass
  def getFocalLength(self):
    pass
  def getFov(self):
    pass
  def getHfov(self):
    pass
  def getInterocularDistance(self):
    pass
  def getKeystone(self):
    pass
  def getLensMat(self):
    pass
  def getLensMatInv(self):
    pass
  def getMinFov(self):
    pass
  def getNear(self):
    pass
  def getNodalPoint(self):
    pass
  def getProjectionMat(self):
    pass
  def getProjectionMatInv(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUpVector(self):
    pass
  def getVfov(self):
    pass
  def getViewHpr(self):
    pass
  def getViewMat(self):
    pass
  def getViewVector(self):
    pass
  def isExactType(self):
    pass
  def isLinear(self):
    pass
  def isOfType(self):
    pass
  def isOrthographic(self):
    pass
  def isPerspective(self):
    pass
  def makeBounds(self):
    pass
  def makeCopy(self):
    pass
  def makeGeometry(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def recomputeAll(self):
    pass
  def ref(self):
    pass
  def setAspectRatio(self):
    pass
  def setChangeEvent(self):
    pass
  def setConvergenceDistance(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setFar(self):
    pass
  def setFilmOffset(self):
    pass
  def setFilmSize(self):
    pass
  def setFocalLength(self):
    pass
  def setFov(self):
    pass
  def setFrustumFromCorners(self):
    pass
  def setInterocularDistance(self):
    pass
  def setKeystone(self):
    pass
  def setMinFov(self):
    pass
  def setNear(self):
    pass
  def setNearFar(self):
    pass
  def setViewHpr(self):
    pass
  def setViewMat(self):
    pass
  def setViewVector(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PiecewiseCurve:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def adjustPoint(self):
    pass
  def adjustPt(self):
    pass
  def adjustTangent(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcLength(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToNurbsCurve(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findLength(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def get2ndtangent(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCurveType(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMaxT(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDimensions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPt(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTangent(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def recompute(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCurveType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNumDimensions(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def stitch(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeEgg(self):
    pass
class PipeOcclusionCullTraverser:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def drawBoundingVolume(self):
    pass
  def endTraverse(self):
    pass
  def flushLevel():
    pass
  def getBuffer(self):
    pass
  def getCameraMask(self):
    pass
  def getCameraTransform(self):
    pass
  def getClassType():
    pass
  def getCurrentThread(self):
    pass
  def getDepthOffsetDecals(self):
    pass
  def getEffectiveIncompleteRender(self):
    pass
  def getGsg(self):
    pass
  def getInitialState(self):
    pass
  def getOcclusionMask(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getTagStateKey(self):
    pass
  def getTexture(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getViewFrustum(self):
    pass
  def getWorldTransform(self):
    pass
  def hasTagStateKey(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def setCameraMask(self):
    pass
  def setOcclusionMask(self):
    pass
  def setScene(self):
    pass
  def setViewFrustum(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def traverse(self):
    pass
  def traverseBelow(self):
    pass
  def unref(self):
    pass
  def upcastToCullTraverser(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class Plane:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def distToPlane(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNormal(self):
    pass
  def getNumComponents(self):
    pass
  def getPoint(self):
    pass
  def getReflectionMat(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def intersectsLine(self):
    pass
  def intersectsPlane(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def write(self):
    pass
  def xform(self):
    pass
  def zero():
    pass
class PlaneD:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def distToPlane(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNormal(self):
    pass
  def getNumComponents(self):
    pass
  def getPoint(self):
    pass
  def getReflectionMat(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def intersectsLine(self):
    pass
  def intersectsPlane(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def write(self):
    pass
  def xform(self):
    pass
  def zero():
    pass
class PlaneNode:
  def __init__(self):
    pass
  CECollision = int

  CEVisible = int

  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getClipEffect(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPlane(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getVizScale(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setClipEffect(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPlane(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setVizScale(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class Point2:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def zero():
    pass
class Point2D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def zero():
    pass
class Point3:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def cross(self):
    pass
  def crossInto(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getStandardizedHpr(self):
    pass
  def getX(self):
    pass
  def getXy(self):
    pass
  def getXz(self):
    pass
  def getY(self):
    pass
  def getYz(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def origin():
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def rfu():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class Point3D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def cross(self):
    pass
  def crossInto(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getStandardizedHpr(self):
    pass
  def getX(self):
    pass
  def getXy(self):
    pass
  def getXz(self):
    pass
  def getY(self):
    pass
  def getYz(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def origin():
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def rfu():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class Point4:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class Point4D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class PointLight:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def activateLens(self):
    pass
  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def asNode(self):
    pass
  def assign(self):
    pass
  def cleanupAuxSceneData(self):
    pass
  def clearAttrib(self):
    pass
  def clearAuxSceneData(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTagState(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copyLens(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def deactivateLens(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttenuation(self):
    pass
  def getAttrib(self):
    pass
  def getAuxSceneData(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCameraMask(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getCullCenter(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInitialState(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLens(self):
    pass
  def getLensActive(self):
    pass
  def getLodCenter(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPoint(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getSpecularColor(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTagState(self):
    pass
  def getTagStateKey(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTagState(self):
    pass
  def hasTags(self):
    pass
  def hideFrustum(self):
    pass
  def isActive(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isInView(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isShadowCaster(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listAuxSceneData(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttenuation(self):
    pass
  def setAttrib(self):
    pass
  def setAuxSceneData(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCameraMask(self):
    pass
  def setColor(self):
    pass
  def setCullCenter(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setInitialState(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLens(self):
    pass
  def setLensActive(self):
    pass
  def setLodCenter(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPoint(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setScene(self):
    pass
  def setShadowCaster(self):
    pass
  def setSpecularColor(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTagState(self):
    pass
  def setTagStateKey(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showFrustum(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToCamera(self):
    pass
  def upcastToLight(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PointerEventList:
  def __init__(self):
    pass
  def addEvent(self):
    pass
  def clear(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encircles(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getDirection(self):
    pass
  def getDx(self):
    pass
  def getDy(self):
    pass
  def getInWindow(self):
    pass
  def getLength(self):
    pass
  def getNumEvents(self):
    pass
  def getRefCount(self):
    pass
  def getRotation(self):
    pass
  def getSequence(self):
    pass
  def getTime(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getXpos(self):
    pass
  def getYpos(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def matchPattern(self):
    pass
  def output(self):
    pass
  def popFront(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def totalTurns(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class PointerToBaseConnection:
  def __init__(self):
    pass
  def clear(self):
    pass
  def getHash(self):
    pass
  def isNull(self):
    pass
  def output(self):
    pass
class PointerToConnection:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def getHash(self):
    pass
  def isNull(self):
    pass
  def output(self):
    pass
  def p(self):
    pass
class PolylightEffect:
  def __init__(self):
    pass
  CTAll = int

  CTProximal = int

  def addLight(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getContrib(self):
    pass
  def getEffectCenter(self):
    pass
  def getNumEffects():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWeight(self):
    pass
  def hasLight(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeLight(self):
    pass
  def setContrib(self):
    pass
  def setEffectCenter(self):
    pass
  def setWeight(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class PolylightNode:
  def __init__(self):
    pass
  ALINEAR = int

  AQUADRATIC = int

  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  FCUSTOM = int

  FRANDOM = int

  FSIN = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def compareTo(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def disable(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def enable(self):
    pass
  def encodeToBamStream(self):
    pass
  def eq(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def flickerOff(self):
    pass
  def flickerOn(self):
    pass
  def getA0(self):
    pass
  def getA1(self):
    pass
  def getA2(self):
    pass
  def getAllCameraMask():
    pass
  def getAttenuation(self):
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getColorScenegraph(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getFlickerType(self):
    pass
  def getFreq(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOffset(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPos(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRadius(self):
    pass
  def getRefCount(self):
    pass
  def getScale(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getStepSize(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isEnabled(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isFlickering(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def lessThan(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setA0(self):
    pass
  def setA1(self):
    pass
  def setA2(self):
    pass
  def setAttenuation(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setColor(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFlickerType(self):
    pass
  def setFreq(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOffset(self):
    pass
  def setOverallHidden(self):
    pass
  def setPos(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setRadius(self):
    pass
  def setScale(self):
    pass
  def setState(self):
    pass
  def setStepSize(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PortalNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def addVertex(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def clearVertices(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCellIn(self):
    pass
  def getCellOut(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getFromPortalMask(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getIntoPortalMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumVertices(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPortalGeom(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isClipPlane(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOpen(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isVisible(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCellIn(self):
    pass
  def setCellOut(self):
    pass
  def setClipPlane(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFromPortalMask(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setIntoPortalMask(self):
    pass
  def setName(self):
    pass
  def setOpen(self):
    pass
  def setOverallHidden(self):
    pass
  def setPortalGeom(self):
    pass
  def setPortalMask(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setVisible(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class PosHprLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def takeLongest(self):
    pass
  def takeShortest(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class PosHprScaleLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def takeLongest(self):
    pass
  def takeShortest(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class PosLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class PreparedGraphicsObjects:
  def __init__(self):
    pass
  def dequeueGeom(self):
    pass
  def dequeueIndexBuffer(self):
    pass
  def dequeueShader(self):
    pass
  def dequeueTexture(self):
    pass
  def dequeueVertexBuffer(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def enqueueGeom(self):
    pass
  def enqueueIndexBuffer(self):
    pass
  def enqueueShader(self):
    pass
  def enqueueTexture(self):
    pass
  def enqueueVertexBuffer(self):
    pass
  def getClassType():
    pass
  def getGraphicsMemoryLimit(self):
    pass
  def getName(self):
    pass
  def getNumPrepared(self):
    pass
  def getNumPreparedGeoms(self):
    pass
  def getNumPreparedIndexBuffers(self):
    pass
  def getNumPreparedShaders(self):
    pass
  def getNumPreparedTextures(self):
    pass
  def getNumPreparedVertexBuffers(self):
    pass
  def getNumQueued(self):
    pass
  def getNumQueuedGeoms(self):
    pass
  def getNumQueuedIndexBuffers(self):
    pass
  def getNumQueuedShaders(self):
    pass
  def getNumQueuedTextures(self):
    pass
  def getNumQueuedVertexBuffers(self):
    pass
  def getRefCount(self):
    pass
  def isGeomPrepared(self):
    pass
  def isGeomQueued(self):
    pass
  def isIndexBufferPrepared(self):
    pass
  def isIndexBufferQueued(self):
    pass
  def isShaderPrepared(self):
    pass
  def isShaderQueued(self):
    pass
  def isTexturePrepared(self):
    pass
  def isTextureQueued(self):
    pass
  def isVertexBufferPrepared(self):
    pass
  def isVertexBufferQueued(self):
    pass
  def prepareGeomNow(self):
    pass
  def prepareIndexBufferNow(self):
    pass
  def prepareShaderNow(self):
    pass
  def prepareTextureNow(self):
    pass
  def prepareVertexBufferNow(self):
    pass
  def ref(self):
    pass
  def releaseAll(self):
    pass
  def releaseAllGeoms(self):
    pass
  def releaseAllIndexBuffers(self):
    pass
  def releaseAllShaders(self):
    pass
  def releaseAllTextures(self):
    pass
  def releaseAllVertexBuffers(self):
    pass
  def releaseGeom(self):
    pass
  def releaseIndexBuffer(self):
    pass
  def releaseShader(self):
    pass
  def releaseTexture(self):
    pass
  def releaseVertexBuffer(self):
    pass
  def setGraphicsMemoryLimit(self):
    pass
  def showGraphicsMemoryLru(self):
    pass
  def showResidencyTrackers(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class PythonCallbackObject:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getFunction(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setFunction(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class PythonTask:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  def Getattr(self):
    pass
  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def Setattr(self):
    pass
  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getArgs(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getFunction(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getOwner(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUponDeath(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setArgs(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setFunction(self):
    pass
  def setName(self):
    pass
  def setOwner(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def setUponDeath(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class PythonThread:
  def __init__(self):
    pass
  def assign(self):
    pass
  def bindThread():
    pass
  def clearName(self):
    pass
  def considerYield():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def forceYield():
    pass
  def getClassType():
    pass
  def getCurrentPipelineStage():
    pass
  def getCurrentThread():
    pass
  def getExternalThread():
    pass
  def getMainThread():
    pass
  def getName(self):
    pass
  def getPipelineStage(self):
    pass
  def getPstatsIndex(self):
    pass
  def getPythonData(self):
    pass
  def getRefCount(self):
    pass
  def getSyncName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUniqueId(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isJoinable(self):
    pass
  def isOfType(self):
    pass
  def isStarted(self):
    pass
  def isThreadingSupported():
    pass
  def isTrueThreads():
    pass
  def join(self):
    pass
  def output(self):
    pass
  def outputBlocker(self):
    pass
  def preempt(self):
    pass
  def prepareForExit():
    pass
  def ref(self):
    pass
  def setMinPipelineStage(self):
    pass
  def setName(self):
    pass
  def setPipelineStage(self):
    pass
  def setPythonData(self):
    pass
  def sleep():
    pass
  def start(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def writeStatus():
    pass
class DoubleBitMaskDoubleBitMaskBitMaskUnsignedInt32:
  def __init__(self):
    pass
  def allOff():
    pass
  def allOn():
    pass
  def assign(self):
    pass
  def bit():
    pass
  def clear(self):
    pass
  def clearBit(self):
    pass
  def clearRange(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def extract(self):
    pass
  def getBit(self):
    pass
  def getClassType():
    pass
  def getHighestOffBit(self):
    pass
  def getHighestOnBit(self):
    pass
  def getLowestOffBit(self):
    pass
  def getLowestOnBit(self):
    pass
  def getMaxNumBits():
    pass
  def getNextHigherDifferentBit(self):
    pass
  def getNumBits():
    pass
  def getNumOffBits(self):
    pass
  def getNumOnBits(self):
    pass
  def hasAllOf(self):
    pass
  def hasAnyOf(self):
    pass
  def hasBitsInCommon(self):
    pass
  def hasMaxNumBits():
    pass
  def invertInPlace(self):
    pass
  def isAllOn(self):
    pass
  def isZero(self):
    pass
  def lessThan(self):
    pass
  def lowerOn():
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def outputBinary(self):
    pass
  def outputHex(self):
    pass
  def range():
    pass
  def setBit(self):
    pass
  def setBitTo(self):
    pass
  def setRange(self):
    pass
  def setRangeTo(self):
    pass
  def store(self):
    pass
  def write(self):
    pass
class Quat:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def almostSameDirection(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def conjugate(self):
    pass
  def conjugateFrom(self):
    pass
  def conjugateInPlace(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def extractToMatrix(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getAngle(self):
    pass
  def getAngleRad(self):
    pass
  def getAxis(self):
    pass
  def getAxisNormalized(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getForward(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getI(self):
    pass
  def getJ(self):
    pass
  def getK(self):
    pass
  def getNumComponents(self):
    pass
  def getR(self):
    pass
  def getRight(self):
    pass
  def getUp(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def identQuat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isAlmostIdentity(self):
    pass
  def isIdentity(self):
    pass
  def isNan(self):
    pass
  def isSameDirection(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pureImaginary():
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setFromAxisAngle(self):
    pass
  def setFromAxisAngleRad(self):
    pass
  def setFromMatrix(self):
    pass
  def setHpr(self):
    pass
  def setI(self):
    pass
  def setJ(self):
    pass
  def setK(self):
    pass
  def setR(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def xform(self):
    pass
  def zero():
    pass
class QuatD:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def almostSameDirection(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def conjugate(self):
    pass
  def conjugateFrom(self):
    pass
  def conjugateInPlace(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def extractToMatrix(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getAngle(self):
    pass
  def getAngleRad(self):
    pass
  def getAxis(self):
    pass
  def getAxisNormalized(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getForward(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getI(self):
    pass
  def getJ(self):
    pass
  def getK(self):
    pass
  def getNumComponents(self):
    pass
  def getR(self):
    pass
  def getRight(self):
    pass
  def getUp(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def identQuat():
    pass
  def invertFrom(self):
    pass
  def invertInPlace(self):
    pass
  def isAlmostIdentity(self):
    pass
  def isIdentity(self):
    pass
  def isNan(self):
    pass
  def isSameDirection(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def multiply(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pureImaginary():
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setFromAxisAngle(self):
    pass
  def setFromAxisAngleRad(self):
    pass
  def setFromMatrix(self):
    pass
  def setHpr(self):
    pass
  def setI(self):
    pass
  def setJ(self):
    pass
  def setK(self):
    pass
  def setR(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def xform(self):
    pass
  def zero():
    pass
class QueuedConnectionListener:
  def __init__(self):
    pass
  def addConnection(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def downcastToQueuedConnectionListener(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getManager(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getNewConnection(self):
    pass
  def getNumThreads(self):
    pass
  def getOverflowFlag(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isConnectionOk(self):
    pass
  def isPolling(self):
    pass
  def newConnectionAvailable(self):
    pass
  def poll(self):
    pass
  def removeConnection(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
  def upcastToConnectionListener(self):
    pass
  def upcastToQueuedReturnConnectionListenerData(self):
    pass
class QueuedConnectionManager:
  def __init__(self):
    pass
  def closeConnection(self):
    pass
  def downcastToQueuedConnectionManager(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getHostName():
    pass
  def getMaxQueueSize(self):
    pass
  def getOverflowFlag(self):
    pass
  def getResetConnection(self):
    pass
  def openTCPClientConnection(self):
    pass
  def openTCPServerRendezvous(self):
    pass
  def openUDPConnection(self):
    pass
  def resetConnectionAvailable(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
  def upcastToConnectionManager(self):
    pass
  def upcastToQueuedReturnPointerToConnection(self):
    pass
class QueuedConnectionReader:
  def __init__(self):
    pass
  def addConnection(self):
    pass
  def dataAvailable(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getData(self):
    pass
  def getManager(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getNumThreads(self):
    pass
  def getOverflowFlag(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isConnectionOk(self):
    pass
  def isPolling(self):
    pass
  def poll(self):
    pass
  def removeConnection(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
  def upcastToConnectionReader(self):
    pass
  def upcastToQueuedReturnNetDatagram(self):
    pass
class QueuedReturnConnectionListenerData:
  def __init__(self):
    pass
  def downcastToQueuedConnectionListener(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getOverflowFlag(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
class QueuedReturnDatagram:
  def __init__(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getOverflowFlag(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
class QueuedReturnNetDatagram:
  def __init__(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getOverflowFlag(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
class QueuedReturnPointerToConnection:
  def __init__(self):
    pass
  def downcastToQueuedConnectionManager(self):
    pass
  def getCurrentQueueSize(self):
    pass
  def getMaxQueueSize(self):
    pass
  def getOverflowFlag(self):
    pass
  def resetOverflowFlag(self):
    pass
  def setMaxQueueSize(self):
    pass
class ReMutex:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def elevateLock(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
  def tryAcquire(self):
    pass
class ReMutexDirect:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def clearName(self):
    pass
  def debugIsLocked(self):
    pass
  def elevateLock(self):
    pass
  def getName(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def setName(self):
    pass
  def tryAcquire(self):
    pass
class RecentConnectionReader:
  def __init__(self):
    pass
  def addConnection(self):
    pass
  def dataAvailable(self):
    pass
  def downcastToDatagramGeneratorNet(self):
    pass
  def downcastToQueuedConnectionReader(self):
    pass
  def getData(self):
    pass
  def getManager(self):
    pass
  def getNumThreads(self):
    pass
  def getRawMode(self):
    pass
  def getTcpHeaderSize(self):
    pass
  def isConnectionOk(self):
    pass
  def isPolling(self):
    pass
  def poll(self):
    pass
  def removeConnection(self):
    pass
  def setRawMode(self):
    pass
  def setTcpHeaderSize(self):
    pass
  def shutdown(self):
    pass
class RecorderBase:
  def __init__(self):
    pass
  def downcastToMouseRecorder(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def isPlaying(self):
    pass
  def isRecording(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
class RecorderController:
  def __init__(self):
    pass
  def addRecorder(self):
    pass
  def beginPlayback(self):
    pass
  def beginRecord(self):
    pass
  def close(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getClockOffset(self):
    pass
  def getFilename(self):
    pass
  def getFrameOffset(self):
    pass
  def getFrameTie(self):
    pass
  def getRandomSeed(self):
    pass
  def getRecorder(self):
    pass
  def getRefCount(self):
    pass
  def getStartTime(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasRecorder(self):
    pass
  def isError(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isOpen(self):
    pass
  def isPlaying(self):
    pass
  def isRecording(self):
    pass
  def playFrame(self):
    pass
  def recordFrame(self):
    pass
  def ref(self):
    pass
  def removeRecorder(self):
    pass
  def setFrameTie(self):
    pass
  def setRandomSeed(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class RenderAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class RenderAttribRegistry:
  def __init__(self):
    pass
  def getGlobalPtr():
    pass
  def getMaxSlots(self):
    pass
  def getNumSlots(self):
    pass
  def getNumSortedSlots(self):
    pass
  def getSlot(self):
    pass
  def getSlotDefault(self):
    pass
  def getSlotSort(self):
    pass
  def getSlotType(self):
    pass
  def getSortedSlot(self):
    pass
  def setSlotSort(self):
    pass
class RenderEffect:
  def __init__(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumEffects():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class RenderEffects:
  def __init__(self):
    pass
  def addEffect(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findEffect(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getEffect(self):
    pass
  def getNumEffects(self):
    pass
  def getNumStates():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lessThan(self):
    pass
  def listStates():
    pass
  def make():
    pass
  def makeEmpty():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeEffect(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateStates():
    pass
  def write(self):
    pass
class RenderModeAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MFilled = int

  MFilledFlat = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPoint = int

  MPointSprite = int

  MUnchanged = int

  MUnused = int

  MWireframe = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getGeomRendering(self):
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getPerspective(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getThickness(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class RenderState:
  def __init__(self):
    pass
  RCache = int

  RNode = int

  def addAttrib(self):
    pass
  def adjustAllPriorities(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearCache():
    pass
  def clearMungerCache():
    pass
  def compareSort(self):
    pass
  def compose(self):
    pass
  def cullCallback(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getAttrib(self):
    pass
  def getAttribDef(self):
    pass
  def getBamModified(self):
    pass
  def getBinIndex(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCompositionCache(self):
    pass
  def getCompositionCacheNumEntries(self):
    pass
  def getCompositionCacheResult(self):
    pass
  def getCompositionCacheSize(self):
    pass
  def getCompositionCacheSource(self):
    pass
  def getDrawOrder(self):
    pass
  def getGeomRendering(self):
    pass
  def getHash(self):
    pass
  def getInvertCompositionCache(self):
    pass
  def getInvertCompositionCacheNumEntries(self):
    pass
  def getInvertCompositionCacheResult(self):
    pass
  def getInvertCompositionCacheSize(self):
    pass
  def getInvertCompositionCacheSource(self):
    pass
  def getMaxPriority():
    pass
  def getNodeRefCount(self):
    pass
  def getNumStates():
    pass
  def getNumUnusedStates():
    pass
  def getOverride(self):
    pass
  def getRefCount(self):
    pass
  def getReferencedBits(self):
    pass
  def getStates():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasAttrib(self):
    pass
  def hasCullCallback(self):
    pass
  def invertCompose(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def lessThan(self):
    pass
  def listCycles():
    pass
  def listStates():
    pass
  def make():
    pass
  def makeEmpty():
    pass
  def makeFullDefault():
    pass
  def markBamModified(self):
    pass
  def nodeRef(self):
    pass
  def nodeUnref(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeAttrib(self):
    pass
  def setAttrib(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateStates():
    pass
  def write(self):
    pass
class RescaleNormalAttrib:
  def __init__(self):
    pass
  MAlways = int

  MAuto = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNormalize = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MRescale = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class RigidBodyCombiner:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def collect(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalScene(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class RopeNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  NMNone = int

  NMVertex = int

  RMBillboard = int

  RMTape = int

  RMThread = int

  RMTube = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  UVDistance = int

  UVDistance2 = int

  UVNone = int

  UVParametric = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearMatrix(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCurve(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMatrix(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNormalMode(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumSlices(self):
    pass
  def getNumStashed(self):
    pass
  def getNumSubdiv(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getRenderMode(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getThickness(self):
    pass
  def getTransform(self):
    pass
  def getTubeUp(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getUseVertexColor(self):
    pass
  def getUseVertexThickness(self):
    pass
  def getUvDirection(self):
    pass
  def getUvMode(self):
    pass
  def getUvScale(self):
    pass
  def getVertexColorDimension():
    pass
  def getVertexThicknessDimension():
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasMatrix(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetBound(self):
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCurve(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMatrix(self):
    pass
  def setName(self):
    pass
  def setNormalMode(self):
    pass
  def setNumSlices(self):
    pass
  def setNumSubdiv(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setRenderMode(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setThickness(self):
    pass
  def setTransform(self):
    pass
  def setTubeUp(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setUseVertexColor(self):
    pass
  def setUseVertexThickness(self):
    pass
  def setUvDirection(self):
    pass
  def setUvMode(self):
    pass
  def setUvScale(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
SUTAdvanced = int

SUTBasic = int

SUTNone = int

SUTUNSPECIFIED = int

class SavedContext:
  def __init__(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class ScaleLerpFunctor:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SceneGraphAnalyzer:
  def __init__(self):
    pass
  LMAll = int

  LMHighest = int

  LMLowest = int

  LMNone = int

  def addNode(self):
    pass
  def clear(self):
    pass
  def getLodMode(self):
    pass
  def getNumColors(self):
    pass
  def getNumGeomNodes(self):
    pass
  def getNumGeomVertexDatas(self):
    pass
  def getNumGeomVertexFormats(self):
    pass
  def getNumGeoms(self):
    pass
  def getNumIndividualTris(self):
    pass
  def getNumInstances(self):
    pass
  def getNumLines(self):
    pass
  def getNumLodNodes(self):
    pass
  def getNumLongNormals(self):
    pass
  def getNumNodes(self):
    pass
  def getNumNodesWithAttribs(self):
    pass
  def getNumNormals(self):
    pass
  def getNumPoints(self):
    pass
  def getNumShortNormals(self):
    pass
  def getNumTexcoords(self):
    pass
  def getNumTransforms(self):
    pass
  def getNumTrianglesInFans(self):
    pass
  def getNumTrianglesInStrips(self):
    pass
  def getNumTrifans(self):
    pass
  def getNumTris(self):
    pass
  def getNumTristrips(self):
    pass
  def getNumVertices(self):
    pass
  def getTextureBytes(self):
    pass
  def getTotalNormalLength(self):
    pass
  def getVertexDataSize(self):
    pass
  def setLodMode(self):
    pass
  def write(self):
    pass
class SceneGraphAnalyzerMeter:
  def __init__(self):
    pass
  ABoxedCenter = int

  ABoxedLeft = int

  ABoxedRight = int

  ACenter = int

  ALeft = int

  ARight = int

  EIso8859 = int

  EUnicode = int

  EUtf8 = int

  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  FFDynamicMerge = int

  FFLight = int

  FFMedium = int

  FFNone = int

  FFStrong = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addProperties(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def appendText(self):
    pass
  def appendUnicodeChar(self):
    pass
  def appendWtext(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcWidth(self):
    pass
  def clear(self):
    pass
  def clearAlign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBin(self):
    pass
  def clearBounds(self):
    pass
  def clearCard(self):
    pass
  def clearCardBorder(self):
    pass
  def clearCardTexture(self):
    pass
  def clearDrawOrder(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFont(self):
    pass
  def clearFrame(self):
    pass
  def clearGlyphScale(self):
    pass
  def clearGlyphShift(self):
    pass
  def clearIndent(self):
    pass
  def clearMaxRows(self):
    pass
  def clearName(self):
    pass
  def clearPreserveTrailingWhitespace(self):
    pass
  def clearPythonTag(self):
    pass
  def clearShadow(self):
    pass
  def clearShadowColor(self):
    pass
  def clearSlant(self):
    pass
  def clearSmallCaps(self):
    pass
  def clearSmallCapsScale(self):
    pass
  def clearState(self):
    pass
  def clearTabWidth(self):
    pass
  def clearTag(self):
    pass
  def clearText(self):
    pass
  def clearTextColor(self):
    pass
  def clearTextScale(self):
    pass
  def clearTransform(self):
    pass
  def clearUnderscore(self):
    pass
  def clearUnderscoreHeight(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def clearWindow(self):
    pass
  def clearWordwrap(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def decodeText(self):
    pass
  def downcastToTextNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def encodeWchar():
    pass
  def encodeWtext(self):
    pass
  def eq(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def forceUpdate(self):
    pass
  def generate(self):
    pass
  def getAlign(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBin(self):
    pass
  def getBottom(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCardActual(self):
    pass
  def getCardAsSet(self):
    pass
  def getCardBorderSize(self):
    pass
  def getCardBorderUvPortion(self):
    pass
  def getCardColor(self):
    pass
  def getCardDecal(self):
    pass
  def getCardTexture(self):
    pass
  def getCardTransformed(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultEncoding():
    pass
  def getDefaultFont():
    pass
  def getDisplayRegion(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawOrder(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEncodedChar(self):
    pass
  def getEncoding(self):
    pass
  def getFancyBits(self):
    pass
  def getFlattenFlags(self):
    pass
  def getFont(self):
    pass
  def getFrameActual(self):
    pass
  def getFrameAsSet(self):
    pass
  def getFrameColor(self):
    pass
  def getFrameCorners(self):
    pass
  def getFrameLineWidth(self):
    pass
  def getGlyphScale(self):
    pass
  def getGlyphShift(self):
    pass
  def getHeight(self):
    pass
  def getIndent(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalGeom(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLeft(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLineHeight(self):
    pass
  def getLowerRight3d(self):
    pass
  def getMaxRows(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNode(self):
    pass
  def getNumChars(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumRows(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPreserveTrailingWhitespace(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getRight(self):
    pass
  def getShadow(self):
    pass
  def getShadowColor(self):
    pass
  def getSlant(self):
    pass
  def getSmallCaps(self):
    pass
  def getSmallCapsScale(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTabWidth(self):
    pass
  def getTag(self):
    pass
  def getText(self):
    pass
  def getTextAsAscii(self):
    pass
  def getTextColor(self):
    pass
  def getTextScale(self):
    pass
  def getTop(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnderscore(self):
    pass
  def getUnderscoreHeight(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getUnicodeChar(self):
    pass
  def getUpdateInterval(self):
    pass
  def getUpperLeft3d(self):
    pass
  def getUsageHint(self):
    pass
  def getWidth(self):
    pass
  def getWindow(self):
    pass
  def getWordwrap(self):
    pass
  def getWordwrappedText(self):
    pass
  def getWordwrappedWtext(self):
    pass
  def getWtext(self):
    pass
  def getWtextAsAscii(self):
    pass
  def hasAlign(self):
    pass
  def hasAttrib(self):
    pass
  def hasBin(self):
    pass
  def hasCard(self):
    pass
  def hasCardBorder(self):
    pass
  def hasCardTexture(self):
    pass
  def hasCharacter(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasDrawOrder(self):
    pass
  def hasEffect(self):
    pass
  def hasExactCharacter(self):
    pass
  def hasFont(self):
    pass
  def hasFrame(self):
    pass
  def hasGlyphScale(self):
    pass
  def hasGlyphShift(self):
    pass
  def hasIndent(self):
    pass
  def hasMaxRows(self):
    pass
  def hasName(self):
    pass
  def hasOverflow(self):
    pass
  def hasPreserveTrailingWhitespace(self):
    pass
  def hasPythonTag(self):
    pass
  def hasShadow(self):
    pass
  def hasShadowColor(self):
    pass
  def hasSlant(self):
    pass
  def hasSmallCaps(self):
    pass
  def hasSmallCapsScale(self):
    pass
  def hasTabWidth(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hasText(self):
    pass
  def hasTextColor(self):
    pass
  def hasTextScale(self):
    pass
  def hasUnderscore(self):
    pass
  def hasUnderscoreHeight(self):
    pass
  def hasWordwrap(self):
    pass
  def isAmbientLight(self):
    pass
  def isAnySpecified(self):
    pass
  def isBoundsStale(self):
    pass
  def isCardAsMargin(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isFrameAsMargin(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isWhitespace(self):
    pass
  def isWtext(self):
    pass
  def listTags(self):
    pass
  def lower():
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def makeLower(self):
    pass
  def makeUpper(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def reencodeText():
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAlign(self):
    pass
  def setAttrib(self):
    pass
  def setBin(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCardActual(self):
    pass
  def setCardAsMargin(self):
    pass
  def setCardBorder(self):
    pass
  def setCardColor(self):
    pass
  def setCardDecal(self):
    pass
  def setCardTexture(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setDefaultEncoding():
    pass
  def setDefaultFont():
    pass
  def setDrawOrder(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setEncoding(self):
    pass
  def setFinal(self):
    pass
  def setFlattenFlags(self):
    pass
  def setFont(self):
    pass
  def setFrameActual(self):
    pass
  def setFrameAsMargin(self):
    pass
  def setFrameColor(self):
    pass
  def setFrameCorners(self):
    pass
  def setFrameLineWidth(self):
    pass
  def setGlyphScale(self):
    pass
  def setGlyphShift(self):
    pass
  def setIndent(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMaxRows(self):
    pass
  def setName(self):
    pass
  def setNode(self):
    pass
  def setOverallHidden(self):
    pass
  def setPreserveTrailingWhitespace(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setShadow(self):
    pass
  def setShadowColor(self):
    pass
  def setSlant(self):
    pass
  def setSmallCaps(self):
    pass
  def setSmallCapsScale(self):
    pass
  def setState(self):
    pass
  def setTabWidth(self):
    pass
  def setTag(self):
    pass
  def setText(self):
    pass
  def setTextColor(self):
    pass
  def setTextScale(self):
    pass
  def setTransform(self):
    pass
  def setUnderscore(self):
    pass
  def setUnderscoreHeight(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setUnicodeChar(self):
    pass
  def setUpdateInterval(self):
    pass
  def setUsageHint(self):
    pass
  def setWordwrap(self):
    pass
  def setWtext(self):
    pass
  def setupWindow(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unicodeIsalpha():
    pass
  def unicodeIsdigit():
    pass
  def unicodeIslower():
    pass
  def unicodeIspunct():
    pass
  def unicodeIsspace():
    pass
  def unicodeIsupper():
    pass
  def unicodeTolower():
    pass
  def unicodeToupper():
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPandaNode(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTextEncoder(self):
    pass
  def upcastToTextProperties(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def update(self):
    pass
  def upper():
    pass
  def write(self):
    pass
class SceneGraphReducer:
  def __init__(self):
    pass
  CSGeomNode = int

  CSOther = int

  CSRecurse = int

  CSWithinRadius = int

  CVDAnimationType = int

  CVDAvoidDynamic = int

  CVDFormat = int

  CVDModel = int

  CVDName = int

  CVDOneNodeOnly = int

  CVDTransform = int

  CVDUsageHint = int

  MNAvoidAnimated = int

  MNAvoidDynamic = int

  MNCompositeOnly = int

  TTApplyTextureColor = int

  TTClipPlane = int

  TTColor = int

  TTColorScale = int

  TTCullFace = int

  TTOther = int

  TTTexMatrix = int

  TTTransform = int

  def applyAttribs(self):
    pass
  def checkLiveFlatten(self):
    pass
  def clearGsg(self):
    pass
  def collectVertexData(self):
    pass
  def decompose(self):
    pass
  def flatten(self):
    pass
  def getCombineRadius(self):
    pass
  def getGsg(self):
    pass
  def makeCompatibleFormat(self):
    pass
  def makeCompatibleState(self):
    pass
  def makeNonindexed(self):
    pass
  def premunge(self):
    pass
  def removeColumn(self):
    pass
  def removeUnusedVertices(self):
    pass
  def setCombineRadius(self):
    pass
  def setGsg(self):
    pass
  def unify(self):
    pass
class SceneSetup:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getCameraNode(self):
    pass
  def getCameraPath(self):
    pass
  def getCameraTransform(self):
    pass
  def getClassType():
    pass
  def getCullCenter(self):
    pass
  def getDisplayRegion(self):
    pass
  def getInitialState(self):
    pass
  def getInverted(self):
    pass
  def getLens(self):
    pass
  def getRefCount(self):
    pass
  def getSceneRoot(self):
    pass
  def getViewportHeight(self):
    pass
  def getViewportWidth(self):
    pass
  def getWorldTransform(self):
    pass
  def ref(self):
    pass
  def setCameraNode(self):
    pass
  def setCameraPath(self):
    pass
  def setCameraTransform(self):
    pass
  def setDisplayRegion(self):
    pass
  def setInitialState(self):
    pass
  def setInverted(self):
    pass
  def setLens(self):
    pass
  def setSceneRoot(self):
    pass
  def setViewportSize(self):
    pass
  def setWorldTransform(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class ScissorAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getFrame(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class ScissorEffect:
  def __init__(self):
    pass
  def addPoint(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getClip(self):
    pass
  def getFrame(self):
    pass
  def getNode(self):
    pass
  def getNodes(self):
    pass
  def getNumEffects():
    pass
  def getNumPoints(self):
    pass
  def getPoint(self):
    pass
  def getPoints(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isScreen(self):
    pass
  def listEffects():
    pass
  def makeNode():
    pass
  def makeScreen():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class SelectiveChildNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToSequenceNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class Semaphore:
  def __init__(self):
    pass
  def acquire(self):
    pass
  def getCount(self):
    pass
  def output(self):
    pass
  def release(self):
    pass
  def tryAcquire(self):
    pass
class SequenceNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToSequenceNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getFrac(self):
    pass
  def getFrame(self):
    pass
  def getFrameRate(self):
    pass
  def getFullFframe(self):
    pass
  def getFullFrame(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNextFrame(self):
    pass
  def getNumChildren(self):
    pass
  def getNumFrames(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPlayRate(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isPlaying(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def loop(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def pingpong(self):
    pass
  def play(self):
    pass
  def pose(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setFrameRate(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPlayRate(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def stop(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToAnimInterface(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToSelectiveChildNode(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class ShadeModelAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MFlat = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MSmooth = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class Shader:
  def __init__(self):
    pass
  SLCg = int

  SLGLSL = int

  SLNone = int

  STFragment = int

  STGeometry = int

  STNone = int

  STVertex = int

  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getErrorFlag(self):
    pass
  def getFilename(self):
    pass
  def getLanguage(self):
    pass
  def getRefCount(self):
    pass
  def getShaderUtilization():
    pass
  def getText(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def haveShaderUtilization():
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isPrepared(self):
    pass
  def load():
    pass
  def make():
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def setShaderUtilization():
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class ShaderAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def autoShader(self):
    pass
  def clearAllShaderInputs(self):
    pass
  def clearFlag(self):
    pass
  def clearShader(self):
    pass
  def clearShaderInput(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getFlag(self):
    pass
  def getInstanceCount(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getShader(self):
    pass
  def getShaderInput(self):
    pass
  def getShaderInputNodepath(self):
    pass
  def getShaderInputTexture(self):
    pass
  def getShaderInputVector(self):
    pass
  def getShaderPriority(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasShader(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def registerWithReadFactory():
    pass
  def setFlag(self):
    pass
  def setInstanceCount(self):
    pass
  def setShader(self):
    pass
  def setShaderAuto(self):
    pass
  def setShaderInput(self):
    pass
  def setShaderOff(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class ShaderContext:
  def __init__(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getShader(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class ShaderGenerator:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def synthesizeShader(self):
    pass
class ShaderInput:
  def __init__(self):
    pass
  MInvalid = int

  MNodepath = int

  MTexture = int

  MVector = int

  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBlank():
    pass
  def getClassType():
    pass
  def getName(self):
    pass
  def getNodepath(self):
    pass
  def getPriority(self):
    pass
  def getRefCount(self):
    pass
  def getTexture(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValueType(self):
    pass
  def getVector(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class ShaderPool:
  def __init__(self):
    pass
  def addShader():
    pass
  def garbageCollect():
    pass
  def hasShader():
    pass
  def listContents():
    pass
  def loadShader():
    pass
  def releaseAllShaders():
    pass
  def releaseShader():
    pass
  def verifyShader():
    pass
  def write():
    pass
class SheetNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getNumUSubdiv(self):
    pass
  def getNumVSubdiv(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getSurface(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getUseVertexColor(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetBound(self):
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNumUSubdiv(self):
    pass
  def setNumVSubdiv(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setSurface(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setUseVertexColor(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class ShowBoundsEffect:
  def __init__(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getNumEffects():
    pass
  def getRefCount(self):
    pass
  def getTight(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class SimpleAllocator:
  def __init__(self):
    pass
  def alloc(self):
    pass
  def downcastToVertexDataPage(self):
    pass
  def getContiguous(self):
    pass
  def getFirstBlock(self):
    pass
  def getMaxSize(self):
    pass
  def getTotalSize(self):
    pass
  def isEmpty(self):
    pass
  def output(self):
    pass
  def setMaxSize(self):
    pass
  def write(self):
    pass
class SimpleAllocatorBlock:
  def __init__(self):
    pass
  def downcastToVertexDataBlock(self):
    pass
  def free(self):
    pass
  def getAllocator(self):
    pass
  def getMaxSize(self):
    pass
  def getNextBlock(self):
    pass
  def getSize(self):
    pass
  def getStart(self):
    pass
  def isFree(self):
    pass
  def output(self):
    pass
  def realloc(self):
    pass
class SimpleLerpFunctorLPoint2f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLPoint3f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLPoint4f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLVecBase2f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLVecBase3f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLVecBase4f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLVector2f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLVector3f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLerpFunctorLVector4f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleLru:
  def __init__(self):
    pass
  def assign(self):
    pass
  def beginEpoch(self):
    pass
  def clearName(self):
    pass
  def considerEvict(self):
    pass
  def countActiveSize(self):
    pass
  def evictTo(self):
    pass
  def getClassType():
    pass
  def getMaxSize(self):
    pass
  def getName(self):
    pass
  def getTotalSize(self):
    pass
  def hasName(self):
    pass
  def output(self):
    pass
  def setMaxSize(self):
    pass
  def setName(self):
    pass
  def upcastToNamable(self):
    pass
  def validate(self):
    pass
  def write(self):
    pass
class SimpleLruPage:
  def __init__(self):
    pass
  def assign(self):
    pass
  def dequeueLru(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToVertexDataPage(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def markUsedLru(self):
    pass
  def output(self):
    pass
  def setLruSize(self):
    pass
  def write(self):
    pass
class SimpleQueryLerpFunctorLPoint2f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLPoint3f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLPoint4f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLVecBase2f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLVecBase3f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLVecBase4f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLVector2f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLVector3f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SimpleQueryLerpFunctorLVector4f:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getEnd(self):
    pass
  def getRefCount(self):
    pass
  def getStart(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getValue(self):
    pass
  def interpolate(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SliderTable:
  def __init__(self):
    pass
  def addSlider(self):
    pass
  def assign(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findSliders(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getModified(self):
    pass
  def getNumSliders(self):
    pass
  def getRefCount(self):
    pass
  def getSlider(self):
    pass
  def getSliderRows(self):
    pass
  def getSliders(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasSlider(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isRegistered(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def registerTable():
    pass
  def removeSlider(self):
    pass
  def setSlider(self):
    pass
  def setSliderRows(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class SocketAddress:
  def __init__(self):
    pass
  def GetIPAddressRaw(self):
    pass
  def clear(self):
    pass
  def eq(self):
    pass
  def getIp(self):
    pass
  def getIpPort(self):
    pass
  def getPort(self):
    pass
  def isMcastRange(self):
    pass
  def lessThan(self):
    pass
  def setAnyIP(self):
    pass
  def setBroadcast(self):
    pass
  def setHost(self):
    pass
  def setPort(self):
    pass
class SocketFdset:
  def __init__(self):
    pass
  def IsSetFor(self):
    pass
  def WaitForError(self):
    pass
  def WaitForRead(self):
    pass
  def WaitForWrite(self):
    pass
  def clear(self):
    pass
  def setForSocket(self):
    pass
class SocketIP:
  def __init__(self):
    pass
  def Active(self):
    pass
  def Close(self):
    pass
  def GetLastError():
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def SetBlocking(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSocket(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class SocketStreamRecorder:
  def __init__(self):
    pass
  def close(self):
    pass
  def considerFlush(self):
    pass
  def downcastToMouseRecorder(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def flush(self):
    pass
  def getClassType():
    pass
  def getCollectTcp(self):
    pass
  def getCollectTcpInterval(self):
    pass
  def getRefCount(self):
    pass
  def isClosed(self):
    pass
  def isPlaying(self):
    pass
  def isRecording(self):
    pass
  def receiveDatagram(self):
    pass
  def ref(self):
    pass
  def sendDatagram(self):
    pass
  def setCollectTcp(self):
    pass
  def setCollectTcpInterval(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
class SocketTCP:
  def __init__(self):
    pass
  def Active(self):
    pass
  def ActiveOpen(self):
    pass
  def ActiveOpenNonBlocking(self):
    pass
  def Close(self):
    pass
  def DontLinger(self):
    pass
  def ErrorIsWouldBlocking(self):
    pass
  def GetLastError():
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def RecvData(self):
    pass
  def SendData(self):
    pass
  def SetBlocking(self):
    pass
  def SetLinger(self):
    pass
  def SetNoDelay(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSendBufferSize(self):
    pass
  def SetSocket(self):
    pass
  def ShutdownSend(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class SocketTCPListen:
  def __init__(self):
    pass
  def Active(self):
    pass
  def Close(self):
    pass
  def GetIncomingConnection(self):
    pass
  def GetLastError():
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def OpenForListen(self):
    pass
  def SetBlocking(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSocket(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class SocketUDP:
  def __init__(self):
    pass
  def Active(self):
    pass
  def Close(self):
    pass
  def GetLastError():
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def InitNoAddress(self):
    pass
  def InitToAddress(self):
    pass
  def OpenForInput(self):
    pass
  def OpenForInputMCast(self):
    pass
  def Send(self):
    pass
  def SendTo(self):
    pass
  def SetBlocking(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSocket(self):
    pass
  def SetToBroadCast(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class SocketUDPIncoming:
  def __init__(self):
    pass
  def Active(self):
    pass
  def Close(self):
    pass
  def GetLastError():
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def InitNoAddress(self):
    pass
  def OpenForInput(self):
    pass
  def OpenForInputMCast(self):
    pass
  def SendTo(self):
    pass
  def SetBlocking(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSocket(self):
    pass
  def SetToBroadCast(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class SocketUDPOutgoing:
  def __init__(self):
    pass
  def Active(self):
    pass
  def Close(self):
    pass
  def GetLastError():
    pass
  def GetPeerName(self):
    pass
  def GetSocket(self):
    pass
  def InitNetworkDriver():
    pass
  def InitNoAddress(self):
    pass
  def InitToAddress(self):
    pass
  def Send(self):
    pass
  def SendTo(self):
    pass
  def SetBlocking(self):
    pass
  def SetNonBlocking(self):
    pass
  def SetRecvBufferSize(self):
    pass
  def SetReuseAddress(self):
    pass
  def SetSocket(self):
    pass
  def SetToBroadCast(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
class SparseArray:
  def __init__(self):
    pass
  def allOff():
    pass
  def allOn():
    pass
  def assign(self):
    pass
  def bit():
    pass
  def clear(self):
    pass
  def clearBit(self):
    pass
  def clearRange(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def getBit(self):
    pass
  def getClassType():
    pass
  def getHighestBits(self):
    pass
  def getHighestOffBit(self):
    pass
  def getHighestOnBit(self):
    pass
  def getLowestOffBit(self):
    pass
  def getLowestOnBit(self):
    pass
  def getMaxNumBits():
    pass
  def getNextHigherDifferentBit(self):
    pass
  def getNumBits(self):
    pass
  def getNumOffBits(self):
    pass
  def getNumOnBits(self):
    pass
  def getNumSubranges(self):
    pass
  def getSubrangeBegin(self):
    pass
  def getSubrangeEnd(self):
    pass
  def hasAllOf(self):
    pass
  def hasAnyOf(self):
    pass
  def hasBitsInCommon(self):
    pass
  def hasMaxNumBits():
    pass
  def invertInPlace(self):
    pass
  def isAllOn(self):
    pass
  def isInverse(self):
    pass
  def isZero(self):
    pass
  def lessThan(self):
    pass
  def lowerOn():
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def range():
    pass
  def setBit(self):
    pass
  def setBitTo(self):
    pass
  def setRange(self):
    pass
  def setRangeTo(self):
    pass
class Spotlight:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def activateLens(self):
    pass
  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def asNode(self):
    pass
  def assign(self):
    pass
  def cleanupAuxSceneData(self):
    pass
  def clearAttrib(self):
    pass
  def clearAuxSceneData(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTagState(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copyLens(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def deactivateLens(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttenuation(self):
    pass
  def getAttrib(self):
    pass
  def getAuxSceneData(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCameraMask(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassPriority(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getCullCenter(self):
    pass
  def getDisplayRegion(self):
    pass
  def getDisplayRegions(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getExponent(self):
    pass
  def getFancyBits(self):
    pass
  def getInitialState(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLens(self):
    pass
  def getLensActive(self):
    pass
  def getLodCenter(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumDisplayRegions(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPriority(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getScene(self):
    pass
  def getSpecularColor(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTagState(self):
    pass
  def getTagStateKey(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTagState(self):
    pass
  def hasTags(self):
    pass
  def hideFrustum(self):
    pass
  def isActive(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isInView(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isShadowCaster(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listAuxSceneData(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def makeSpot():
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setActive(self):
    pass
  def setAttenuation(self):
    pass
  def setAttrib(self):
    pass
  def setAuxSceneData(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCameraMask(self):
    pass
  def setColor(self):
    pass
  def setCullCenter(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setExponent(self):
    pass
  def setFinal(self):
    pass
  def setInitialState(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setLens(self):
    pass
  def setLensActive(self):
    pass
  def setLodCenter(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPriority(self):
    pass
  def setPythonTag(self):
    pass
  def setScene(self):
    pass
  def setShadowCaster(self):
    pass
  def setSpecularColor(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTagState(self):
    pass
  def setTagStateKey(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def showFrustum(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToCamera(self):
    pass
  def upcastToLight(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class StackedPerlinNoise2:
  def __init__(self):
    pass
  def addLevel(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def noise(self):
    pass
class StackedPerlinNoise3:
  def __init__(self):
    pass
  def addLevel(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def noise(self):
    pass
class StaticTextFont:
  def __init__(self):
    pass
  RMExtruded = int

  RMInvalid = int

  RMPolygon = int

  RMSolid = int

  RMTexture = int

  RMWireframe = int

  WODefault = int

  WOInvalid = int

  WOLeft = int

  WORight = int

  def assign(self):
    pass
  def clearName(self):
    pass
  def downcastToDynamicTextFont(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getLineHeight(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSpaceAdvance(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setLineHeight(self):
    pass
  def setName(self):
    pass
  def setSpaceAdvance(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def write(self):
    pass
class StencilAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  SCFAlways = int

  SCFEqual = int

  SCFGreaterThan = int

  SCFGreaterThanOrEqual = int

  SCFLessThan = int

  SCFLessThanOrEqual = int

  SCFNever = int

  SCFNotEqual = int

  SMDefault = int

  SODecrement = int

  SODecrementSaturate = int

  SOIncrement = int

  SOIncrementSaturate = int

  SOInvert = int

  SOKeep = int

  SOReplace = int

  SOZero = int

  SRSBackComparisonFunction = int

  SRSBackEnable = int

  SRSBackStencilFailOperation = int

  SRSBackStencilPassZFailOperation = int

  SRSBackStencilPassZPassOperation = int

  SRSClear = int

  SRSClearValue = int

  SRSFirst = int

  SRSFrontComparisonFunction = int

  SRSFrontEnable = int

  SRSFrontStencilFailOperation = int

  SRSFrontStencilPassZFailOperation = int

  SRSFrontStencilPassZPassOperation = int

  SRSReadMask = int

  SRSReference = int

  SRSTotal = int

  SRSWriteMask = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getRenderState(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def make2Sided():
    pass
  def make2SidedWithClear():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def makeWithClear():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class StencilRenderStates:
  def __init__(self):
    pass
  SCFAlways = int

  SCFEqual = int

  SCFGreaterThan = int

  SCFGreaterThanOrEqual = int

  SCFLessThan = int

  SCFLessThanOrEqual = int

  SCFNever = int

  SCFNotEqual = int

  SODecrement = int

  SODecrementSaturate = int

  SOIncrement = int

  SOIncrementSaturate = int

  SOInvert = int

  SOKeep = int

  SOReplace = int

  SOZero = int

  SRSBackComparisonFunction = int

  SRSBackEnable = int

  SRSBackStencilFailOperation = int

  SRSBackStencilPassZFailOperation = int

  SRSBackStencilPassZPassOperation = int

  SRSClear = int

  SRSClearValue = int

  SRSFirst = int

  SRSFrontComparisonFunction = int

  SRSFrontEnable = int

  SRSFrontStencilFailOperation = int

  SRSFrontStencilPassZFailOperation = int

  SRSFrontStencilPassZPassOperation = int

  SRSReadMask = int

  SRSReference = int

  SRSTotal = int

  SRSWriteMask = int

class StereoDisplayRegion:
  def __init__(self):
    pass
  RTPAuxFloat0 = int

  RTPAuxFloat1 = int

  RTPAuxFloat2 = int

  RTPAuxFloat3 = int

  RTPAuxHrgba0 = int

  RTPAuxHrgba1 = int

  RTPAuxHrgba2 = int

  RTPAuxHrgba3 = int

  RTPAuxRgba0 = int

  RTPAuxRgba1 = int

  RTPAuxRgba2 = int

  RTPAuxRgba3 = int

  RTPCOUNT = int

  RTPColor = int

  RTPDepth = int

  RTPDepthStencil = int

  RTPStencil = int

  def clearCullCallback(self):
    pass
  def clearDrawCallback(self):
    pass
  def disableClears(self):
    pass
  def downcastToDisplayRegion(self):
    pass
  def downcastToGraphicsOutput(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getBottom(self):
    pass
  def getCamera(self):
    pass
  def getClassType():
    pass
  def getClearActive(self):
    pass
  def getClearColor(self):
    pass
  def getClearColorActive(self):
    pass
  def getClearDepth(self):
    pass
  def getClearDepthActive(self):
    pass
  def getClearStencil(self):
    pass
  def getClearStencilActive(self):
    pass
  def getClearValue(self):
    pass
  def getCubeMapIndex(self):
    pass
  def getCullCallback(self):
    pass
  def getCullTraverser(self):
    pass
  def getDrawCallback(self):
    pass
  def getIncompleteRender(self):
    pass
  def getLeft(self):
    pass
  def getLeftEye(self):
    pass
  def getLensIndex(self):
    pass
  def getPipe(self):
    pass
  def getPixelFactor(self):
    pass
  def getPixelHeight(self):
    pass
  def getPixelWidth(self):
    pass
  def getPixelZoom(self):
    pass
  def getRefCount(self):
    pass
  def getRenderbufferType():
    pass
  def getRight(self):
    pass
  def getRightEye(self):
    pass
  def getScreenshot(self):
    pass
  def getSort(self):
    pass
  def getStereoChannel(self):
    pass
  def getTextureReloadPriority(self):
    pass
  def getTop(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWindow(self):
    pass
  def isActive(self):
    pass
  def isAnyClearActive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isStereo(self):
    pass
  def makeCullResultGraph(self):
    pass
  def makeScreenshotFilename():
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def saveScreenshot(self):
    pass
  def saveScreenshotDefault(self):
    pass
  def setActive(self):
    pass
  def setCamera(self):
    pass
  def setClearActive(self):
    pass
  def setClearColor(self):
    pass
  def setClearColorActive(self):
    pass
  def setClearDepth(self):
    pass
  def setClearDepthActive(self):
    pass
  def setClearStencil(self):
    pass
  def setClearStencilActive(self):
    pass
  def setClearValue(self):
    pass
  def setCubeMapIndex(self):
    pass
  def setCullCallback(self):
    pass
  def setCullTraverser(self):
    pass
  def setDimensions(self):
    pass
  def setDrawCallback(self):
    pass
  def setIncompleteRender(self):
    pass
  def setLensIndex(self):
    pass
  def setPixelZoom(self):
    pass
  def setSort(self):
    pass
  def setStereoChannel(self):
    pass
  def setTextureReloadPriority(self):
    pass
  def supportsPixelZoom(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToDisplayRegionBase(self):
    pass
  def upcastToDrawableRegion(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class SwitchNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToSequenceNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getVisibleChild(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setVisibleChild(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
TPHigh = int

TPLow = int

TPNormal = int

TPUrgent = int

class TexGenAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def addStage(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getConstantValue(self):
    pass
  def getGeomRendering(self):
    pass
  def getLight(self):
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getSourceName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasGenTexcoordStage(self):
    pass
  def hasStage(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeStage(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class TexMatrixAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def addStage(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getGeomRendering(self):
    pass
  def getMat(self):
    pass
  def getNumAttribs():
    pass
  def getNumStages(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getStage(self):
    pass
  def getStages(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasStage(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeStage(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class TexProjectorEffect:
  def __init__(self):
    pass
  def addStage(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFrom(self):
    pass
  def getNumEffects():
    pass
  def getRefCount(self):
    pass
  def getTo(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasStage(self):
    pass
  def isEmpty(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listEffects():
    pass
  def make():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeStage(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateEffects():
    pass
  def write(self):
    pass
class TextAssembler:
  def __init__(self):
    pass
  def assembleText(self):
    pass
  def assign(self):
    pass
  def calcC(self):
    pass
  def calcIndex(self):
    pass
  def calcR(self):
    pass
  def calcWidth():
    pass
  def clear(self):
    pass
  def getCharacter(self):
    pass
  def getDynamicMerge(self):
    pass
  def getGraphic(self):
    pass
  def getLr(self):
    pass
  def getMaxRows(self):
    pass
  def getMultilineMode(self):
    pass
  def getNumCharacters(self):
    pass
  def getNumCols(self):
    pass
  def getNumRows(self):
    pass
  def getPlainWtext(self):
    pass
  def getProperties(self):
    pass
  def getUl(self):
    pass
  def getUsageHint(self):
    pass
  def getWidth(self):
    pass
  def getWordwrappedPlainWtext(self):
    pass
  def getWordwrappedWtext(self):
    pass
  def getWtext(self):
    pass
  def getXpos(self):
    pass
  def getYpos(self):
    pass
  def hasCharacter():
    pass
  def hasExactCharacter():
    pass
  def isWhitespace():
    pass
  def setDynamicMerge(self):
    pass
  def setMaxRows(self):
    pass
  def setMultilineMode(self):
    pass
  def setProperties(self):
    pass
  def setUsageHint(self):
    pass
  def setWsubstr(self):
    pass
  def setWtext(self):
    pass
class TextFont:
  def __init__(self):
    pass
  RMExtruded = int

  RMInvalid = int

  RMPolygon = int

  RMSolid = int

  RMTexture = int

  RMWireframe = int

  WODefault = int

  WOInvalid = int

  WOLeft = int

  WORight = int

  def assign(self):
    pass
  def clearName(self):
    pass
  def downcastToDynamicTextFont(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getLineHeight(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSpaceAdvance(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setLineHeight(self):
    pass
  def setName(self):
    pass
  def setSpaceAdvance(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def write(self):
    pass
class TextGraphic:
  def __init__(self):
    pass
  def getFrame(self):
    pass
  def getInstanceFlag(self):
    pass
  def getModel(self):
    pass
  def setFrame(self):
    pass
  def setInstanceFlag(self):
    pass
  def setModel(self):
    pass
class TextNode:
  def __init__(self):
    pass
  ABoxedCenter = int

  ABoxedLeft = int

  ABoxedRight = int

  ACenter = int

  ALeft = int

  ARight = int

  EIso8859 = int

  EUnicode = int

  EUtf8 = int

  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  FFDynamicMerge = int

  FFLight = int

  FFMedium = int

  FFNone = int

  FFStrong = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addProperties(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def appendText(self):
    pass
  def appendUnicodeChar(self):
    pass
  def appendWtext(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def calcWidth(self):
    pass
  def clear(self):
    pass
  def clearAlign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBin(self):
    pass
  def clearBounds(self):
    pass
  def clearCard(self):
    pass
  def clearCardBorder(self):
    pass
  def clearCardTexture(self):
    pass
  def clearDrawOrder(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearFont(self):
    pass
  def clearFrame(self):
    pass
  def clearGlyphScale(self):
    pass
  def clearGlyphShift(self):
    pass
  def clearIndent(self):
    pass
  def clearMaxRows(self):
    pass
  def clearName(self):
    pass
  def clearPreserveTrailingWhitespace(self):
    pass
  def clearPythonTag(self):
    pass
  def clearShadow(self):
    pass
  def clearShadowColor(self):
    pass
  def clearSlant(self):
    pass
  def clearSmallCaps(self):
    pass
  def clearSmallCapsScale(self):
    pass
  def clearState(self):
    pass
  def clearTabWidth(self):
    pass
  def clearTag(self):
    pass
  def clearText(self):
    pass
  def clearTextColor(self):
    pass
  def clearTextScale(self):
    pass
  def clearTransform(self):
    pass
  def clearUnderscore(self):
    pass
  def clearUnderscoreHeight(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def clearWordwrap(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def decodeText(self):
    pass
  def downcastToTextNode(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def encodeWchar():
    pass
  def encodeWtext(self):
    pass
  def eq(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def forceUpdate(self):
    pass
  def generate(self):
    pass
  def getAlign(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBin(self):
    pass
  def getBottom(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getCardActual(self):
    pass
  def getCardAsSet(self):
    pass
  def getCardBorderSize(self):
    pass
  def getCardBorderUvPortion(self):
    pass
  def getCardColor(self):
    pass
  def getCardDecal(self):
    pass
  def getCardTexture(self):
    pass
  def getCardTransformed(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCoordinateSystem(self):
    pass
  def getDefaultEncoding():
    pass
  def getDefaultFont():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawOrder(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getEncodedChar(self):
    pass
  def getEncoding(self):
    pass
  def getFancyBits(self):
    pass
  def getFlattenFlags(self):
    pass
  def getFont(self):
    pass
  def getFrameActual(self):
    pass
  def getFrameAsSet(self):
    pass
  def getFrameColor(self):
    pass
  def getFrameCorners(self):
    pass
  def getFrameLineWidth(self):
    pass
  def getGlyphScale(self):
    pass
  def getGlyphShift(self):
    pass
  def getHeight(self):
    pass
  def getIndent(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalGeom(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLeft(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getLineHeight(self):
    pass
  def getLowerRight3d(self):
    pass
  def getMaxRows(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChars(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumRows(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPreserveTrailingWhitespace(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getRight(self):
    pass
  def getShadow(self):
    pass
  def getShadowColor(self):
    pass
  def getSlant(self):
    pass
  def getSmallCaps(self):
    pass
  def getSmallCapsScale(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTabWidth(self):
    pass
  def getTag(self):
    pass
  def getText(self):
    pass
  def getTextAsAscii(self):
    pass
  def getTextColor(self):
    pass
  def getTextScale(self):
    pass
  def getTop(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnderscore(self):
    pass
  def getUnderscoreHeight(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getUnicodeChar(self):
    pass
  def getUpperLeft3d(self):
    pass
  def getUsageHint(self):
    pass
  def getWidth(self):
    pass
  def getWordwrap(self):
    pass
  def getWordwrappedText(self):
    pass
  def getWordwrappedWtext(self):
    pass
  def getWtext(self):
    pass
  def getWtextAsAscii(self):
    pass
  def hasAlign(self):
    pass
  def hasAttrib(self):
    pass
  def hasBin(self):
    pass
  def hasCard(self):
    pass
  def hasCardBorder(self):
    pass
  def hasCardTexture(self):
    pass
  def hasCharacter(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasDrawOrder(self):
    pass
  def hasEffect(self):
    pass
  def hasExactCharacter(self):
    pass
  def hasFont(self):
    pass
  def hasFrame(self):
    pass
  def hasGlyphScale(self):
    pass
  def hasGlyphShift(self):
    pass
  def hasIndent(self):
    pass
  def hasMaxRows(self):
    pass
  def hasName(self):
    pass
  def hasOverflow(self):
    pass
  def hasPreserveTrailingWhitespace(self):
    pass
  def hasPythonTag(self):
    pass
  def hasShadow(self):
    pass
  def hasShadowColor(self):
    pass
  def hasSlant(self):
    pass
  def hasSmallCaps(self):
    pass
  def hasSmallCapsScale(self):
    pass
  def hasTabWidth(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hasText(self):
    pass
  def hasTextColor(self):
    pass
  def hasTextScale(self):
    pass
  def hasUnderscore(self):
    pass
  def hasUnderscoreHeight(self):
    pass
  def hasWordwrap(self):
    pass
  def isAmbientLight(self):
    pass
  def isAnySpecified(self):
    pass
  def isBoundsStale(self):
    pass
  def isCardAsMargin(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isFrameAsMargin(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isWhitespace(self):
    pass
  def isWtext(self):
    pass
  def listTags(self):
    pass
  def lower():
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def makeLower(self):
    pass
  def makeUpper(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def reencodeText():
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAlign(self):
    pass
  def setAttrib(self):
    pass
  def setBin(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCardActual(self):
    pass
  def setCardAsMargin(self):
    pass
  def setCardBorder(self):
    pass
  def setCardColor(self):
    pass
  def setCardDecal(self):
    pass
  def setCardTexture(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setDefaultEncoding():
    pass
  def setDefaultFont():
    pass
  def setDrawOrder(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setEncoding(self):
    pass
  def setFinal(self):
    pass
  def setFlattenFlags(self):
    pass
  def setFont(self):
    pass
  def setFrameActual(self):
    pass
  def setFrameAsMargin(self):
    pass
  def setFrameColor(self):
    pass
  def setFrameCorners(self):
    pass
  def setFrameLineWidth(self):
    pass
  def setGlyphScale(self):
    pass
  def setGlyphShift(self):
    pass
  def setIndent(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMaxRows(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPreserveTrailingWhitespace(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setShadow(self):
    pass
  def setShadowColor(self):
    pass
  def setSlant(self):
    pass
  def setSmallCaps(self):
    pass
  def setSmallCapsScale(self):
    pass
  def setState(self):
    pass
  def setTabWidth(self):
    pass
  def setTag(self):
    pass
  def setText(self):
    pass
  def setTextColor(self):
    pass
  def setTextScale(self):
    pass
  def setTransform(self):
    pass
  def setUnderscore(self):
    pass
  def setUnderscoreHeight(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setUnicodeChar(self):
    pass
  def setUsageHint(self):
    pass
  def setWordwrap(self):
    pass
  def setWtext(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unicodeIsalpha():
    pass
  def unicodeIsdigit():
    pass
  def unicodeIslower():
    pass
  def unicodeIspunct():
    pass
  def unicodeIsspace():
    pass
  def unicodeIsupper():
    pass
  def unicodeTolower():
    pass
  def unicodeToupper():
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToPandaNode(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTextEncoder(self):
    pass
  def upcastToTextProperties(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def update(self):
    pass
  def upper():
    pass
  def write(self):
    pass
class TextProperties:
  def __init__(self):
    pass
  ABoxedCenter = int

  ABoxedLeft = int

  ABoxedRight = int

  ACenter = int

  ALeft = int

  ARight = int

  def addProperties(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def clearAlign(self):
    pass
  def clearBin(self):
    pass
  def clearDrawOrder(self):
    pass
  def clearFont(self):
    pass
  def clearGlyphScale(self):
    pass
  def clearGlyphShift(self):
    pass
  def clearIndent(self):
    pass
  def clearPreserveTrailingWhitespace(self):
    pass
  def clearShadow(self):
    pass
  def clearShadowColor(self):
    pass
  def clearSlant(self):
    pass
  def clearSmallCaps(self):
    pass
  def clearSmallCapsScale(self):
    pass
  def clearTabWidth(self):
    pass
  def clearTextColor(self):
    pass
  def clearTextScale(self):
    pass
  def clearUnderscore(self):
    pass
  def clearUnderscoreHeight(self):
    pass
  def clearWordwrap(self):
    pass
  def downcastToTextNode(self):
    pass
  def eq(self):
    pass
  def getAlign(self):
    pass
  def getBin(self):
    pass
  def getClassType():
    pass
  def getDefaultFont():
    pass
  def getDrawOrder(self):
    pass
  def getFont(self):
    pass
  def getGlyphScale(self):
    pass
  def getGlyphShift(self):
    pass
  def getIndent(self):
    pass
  def getPreserveTrailingWhitespace(self):
    pass
  def getShadow(self):
    pass
  def getShadowColor(self):
    pass
  def getSlant(self):
    pass
  def getSmallCaps(self):
    pass
  def getSmallCapsScale(self):
    pass
  def getTabWidth(self):
    pass
  def getTextColor(self):
    pass
  def getTextScale(self):
    pass
  def getUnderscore(self):
    pass
  def getUnderscoreHeight(self):
    pass
  def getWordwrap(self):
    pass
  def hasAlign(self):
    pass
  def hasBin(self):
    pass
  def hasDrawOrder(self):
    pass
  def hasFont(self):
    pass
  def hasGlyphScale(self):
    pass
  def hasGlyphShift(self):
    pass
  def hasIndent(self):
    pass
  def hasPreserveTrailingWhitespace(self):
    pass
  def hasShadow(self):
    pass
  def hasShadowColor(self):
    pass
  def hasSlant(self):
    pass
  def hasSmallCaps(self):
    pass
  def hasSmallCapsScale(self):
    pass
  def hasTabWidth(self):
    pass
  def hasTextColor(self):
    pass
  def hasTextScale(self):
    pass
  def hasUnderscore(self):
    pass
  def hasUnderscoreHeight(self):
    pass
  def hasWordwrap(self):
    pass
  def isAnySpecified(self):
    pass
  def ne(self):
    pass
  def setAlign(self):
    pass
  def setBin(self):
    pass
  def setDefaultFont():
    pass
  def setDrawOrder(self):
    pass
  def setFont(self):
    pass
  def setGlyphScale(self):
    pass
  def setGlyphShift(self):
    pass
  def setIndent(self):
    pass
  def setPreserveTrailingWhitespace(self):
    pass
  def setShadow(self):
    pass
  def setShadowColor(self):
    pass
  def setSlant(self):
    pass
  def setSmallCaps(self):
    pass
  def setSmallCapsScale(self):
    pass
  def setTabWidth(self):
    pass
  def setTextColor(self):
    pass
  def setTextScale(self):
    pass
  def setUnderscore(self):
    pass
  def setUnderscoreHeight(self):
    pass
  def setWordwrap(self):
    pass
  def write(self):
    pass
class TextPropertiesManager:
  def __init__(self):
    pass
  def clearGraphic(self):
    pass
  def clearProperties(self):
    pass
  def getGlobalPtr():
    pass
  def getGraphic(self):
    pass
  def getProperties(self):
    pass
  def hasGraphic(self):
    pass
  def hasProperties(self):
    pass
  def setGraphic(self):
    pass
  def setProperties(self):
    pass
  def write(self):
    pass
class Texture:
  def __init__(self):
    pass
  CMDefault = int

  CMDxt1 = int

  CMDxt2 = int

  CMDxt3 = int

  CMDxt4 = int

  CMDxt5 = int

  CMFxt1 = int

  CMOff = int

  CMOn = int

  FAlpha = int

  FBlue = int

  FColorIndex = int

  FDepthComponent = int

  FDepthComponent16 = int

  FDepthComponent24 = int

  FDepthComponent32 = int

  FDepthStencil = int

  FGreen = int

  FLuminance = int

  FLuminanceAlpha = int

  FLuminanceAlphamask = int

  FRed = int

  FRgb = int

  FRgb12 = int

  FRgb332 = int

  FRgb5 = int

  FRgb8 = int

  FRgba = int

  FRgba12 = int

  FRgba16 = int

  FRgba32 = int

  FRgba4 = int

  FRgba5 = int

  FRgba8 = int

  FRgbm = int

  FTDefault = int

  FTInvalid = int

  FTLinear = int

  FTLinearMipmapLinear = int

  FTLinearMipmapNearest = int

  FTNearest = int

  FTNearestMipmapLinear = int

  FTNearestMipmapNearest = int

  FTShadow = int

  QLBest = int

  QLDefault = int

  QLFastest = int

  QLNormal = int

  TFloat = int

  TT1dTexture = int

  TT2dTexture = int

  TT3dTexture = int

  TTCubeMap = int

  TUnsignedByte = int

  TUnsignedInt248 = int

  TUnsignedShort = int

  WMBorderColor = int

  WMClamp = int

  WMInvalid = int

  WMMirror = int

  WMMirrorOnce = int

  WMRepeat = int

  def assign(self):
    pass
  def clear(self):
    pass
  def clearAlphaFilename(self):
    pass
  def clearAlphaFullpath(self):
    pass
  def clearAuxData(self):
    pass
  def clearFilename(self):
    pass
  def clearFullpath(self):
    pass
  def clearName(self):
    pass
  def clearRamImage(self):
    pass
  def clearRamMipmapImage(self):
    pass
  def clearRamMipmapImages(self):
    pass
  def clearSimpleRamImage(self):
    pass
  def compressRamImage(self):
    pass
  def considerRescale(self):
    pass
  def decodeFromBamStream():
    pass
  def downToPower2():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def downcastToVideoTexture(self):
    pass
  def encodeToBamStream(self):
    pass
  def estimateTextureMemory(self):
    pass
  def generateAlphaScaleMap(self):
    pass
  def generateNormalizationCubeMap(self):
    pass
  def generateRamMipmapImages(self):
    pass
  def generateSimpleRamImage(self):
    pass
  def getActive(self):
    pass
  def getAlphaFilename(self):
    pass
  def getAlphaFullpath(self):
    pass
  def getAnisotropicDegree(self):
    pass
  def getAuxData(self):
    pass
  def getBamModified(self):
    pass
  def getBorderColor(self):
    pass
  def getClassType():
    pass
  def getComponentType(self):
    pass
  def getComponentWidth(self):
    pass
  def getCompression(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getEffectiveAnisotropicDegree(self):
    pass
  def getEffectiveMagfilter(self):
    pass
  def getEffectiveMinfilter(self):
    pass
  def getEffectiveQualityLevel(self):
    pass
  def getExpectedMipmapXSize(self):
    pass
  def getExpectedMipmapYSize(self):
    pass
  def getExpectedMipmapZSize(self):
    pass
  def getExpectedNumMipmapLevels(self):
    pass
  def getExpectedRamImageSize(self):
    pass
  def getExpectedRamMipmapImageSize(self):
    pass
  def getExpectedRamMipmapPageSize(self):
    pass
  def getExpectedRamPageSize(self):
    pass
  def getFilename(self):
    pass
  def getFormat(self):
    pass
  def getFullpath(self):
    pass
  def getImageModified(self):
    pass
  def getKeepRamImage(self):
    pass
  def getLoadedFromImage(self):
    pass
  def getLoadedFromTxo(self):
    pass
  def getMagfilter(self):
    pass
  def getMatchFramebufferFormat(self):
    pass
  def getMinfilter(self):
    pass
  def getName(self):
    pass
  def getNumComponents(self):
    pass
  def getNumLoadableRamMipmapImages(self):
    pass
  def getNumRamMipmapImages(self):
    pass
  def getOrigFileXSize(self):
    pass
  def getOrigFileYSize(self):
    pass
  def getOrigFileZSize(self):
    pass
  def getPadXSize(self):
    pass
  def getPadYSize(self):
    pass
  def getPadZSize(self):
    pass
  def getPostLoadStoreCache(self):
    pass
  def getPropertiesModified(self):
    pass
  def getQualityLevel(self):
    pass
  def getRamImage(self):
    pass
  def getRamImageAs(self):
    pass
  def getRamImageCompression(self):
    pass
  def getRamImageSize(self):
    pass
  def getRamMipmapImage(self):
    pass
  def getRamMipmapImageSize(self):
    pass
  def getRamMipmapPageSize(self):
    pass
  def getRamPageSize(self):
    pass
  def getRefCount(self):
    pass
  def getRenderToTexture(self):
    pass
  def getResident(self):
    pass
  def getSimpleImageModified(self):
    pass
  def getSimpleRamImage(self):
    pass
  def getSimpleRamImageSize(self):
    pass
  def getSimpleXSize(self):
    pass
  def getSimpleYSize(self):
    pass
  def getTextureType(self):
    pass
  def getTexturesPower2():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUncompressedRamImage(self):
    pass
  def getWrapU(self):
    pass
  def getWrapV(self):
    pass
  def getWrapW(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def getZSize(self):
    pass
  def hasAllRamMipmapImages(self):
    pass
  def hasAlphaFilename(self):
    pass
  def hasAlphaFullpath(self):
    pass
  def hasCompression(self):
    pass
  def hasFilename(self):
    pass
  def hasFullpath(self):
    pass
  def hasName(self):
    pass
  def hasRamImage(self):
    pass
  def hasRamMipmapImage(self):
    pass
  def hasSimpleRamImage(self):
    pass
  def hasUncompressedRamImage(self):
    pass
  def haveTexturesPower2():
    pass
  def isExactType(self):
    pass
  def isMipmap():
    pass
  def isOfType(self):
    pass
  def isPrepared(self):
    pass
  def load(self):
    pass
  def loadRelated(self):
    pass
  def makeCopy(self):
    pass
  def makeRamImage(self):
    pass
  def makeRamMipmapImage(self):
    pass
  def markBamModified(self):
    pass
  def mightHaveRamImage(self):
    pass
  def modifyRamImage(self):
    pass
  def modifyRamMipmapImage(self):
    pass
  def modifySimpleRamImage(self):
    pass
  def newSimpleRamImage(self):
    pass
  def output(self):
    pass
  def peek(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def read(self):
    pass
  def readDds(self):
    pass
  def readTxo(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def reload(self):
    pass
  def setAlphaFilename(self):
    pass
  def setAlphaFullpath(self):
    pass
  def setAnisotropicDegree(self):
    pass
  def setAuxData(self):
    pass
  def setBorderColor(self):
    pass
  def setComponentType(self):
    pass
  def setCompression(self):
    pass
  def setFilename(self):
    pass
  def setFormat(self):
    pass
  def setFullpath(self):
    pass
  def setKeepRamImage(self):
    pass
  def setLoadedFromImage(self):
    pass
  def setLoadedFromTxo(self):
    pass
  def setMagfilter(self):
    pass
  def setMatchFramebufferFormat(self):
    pass
  def setMinfilter(self):
    pass
  def setName(self):
    pass
  def setOrigFileSize(self):
    pass
  def setPadSize(self):
    pass
  def setPostLoadStoreCache(self):
    pass
  def setQualityLevel(self):
    pass
  def setRamImage(self):
    pass
  def setRamMipmapImage(self):
    pass
  def setRamMipmapPointerFromInt(self):
    pass
  def setRenderToTexture(self):
    pass
  def setSimpleRamImage(self):
    pass
  def setSizePadded(self):
    pass
  def setTexturesPower2():
    pass
  def setWrapU(self):
    pass
  def setWrapV(self):
    pass
  def setWrapW(self):
    pass
  def setXSize(self):
    pass
  def setYSize(self):
    pass
  def setZSize(self):
    pass
  def setup1dTexture(self):
    pass
  def setup2dTexture(self):
    pass
  def setup3dTexture(self):
    pass
  def setupCubeMap(self):
    pass
  def setupTexture(self):
    pass
  def store(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncompressRamImage(self):
    pass
  def unref(self):
    pass
  def upToPower2():
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def usesMipmaps(self):
    pass
  def wasImageModified(self):
    pass
  def write(self):
    pass
  def writeTxo(self):
    pass
class TextureAttrib:
  def __init__(self):
    pass
  MAlways = int

  MConstant = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MNever = int

  MNone = int

  MNotEqual = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def addOffStage(self):
    pass
  def addOnStage(self):
    pass
  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findOnStage(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getFfTcIndex(self):
    pass
  def getNumAttribs():
    pass
  def getNumOffStages(self):
    pass
  def getNumOnFfStages(self):
    pass
  def getNumOnStages(self):
    pass
  def getOffStage(self):
    pass
  def getOffStages(self):
    pass
  def getOnFfStage(self):
    pass
  def getOnFfStages(self):
    pass
  def getOnStage(self):
    pass
  def getOnStages(self):
    pass
  def getOnTexture(self):
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getTexture(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def hasAllOff(self):
    pass
  def hasOffStage(self):
    pass
  def hasOnStage(self):
    pass
  def isExactType(self):
    pass
  def isIdentity(self):
    pass
  def isOfType(self):
    pass
  def isOff(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeAllOff():
    pass
  def makeDefault():
    pass
  def makeOff():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def removeOffStage(self):
    pass
  def removeOnStage(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unifyTextureStages(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class TextureCollection:
  def __init__(self):
    pass
  def addTexture(self):
    pass
  def addTexturesFrom(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def findTexture(self):
    pass
  def getNumTextures(self):
    pass
  def getTexture(self):
    pass
  def getTextures(self):
    pass
  def hasTexture(self):
    pass
  def output(self):
    pass
  def removeDuplicateTextures(self):
    pass
  def removeTexture(self):
    pass
  def removeTexturesFrom(self):
    pass
  def size(self):
    pass
  def write(self):
    pass
class TextureContext:
  def __init__(self):
    pass
  def assign(self):
    pass
  def dequeueLru(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToIndexBufferContext(self):
    pass
  def downcastToTextureContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToVertexBufferContext(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def getActive(self):
    pass
  def getClassType():
    pass
  def getDataSizeBytes(self):
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def getModified(self):
    pass
  def getNumFrames(self):
    pass
  def getNumInactiveFrames(self):
    pass
  def getResident(self):
    pass
  def getTexture(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markUsedLru(self):
    pass
  def output(self):
    pass
  def setLruSize(self):
    pass
  def upcastToAdaptiveLruPage(self):
    pass
  def upcastToBufferContext(self):
    pass
  def upcastToSavedContext(self):
    pass
  def wasImageModified(self):
    pass
  def wasModified(self):
    pass
  def wasPropertiesModified(self):
    pass
  def wasSimpleImageModified(self):
    pass
  def write(self):
    pass
class TexturePeeker:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def filterRect(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def getZSize(self):
    pass
  def lookup(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
class TexturePool:
  def __init__(self):
    pass
  def addTexture():
    pass
  def clearFakeTextureImage():
    pass
  def findAllTextures():
    pass
  def findTexture():
    pass
  def garbageCollect():
    pass
  def getAlphaScaleMap():
    pass
  def getFakeTextureImage():
    pass
  def getNormalizationCubeMap():
    pass
  def hasFakeTextureImage():
    pass
  def hasTexture():
    pass
  def listContents():
    pass
  def load3dTexture():
    pass
  def loadCubeMap():
    pass
  def loadTexture():
    pass
  def rehash():
    pass
  def releaseAllTextures():
    pass
  def releaseTexture():
    pass
  def setFakeTextureImage():
    pass
  def verifyTexture():
    pass
  def write():
    pass
class TextureReloadRequest:
  def __init__(self):
    pass
  DSAgain = int

  DSCont = int

  DSDone = int

  DSExit = int

  DSInterrupt = int

  DSPause = int

  DSPickup = int

  SActive = int

  SActiveNested = int

  SInactive = int

  SServicing = int

  SServicingRemoved = int

  SSleeping = int

  def assign(self):
    pass
  def clearDelay(self):
    pass
  def clearName(self):
    pass
  def downcastToAsyncTaskSequence(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getAllowCompressed(self):
    pass
  def getAverageDt(self):
    pass
  def getClassType():
    pass
  def getDelay(self):
    pass
  def getDoneEvent(self):
    pass
  def getDt(self):
    pass
  def getElapsedFrames(self):
    pass
  def getElapsedTime(self):
    pass
  def getManager(self):
    pass
  def getMaxDt(self):
    pass
  def getName(self):
    pass
  def getNamePrefix(self):
    pass
  def getPreparedGraphicsObjects(self):
    pass
  def getPriority(self):
    pass
  def getPythonObject(self):
    pass
  def getRefCount(self):
    pass
  def getSort(self):
    pass
  def getStartFrame(self):
    pass
  def getStartTime(self):
    pass
  def getState(self):
    pass
  def getTaskChain(self):
    pass
  def getTaskId(self):
    pass
  def getTexture(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getWakeTime(self):
    pass
  def hasDelay(self):
    pass
  def hasName(self):
    pass
  def isAlive(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isReady(self):
    pass
  def output(self):
    pass
  def recalcWakeTime(self):
    pass
  def ref(self):
    pass
  def remove(self):
    pass
  def setDelay(self):
    pass
  def setDoneEvent(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setPythonObject(self):
    pass
  def setSort(self):
    pass
  def setTaskChain(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
class TextureStage:
  def __init__(self):
    pass
  CMAdd = int

  CMAddSigned = int

  CMDot3Rgb = int

  CMDot3Rgba = int

  CMInterpolate = int

  CMModulate = int

  CMReplace = int

  CMSubtract = int

  CMUndefined = int

  COOneMinusSrcAlpha = int

  COOneMinusSrcColor = int

  COSrcAlpha = int

  COSrcColor = int

  COUndefined = int

  CSConstant = int

  CSConstantColorScale = int

  CSLastSavedResult = int

  CSPrevious = int

  CSPrimaryColor = int

  CSTexture = int

  CSUndefined = int

  MAdd = int

  MBlend = int

  MBlendColorScale = int

  MCombine = int

  MDecal = int

  MGloss = int

  MGlow = int

  MHeight = int

  MModulate = int

  MModulateGloss = int

  MModulateGlow = int

  MNormal = int

  MNormalHeight = int

  MReplace = int

  MSelector = int

  def assign(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getAlphaScale(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getColor(self):
    pass
  def getCombineAlphaMode(self):
    pass
  def getCombineAlphaOperand0(self):
    pass
  def getCombineAlphaOperand1(self):
    pass
  def getCombineAlphaOperand2(self):
    pass
  def getCombineAlphaSource0(self):
    pass
  def getCombineAlphaSource1(self):
    pass
  def getCombineAlphaSource2(self):
    pass
  def getCombineRgbMode(self):
    pass
  def getCombineRgbOperand0(self):
    pass
  def getCombineRgbOperand1(self):
    pass
  def getCombineRgbOperand2(self):
    pass
  def getCombineRgbSource0(self):
    pass
  def getCombineRgbSource1(self):
    pass
  def getCombineRgbSource2(self):
    pass
  def getDefault():
    pass
  def getMode(self):
    pass
  def getName(self):
    pass
  def getNumCombineAlphaOperands(self):
    pass
  def getNumCombineRgbOperands(self):
    pass
  def getPriority(self):
    pass
  def getRefCount(self):
    pass
  def getRgbScale(self):
    pass
  def getSavedResult(self):
    pass
  def getSort(self):
    pass
  def getTexcoordName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def involvesColorScale(self):
    pass
  def isExactType(self):
    pass
  def isFixedFunction(self):
    pass
  def isOfType(self):
    pass
  def lessThan(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setAlphaScale(self):
    pass
  def setColor(self):
    pass
  def setCombineAlpha(self):
    pass
  def setCombineRgb(self):
    pass
  def setMode(self):
    pass
  def setName(self):
    pass
  def setPriority(self):
    pass
  def setRgbScale(self):
    pass
  def setSavedResult(self):
    pass
  def setSort(self):
    pass
  def setTexcoordName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def usesColor(self):
    pass
  def usesLastSavedResult(self):
    pass
  def usesPrimaryColor(self):
    pass
  def write(self):
    pass
class TextureStageCollection:
  def __init__(self):
    pass
  def addTextureStage(self):
    pass
  def addTextureStagesFrom(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def findTextureStage(self):
    pass
  def getNumTextureStages(self):
    pass
  def getTextureStage(self):
    pass
  def getTextureStages(self):
    pass
  def hasTextureStage(self):
    pass
  def output(self):
    pass
  def removeDuplicateTextureStages(self):
    pass
  def removeTextureStage(self):
    pass
  def removeTextureStagesFrom(self):
    pass
  def size(self):
    pass
  def sort(self):
    pass
  def write(self):
    pass
class Thread:
  def __init__(self):
    pass
  def assign(self):
    pass
  def bindThread():
    pass
  def clearName(self):
    pass
  def considerYield():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def forceYield():
    pass
  def getClassType():
    pass
  def getCurrentPipelineStage():
    pass
  def getCurrentThread():
    pass
  def getExternalThread():
    pass
  def getMainThread():
    pass
  def getName(self):
    pass
  def getPipelineStage(self):
    pass
  def getPstatsIndex(self):
    pass
  def getPythonData(self):
    pass
  def getRefCount(self):
    pass
  def getSyncName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUniqueId(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isJoinable(self):
    pass
  def isOfType(self):
    pass
  def isStarted(self):
    pass
  def isThreadingSupported():
    pass
  def isTrueThreads():
    pass
  def join(self):
    pass
  def output(self):
    pass
  def outputBlocker(self):
    pass
  def preempt(self):
    pass
  def prepareForExit():
    pass
  def ref(self):
    pass
  def setMinPipelineStage(self):
    pass
  def setName(self):
    pass
  def setPipelineStage(self):
    pass
  def setPythonData(self):
    pass
  def sleep():
    pass
  def start(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def upcastToTypedReferenceCount(self):
    pass
  def writeStatus():
    pass
class TimeVal:
  def __init__(self):
    pass
  def getSec(self):
    pass
  def getUsec(self):
    pass
class Trackball:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAllButtons(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearButton(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getCoordinateSystem(self):
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getForwardScale(self):
    pass
  def getH(self):
    pass
  def getHpr(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getInvert(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getMat(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOrigin(self):
    pass
  def getOverallBit():
    pass
  def getP(self):
    pass
  def getParent(self):
    pass
  def getPos(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getR(self):
    pass
  def getRefCount(self):
    pass
  def getRelTo(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransMat(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def moveOrigin(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def requireButton(self):
    pass
  def reset(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetOriginHere(self):
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setCoordinateSystem(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setForwardScale(self):
    pass
  def setH(self):
    pass
  def setHpr(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setInvert(self):
    pass
  def setMat(self):
    pass
  def setName(self):
    pass
  def setOrigin(self):
    pass
  def setOverallHidden(self):
    pass
  def setP(self):
    pass
  def setPos(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setR(self):
    pass
  def setRelTo(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class TrackerNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getGraphCoordinateSystem(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOrient(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPos(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTime(self):
    pass
  def getTrackerCoordinateSystem(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def hasTime(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def isValid(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setGraphCoordinateSystem(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTrackerCoordinateSystem(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class Transform2SG:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNode(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setNode(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class TransformBlend:
  def __init__(self):
    pass
  def addTransform(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def eq(self):
    pass
  def getBlend(self):
    pass
  def getClassType():
    pass
  def getModified(self):
    pass
  def getNumTransforms(self):
    pass
  def getTransform(self):
    pass
  def getTransforms(self):
    pass
  def getWeight(self):
    pass
  def hasTransform(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalizeWeights(self):
    pass
  def output(self):
    pass
  def removeTransform(self):
    pass
  def setTransform(self):
    pass
  def setWeight(self):
    pass
  def transformPoint(self):
    pass
  def transformVector(self):
    pass
  def updateBlend(self):
    pass
  def write(self):
    pass
class TransformBlendTable:
  def __init__(self):
    pass
  def addBlend(self):
    pass
  def assign(self):
    pass
  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getBlend(self):
    pass
  def getBlends(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getMaxSimultaneousTransforms(self):
    pass
  def getModified(self):
    pass
  def getNumBlends(self):
    pass
  def getNumTransforms(self):
    pass
  def getRefCount(self):
    pass
  def getRows(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def modifyRows(self):
    pass
  def ref(self):
    pass
  def removeBlend(self):
    pass
  def setBlend(self):
    pass
  def setRows(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class TransformState:
  def __init__(self):
    pass
  RCache = int

  RNode = int

  def cacheRef(self):
    pass
  def cacheUnref(self):
    pass
  def clearCache():
    pass
  def componentsGiven(self):
    pass
  def compose(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getCacheRefCount(self):
    pass
  def getClassType():
    pass
  def getCompositionCache(self):
    pass
  def getCompositionCacheNumEntries(self):
    pass
  def getCompositionCacheResult(self):
    pass
  def getCompositionCacheSize(self):
    pass
  def getCompositionCacheSource(self):
    pass
  def getGeomRendering(self):
    pass
  def getHash(self):
    pass
  def getHpr(self):
    pass
  def getInverse(self):
    pass
  def getInvertCompositionCache(self):
    pass
  def getInvertCompositionCacheNumEntries(self):
    pass
  def getInvertCompositionCacheResult(self):
    pass
  def getInvertCompositionCacheSize(self):
    pass
  def getInvertCompositionCacheSource(self):
    pass
  def getMat(self):
    pass
  def getMat3(self):
    pass
  def getNodeRefCount(self):
    pass
  def getNormQuat(self):
    pass
  def getNumStates():
    pass
  def getNumUnusedStates():
    pass
  def getPos(self):
    pass
  def getPos2d(self):
    pass
  def getQuat(self):
    pass
  def getRefCount(self):
    pass
  def getReferencedBits(self):
    pass
  def getRotate2d(self):
    pass
  def getScale(self):
    pass
  def getScale2d(self):
    pass
  def getShear(self):
    pass
  def getShear2d(self):
    pass
  def getStates():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUniformScale(self):
    pass
  def getUnique(self):
    pass
  def hasComponents(self):
    pass
  def hasHpr(self):
    pass
  def hasIdentityScale(self):
    pass
  def hasMat(self):
    pass
  def hasNonzeroShear(self):
    pass
  def hasPos(self):
    pass
  def hasQuat(self):
    pass
  def hasScale(self):
    pass
  def hasShear(self):
    pass
  def hasUniformScale(self):
    pass
  def hprGiven(self):
    pass
  def invertCompose(self):
    pass
  def is2d(self):
    pass
  def isExactType(self):
    pass
  def isIdentity(self):
    pass
  def isInvalid(self):
    pass
  def isOfType(self):
    pass
  def isSingular(self):
    pass
  def lessThan(self):
    pass
  def listCycles():
    pass
  def listStates():
    pass
  def makeHpr():
    pass
  def makeIdentity():
    pass
  def makeInvalid():
    pass
  def makeMat():
    pass
  def makeMat3():
    pass
  def makePos():
    pass
  def makePos2d():
    pass
  def makePosHpr():
    pass
  def makePosHprScale():
    pass
  def makePosHprScaleShear():
    pass
  def makePosQuatScale():
    pass
  def makePosQuatScaleShear():
    pass
  def makePosRotate2d():
    pass
  def makePosRotateScale2d():
    pass
  def makePosRotateScaleShear2d():
    pass
  def makeQuat():
    pass
  def makeRotate2d():
    pass
  def makeScale():
    pass
  def makeScale2d():
    pass
  def makeShear():
    pass
  def makeShear2d():
    pass
  def markBamModified(self):
    pass
  def nodeRef(self):
    pass
  def nodeUnref(self):
    pass
  def output(self):
    pass
  def quatGiven(self):
    pass
  def ref(self):
    pass
  def setHpr(self):
    pass
  def setPos(self):
    pass
  def setPos2d(self):
    pass
  def setQuat(self):
    pass
  def setRotate2d(self):
    pass
  def setScale(self):
    pass
  def setScale2d(self):
    pass
  def setShear(self):
    pass
  def setShear2d(self):
    pass
  def sortsLess(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateStates():
    pass
  def write(self):
    pass
  def writeCompositionCache(self):
    pass
class TransformTable:
  def __init__(self):
    pass
  def addTransform(self):
    pass
  def assign(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getModified(self):
    pass
  def getNumTransforms(self):
    pass
  def getRefCount(self):
    pass
  def getTransform(self):
    pass
  def getTransforms(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def isRegistered(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def registerTable():
    pass
  def removeTransform(self):
    pass
  def setTransform(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class TransparencyAttrib:
  def __init__(self):
    pass
  MAlpha = int

  MAlways = int

  MBinary = int

  MConstant = int

  MDual = int

  MEqual = int

  MEyeCubeMap = int

  MEyeNormal = int

  MEyePosition = int

  MEyeSphereMap = int

  MGreater = int

  MGreaterEqual = int

  MLess = int

  MLessEqual = int

  MLightVector = int

  MMultisample = int

  MMultisampleMask = int

  MNever = int

  MNone = int

  MNotEqual = int

  MNotused = int

  MOff = int

  MPointSprite = int

  MUnused = int

  MWorldCubeMap = int

  MWorldNormal = int

  MWorldPosition = int

  def compareTo(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassSlot():
    pass
  def getClassType():
    pass
  def getMode(self):
    pass
  def getNumAttribs():
    pass
  def getRefCount(self):
    pass
  def getSlot(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnique(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def listAttribs():
    pass
  def make():
    pass
  def makeDefault():
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def validateAttribs():
    pass
  def write(self):
    pass
class Triangulator:
  def __init__(self):
    pass
  def addHoleVertex(self):
    pass
  def addPolygonVertex(self):
    pass
  def addVertex(self):
    pass
  def beginHole(self):
    pass
  def clear(self):
    pass
  def clearPolygon(self):
    pass
  def getNumTriangles(self):
    pass
  def getNumVertices(self):
    pass
  def getTriangleV0(self):
    pass
  def getTriangleV1(self):
    pass
  def getTriangleV2(self):
    pass
  def getVertex(self):
    pass
  def getVertices(self):
    pass
  def isLeftWinding(self):
    pass
  def triangulate(self):
    pass
class TypedWritable:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
class TypedWritableReferenceCount:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class UniqueIdAllocator:
  def __init__(self):
    pass
  def allocate(self):
    pass
  def fractionUsed(self):
    pass
  def free(self):
    pass
  def initialReserveId(self):
    pass
  def output(self):
    pass
  def write(self):
    pass
class UpdateSeq:
  def __init__(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def eq(self):
    pass
  def fresh():
    pass
  def greaterThan(self):
    pass
  def greaterThanOrEqual(self):
    pass
  def increment(self):
    pass
  def initial():
    pass
  def isFresh(self):
    pass
  def isInitial(self):
    pass
  def isOld(self):
    pass
  def isSpecial(self):
    pass
  def lessThan(self):
    pass
  def lessThanOrEqual(self):
    pass
  def ne(self):
    pass
  def old():
    pass
  def output(self):
    pass
class UserDataAudio:
  def __init__(self):
    pass
  def append(self):
    pass
  def assign(self):
    pass
  def clearName(self):
    pass
  def decodeFromBamStream():
    pass
  def done(self):
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def get():
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getFilename(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def hasName(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def open(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setName(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
class UserDataAudioCursor:
  def __init__(self):
    pass
  def aborted(self):
    pass
  def audioChannels(self):
    pass
  def audioRate(self):
    pass
  def canSeek(self):
    pass
  def canSeekFast(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getRefCount(self):
    pass
  def getSource(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def length(self):
    pass
  def markBamModified(self):
    pass
  def readSamples(self):
    pass
  def ready(self):
    pass
  def ref(self):
    pass
  def seek(self):
    pass
  def skipSamples(self):
    pass
  def tell(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
class UserVertexSlider:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getModified(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSlider(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setSlider(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class UserVertexTransform:
  def __init__(self):
    pass
  def accumulateMatrix(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getGlobalModified():
    pass
  def getMatrix(self):
    pass
  def getModified(self):
    pass
  def getName(self):
    pass
  def getNextModified():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def multMatrix(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def setMatrix(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class UvScrollNode:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRSpeed(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUSpeed(self):
    pass
  def getUnexpectedChange(self):
    pass
  def getVSpeed(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def ref(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setRSpeed(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUSpeed(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setVSpeed(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class VBase2:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def zero():
    pass
class VBase2D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def zero():
    pass
class VBase3:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def cross(self):
    pass
  def crossInto(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getStandardizedHpr(self):
    pass
  def getX(self):
    pass
  def getXy(self):
    pass
  def getXz(self):
    pass
  def getY(self):
    pass
  def getYz(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class VBase3D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def cross(self):
    pass
  def crossInto(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getStandardizedHpr(self):
    pass
  def getX(self):
    pass
  def getXy(self):
    pass
  def getXz(self):
    pass
  def getY(self):
    pass
  def getYz(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class VBase4:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class VBase4D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class Vec2:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def signedAngleDeg(self):
    pass
  def signedAngleRad(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def zero():
    pass
class Vec2D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def signedAngleDeg(self):
    pass
  def signedAngleRad(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def zero():
    pass
class Vec3:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def back():
    pass
  def compareTo(self):
    pass
  def cross(self):
    pass
  def crossInto(self):
    pass
  def dot(self):
    pass
  def down():
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def forward():
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getStandardizedHpr(self):
    pass
  def getX(self):
    pass
  def getXy(self):
    pass
  def getXz(self):
    pass
  def getY(self):
    pass
  def getYz(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def left():
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def relativeAngleDeg(self):
    pass
  def relativeAngleRad(self):
    pass
  def rfu():
    pass
  def right():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def signedAngleDeg(self):
    pass
  def signedAngleRad(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def up():
    pass
  def zero():
    pass
class Vec3D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def angleDeg(self):
    pass
  def angleRad(self):
    pass
  def assign(self):
    pass
  def back():
    pass
  def compareTo(self):
    pass
  def cross(self):
    pass
  def crossInto(self):
    pass
  def dot(self):
    pass
  def down():
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def forward():
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getStandardizedHpr(self):
    pass
  def getX(self):
    pass
  def getXy(self):
    pass
  def getXz(self):
    pass
  def getY(self):
    pass
  def getYz(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def left():
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def relativeAngleDeg(self):
    pass
  def relativeAngleRad(self):
    pass
  def rfu():
    pass
  def right():
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def signedAngleDeg(self):
    pass
  def signedAngleRad(self):
    pass
  def size():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def up():
    pass
  def zero():
    pass
class Vec4:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def asTuple():
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def pPrintValues():
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class Vec4D:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def addHash(self):
    pass
  def addToCell(self):
    pass
  def addW(self):
    pass
  def addX(self):
    pass
  def addY(self):
    pass
  def addZ(self):
    pass
  def almostEqual(self):
    pass
  def assign(self):
    pass
  def compareTo(self):
    pass
  def dot(self):
    pass
  def eq(self):
    pass
  def fill(self):
    pass
  def fmax(self):
    pass
  def fmin(self):
    pass
  def getCell(self):
    pass
  def getClassType():
    pass
  def getHash(self):
    pass
  def getNumComponents(self):
    pass
  def getW(self):
    pass
  def getX(self):
    pass
  def getY(self):
    pass
  def getZ(self):
    pass
  def isNan(self):
    pass
  def length(self):
    pass
  def lengthSquared(self):
    pass
  def lessThan(self):
    pass
  def ne(self):
    pass
  def normalize(self):
    pass
  def output(self):
    pass
  def project(self):
    pass
  def pythonRepr(self):
    pass
  def set(self):
    pass
  def setCell(self):
    pass
  def setW(self):
    pass
  def setX(self):
    pass
  def setY(self):
    pass
  def setZ(self):
    pass
  def size():
    pass
  def unitW():
    pass
  def unitX():
    pass
  def unitY():
    pass
  def unitZ():
    pass
  def zero():
    pass
class VertexBufferContext:
  def __init__(self):
    pass
  def assign(self):
    pass
  def changedSize(self):
    pass
  def changedUsageHint(self):
    pass
  def dequeueLru(self):
    pass
  def downcastToBufferContext(self):
    pass
  def downcastToIndexBufferContext(self):
    pass
  def downcastToTextureContext(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToVertexBufferContext(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def getActive(self):
    pass
  def getClassType():
    pass
  def getData(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def getModified(self):
    pass
  def getNumFrames(self):
    pass
  def getNumInactiveFrames(self):
    pass
  def getResident(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markUsedLru(self):
    pass
  def output(self):
    pass
  def setLruSize(self):
    pass
  def upcastToAdaptiveLruPage(self):
    pass
  def upcastToBufferContext(self):
    pass
  def upcastToSavedContext(self):
    pass
  def wasModified(self):
    pass
  def write(self):
    pass
class VertexDataBlock:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToVertexDataBlock(self):
    pass
  def free(self):
    pass
  def getAllocator(self):
    pass
  def getClassType():
    pass
  def getMaxSize(self):
    pass
  def getNextBlock(self):
    pass
  def getPage(self):
    pass
  def getRefCount(self):
    pass
  def getSize(self):
    pass
  def getStart(self):
    pass
  def isFree(self):
    pass
  def output(self):
    pass
  def realloc(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToSimpleAllocatorBlock(self):
    pass
class VertexDataBook:
  def __init__(self):
    pass
  def alloc(self):
    pass
  def countAllocatedSize(self):
    pass
  def countTotalPageSize(self):
    pass
  def getNumPages(self):
    pass
  def saveToDisk(self):
    pass
class VertexDataPage:
  def __init__(self):
    pass
  RCCompressed = int

  RCDisk = int

  RCEndOfList = int

  RCResident = int

  def alloc(self):
    pass
  def assign(self):
    pass
  def dequeueLru(self):
    pass
  def downcastToGeomVertexArrayData(self):
    pass
  def downcastToVertexDataPage(self):
    pass
  def enqueueLru(self):
    pass
  def evictLru(self):
    pass
  def flushThreads():
    pass
  def getBook(self):
    pass
  def getClassType():
    pass
  def getContiguous(self):
    pass
  def getFirstBlock(self):
    pass
  def getGlobalLru():
    pass
  def getLru(self):
    pass
  def getLruSize(self):
    pass
  def getMaxSize(self):
    pass
  def getNumPendingReads():
    pass
  def getNumPendingWrites():
    pass
  def getNumThreads():
    pass
  def getPendingLru():
    pass
  def getPendingRamClass(self):
    pass
  def getRamClass(self):
    pass
  def getSaveFile():
    pass
  def getTotalSize(self):
    pass
  def isEmpty(self):
    pass
  def markUsedLru(self):
    pass
  def output(self):
    pass
  def requestResident(self):
    pass
  def saveToDisk(self):
    pass
  def setLruSize(self):
    pass
  def setMaxSize(self):
    pass
  def stopThreads():
    pass
  def upcastToSimpleAllocator(self):
    pass
  def upcastToSimpleLruPage(self):
    pass
  def write(self):
    pass
class VertexDataSaveFile:
  def __init__(self):
    pass
  def alloc(self):
    pass
  def downcastToVertexDataPage(self):
    pass
  def getContiguous(self):
    pass
  def getFirstBlock(self):
    pass
  def getMaxSize(self):
    pass
  def getTotalFileSize(self):
    pass
  def getTotalSize(self):
    pass
  def getUsedFileSize(self):
    pass
  def isEmpty(self):
    pass
  def isValid(self):
    pass
  def output(self):
    pass
  def setMaxSize(self):
    pass
  def write(self):
    pass
class VertexSlider:
  def __init__(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getModified(self):
    pass
  def getName(self):
    pass
  def getRefCount(self):
    pass
  def getSlider(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class VertexTransform:
  def __init__(self):
    pass
  def accumulateMatrix(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getGlobalModified():
    pass
  def getMatrix(self):
    pass
  def getModified(self):
    pass
  def getNextModified():
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
  def multMatrix(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
class VideoTexture:
  def __init__(self):
    pass
  CMDefault = int

  CMDxt1 = int

  CMDxt2 = int

  CMDxt3 = int

  CMDxt4 = int

  CMDxt5 = int

  CMFxt1 = int

  CMOff = int

  CMOn = int

  FAlpha = int

  FBlue = int

  FColorIndex = int

  FDepthComponent = int

  FDepthComponent16 = int

  FDepthComponent24 = int

  FDepthComponent32 = int

  FDepthStencil = int

  FGreen = int

  FLuminance = int

  FLuminanceAlpha = int

  FLuminanceAlphamask = int

  FRed = int

  FRgb = int

  FRgb12 = int

  FRgb332 = int

  FRgb5 = int

  FRgb8 = int

  FRgba = int

  FRgba12 = int

  FRgba16 = int

  FRgba32 = int

  FRgba4 = int

  FRgba5 = int

  FRgba8 = int

  FRgbm = int

  FTDefault = int

  FTInvalid = int

  FTLinear = int

  FTLinearMipmapLinear = int

  FTLinearMipmapNearest = int

  FTNearest = int

  FTNearestMipmapLinear = int

  FTNearestMipmapNearest = int

  FTShadow = int

  QLBest = int

  QLDefault = int

  QLFastest = int

  QLNormal = int

  TFloat = int

  TT1dTexture = int

  TT2dTexture = int

  TT3dTexture = int

  TTCubeMap = int

  TUnsignedByte = int

  TUnsignedInt248 = int

  TUnsignedShort = int

  WMBorderColor = int

  WMClamp = int

  WMInvalid = int

  WMMirror = int

  WMMirrorOnce = int

  WMRepeat = int

  def assign(self):
    pass
  def clear(self):
    pass
  def clearAlphaFilename(self):
    pass
  def clearAlphaFullpath(self):
    pass
  def clearAuxData(self):
    pass
  def clearFilename(self):
    pass
  def clearFullpath(self):
    pass
  def clearName(self):
    pass
  def clearRamImage(self):
    pass
  def clearRamMipmapImage(self):
    pass
  def clearRamMipmapImages(self):
    pass
  def clearSimpleRamImage(self):
    pass
  def compressRamImage(self):
    pass
  def considerRescale(self):
    pass
  def decodeFromBamStream():
    pass
  def downToPower2():
    pass
  def downcastToBamCacheRecord(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def downcastToVideoTexture(self):
    pass
  def encodeToBamStream(self):
    pass
  def estimateTextureMemory(self):
    pass
  def generateAlphaScaleMap(self):
    pass
  def generateNormalizationCubeMap(self):
    pass
  def generateRamMipmapImages(self):
    pass
  def generateSimpleRamImage(self):
    pass
  def getActive(self):
    pass
  def getAlphaFilename(self):
    pass
  def getAlphaFullpath(self):
    pass
  def getAnisotropicDegree(self):
    pass
  def getAuxData(self):
    pass
  def getBamModified(self):
    pass
  def getBorderColor(self):
    pass
  def getClassType():
    pass
  def getComponentType(self):
    pass
  def getComponentWidth(self):
    pass
  def getCompression(self):
    pass
  def getDataSizeBytes(self):
    pass
  def getEffectiveAnisotropicDegree(self):
    pass
  def getEffectiveMagfilter(self):
    pass
  def getEffectiveMinfilter(self):
    pass
  def getEffectiveQualityLevel(self):
    pass
  def getExpectedMipmapXSize(self):
    pass
  def getExpectedMipmapYSize(self):
    pass
  def getExpectedMipmapZSize(self):
    pass
  def getExpectedNumMipmapLevels(self):
    pass
  def getExpectedRamImageSize(self):
    pass
  def getExpectedRamMipmapImageSize(self):
    pass
  def getExpectedRamMipmapPageSize(self):
    pass
  def getExpectedRamPageSize(self):
    pass
  def getFilename(self):
    pass
  def getFormat(self):
    pass
  def getFrac(self):
    pass
  def getFrame(self):
    pass
  def getFrameRate(self):
    pass
  def getFullFframe(self):
    pass
  def getFullFrame(self):
    pass
  def getFullpath(self):
    pass
  def getImageModified(self):
    pass
  def getKeepRamImage(self):
    pass
  def getLoadedFromImage(self):
    pass
  def getLoadedFromTxo(self):
    pass
  def getMagfilter(self):
    pass
  def getMatchFramebufferFormat(self):
    pass
  def getMinfilter(self):
    pass
  def getName(self):
    pass
  def getNextFrame(self):
    pass
  def getNumComponents(self):
    pass
  def getNumFrames(self):
    pass
  def getNumLoadableRamMipmapImages(self):
    pass
  def getNumRamMipmapImages(self):
    pass
  def getOrigFileXSize(self):
    pass
  def getOrigFileYSize(self):
    pass
  def getOrigFileZSize(self):
    pass
  def getPadXSize(self):
    pass
  def getPadYSize(self):
    pass
  def getPadZSize(self):
    pass
  def getPlayRate(self):
    pass
  def getPostLoadStoreCache(self):
    pass
  def getPropertiesModified(self):
    pass
  def getQualityLevel(self):
    pass
  def getRamImage(self):
    pass
  def getRamImageAs(self):
    pass
  def getRamImageCompression(self):
    pass
  def getRamImageSize(self):
    pass
  def getRamMipmapImage(self):
    pass
  def getRamMipmapImageSize(self):
    pass
  def getRamMipmapPageSize(self):
    pass
  def getRamPageSize(self):
    pass
  def getRefCount(self):
    pass
  def getRenderToTexture(self):
    pass
  def getResident(self):
    pass
  def getSimpleImageModified(self):
    pass
  def getSimpleRamImage(self):
    pass
  def getSimpleRamImageSize(self):
    pass
  def getSimpleXSize(self):
    pass
  def getSimpleYSize(self):
    pass
  def getTexScale(self):
    pass
  def getTextureType(self):
    pass
  def getTexturesPower2():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUncompressedRamImage(self):
    pass
  def getVideoHeight(self):
    pass
  def getVideoWidth(self):
    pass
  def getWrapU(self):
    pass
  def getWrapV(self):
    pass
  def getWrapW(self):
    pass
  def getXSize(self):
    pass
  def getYSize(self):
    pass
  def getZSize(self):
    pass
  def hasAllRamMipmapImages(self):
    pass
  def hasAlphaFilename(self):
    pass
  def hasAlphaFullpath(self):
    pass
  def hasCompression(self):
    pass
  def hasFilename(self):
    pass
  def hasFullpath(self):
    pass
  def hasName(self):
    pass
  def hasRamImage(self):
    pass
  def hasRamMipmapImage(self):
    pass
  def hasSimpleRamImage(self):
    pass
  def hasUncompressedRamImage(self):
    pass
  def haveTexturesPower2():
    pass
  def isExactType(self):
    pass
  def isMipmap():
    pass
  def isOfType(self):
    pass
  def isPlaying(self):
    pass
  def isPrepared(self):
    pass
  def load(self):
    pass
  def loadRelated(self):
    pass
  def loop(self):
    pass
  def makeCopy(self):
    pass
  def makeRamImage(self):
    pass
  def makeRamMipmapImage(self):
    pass
  def markBamModified(self):
    pass
  def mightHaveRamImage(self):
    pass
  def modifyRamImage(self):
    pass
  def modifyRamMipmapImage(self):
    pass
  def modifySimpleRamImage(self):
    pass
  def newSimpleRamImage(self):
    pass
  def output(self):
    pass
  def peek(self):
    pass
  def pingpong(self):
    pass
  def play(self):
    pass
  def pose(self):
    pass
  def prepare(self):
    pass
  def prepareNow(self):
    pass
  def read(self):
    pass
  def readDds(self):
    pass
  def readTxo(self):
    pass
  def ref(self):
    pass
  def release(self):
    pass
  def releaseAll(self):
    pass
  def reload(self):
    pass
  def setAlphaFilename(self):
    pass
  def setAlphaFullpath(self):
    pass
  def setAnisotropicDegree(self):
    pass
  def setAuxData(self):
    pass
  def setBorderColor(self):
    pass
  def setComponentType(self):
    pass
  def setCompression(self):
    pass
  def setFilename(self):
    pass
  def setFormat(self):
    pass
  def setFullpath(self):
    pass
  def setKeepRamImage(self):
    pass
  def setLoadedFromImage(self):
    pass
  def setLoadedFromTxo(self):
    pass
  def setMagfilter(self):
    pass
  def setMatchFramebufferFormat(self):
    pass
  def setMinfilter(self):
    pass
  def setName(self):
    pass
  def setOrigFileSize(self):
    pass
  def setPadSize(self):
    pass
  def setPlayRate(self):
    pass
  def setPostLoadStoreCache(self):
    pass
  def setQualityLevel(self):
    pass
  def setRamImage(self):
    pass
  def setRamMipmapImage(self):
    pass
  def setRamMipmapPointerFromInt(self):
    pass
  def setRenderToTexture(self):
    pass
  def setSimpleRamImage(self):
    pass
  def setSizePadded(self):
    pass
  def setTexturesPower2():
    pass
  def setWrapU(self):
    pass
  def setWrapV(self):
    pass
  def setWrapW(self):
    pass
  def setXSize(self):
    pass
  def setYSize(self):
    pass
  def setZSize(self):
    pass
  def setup1dTexture(self):
    pass
  def setup2dTexture(self):
    pass
  def setup3dTexture(self):
    pass
  def setupCubeMap(self):
    pass
  def setupTexture(self):
    pass
  def stop(self):
    pass
  def store(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def uncompressRamImage(self):
    pass
  def unref(self):
    pass
  def upToPower2():
    pass
  def upcastToAnimInterface(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTexture(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def upcastToTypedWritableReferenceCount(self):
    pass
  def usesMipmaps(self):
    pass
  def wasImageModified(self):
    pass
  def write(self):
    pass
  def writeTxo(self):
    pass
class VirtualMouse:
  def __init__(self):
    pass
  FBCullCallback = int

  FBDrawMask = int

  FBEffects = int

  FBState = int

  FBTag = int

  FBTransform = int

  UCChildren = int

  UCDrawMask = int

  UCParents = int

  UCState = int

  UCTransform = int

  def addChild(self):
    pass
  def addStashed(self):
    pass
  def adjustDrawMask(self):
    pass
  def asLight(self):
    pass
  def assign(self):
    pass
  def clearAttrib(self):
    pass
  def clearBounds(self):
    pass
  def clearEffect(self):
    pass
  def clearEffects(self):
    pass
  def clearName(self):
    pass
  def clearPythonTag(self):
    pass
  def clearState(self):
    pass
  def clearTag(self):
    pass
  def clearTransform(self):
    pass
  def clearUnexpectedChange(self):
    pass
  def combineWith(self):
    pass
  def compareTags(self):
    pass
  def copyAllProperties(self):
    pass
  def copyChildren(self):
    pass
  def copySubgraph(self):
    pass
  def copyTags(self):
    pass
  def countNumDescendants(self):
    pass
  def decodeFromBamStream():
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def findChild(self):
    pass
  def findParent(self):
    pass
  def findStashed(self):
    pass
  def getAllCameraMask():
    pass
  def getAttrib(self):
    pass
  def getBamModified(self):
    pass
  def getBounds(self):
    pass
  def getBoundsType(self):
    pass
  def getChild(self):
    pass
  def getChildSort(self):
    pass
  def getClassType():
    pass
  def getDrawControlMask(self):
    pass
  def getDrawShowMask(self):
    pass
  def getEffect(self):
    pass
  def getEffects(self):
    pass
  def getFancyBits(self):
    pass
  def getInternalBounds(self):
    pass
  def getInternalVertices(self):
    pass
  def getIntoCollideMask(self):
    pass
  def getLegalCollideMask(self):
    pass
  def getName(self):
    pass
  def getNestedVertices(self):
    pass
  def getNetCollideMask(self):
    pass
  def getNetDrawControlMask(self):
    pass
  def getNetDrawShowMask(self):
    pass
  def getNumChildren(self):
    pass
  def getNumParents(self):
    pass
  def getNumStashed(self):
    pass
  def getOffClipPlanes(self):
    pass
  def getOverallBit():
    pass
  def getParent(self):
    pass
  def getPrevTransform(self):
    pass
  def getPythonTag(self):
    pass
  def getRefCount(self):
    pass
  def getStashed(self):
    pass
  def getStashedSort(self):
    pass
  def getState(self):
    pass
  def getTag(self):
    pass
  def getTransform(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def getUnexpectedChange(self):
    pass
  def hasAttrib(self):
    pass
  def hasDirtyPrevTransform(self):
    pass
  def hasEffect(self):
    pass
  def hasName(self):
    pass
  def hasPythonTag(self):
    pass
  def hasTag(self):
    pass
  def hasTags(self):
    pass
  def isAmbientLight(self):
    pass
  def isBoundsStale(self):
    pass
  def isExactType(self):
    pass
  def isFinal(self):
    pass
  def isGeomNode(self):
    pass
  def isLodNode(self):
    pass
  def isOfType(self):
    pass
  def isOverallHidden(self):
    pass
  def isSceneRoot(self):
    pass
  def isUnderSceneRoot(self):
    pass
  def listTags(self):
    pass
  def ls(self):
    pass
  def makeCopy(self):
    pass
  def markBamModified(self):
    pass
  def markBoundsStale(self):
    pass
  def markInternalBoundsStale(self):
    pass
  def output(self):
    pass
  def prepareScene(self):
    pass
  def pressButton(self):
    pass
  def ref(self):
    pass
  def releaseButton(self):
    pass
  def removeAllChildren(self):
    pass
  def removeChild(self):
    pass
  def removeStashed(self):
    pass
  def replaceChild(self):
    pass
  def replaceNode(self):
    pass
  def resetAllPrevTransform():
    pass
  def resetPrevTransform(self):
    pass
  def setAttrib(self):
    pass
  def setBound(self):
    pass
  def setBounds(self):
    pass
  def setBoundsType(self):
    pass
  def setEffect(self):
    pass
  def setEffects(self):
    pass
  def setFinal(self):
    pass
  def setIntoCollideMask(self):
    pass
  def setMouseOn(self):
    pass
  def setMousePos(self):
    pass
  def setName(self):
    pass
  def setOverallHidden(self):
    pass
  def setPrevTransform(self):
    pass
  def setPythonTag(self):
    pass
  def setState(self):
    pass
  def setTag(self):
    pass
  def setTransform(self):
    pass
  def setUnexpectedChange(self):
    pass
  def setWindowSize(self):
    pass
  def stashChild(self):
    pass
  def stealChildren(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def unstashChild(self):
    pass
  def upcastToNamable(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedWritable(self):
    pass
  def write(self):
    pass
  def writeConnections(self):
    pass
  def writeInputs(self):
    pass
  def writeOutputs(self):
    pass
class VrpnClient:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def forkAsynchronousThread(self):
    pass
  def getClassType():
    pass
  def getCoordinateSystem(self):
    pass
  def getLastPollTime(self):
    pass
  def getRefCount(self):
    pass
  def getServerName(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isConnected(self):
    pass
  def isExactType(self):
    pass
  def isForked(self):
    pass
  def isOfType(self):
    pass
  def isValid(self):
    pass
  def poll(self):
    pass
  def ref(self):
    pass
  def setCoordinateSystem(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
  def write(self):
    pass
class WindowHandle:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def getClassType():
    pass
  def getIntHandle(self):
    pass
  def getOsHandle(self):
    pass
  def getRefCount(self):
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def output(self):
    pass
  def ref(self):
    pass
  def sendWindowsMessage(self):
    pass
  def setOsHandle(self):
    pass
  def testRefCountIntegrity(self):
    pass
  def testRefCountNonzero(self):
    pass
  def unref(self):
    pass
  def upcastToReferenceCount(self):
    pass
  def upcastToTypedObject(self):
    pass
class WindowProperties:
  def __init__(self):
    pass
  MAbsolute = int

  MRelative = int

  ZBottom = int

  ZNormal = int

  ZTop = int

  def addProperties(self):
    pass
  def assign(self):
    pass
  def clear(self):
    pass
  def clearCursorFilename(self):
    pass
  def clearCursorHidden(self):
    pass
  def clearDefault():
    pass
  def clearFixedSize(self):
    pass
  def clearForeground(self):
    pass
  def clearFullscreen(self):
    pass
  def clearIconFilename(self):
    pass
  def clearMinimized(self):
    pass
  def clearMouseMode(self):
    pass
  def clearOpen(self):
    pass
  def clearOrigin(self):
    pass
  def clearParentWindow(self):
    pass
  def clearRawMice(self):
    pass
  def clearSize(self):
    pass
  def clearTitle(self):
    pass
  def clearUndecorated(self):
    pass
  def clearZOrder(self):
    pass
  def eq(self):
    pass
  def getConfigProperties():
    pass
  def getCursorFilename(self):
    pass
  def getCursorHidden(self):
    pass
  def getDefault():
    pass
  def getFixedSize(self):
    pass
  def getForeground(self):
    pass
  def getFullscreen(self):
    pass
  def getIconFilename(self):
    pass
  def getMinimized(self):
    pass
  def getMouseMode(self):
    pass
  def getOpen(self):
    pass
  def getParentWindow(self):
    pass
  def getRawMice(self):
    pass
  def getTitle(self):
    pass
  def getUndecorated(self):
    pass
  def getXOrigin(self):
    pass
  def getXSize(self):
    pass
  def getYOrigin(self):
    pass
  def getYSize(self):
    pass
  def getZOrder(self):
    pass
  def hasCursorFilename(self):
    pass
  def hasCursorHidden(self):
    pass
  def hasFixedSize(self):
    pass
  def hasForeground(self):
    pass
  def hasFullscreen(self):
    pass
  def hasIconFilename(self):
    pass
  def hasMinimized(self):
    pass
  def hasMouseMode(self):
    pass
  def hasOpen(self):
    pass
  def hasOrigin(self):
    pass
  def hasParentWindow(self):
    pass
  def hasRawMice(self):
    pass
  def hasSize(self):
    pass
  def hasTitle(self):
    pass
  def hasUndecorated(self):
    pass
  def hasZOrder(self):
    pass
  def isAnySpecified(self):
    pass
  def ne(self):
    pass
  def output(self):
    pass
  def setCursorFilename(self):
    pass
  def setCursorHidden(self):
    pass
  def setDefault():
    pass
  def setFixedSize(self):
    pass
  def setForeground(self):
    pass
  def setFullscreen(self):
    pass
  def setIconFilename(self):
    pass
  def setMinimized(self):
    pass
  def setMouseMode(self):
    pass
  def setOpen(self):
    pass
  def setOrigin(self):
    pass
  def setParentWindow(self):
    pass
  def setRawMice(self):
    pass
  def setSize(self):
    pass
  def setTitle(self):
    pass
  def setUndecorated(self):
    pass
  def setZOrder(self):
    pass
  def size():
    pass
class WritableConfigurable:
  def __init__(self):
    pass
  def downcastToTypedReferenceCount(self):
    pass
  def downcastToTypedWritableReferenceCount(self):
    pass
  def encodeToBamStream(self):
    pass
  def getBamModified(self):
    pass
  def getClassType():
    pass
  def getType(self):
    pass
  def getTypeIndex(self):
    pass
  def isExactType(self):
    pass
  def isOfType(self):
    pass
  def markBamModified(self):
    pass
class Pixel:
  def __init__(self):
    pass
  def Setitem(self):
    pass
  def size():
    pass
def autoBind():
  pass
def composeMatrix():
  pass
def composeMatrixNewHpr():
  pass
def composeMatrixOldHpr():
  pass
def decomposeMatrix():
  pass
def decomposeMatrixNewHpr():
  pass
def decomposeMatrixOldHpr():
  pass
def deg2Rad():
  pass
def genericReadDatagram():
  pass
def genericWriteDatagram():
  pass
def getDefaultCoordinateSystem():
  pass
def getModelPath():
  pass
def getPluginPath():
  pass
def hashPrcVariables():
  pass
def headsUp():
  pass
def invert():
  pass
def loadPrcFile():
  pass
def loadPrcFileData():
  pass
def lookAt():
  pass
def newToOldHpr():
  pass
def oldToNewHpr():
  pass
def pyDecodeNodePathFromBamStream():
  pass
def pyDecodeTypedWritableFromBamStream():
  pass
def rad2Deg():
  pass
def rotateTo():
  pass
def transpose():
  pass
def unloadPrcFile():
  pass
