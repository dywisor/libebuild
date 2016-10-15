__all__ = ["InvalidCPV", "InvalidVersion", "MalformedAtom"]

try:
    import pkgcore.ebuild.errors

except ImportError:

    class InvalidCPV(Exception):
        pass

    class InvalidVersion(Exception):
        pass

    class MalformedAtom(Exception):
        pass

else:
    from pkgcore.ebuild.errors import InvalidCPV, InvalidVersion, MalformedAtom
