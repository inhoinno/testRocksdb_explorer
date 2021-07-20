CC=cc
CXX=g++
AR=gcc-ar
PLATFORM=OS_LINUX
PLATFORM_LDFLAGS= -lpthread -lrt -ldl -lsnappy -lgflags -lz -lbz2 -llz4 -lzstd
PLATFORM_CMAKE_FLAGS=
JAVA_LDFLAGS= -lpthread -lrt -ldl -lsnappy -lz -lbz2 -llz4 -lzstd
JAVA_STATIC_LDFLAGS= -lpthread -lrt -ldl
JAVA_STATIC_DEPS_CCFLAGS=
JAVA_STATIC_DEPS_CXXFLAGS=
JAVA_STATIC_DEPS_LDFLAGS=
JAVAC_ARGS=-source 7
VALGRIND_VER=
PLATFORM_CCFLAGS= -DROCKSDB_PLATFORM_POSIX -DROCKSDB_LIB_IO_POSIX  -DOS_LINUX -fno-builtin-memcmp -DROCKSDB_FALLOCATE_PRESENT -DSNAPPY -DGFLAGS=1 -DZLIB -DBZIP2 -DLZ4 -DZSTD -DROCKSDB_MALLOC_USABLE_SIZE -DROCKSDB_PTHREAD_ADAPTIVE_MUTEX -DROCKSDB_BACKTRACE -DROCKSDB_RANGESYNC_PRESENT -DROCKSDB_SCHED_GETCPU_PRESENT -DROCKSDB_AUXV_GETAUXVAL_PRESENT -march=native   -DHAVE_SSE42  -DHAVE_PCLMUL  -DHAVE_AVX2  -DHAVE_BMI  -DHAVE_LZCNT -DHAVE_UINT128_EXTENSION -DROCKSDB_SUPPORT_THREAD_LOCAL
PLATFORM_CXXFLAGS=-std=c++11  -faligned-new -DHAVE_ALIGNED_NEW -DROCKSDB_PLATFORM_POSIX -DROCKSDB_LIB_IO_POSIX  -DOS_LINUX -fno-builtin-memcmp -DROCKSDB_FALLOCATE_PRESENT -DSNAPPY -DGFLAGS=1 -DZLIB -DBZIP2 -DLZ4 -DZSTD -DROCKSDB_MALLOC_USABLE_SIZE -DROCKSDB_PTHREAD_ADAPTIVE_MUTEX -DROCKSDB_BACKTRACE -DROCKSDB_RANGESYNC_PRESENT -DROCKSDB_SCHED_GETCPU_PRESENT -DROCKSDB_AUXV_GETAUXVAL_PRESENT -march=native   -DHAVE_SSE42  -DHAVE_PCLMUL  -DHAVE_AVX2  -DHAVE_BMI  -DHAVE_LZCNT -DHAVE_UINT128_EXTENSION -DROCKSDB_SUPPORT_THREAD_LOCAL
PLATFORM_SHARED_CFLAGS=-fPIC
PLATFORM_SHARED_EXT=so
PLATFORM_SHARED_LDFLAGS=-Wl,--no-as-needed -shared -Wl,-soname -Wl,
PLATFORM_SHARED_VERSIONED=true
EXEC_LDFLAGS=-ldl
JEMALLOC_INCLUDE=
JEMALLOC_LIB=
ROCKSDB_MAJOR=6
ROCKSDB_MINOR=21
ROCKSDB_PATCH=0
CLANG_SCAN_BUILD=scan-build
CLANG_ANALYZER=
PROFILING_FLAGS=-pg
FIND=find
WATCH=watch
LUA_PATH=
USE_FOLLY_DISTRIBUTED_MUTEX=1