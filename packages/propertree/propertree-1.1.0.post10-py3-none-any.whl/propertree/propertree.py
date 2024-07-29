# Copyright 2021 Edward Hope-Morley
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=protected-access

import abc

from propertree.log import log


class PTreeException(Exception):  # pylint: disable=missing-class-docstring
    pass


class OverrideState():  # pylint: disable=missing-class-docstring
    def __init__(self, owner, content):
        self._whoami = "{}.{}".format(owner.__class__.__name__,  # noqa, pylint: disable=consider-using-f-string
                                      self.__class__.__name__)
        log.debug("%s.__init__: id=%s content=%s", self._whoami, id(self),
                  content)
        self._content = content

    @property
    def content(self):  # pylint: disable=missing-function-docstring
        # log.debug("%s.content", self._whoami))
        return self._content

    def __getattr__(self, name):
        # log.debug("%s.__getattr__: %s", self._whoami, name))
        _name = name.replace('_', '-')
        if not isinstance(self.content, dict) or _name not in self.content:
            raise AttributeError("'{}' object has no attribute '{}'". # noqa, pylint: disable=consider-using-f-string
                                 format(self._whoami, name))

        return self.content[_name]


class OverrideStack():  # pylint: disable=missing-class-docstring
    def __init__(self, owner):
        self._whoami = "{}.{}".format(owner.__class__.__name__,   # noqa, pylint: disable=consider-using-f-string
                                      self.__class__.__name__)
        self.items = []
        log.debug("%s.__init__ id=%s (owner=%s)", self._whoami, id(self),
                  id(owner))

    def push(self, item):  # pylint: disable=missing-function-docstring
        self.items.append(item)
        log.debug("%s: push (stack_id=%s) \n%s\n", self._whoami, id(self),
                  repr(self))

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        r = []
        for item in self.items:
            if isinstance(item, OverrideState):
                r.append("[{}] type={} content={}".  # noqa, pylint: disable=consider-using-f-string
                         format(id(item), item._whoami, item.content))
            else:
                r.append("[{}] {} depth={}".format(id(item), item._whoami,   # noqa, pylint: disable=consider-using-f-string
                                                   len(item)))

        return '\n'.join(r)

    @property
    def current(self):
        """ Return most recent object if available. """
        if len(self.items) > 0:
            log.debug("%s: using current", self._whoami)
            return self.items[-1]

        return None

    def __iter__(self):
        log.debug("%s.__iter__ id=%s", self._whoami, id(self))
        for item in self.items:  # pylint: disable=R1737
            yield item


class OverrideBase(abc.ABC):  # pylint: disable=missing-class-docstring

    def __init__(self, name, content, context, resolve_path, state=None):   # noqa, pylint: disable=too-many-arguments
        self._whoami = self.__class__.__name__
        self._context = context
        log.debug("%s.__init__: id=%s name=%s content=%s resolve_path=%s "
                  "state=%s", self._whoami, id(self), name, content,
                  resolve_path, state)
        self._override_resolved_name = name
        self._override_resolve_path = resolve_path
        log.debug("creating new stack for override id=%s", id(self))
        self._stack = OverrideStack(self)
        self.add_state(name, content, state=state)

    @classmethod
    @abc.abstractmethod
    def _override_keys(cls):
        """ Must be implemented and return a list of one or more unique keys
        that will be used to identify this override.
        """

    @property
    def _override_name(self):
        """ This is the key name that was used to resolve this override. """
        log.debug("%s._override_name", self._whoami)
        return self._override_resolved_name

    @property
    def _override_path(self):
        """ This is the full resolve path for this override object. """
        path = "{}.{}".format(self._override_resolve_path, self._override_name)   # noqa, pylint: disable=consider-using-f-string
        log.debug("%s._override_path %s", self._whoami, path)
        return path

    @classmethod
    def valid_parse_content_types(cls):
        """ Override this if you want to restrict what content can be parsed
        e.g. of the content only contains dicts as properties and not lists of
        properties we can constrain that here.
        """
        return [dict, list]

    @property
    def context(self):  # pylint: disable=missing-function-docstring
        # log.debug("%s.context", self._whoami)
        return self._context

    @property
    def content(self):  # pylint: disable=missing-function-docstring
        # log.debug("%s.content (%s)", self._whoami, len(self._stack))
        if len(self._stack):
            return self._stack.current.content

        return None

    def add_state(self, _name, content, state=None):
        """
        We don't both saving name in state for unmapped overrides.
        """
        log.debug("saving override state")
        if state is None:
            state = OverrideState(self, content)

        self._stack.push(state)

    def __len__(self):
        return len(self._stack)

    def __iter__(self):
        log.debug("%s.__iter__ unmapped", self._whoami)
        for item in self._stack:
            yield self.__class__(self._override_name, None, self.context,
                                 self._override_path, state=item)

    @abc.abstractmethod
    def __getattr__(self, name):
        """ Each implementation must have their own means of lookups. """


class PTreeOverrideBase(OverrideBase):  # noqa, pylint: disable=missing-class-docstring

    def __getattr__(self, name):
        log.debug("%s.__getattr__: unmapped name=%s", self._whoami, name)
        if len(self._stack):
            # none is allowed as a return value
            return getattr(self._stack.current, name)

        raise AttributeError("'{}' object has no attribute '{}'".  # noqa, pylint: disable=consider-using-f-string
                             format(self._whoami, name))


class PTreeOverrideRawType(OverrideBase):  # noqa, pylint: disable=missing-class-docstring

    @classmethod
    def _override_keys(cls):  # pylint: disable=missing-function-docstring
        return ['__raw_type__']

    @classmethod
    def check_is_raw_value(cls, content):  # noqa, pylint: disable=missing-function-docstring
        if type(content) in cls.valid_parse_content_types():
            return False

        return True

    def __type__(self):
        return type(self.content)

    def __int__(self):
        return int(self.content)

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.content

    def __getattr__(self, name):
        """ These objects wont have any custom attributes. """
        raise AttributeError("'{}' object has no attribute '{}'".  # noqa, pylint: disable=consider-using-f-string
                             format(self._whoami, name))


class MappedOverrideState():  # pylint: disable=missing-class-docstring

    def __init__(self, owner, content, member_keys):
        self._whoami = "{}.{}".format(owner.__class__.__name__,   # noqa, pylint: disable=consider-using-f-string
                                      self.__class__.__name__)
        self._owner = owner
        self._content = content
        self._stacks = {'member': {}, 'nested': {}}
        self._member_keys = member_keys
        log.debug("%s.__init__: id=%s content=%s", self._whoami, id(self),
                  content)

    @property
    def _override_name(self):  # pylint: disable=missing-function-docstring
        return self._owner._override_name  # noqa, pylint: disable=protected-access

    @property
    def content(self):  # pylint: disable=missing-function-docstring
        # log.debug("%s.content", self._whoami)
        _content = {}
        for stype in self._stacks:  # pylint: disable=C0206
            for name, stack in self._stacks[stype].items():
                _content.update({name: stack})

        return _content

    def add_obj(self, obj):  # pylint: disable=missing-function-docstring
        if isinstance(obj, self._owner.__class__):
            log.debug("obj name='%s' is a nested mapping", obj._override_name)  # noqa, pylint: disable=protected-access
            stack_type = 'nested'
        else:
            log.debug("obj name='%s' is a mapping member", obj._override_name)  # noqa, pylint: disable=protected-access
            stack_type = 'member'

        name = obj._override_name  # noqa, pylint: disable=protected-access
        stack = self._stacks[stack_type]
        log.debug("%s.add_obj: stack_type=%s name=%s id=%s",   # noqa, pylint: disable=protected-access
                  self._whoami, stack_type, name, id(obj))
        if name not in stack:
            log.debug("no stack found for %s '%s' so creating new one",
                      stack_type, name)
            stack[name] = OverrideStack(self)
        else:
            log.debug("using existing stack for %s '%s'", stack_type, name)

        stack[name].push(obj)
        log.debug("%s %s stack: \n%s\n", self._whoami, stack_type, repr(self))

    def __len__(self):
        return sum([len(self._stacks[stype]) for stype in self._stacks])  # noqa, pylint: disable=R1728,C0206

    def __repr__(self):
        log.debug("%s.repr", self._whoami)
        r = []
        for stype in self._stacks:  # pylint: disable=C0206
            for name, stack in self._stacks[stype].items():
                r.append("[{}] depth={} ".format(name, len(stack)))   # noqa, pylint: disable=consider-using-f-string

        return '\n'.join(r)

    def __iter__(self):
        log.debug("%s.__iter__", self._whoami)
        for stype in self._stacks:  # pylint: disable=C0206
            for obj in self._stacks[stype].values():
                for item in obj:  # pylint: disable=R1737
                    yield item

    def __getattr__(self, name):
        log.debug("%s.__getattr__: mapped state %s", self._whoami, name)
        _name = name.replace('_', '-')
        for stype in self._stacks:  # pylint: disable=C0206
            obj = self._stacks[stype].get(_name)
            if obj is not None:
                break

        if obj:
            log.debug("%s found (len=%s)", _name, len(obj))
            if len(obj) > 1:
                return obj

            m = obj.current
            try:
                # Allow overrides to define a property for non-simple
                # content to be returned as-is.
                return getattr(m, _name)
            except Exception:   # noqa, pylint: disable=broad-exception-caught
                log.debug("%s not found in %s", _name,
                          m.__class__.__name__)
                if type(m.content) not in [dict, list]:
                    log.debug("returning raw content")
                    return m.content

                return m

        if _name in self._member_keys:
            # allow members to be empty
            return None

        raise AttributeError("'{}' object has no attribute '{}'".   # noqa, pylint: disable=consider-using-f-string
                             format(self._whoami, name))


class PTreeMappedOverrideBase(OverrideBase):  # noqa, pylint: disable=missing-class-docstring

    def __init__(self, name, content, *args, **kwargs):
        log.debug("creating new mapped override id=%s type=%s name=%s",
                  id(self), type(self), name)
        self._current_state_obj = None
        super().__init__(name, content, *args, **kwargs)

    @property
    def _override_name(self):  # pylint: disable=missing-function-docstring
        """
        We override this to ensure that we return the principle objects name
        even if the name provided is a member name.
        """
        log.debug("%s._override_name", self._whoami)
        name = self._override_resolved_name
        if name not in self._override_keys():
            log.debug("'%s' not found in %s so using '%s' for override name",
                      name, self._override_keys(), self._override_keys()[0])
            name = self._override_keys()[0]

        return name

    @classmethod
    @abc.abstractmethod
    def _override_mapped_member_types(cls):
        """ All mapped override implementations must implement this as a list
        of override types that can be found within or in lieu of the primary
        override_keys.
        """

    def get_member_with_key(self, key):  # noqa, pylint: disable=missing-function-docstring
        log.debug("%s.get_member_with_key: %s", self._whoami, key)
        for m in self._override_mapped_member_types():
            if key in m._override_keys():  # noqa, pylint: disable=protected-access
                return m

        return None

    @property
    def member_keys(self):  # pylint: disable=missing-function-docstring
        keys = []
        for m in self._override_mapped_member_types():
            keys += m._override_keys()  # noqa, pylint: disable=protected-access

        return keys

    @property
    def resolved_member_names(self):  # noqa, pylint: disable=missing-function-docstring
        names = []
        for m in self.members:
            names.append(m._override_name)  # noqa, pylint: disable=protected-access

        return names

    @property
    def num_members(self):  # noqa, pylint: disable=missing-function-docstring
        return sum([len(item) for item in self._stack])  # noqa, pylint: disable=R1728

    @property
    def members(self):  # noqa, pylint: disable=missing-function-docstring
        """
        This combines iterating over the stack with iterating over the stack
        of each item on the stack. This mainly makes sense in scenarios where
        the depth of the local stack is 1.
        """
        log.debug("%s.members (depth=%s)", self._whoami, len(self._stack))
        for item in self._stack:
            log.debug("%s.__iter__ item=%s\n%s", self._whoami, item._whoami,  # noqa, pylint: disable=protected-access
                      repr(item))
            for _item in item:  # pylint: disable=R1737
                yield _item

    def __iter__(self):
        log.debug("%s.__iter__ mappings \n%s", self._whoami, repr(self._stack))
        for item in self._stack:
            log.debug("%s.__iter__ members item=%s (%s)", self._whoami,
                      item._whoami, repr(item))
            yield item

    def add_state(self, name, content, state=None, flush_current=False):  # noqa, pylint: disable=missing-function-docstring,too-many-branches,too-many-statements
        """
        @param flush_current: Flush the current state and start a new one.
        """
        log.debug("%s.add_state: name=%s content=%s current=%s "
                  "flush_current=%s", self._whoami, name, content,
                  self._current_state_obj, flush_current)
        log.debug("saving mapped override state")
        if not self._current_state_obj or flush_current:
            if state is None:
                state = MappedOverrideState(self, content, self.member_keys)

            self._current_state_obj = None
        else:
            state = self._current_state_obj

        if name in self._override_keys():
            log.debug("name is principle (%s)", name)
            self._current_state_obj = None
            if state is None:
                state = MappedOverrideState(self, content, self.member_keys)

            if type(content) in self.valid_parse_content_types():
                log.debug("resolving contents of mapped override '%s'",
                          self._override_name)
                mapping_members = self._override_mapped_member_types()
                mapping_members.append(self.__class__)
                s = PTreeSection(name, content,
                                 resolve_path=self._override_path,
                                 override_handlers=mapping_members,
                                 context=self._context)

                # Now see what members got resolved (if any)
                for mname in self.member_keys:
                    log.debug("checking for mapping '%s' member '%s'",
                              self._override_name, mname)
                    try:
                        obj = getattr(s, mname)
                        if obj is not None:
                            log.debug("member '%s' found, adding to principle",
                                      mname)
                            state.add_obj(obj)
                        else:
                            log.debug("member '%s' not found", mname)
                    except AttributeError:
                        log.debug("member '%s' not found and raised "
                                  "AttributeError which was unexpected", mname)

                # Now see what mappings got resolved (if any)
                for key in self._override_keys():
                    log.debug("checking for nested %s", key)
                    obj = getattr(s, key)
                    if obj is not None:
                        log.debug("nested mapping '%s' found, adding to "
                                  "principle", key)
                        state.add_obj(obj)

                for obj in s.get_resolved_by_type(PTreeOverrideRawType):
                    state.add_obj(obj)
            else:
                log.debug("content type '%s' not parsable (%s) so "
                          "treating as %s", type(content),
                          self.valid_parse_content_types(),
                          PTreeOverrideRawType.__name__)

                if not isinstance(content, list):
                    content = [content]

                for item in content:
                    obj = PTreeOverrideRawType(item, item, self.context,
                                               self._override_path)
                    state.add_obj(obj)

            log.debug("pushing updated mapping state to stack")
            self._stack.push(state)
        else:
            log.debug("name is member (%s)", name)
            handler = self.get_member_with_key(name)
            obj = handler(name, content, self.context, self._override_path)
            state.add_obj(obj)
            if not self._current_state_obj:
                self._current_state_obj = state
                log.debug("pushing mapping state to stack")
                self._stack.push(state)

    def __getattr__(self, name):
        """
        This should only be used if stack length == 1. Otherwise need to
        iterate over the stack.
        """
        log.debug("%s.__getattr__: mapped name=%s", self._whoami, name)
        _name = name.replace('_', '-')
        if len(self._stack):
            for stype in self._stack.current._stacks:
                obj = self._stack.current._stacks[stype].get(_name)
                if obj:
                    return obj.current

        if _name in self.member_keys:
            # allow members to be empty
            return None

        raise AttributeError("'{}' object has no attribute '{}'".   # noqa, pylint: disable=consider-using-f-string
                             format(self._whoami, name))


class PTreeOverrideManager():  # pylint: disable=missing-class-docstring

    def __init__(self, handlers=None, manager=None, context=None):
        self.allow_stacking = False
        self._resolved = {}
        self._resolved_mapped = {}
        if not handlers:
            handlers = [PTreeOverrideRawType]

        if manager:
            # clone it
            self._context = manager._context
            self._handlers = manager._handlers
            self._mappings = manager._mappings
            self._resolved.update(manager._resolved)
        else:
            self._context = context
            self._handlers = []
            self._mappings = []
            for h in handlers:
                if issubclass(h, PTreeMappedOverrideBase):
                    self._mappings.append(h)
                else:
                    self._handlers.append(h)

    def switch_to_stacked(self):
        """
        With stacking enabled we say that if an override has already been
        resolved, we can treat further resolves of the same override as extra
        state of the current one rather than treating them as separate
        instances.

        This also clears the set of resolved overrides so that we start afresh.
        """
        log.debug("enabling stacking (clearing resolved=%s)", self._resolved)
        self.allow_stacking = True
        self._resolved = {}

    def get_mapping(self, name):  # pylint: disable=missing-function-docstring
        for mapping in self._mappings:
            if name in mapping._override_keys():  # noqa, pylint: disable=protected-access
                return mapping, None

            for member in mapping._override_mapped_member_types():  # noqa, pylint: disable=protected-access
                if name in member._override_keys():  # noqa, pylint: disable=protected-access
                    return mapping, member

        return None, None

    def get_handler(self, name):  # pylint: disable=missing-function-docstring
        for h in self._handlers:
            if name in h._override_keys():  # noqa, pylint: disable=protected-access
                return h

        return None

    def get_resolved_by_type(self, otype):  # noqa, pylint: disable=missing-function-docstring
        _results = []
        for item in self._resolved.values():
            if isinstance(item, otype):
                _results.append(item)

        return _results

    def get_resolved(self, name):  # noqa, pylint: disable=missing-function-docstring
        log.debug("%s.get_resolved: name=%s (total_resolved=%s)",
                  self.__class__.__name__, name, len(self._resolved))
        name = name.replace('_', '-')
        return self._resolved.get(name)

    def add_resolved(self, name, content, handler, resolve_path,   # noqa, pylint: disable=too-many-arguments
                     member_name=None, flush_mapped=False):
        """
        @param flush_mapped: if True this tells a mapped override to flush it's
        member states and start a new set.
        """
        log.debug("%s.add_resolved: name=%s member_name=%s content=%s "
                  "handler=%s resolve_path=%s flush_mapped=%s "
                  "allow_stacking=%s", self.__class__.__name__, name,
                  member_name, content, handler.__name__, resolve_path,
                  flush_mapped, self.allow_stacking)
        resolved_obj = self._resolved.get(name)
        if resolved_obj:
            log.debug("found existing resolved obj for name=%s type=%s", name,
                      resolved_obj.__class__.__name__)

        resolved_name = name
        add_member = False
        if member_name:
            name = member_name
            if resolved_obj:
                add_member = True

        if resolved_obj and (self.allow_stacking or add_member):
            if isinstance(resolved_obj, PTreeMappedOverrideBase):
                log.debug("%s is an instance of %s",
                          resolved_obj.__class__.__name__,
                          PTreeMappedOverrideBase.__name__)
                resolved_obj.add_state(name, content,
                                       flush_current=flush_mapped)
            else:
                log.debug("obj id=%s, type=%s is not an instance of %s and is "
                          "therefore assumed to be a member or unmapped "
                          "override", id(resolved_obj),
                          resolved_obj.__class__.__name__,
                          PTreeMappedOverrideBase.__name__)
                resolved_obj.add_state(name, content)
        else:
            obj = handler(name, content, self._context, resolve_path)
            self._resolved[resolved_name] = obj

    def resolve(self, name, content, resolve_path, flush_mapped=False):  # noqa, pylint: disable=missing-function-docstring
        log.debug("%s.resolve: name=%s content=%s resolve_path=%s "
                  "flush_mapped=%s", self.__class__.__name__, name, content,
                  resolve_path, flush_mapped)
        if name == content:
            log.debug("resolved principle override with raw content")
            self.add_resolved(name, content, PTreeOverrideRawType,
                              resolve_path)
            return

        handler = self.get_handler(name)
        if handler:
            log.debug("resolving using unmapped override type=%s", handler)
            self.add_resolved(name, content, handler, resolve_path)
            return

        mapping, member = self.get_mapping(name)
        if mapping:
            if not member:
                log.debug("resolved mapped override mapping=%s (member=None)",
                          mapping.__name__)
                self.add_resolved(name, content, mapping, resolve_path)
                return

            log.debug("resolved mapped override mapping=%s (member=%s)",
                      mapping.__name__, member.__name__)
            member_name = name
            name = mapping._override_keys()[0]  # noqa, pylint: disable=protected-access
            log.debug("using mapping name '%s' (member=%s)", name, member_name)
            self.add_resolved(name, content, mapping, resolve_path,
                              member_name=member_name,
                              flush_mapped=flush_mapped)
            self._resolved_mapped[member_name] = name
            return

        log.debug("nothing to resolve")

    @property
    def resolved_unmapped(self):  # pylint: disable=missing-function-docstring
        return self._resolved

    @property
    def resolved(self):  # pylint: disable=missing-function-docstring
        _r = {}
        _r.update(self._resolved)
        _r.update(self._resolved_mapped)
        return _r


class PTreeSection():  # noqa, pylint: disable=missing-class-docstring,too-many-instance-attributes
    def __init__(self, name, content, parent=None, root=None,   # noqa, pylint: disable=too-many-arguments
                 override_handlers=None, override_manager=None,
                 run_hooks=False, resolve_path=None, context=None):
        log.warning("DEPRECATED: this version of propertree is deprecated and "
                    "will soon be removed. Please switch to the new "
                    "implementation i.e. propertree2")
        self.run_hooks = run_hooks
        if root is None:
            self.root = self
        else:
            self.root = root

        log.debug("%s.__init__: name=%s content=%s", self.__class__.__name__,
                  name, content)
        self.name = name
        self.parent = parent
        self.content = content
        self.sections = []
        if resolve_path:
            self.resolve_path = resolve_path
        else:
            self.resolve_path = name

        if override_manager:
            self.manager = PTreeOverrideManager(manager=override_manager)
        else:
            self.manager = PTreeOverrideManager(handlers=override_handlers,
                                                context=context)

        self.run()

    def _find_leaf_sections(self, section):  # noqa, pylint: disable=missing-function-docstring
        if section.is_leaf:
            return [section]

        leaves = []
        for s in section.sections:
            leaves += self._find_leaf_sections(s)

        return leaves

    @property
    def branch_sections(self):  # pylint: disable=missing-function-docstring
        return list(set([s.parent for s in self.leaf_sections]))  # noqa, pylint: disable=R1718

    @property
    def leaf_sections(self):  # pylint: disable=missing-function-docstring
        return self._find_leaf_sections(self)

    @property
    def is_leaf(self):  # pylint: disable=missing-function-docstring
        return self.content and len(self.sections) == 0

    def __getattr__(self, name):
        log.debug("%s.__getattr__: %s", self.__class__.__name__, name)
        return self.manager.get_resolved(name)

    def get_resolved_by_type(self, otype):  # noqa, pylint: disable=missing-function-docstring
        return self.manager.get_resolved_by_type(otype)

    def run(self):  # noqa, pylint: disable=missing-function-docstring,too-many-branches
        if self.root == self and self.run_hooks:
            log.debug("%s.run: running pre_hook", self.__class__.__name__)
            self.pre_hook()

        if isinstance(self.content, list):
            log.debug("content is list")
            self.manager.switch_to_stacked()
            for _ref, item in enumerate(self.content):
                log.debug("%s.run: item=%s", self.__class__.__name__, item)
                if PTreeOverrideRawType.check_is_raw_value(item):
                    self.manager.resolve(item, item, self.resolve_path)
                else:
                    flush_mapped = True
                    for name, content in item.items():
                        self.manager.resolve(name, content, self.resolve_path,
                                             flush_mapped)
                        flush_mapped = False
        else:
            self.manager.allow_stacking = False
            if not isinstance(self.content, dict):
                raise PTreeException("undefined override '{}'".   # noqa, pylint: disable=consider-using-f-string
                                     format(self.name))

            log.debug("content is dict")
            # first get all overrides at this level
            unresolved = {}
            for name, content in self.content.items():
                self.manager.resolve(name, content, self.resolve_path)
                if name not in self.manager.resolved:
                    unresolved[name] = content

            for name, content in unresolved.items():
                if PTreeOverrideRawType.check_is_raw_value(content):
                    log.debug("%s.run: terminating override=%s with raw "
                              "content '%s'", self.__class__.__name__, name,
                              content)
                    continue

                rpath = "{}.{}".format(self.resolve_path, name)   # noqa, pylint: disable=consider-using-f-string
                s = PTreeSection(name, content, parent=self, root=self.root,
                                 override_manager=self.manager,
                                 resolve_path=rpath)
                self.sections.append(s)

        if self.root == self and self.run_hooks:
            log.debug("%s.run: running post_hook", self.__class__.__name__)
            self.post_hook()

        log.debug("%s.run: %s END\n", self.__class__.__name__, self.name)

    def pre_hook(self):
        """
        This can be implemented and will be run before parsing begins.
        """

    def post_hook(self):
        """
        This can be implemented and will be run after parsing has completed.
        """
