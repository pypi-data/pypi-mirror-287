from . import *

class Database:
    """path: Your db path, leave None if you need in-memory type\n
    lock: Async-sync db type, slower but more stable\n
    autocommit: Autosave database when changed, leave False if changes are too frequent\n
    backup: Leave None if you don't need backups or if you chose a type in-memory"""
    def __init__(
        self,
        name: str = "MDB.json",
        path: str | Path = "memory",
        lock: asyncio.Lock = None,
        autocommit: bool = False,
        backup: int = False
    ):
        
        if type == "memory" and autocommit:
            raise InMemoryAutocommitError("Can't use autocommit when in-memory type")
        
        if type == "memory" and backup:
            raise InMemoryBackupError("Can't use backup's when in-memory type")
        
        if not lock:
            pass

        elif type(lock) != type(asyncio.Lock()):
            raise WrongLockTypeError("You must use asyncio.Lock() in that param")

        if not type == "memory":
            if type(path) != type(Path()):
                self.path = Path(path)
            else:
                self.path = path

            try:
                name = str(name)
            except:
                raise WrongNameTypeError("The name must be a string or a number")
            
            if not name.endswith(".json"):
                name += ".json"


            self.backup_path = self.path / "backups"
            self._path = self.path / name

            if not self._path.exists():
                try:
                    if not self.backup_path.exists():
                        self.backup_path.mkdir(parents=True, exist_ok=True)
                    self._path.write_text("{}")
                except:
                    raise BadPathError("The directory is incorrect or there is no access to it")
                

                self.data = {}
            else:
                try:
                    if not self.backup_path.exists():
                        self.backup_path.mkdir(parents=True, exist_ok=True)
                    with open(self._path, mode='r', encoding='utf-8') as file:
                        data = file.read()
                except PermissionError:
                    raise BadPathError("The directory is incorrect or there is no access to it")
                
                self.data = json.loads(data)
        else:
            self.data = {}

        self.backup = backup

        if isinstance(backup, int) and backup > 0:
            print("backup")
            self.b_task = asyncio.create_task(self.auto_backup())
        else:
            self.b_task = None

        self.lock = lock
        self.autocommit = autocommit

        
    async def auto_backup(self):
        while True:
            path = Path(self.backup_path / ("db-backup-" + datetime.now().strftime("%Y.%m.%d %H-%M-%S") + ".json"))
            async with aiofiles.open(path, "wt") as backup:
                await backup.write(json.dumps(self.data, indent=4))
            await asyncio.sleep(self.backup)


    async def save(self):
        """Manually saving database changes"""
        if self.lock:
            async with self.lock:
                async with aiofiles.open(self._path, "wt") as file:
                    await file.write(json.dumps(self.data, indent=4))

    async def set(
        self,
        key: str | int | list | tuple,
        *args
    ):
        """Recording data:\n
            await db.set("key", "value") -> {"key": "value"}\n
            await db.set("key", ["value", {"key1": "value1"}]) -> {"key": ["value", {"key1": "value1"}]}"""
        
        if self.lock:
            async with self.lock:
                await self._set(key, *args)
                
        else:
            await self._set(key, *args)

        await self.save() if self.autocommit else None
        
        

    async def _set(
        self,
        key: str | int | list | tuple,
        *args
    ):
        
        keys = key

        if isinstance(keys, (str, int)):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            raise WrongValueTypeError("You must use only str, int, tuple or list values as keys")
        
        for key in keys:
            key = str(key)

            if len(args) == 1:
                value = args[0]
                self.data[key] = value
            
            else:
                current_value = self.data.get(key) or {}
                target = current_value

                for arg in args[:-2]:
                    if arg not in target or not isinstance(target[arg], dict):
                        target[arg] = {}
                    target = target[arg]

                target[args[-2]] = args[-1]
                self.data[key] = current_value

        


    async def get(
        self,
        key: str | int | list | tuple,
        *args
    ) -> any:
        """Receiving data:\n

            await db.get("value") -> any | tuple\n
            data = dict({"your_data": "value", "another_data": {"key1": 123, "key2": 321}})\n
            await db.get("your_data") -> "value"\n
            await db.get("another_data") -> {"key1": 123, "key2": 321}\n
            await db.get("another_data", "key1") -> 123\n
            await db.get(["your_data", "another_data"]) -> ("value", {"key1": 123, "key2": 321})\n
            await db.get(["your_data", "another_data"], "key1") -> (None, 123)"""
        
        
        keys = key
        results = []

        if isinstance(keys, (str, int)):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            raise WrongValueTypeError("You must use only str, int, tuple or list values as keys")


        for key in keys:
            data = self.data.get(key)
            if data:
                for arg in args:
                    if isinstance(data, dict) and arg in data:
                        data = data[arg]
                    else:
                        data = None
                        break
                results.append(data)
            else:
                results.append(None)
        
        return tuple(results) if len(results) > 1 else results[0]