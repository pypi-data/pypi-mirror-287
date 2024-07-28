import os
import sys
from typing import Optional, TypeVar
from logging import Logger, StreamHandler, Formatter, getLogger
from mongey.db import DB, DatabaseConfig
from mongey.cache.abc import AbstractCache
from mongey.cache import CACHE_ENGINE_MAP, NoCache
from mongey.context import ctx as mongeyctx
from .config import Config

TCache = TypeVar("TCache", bound=AbstractCache)

class Context:
    _ctx: Optional[Config]
    _db: Optional[DB]
    _log: Optional[Logger] = None
    _l1_cache: Optional[AbstractCache] = None
    _l2_cache: Optional[AbstractCache] = None

    @property
    def project_dir(self) -> str:
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

    @property
    def cfg(self) -> Config:
        if self._cfg is None:
            cfg_filename = os.environ.get("APP_CONFIG", "application.toml")
            if not os.path.isfile(cfg_filename):
                cfg_filename = os.path.join(self.project_dir, cfg_filename)
            if os.path.isfile(cfg_filename):
                self._cfg = Config.parse(cfg_filename)
            else:
                print("no configuration files found, using default config values")
                self._cfg = Config()
        return self._cfg

    @property
    def log(self) -> Logger:
        if self._log is None:
            logger = getLogger(__name__)
            logger.propagate = False
            logger.setLevel(self.cfg.logging.level)
            for handler in logger.handlers:
                logger.removeHandler(handler)
            log_format = Formatter("[%(asctime)s] %(levelname)s %(filename)s:%(lineno)d %(message)s")
            handler = StreamHandler(stream=sys.stdout)
            handler.setLevel(self.cfg.logging.level)
            handler.setFormatter(log_format)
            logger.addHandler(handler)
            self._log = logger
        return self._log

    @property
    def l1_cache(self) -> AbstractCache:
        if self._l1_cache is None:
            cache = CACHE_ENGINE_MAP.get(self.cfg.cache.level1)
            if cache is None:
                self.log.error(f"cache engine {self.cfg.cache.level1} not found, falling back to NoCache")
                self._l1_cache = NoCache()
            else:
                self._l1_cache = cache()
        return self._l1_cache
    
    @property
    def l2_cache(self) -> AbstractCache:
        if self._l2_cache is None:
            cache = CACHE_ENGINE_MAP.get(self.cfg.cache.level1)
            if cache is None:
                self.log.error(f"cache engine {self.cfg.cache.level1} not found, falling back to NoCache")
                self._l2_cache = NoCache()
            else:
                self._l2_cache = cache()
        return self._l2_cache

    @property
    def db(self) -> "DB":
        if self._db is None:
            self._db = mongeyctx.db
            dbcfg: DatabaseConfig = {
                "meta": {
                    "uri": self.cfg.database.uri,
                    "kwargs": {
                        "serverSelectionTimeout": self.cfg.database.timeout
                    }
                },
                "shards": {}
            }
            self._db.configure(dbcfg, mock=False)
        return self._db

ctx = Context()
